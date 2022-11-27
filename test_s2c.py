from s2c import Converter

FULL_FILE_NAME = 'test_files/document.md'
SMALL_FILE_NAME = 'test_files/test_document.md'

def test_read():
    converter = Converter()
    spells = converter.read(SMALL_FILE_NAME)
    assert len(spells) == 16

    abscondi_spell = spells[0]
    assert abscondi_spell.title == 'Abscondi'
    assert abscondi_spell.subtitle == 'The Track Obliteration Charm'
    assert abscondi_spell.lvl == 2
    assert abscondi_spell.type == 'Charm'
    assert abscondi_spell.is_ritual

    levicorpus_spell = spells[11]
    assert levicorpus_spell.title == 'Levicorpus/Liberacorpus'
    assert levicorpus_spell.subtitle == 'The Dangling Jinx'
    assert levicorpus_spell.lvl == 4
    assert levicorpus_spell.type == 'Curse'
    assert not levicorpus_spell.is_ritual


    wingardium_spell = spells[15]
    assert wingardium_spell.title == 'Wingardium Leviosa'
    assert wingardium_spell.subtitle == 'The Levitation Charm'
    assert wingardium_spell.lvl == 0
    assert wingardium_spell.type == 'Charm'
    assert not wingardium_spell.is_ritual

    
    