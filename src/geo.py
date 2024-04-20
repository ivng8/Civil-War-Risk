import json
import pygame as pg
import random
from pandas import Series

from shapely.geometry import Point, Polygon

from src.utils import draw_text, draw_multiline_text, keyevent


class State:
    def __init__(self, name: str, coords: list) -> None:
        self.name = name
        self.coords = coords
        self.font = pg.font.SysFont(None, 24)
        self.polygon = Polygon(self.coords)
        self.center = self.get_center()
        self.units = random.randint(1, 3)
        self.color = (72, 126, 176)
        self.hovered = False
        self.neighbours = None
        self.has_attacked = False
        self.controlled_by = self.name

    def update(self, mouse_pos: pg.Vector2) -> None:
        self.hovered = False
        if Point(mouse_pos.x, mouse_pos.y).within(self.polygon):
            self.hovered = True

    def draw(self, screen: pg.Surface, scroll: pg.Vector2) -> None:
        pg.draw.polygon(
            screen,
            (255, 0, 0) if self.hovered else self.color,
            [(x - scroll.x, y - scroll.y) for x, y in self.coords],
        )
        pg.draw.polygon(
            screen,
            (255, 255, 255),
            [(x - scroll.x, y - scroll.y) for x, y in self.coords],
            width=1,
        )
        draw_text(
            screen,
            self.font,
            str(self.units),
            (255, 255, 255),
            self.center.x - scroll.x,
            self.center.y - scroll.y,
            True,
        )

    def get_center(self) -> pg.Vector2:
        return pg.Vector2(
            Series([x for x, y in self.coords]).mean(),
            Series([y for x, y in self.coords]).mean(),
        )


class World:
    MAP_WIDTH = 2.05 * 4000
    MAP_HEIGHT = 1.0 * 4000

    def __init__(self) -> None:
        self.read_geo_data()
        self.states = self.create_states()
        self.create_neighbours()
        self.scroll = pg.Vector2(3650, 395)
        self.font = pg.font.SysFont(None, 24)

        # hovering states panel
        self.hovered_state = None
        self.hover_surface = pg.Surface((300, 100), pg.SRCALPHA)
        self.hover_surface.fill((25, 42, 86, 155))

        self.battle_res = None

    def read_geo_data(self) -> None:
        with open("./data/state_coordinates_filtered.json", "r") as f:
            self.geo_data = json.load(f)

    def create_states(self) -> dict:
        states = {}
        for name, coords in self.geo_data.items():
            xy_coords = []
            for sub_coords in coords:  # Iterate over the lists of lists
                for coord in sub_coords:  # Iterate over the lists of vectors
                    if isinstance(coord[0], list):
                        for in_coord in coord:
                            x = (self.MAP_WIDTH / 360) * (180 + in_coord[0])
                            y = (self.MAP_HEIGHT / 180) * (90 - in_coord[1])
                            xy_coords.append(pg.Vector2(x, y))
                    else:
                        x = (self.MAP_WIDTH / 360) * (180 + coord[0])
                        y = (self.MAP_HEIGHT / 180) * (90 - coord[1])
                        xy_coords.append(pg.Vector2(x, y))
            states[name] = State(name, xy_coords)
        return states

    def draw(self, screen: pg.Surface) -> None:
        for state in self.states.values():
            state.draw(screen, self.scroll)
        if self.hovered_state is not None:
            self.draw_hovered_state(screen)

    def update(self) -> None:
        self.update_camera()
        mouse_pos = pg.mouse.get_pos()
        self.hovered_state = None
        for state in self.states.values():
            state.update(
                pg.Vector2(mouse_pos[0] + self.scroll.x, mouse_pos[1] + self.scroll.y)
            )
            if state.hovered:
                self.hovered_state = state

    def update_camera(self) -> None:
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.scroll.x -= 10
        elif keys[pg.K_d]:
            self.scroll.x += 10

        if keys[pg.K_w]:
            self.scroll.y -= 10
        elif keys[pg.K_s]:
            self.scroll.y += 10

        if keys[pg.K_SPACE]:
            self.scroll = pg.Vector2(1240, 800)

    def draw_hovered_state(self, screen: pg.Surface) -> None:
        screen.blit(self.hover_surface, (1280 - 310, 720 - 110))
        draw_text(
            screen,
            self.font,
            self.hovered_state.name,
            (255, 255, 255),
            1280 - 310 / 2,
            720 - 100,
            True,
            24,
        )
        draw_multiline_text(
            screen,
            self.font,
            [f"Units: {str(self.hovered_state.units)}"],
            (255, 255, 255),
            1280 - 310 + 5,
            720 - 90 + 5,
            False,
            20,
        )

    def create_neighbours(self) -> None:
        for k, v in self.states.items():
            v.neighbours = self.get_state_neighbours(k)

    def get_state_neighbours(self, state: str) -> list:
        neighbours = []
        state_poly = self.states[state].polygon
        for other_state_key, other_state_value in self.states.items():
            if state != other_state_key:
                if state_poly.intersects(other_state_value.polygon):
                    neighbours.append(other_state_key)
        return neighbours

    def battle(self, attacking_state:str, defending_state:str) -> None:

        a_c = self.states[attacking_state]
        d_c = self.states[defending_state]

        a_c.has_attacked = True

        res = {
            "attacking_state": attacking_state,
            "defending_state": defending_state,
            "victory": False,
            "attacking_state_losses": 0,
            "defending_state_losses": 0
        }

        keyevent("attacking_state", "defending_state")

        while (a_c.units > 1) and (d_c.units > 0):

            if a_c.units - d_c.units > 2:
                attack_dice = max(random.randint(1, 6), random.randint(1, 6))
            else:
                attack_dice = random.randint(1, 6)

            defend_dice = random.randint(1, 6)

            if attack_dice > defend_dice:
                d_c.units -= 1
                res["defending_state_losses"] += 1
            else:
                a_c.units -= 1
                res["attacking_state_losses"] += 1

            if d_c.units == 0:
                res["victory"] = True

        if res["victory"]:
            d_c.units = 1
            a_c.units -= 1

        self.battle_res = res
