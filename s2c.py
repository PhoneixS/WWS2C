from enum import Enum
from typing import List

FILE_NAME = 'test_files/document.md'
FILE_NAME_OUTPUT = 'test_files_output/document.json'

class Spell:
    pass

class ConverterStatus(Enum):
    NONE = 0,
    SEARCHING_SPELLS_SECTION = 1,
    SEARCHING_SPELL_DEFINITION = 2,
    READING_SPELL = 3

class Converter:
    
    def __init__(self) -> None:
        self.status = ConverterStatus.NONE
    
    
    def read(self, file: str) -> List[Spell]:

        spells = []
        self.status = ConverterStatus.SEARCHING_SPELLS_SECTION
    
        with open(file) as f:
            for line in file:
                if (line == '## Spell Descriptions'):
                    self.status = ConverterStatus.SEARCHING_SPELL_DEFINITION
        
        return spells
    
    def save_as_json(self, spells: List[Spell], file_name: str):
        pass

def main():
    
    converter = Converter()
    spells = converter.read(FILE_NAME)
    converter.save_as_json(spells, FILE_NAME_OUTPUT)

if __name__ == '__main__':
    main()