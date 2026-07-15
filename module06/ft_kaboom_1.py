import alchemy.grimoire.dark_spellbook

if __name__ == "__main__":
    try:
        print(f"{alchemy.grimoire.dark_spellbook.dark_spell_record}")
    except ImportError as e:
        print(f"{e}")
