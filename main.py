import random
from random import randint

print("Герой, добро пожаловать!")
hero_hp = 15
hero_attack = 10
monster_counter = 0


def userChoice() -> int:
    """Выбор действия."""
    i = int(input())
    while i != 1 or i != 2:
        if i == 1 or i == 2:
            break
        else:
            print('Необходимо выбрать значения: "1" или "2"')
            i = int(input())
    return i


def fight() -> int:
    """Функция боя."""
    global hero_hp
    hp_monster = randint(5, 6)
    attack_monster = randint(5, 6)
    print(
        f"БОЙ! Вы встречаете чудовище со здоровьем равным {hp_monster} и силой атаки {attack_monster}"
    )
    print("Сделайте свой выбор: 1 - Вступить в бой; 2 - Покинуть поле сражения")
    otv1 = userChoice()
    if otv1 == 1:
        while hero_hp > 0 or hp_monster > 0:
            hero_hp -= attack_monster
            hp_monster -= hero_attack
            if hp_monster < 1 and hero_hp > 1:
                print("Вы победили этого монстра!")
                return 1
            else:
                print("ПОРАЖЕНИЕ!")
                return 0
    if otv1 == 2:
        print("Вы убегаете с поля боя :(")
        return 2
    return 0


def health() -> int:
    """Генерация для пополнения жизней героя."""
    global hero_hp
    apple = randint(1, 10)
    print("ОГО! Вы нашли яблочко. Нужно его съесть")
    hero_hp += apple
    print(f"Теперь ваше здоровье равно {hero_hp}")
    return hero_hp


def damage() -> int:
    """Генерация для подбора нового меча."""
    global hero_attack
    sword = randint(7, 20)
    print(
        f"МЕЧ!Герой, вы нашли новый меч с уроном равным {sword}. "
        f"На данный момент урон вашего меча составляет {hero_attack}"
    )
    print("Сделайте свой выбор: 1-взять меч себе выбросив старый, 2-пройти мимо меча")
    otv2 = userChoice()
    if otv2 == 1:
        hero_attack = 0
        hero_attack += sword
        print(f"Теперь ваш меч имеет {hero_attack} урона")
        return hero_attack
    if otv2 == 2:
        print("Герой проходит мимо меча")
    return 0


def game() -> None:
    """Главная функция."""
    global monster_counter
    while monster_counter != 10:
        i = random.randint(1, 3)
        if i == 1:
            f = fight()
            if f == 1:
                monster_counter += 1
            elif f == 2:
                print("Герой наберись сил")
            else:
                break
        elif i == 2:
            damage()
        else:
            health()
    if monster_counter == 10:
        print("ПОБЕДА")


game()

