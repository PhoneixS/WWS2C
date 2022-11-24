from s2c import Converter

FULL_FILE_NAME = 'test_files/document.md'
SMALL_FILE_NAME = 'test_files/test_document.md'

def test_read():
    converter = Converter()
    spells = converter.read(SMALL_FILE_NAME)
    assert len(spells) == 16
    