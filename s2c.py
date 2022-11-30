import logging
import re
from enum import Enum
from typing import List, Mapping

FILE_NAME = 'test_files/document.md'
FILE_NAME_OUTPUT = 'test_files_output/document.json'
RE_TITLE = re.compile(r'#### \[([^]\n]+)\]\(#spell-list\)\n', re.IGNORECASE)
RE_SUBTITLE = re.compile(r'\*(.+) - ((((\d)(st|nd|rd|th)-level) (\w+))|((\w+) (cantrip)))( \(ritual\))?\*', re.IGNORECASE)
RE_PROPERTY = re.compile(r'- \*\*(.+):\*\* +(.+)')
RE_PROPERTY_TAG = re.compile(r'(Dark(, )?)?( - \*Unforgivable Curse\*)?(School of Magic - \*(.+)\*)?', re.IGNORECASE)

class Spell:
    
    def __init__(self, title: str) -> None:
        self.title: str = title
        self.subtitle: str = None
        self.lvl: int = None
        self.type: str = None
        self.is_ritual: bool = False
        self.description: str = ''
        self.is_dark: bool = False
        self.is_unforgivable: bool = False
        self.schools: List[str] = []
        self.casting_time: str = None
        self.range: str = None
        self.duration: str = None

class ConverterStatus(Enum):
    NONE = 0,
    SEARCHING_SPELLS_SECTION = 1,
    SEARCHING_SPELL_DEFINITION = 2,
    READING_SPELL = 3
    FINISHED_READING = 4

class SpellReaderStatus(Enum):
    NONE = 0,
    COMMENT = 1,
    SPAN_ID = 2,
    SUBTITLE = 3,
    PROPERTIES_START = 4,
    PROPERTIES_BODY = 5,
    DESCRIPTION = 6

