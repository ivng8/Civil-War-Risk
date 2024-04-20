import pygame as pg

from src.geo import State, World


class Player:
    def __init__(self, state: State, world: World, color: tuple) -> None:
        self.state = state
        self.world = world
        self.color = color
        self.state.color = self.color
        self.timer = pg.time.get_ticks()
        self.controlled_states = [self.state.name]
        self.neighbours = self.get_neighbours()

        # moving units
        self.move_state_from = ""
        self.move_state_to = ""
        self.move_n_units = 0

        # attacking states
        self.attack_state_from = ""
        self.attack_state_to = ""

    def update(self, phase: str) -> None:
        if phase == "place_units":
            self.place_units()
        elif phase == "move_units":
            self.move_units()
        elif phase == "attack_state":
            self.attack_state()

    def place_units(self) -> None:
        now = pg.time.get_ticks()
        for state in self.controlled_states:
            c = self.world.states[state]
            if c.hovered and pg.mouse.get_pressed()[0] and (now - self.timer > 300):
                self.timer = now
                c.units += 1

    def move_units(self) -> None:

        now = pg.time.get_ticks()
        
        if self.move_state_from == "":
            for state in self.controlled_states:
                c = self.world.states[state]
                if c.hovered and pg.mouse.get_pressed()[0]:
                    self.move_state_from = c.name
                    print(f"Moving from {self.move_state_from}")

        if (self.move_state_to == "") and (self.move_state_from != ""):
            for state in self.controlled_states:
                c = self.world.states[state]
                if (c.hovered and pg.mouse.get_pressed()[0] and c.name != self.move_state_from):
                    self.move_state_to = c.name
                    print(f"Moving to {self.move_state_to}")

        if pg.mouse.get_pressed()[2]:
            self.move_state_from = ""
            self.move_state_to = ""
            self.move_n_units = 0

        keys = pg.key.get_pressed()
        if self.move_state_from != "" and self.move_state_to != "":
            c_from = self.world.states[self.move_state_from]
            c_to = self.world.states[self.move_state_to]
            if keys[pg.K_UP] and (now - self.timer > 200) and (c_from.units - self.move_n_units > 1):
                self.timer = now
                self.move_n_units += 1
                print(f"Number of units to move: {self.move_n_units}")
            if keys[pg.K_DOWN] and (now - self.tiemr > 200) and (self.move_n_units > 0):
                self.timer = now
                self.move_n_units -= 1
                print(f"Number of units to move: {self.move_n_units}")
            
            if keys[pg.K_RETURN]:
                c_from.units -= self.move_n_units
                c_to.units += self.move_n_units
                print(f"Moved {self.move_n_units} from {self.move_state_from} to {self.move_state_to}")
                self.move_state_from = ""
                self.move_state_to = ""
                self.move_n_units = 0


    def attack_state(self) -> None:
        
        if self.attack_state_from == "":
            for state in self.controlled_states:
                c = self.world.states[state]
                if c.hovered and pg.mouse.get_pressed()[0] and (not c.has_attacked):
                    self.attack_state_from = c.name
                    print(f"Attacking from {self.attack_state_from}")

        if (self.attack_state_to == "") and (self.attack_state_from != ""):
            for state in self.world.states[self.attack_state_from].neighbours:
                if state not in self.controlled_states:
                    c = self.world.states[state]
                    if c.hovered and pg.mouse.get_pressed()[0]:
                        self.attack_state_to = c.name
                        print(f"Attacking {self.attack_state_to}")

        # cancel selection
        if pg.mouse.get_pressed()[2]:
            self.attack_state_from = ""
            self.attack_state_to = ""

        # battle
        keys = pg.key.get_pressed()
        if (
            keys[pg.K_RETURN] and (self.attack_state_from != "") and (self.attack_state_to != "")
        ):
            self.world.battle(self.attack_state_from, self.attack_state_to)
            self.attack_state_from = ""
            self.attack_state_to = ""

    def get_neighbours(self) -> list:
        neighbours = []
        for state in self.controlled_states:
            for neighbour in self.world.states[state].neighbours:
                if neighbour not in self.controlled_states:
                    neighbours.append(neighbour)
        return set(neighbours)
    
    def conquer(self, state:str) -> None:
        self.world.states[state].color = self.color
        self.world.states[state].controlled_by = self.state.name
        self.controlled_states.append(state)
        self.neighbours = self.get_neighbours()

    def reset_turn(self) -> None:

        print("Reset turn")
        self.timer = 0

        self.move_state_from = ""
        self.move_state_to = ""
        self.move_n_units = 0

        self.attack_state_from = ""
        self.attack_state_to = ""

        for state in self.controlled_states:
            c = self.world.states[state]
            c.has_attacked = False

