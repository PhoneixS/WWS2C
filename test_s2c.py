from s2c import Converter

FULL_FILE_NAME = 'test_files/document.md'
SMALL_FILE_NAME = 'test_files/test_document.md'

def test_read():
    converter = Converter()
    spells = converter.read(SMALL_FILE_NAME)
    assert len(spells) == 17

    abscondi_spell = spells[0]
    assert abscondi_spell.title == 'Abscondi'
    assert abscondi_spell.subtitle == 'The Track Obliteration Charm'
    assert abscondi_spell.lvl == 2
    assert abscondi_spell.type == 'Charm'
    assert abscondi_spell.is_ritual
    assert abscondi_spell.casting_time == '1 action'
    assert abscondi_spell.range == 'Self'
    assert abscondi_spell.duration == 'Concentration, up to 1 hour'
    assert not abscondi_spell.is_dark
    assert not abscondi_spell.is_unforgivable
    assert len(abscondi_spell.schools) == 0

    levicorpus_spell = spells[11]
    assert levicorpus_spell.title == 'Levicorpus/Liberacorpus'
    assert levicorpus_spell.subtitle == 'The Dangling Jinx'
    assert levicorpus_spell.lvl == 4
    assert levicorpus_spell.type == 'Curse'
    assert not levicorpus_spell.is_ritual
    assert levicorpus_spell.casting_time == '1 action'
    assert levicorpus_spell.range == '30 feet'
    assert levicorpus_spell.duration == '1 minute'
    assert not levicorpus_spell.is_dark
    assert not levicorpus_spell.is_unforgivable
    assert len(levicorpus_spell.schools) == 0

    sectumsempra_spell = spells[14]
    assert sectumsempra_spell.title == 'Sectumsempra'
    assert sectumsempra_spell.subtitle == 'The Lacerating Curse'
    assert sectumsempra_spell.lvl == 4
    assert sectumsempra_spell.type == 'Curse'
    assert not sectumsempra_spell.is_ritual
    assert sectumsempra_spell.casting_time == '1 action'
    assert sectumsempra_spell.range == '60 feet'
    assert sectumsempra_spell.duration == 'Instantaneous'
    assert sectumsempra_spell.is_dark
    assert not sectumsempra_spell.is_unforgivable
    assert sectumsempra_spell.schools == ['Jinxes', 'Hexes', 'Curses']

    wingardium_spell = spells[16]
    assert wingardium_spell.title == 'Wingardium Leviosa'
    assert wingardium_spell.subtitle == 'The Levitation Charm'
    assert wingardium_spell.lvl == 0
    assert wingardium_spell.type == 'Charm'
    assert not wingardium_spell.is_ritual
    assert wingardium_spell.casting_time == '1 action'
    assert wingardium_spell.range == '30 feet'
    assert wingardium_spell.duration == 'Dedication, up to 1 minute'
    assert not wingardium_spell.is_dark
    assert not wingardium_spell.is_unforgivable
    assert len(wingardium_spell.schools) == 0

    
def test_full_read():
    converter = Converter()
    spells = converter.read(FULL_FILE_NAME)
    assert len(spells) == 144

    for spell in spells:

        if spell.title == 'Crucio':
            assert spell.is_unforgivable

        elif spell.title == 'Ferula':
            assert spell.description == 'Bandages and splints are conjured on a being you can see within range, with no more than half of its hit point maximum, and it gains hit points equal to two times your spellcasting ability modifier. Additionally, any Wisdom (Medicine) checks to stabilize that target within the duration are made at advantage, and if the target is successfully stabilized, it regains 1 hit point.\n'