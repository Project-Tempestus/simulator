from dataclasses import dataclass

_BASE_MARKSMANSHIP = 15
_BASE_CQB = 40
_BASE_STRENGTH = 40
_BASE_CONSTITUTION = 40
_BASE_AGILITY = 40
_BASE_KNOWLEDGE = 30
_BASE_HP = 100


@dataclass
class Bonus:
    marksmanship: int = 0
    cqb: int = 0
    strength: int = 0
    constitution: int = 0
    agility: int = 0
    knowledge: int = 0
    hp: int = 0


@dataclass
class Stats:
    marksmanship: int = _BASE_MARKSMANSHIP
    cqb: int = _BASE_CQB
    strength: int = _BASE_STRENGTH
    constitution: int = _BASE_CONSTITUTION
    agility: int = _BASE_AGILITY
    knowledge: int = _BASE_KNOWLEDGE
    hp: int = _BASE_HP

    def add(self, bonus):
        self.marksmanship += bonus.marksmanship
        self.cqb += bonus.cqb
        self.strength += bonus.strength
        self.constitution += bonus.constitution
        self.agility += bonus.agility
        self.knowledge += bonus.knowledge
        self.hp += bonus.hp

    def __eq__(self, other):
        assert self.marksmanship == other.marksmanship
        assert self.cqb == other.cqb
        assert self.strength == other.strength
        assert self.constitution == other.constitution
        assert self.agility == other.agility
        assert self.knowledge == other.knowledge
        assert self.hp == other.hp
        return 1


cadia_bonus = Bonus(marksmanship=5, cqb=5, constitution=5, agility=5)
catachan_bonus = Bonus(cqb=10, strength=5, agility=5, hp=15)
krieg_bonus = Bonus(cqb=5, constitution=10, knowledge=5)
armageddon_bonus = Bonus(agility=10, knowledge=30)
vostroya_bonus = Bonus(constitution=10, strength=10, hp=30)
chr_bonus = Bonus(constitution=15, knowledge=15)
eng_bonus = Bonus(strength=10, knowledge=20)
grd_bonus = Bonus(strength=15, constitution=15)
srg_bonus = Bonus(constitution=10, hp=10)
sct_bonus = Bonus(agility=30, knowledge=10)
mrk_bonus = Bonus(marksmanship=5)
stm_bonus = Bonus(cqb=15, agility=15)

preset_bonuses = {
    "cadia": cadia_bonus,
    "catachan": catachan_bonus,
    "krieg": krieg_bonus,
    "armageddon": armageddon_bonus,
    "vostroya": vostroya_bonus,
    "chr": chr_bonus,
    "eng": eng_bonus,
    "grd": grd_bonus,
    "srg": srg_bonus,
    "sct": sct_bonus,
    "mrk": mrk_bonus,
    "stm": stm_bonus,
}
