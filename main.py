from __future__ import annotations

import random
from enum import Enum, auto
import typing
import types

from game_classes.base import GameObject, GameActor, GameActorNPC, GameItem, GameStructure, Consts
from locations import Loc, Locations
import format_templates as ft
import utility


class GameTurn:
    class Enum(Enum):
        MOVE = auto

    def __init__(self, session: GameSession):
        self.session = session
        self.command = input("> ")
        self.events = []

    def encounter(self):
        pass


class Player(GameActor):
    def __init__(self):
        super().__init__(value=0, max_health=100)
        self.name = input("Name> ")


class GameSession:
    def __init__(self):
        self.turns = []  # type:typing.List[GameTurn]
        self.player = Player()
        self.locations = Locations()
        self.func_format = ft.FuncFormat()
        self.random = self._init_random_ns()

        self.world = utility.get_rand_name()

    def _init_random_ns(self):
        return types.SimpleNamespace(
            name=utility.get_rand_name,
            location=self.locations.get_rand_str,
            enemy=utility.get_rand_name
        )

    def display_welcome(self):
        self.func_format.display(
            'welcome',
            random=self.random,
            player=self.player,
            world=self.world
            )

    def display_encounter(self):
        self.func_format.display(
            'encounter',
            random=self.random,
            player=self.player
        )


def game_main():
    # TODO: load session data
    session = GameSession()  # Will ask for input for name if no save data
    session.display_welcome()

    beast = GameActorNPC.from_enum(Consts.Enemies.MID_LVL)




if __name__ == "__main__":
    game_main()
