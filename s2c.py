from enum import Enum

FILE_NAME = 'test_files/document.md'

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
    
    
    def read(self, file: str) -> list(Spell):

        spells = []
        self.status = ConverterStatus.SEARCHING_SPELLS_SECTION
    
        with open(file) as f:
            for line in file:
                if (line == '## Spell Descriptions'):
                    self.status = ConverterStatus.SEARCHING_SPELL_DEFINITION
        
        return spells
    
    def save_as_json(self, spells: list(Spell)):
        pass

def main():
    
    converter = Converter()
    spells = converter.read(FILE_NAME)
    converter.save_as_json(spells)

if __name__ == '__main__':
    main()