class Converter:
    
    def __init__(self) -> None:
        self.status: ConverterStatus = ConverterStatus.NONE
        self.spell_reading_status: SpellReaderStatus = SpellReaderStatus.NONE
        self.previous_spell_reading_status: SpellReaderStatus = SpellReaderStatus.NONE
        self._last_readed_spell: Spell = None
    
    def _parse_spell_line(self, line: str) -> None:
        if line.startswith('<!--'):
            self.previous_spell_reading_status = self.spell_reading_status
            self.spell_reading_status = SpellReaderStatus.COMMENT
        elif self.spell_reading_status == SpellReaderStatus.COMMENT and ('-->' in line):
            self.spell_reading_status = self.previous_spell_reading_status
            self.previous_spell_reading_status = None
            lefout = line.split('-->', 1)[1]
            if lefout:
                self._parse_spell_line(lefout)
        elif self.spell_reading_status == SpellReaderStatus.COMMENT:
            # ignore commented lines
            return
        elif self.spell_reading_status == SpellReaderStatus.SPAN_ID:
            if line.startswith('<span id="spell-descr-'):
                # Ignore the span, we don't need it
                self.spell_reading_status = SpellReaderStatus.SUBTITLE
            else:
                logging.warning('After spell title must be a span with id, but found ' + line)
        elif self.spell_reading_status == SpellReaderStatus.SUBTITLE:
            if line.startswith('*'):
                subtitle_info = RE_SUBTITLE.match(line)
                if not subtitle_info:
                    logging.error('Found a subtitle line that doesn\'t match the regex: ' + line)
                self._last_readed_spell.subtitle = subtitle_info.group(1)
                self._last_readed_spell.lvl = int(subtitle_info.group(5) if subtitle_info.group(5) else 0)
                self._last_readed_spell.type = subtitle_info.group(7) if subtitle_info.group(7) else subtitle_info.group(9)
                self._last_readed_spell.is_ritual = True if subtitle_info.group(11) else False
                self.spell_reading_status = SpellReaderStatus.PROPERTIES_START
            else:
                logging.warning('After spell title must be a subtitle enclosed in *, but found ' + line)
                self.spell_reading_status = SpellReaderStatus.PROPERTIES_START
        elif self.spell_reading_status == SpellReaderStatus.PROPERTIES_START:
            if line.startswith('___'):
                self.spell_reading_status = SpellReaderStatus.PROPERTIES_BODY
            else:
                logging.warning('Found spell without properties, which is strange, line: ' + line)
                self.spell_reading_status = SpellReaderStatus.DESCRIPTION
                self._parse_spell_line(line)
        elif self.spell_reading_status == SpellReaderStatus.PROPERTIES_BODY and line.startswith('___'):
            self.spell_reading_status = SpellReaderStatus.DESCRIPTION
        elif self.spell_reading_status == SpellReaderStatus.PROPERTIES_BODY:
            self._parse_property_line(line)
        elif self.spell_reading_status == SpellReaderStatus.DESCRIPTION:
            self._last_readed_spell.description += line

    def _parse_property_line(self, line: str):
        property_info = RE_PROPERTY.match(line)
        if not property_info:
            logging.error('Found a subtitle line that doesn\'t match the regex: ' + line)
        key = property_info.group(1).lower()
        value = property_info.group(2)

        if key == 'casting time':
            self._last_readed_spell.casting_time = value
        elif key == 'duration':
            self._last_readed_spell.duration = value
        elif key == 'range':
            self._last_readed_spell.range = value
        elif key == 'tags':
            self._parse_tag(value)
        else:
            logging.warning('Unknow propertie ' + key)
            


    
    def _parse_tag(self, tag: str):
        tag_info = RE_PROPERTY_TAG.match(tag)
        if not tag_info:
            logging.error('Found a tag line that doesn\'t match the regex: ' + tag)
        self._last_readed_spell.is_dark = bool(tag_info.group(1))
        self._last_readed_spell.is_unforgivable = bool(tag_info.group(3))
        if tag_info.group(5):
            self._last_readed_spell.schools = [ remove_and(school) for school in tag_info.group(5).split(', ')]

    
    def read(self, file: str) -> List[Spell]:
        logging.info('Reading file')
        spells = []
        self.status = ConverterStatus.SEARCHING_SPELLS_SECTION
        self._last_readed_spell = None
        
    
        with open(file) as f:
            for line in f:
                if line == '## Spell Descriptions\n':
                    logging.info('Spell descriptions section found')
                    self.status = ConverterStatus.SEARCHING_SPELL_DEFINITION
                elif self.status == ConverterStatus.READING_SPELL and (line.startswith('# ') or line.startswith('## ')):
                    logging.info('Finished reading spells')
                    # We have finished searching for spells, new section appeared
                    if self._last_readed_spell:
                        spells.append(self._last_readed_spell)
                    self.status = ConverterStatus.FINISHED_READING
                    break
                elif self.status in [ConverterStatus.SEARCHING_SPELL_DEFINITION, ConverterStatus.READING_SPELL] and line.startswith('#### '):
                    # End last spell
                    if self._last_readed_spell:
                        spells.append(self._last_readed_spell)

                    # Start new spell
                    title_info = RE_TITLE.match(line)
                    self._last_readed_spell = Spell(title_info.group(1))
                    self.status = ConverterStatus.READING_SPELL
                    self.spell_reading_status = SpellReaderStatus.SPAN_ID
                elif self.status == ConverterStatus.READING_SPELL:
                    self._parse_spell_line(line)
        
        return spells
    
    def save_as_json(self, spells: List[Spell], file_name: str):
        pass

def remove_and(text: str) -> str:
    if text.startswith('and '):
        return text[4:]
    return text

def main():
    
    converter = Converter()
    spells = converter.read(FILE_NAME)
    for s in spells:
        print('-----------')
        print(s.title)
        print(s.description)
        print('+++++++++++')
    converter.save_as_json(spells, FILE_NAME_OUTPUT)

if __name__ == '__main__':
    main()