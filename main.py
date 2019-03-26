#!/usr/bin/env python3

import RogueOne.Console as Console
import RogueOne.Planet as Planet
import RogueOne.Ship as Ship
import RogueOne.Resource as Resource
from RogueOne.Events import EventGUI as Game

console = Console.ConsoleApplication()
ship = Ship.ShipOne(Console.PLAYER, '#', 1, 20)
planet = Planet.PlanetOne("Home World", 'h', 3, 15)
resource = Resource.PlayerResource("Credit", '$', 5, 10)

console.add_mover(ship)
console.add_marker(planet)
console.add_resource(resource)

game = Game()
game.mainloop(console)
