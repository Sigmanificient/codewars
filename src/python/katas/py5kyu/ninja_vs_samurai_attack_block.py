Position = {'high': 'h', 'low': 'l'}


class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.block = ""

        self.deceased = False
        self.zombie = False

    @staticmethod
    def attack(enemy, position):
        damage = 0

        if enemy.block != position:
            damage += 10 if position == Position['high'] else 5

        if enemy.block == "":
            damage += 5

        enemy.set_health(enemy.health - damage)

    def set_health(self, new_health):
        self.health = max(0, new_health)

        if self.deceased:
            self.zombie = True

        if self.health == 0:
            self.deceased = True
            self.zombie = False


def test_warrior():
    from random import randint

    ninja = Warrior('Hanzo Hattori')
    samurai = Warrior('Miyamoto Musashi')

    assert ninja.name =='Hanzo Hattori'
    assert samurai.name == 'Miyamoto Musashi'

    assert ninja.health == 100
    assert samurai.health == 100

    def check_attack(enemy, position):
        damage = 0
        if enemy.block != position:
            damage += 10 if position == Position['high'] else 5
        if enemy.block == "":
            damage += 5
        return max(0, enemy.health - damage)

    attacker = [ninja, samurai][randint(0, 1)]
    enemy = samurai if attacker == ninja else ninja

    position = Position[["high", "low"][randint(0, 1)]]
    en_h = check_attack(enemy, position)
    attacker.attack(enemy, position)
    assert enemy.health == en_h

    while ninja.health > 0 and samurai.health > 0:
        attacker, enemy = enemy, attacker
        enemy.block = Position[["high", "low"][randint(0, 1)]]
        position = Position[["high", "low"][randint(0, 1)]]
        en_h = check_attack(enemy, position)
        attacker.attack(enemy, position)
        assert enemy.health == en_h

    assert not attacker.deceased
    assert not attacker.zombie

    assert enemy.deceased
    assert not enemy.zombie
