#!/usr/bin/env python3.5

# Copyright Bendodroid [2017]


class Character:

    current_level = int()
    std_hp = int()
    std_dmg = int()
    cur_hp = int()
    cur_dmg = int()

    def heal(self, heal_hp):
        self.cur_hp += heal_hp
        if self.cur_hp > self.std_hp:
            self.cur_hp = self.std_hp
