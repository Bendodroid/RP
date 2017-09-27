#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


class Unit:
    unit_id = 0
    unit_count = 0

    def __init__(self, name: str, level: int, max_health: int, max_attack_dmg: int,
                 inventory: dict, location=None, is_alive=bool):
        self.unit_id = Unit.unit_count
        Unit.unit_count = Unit.unit_count + 1

        self.name = name
        self.level = level
        self.max_health = max_health
        self.cur_health = max_health
        self.max_attack_dmg = max_attack_dmg
        self.cur_attack_dmg = max_attack_dmg
        self.inventory = inventory
        self.location = location
        self.is_alive = is_alive

    def kill_text(self):
        return "You defeat the " + self.name + " with a killing strike!"

    def attack(self, target):
        # target.health -= self.attack_damage
        # if target.health <= 0:
        #     target.is_alive = False
        pass
