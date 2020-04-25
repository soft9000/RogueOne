#!/usr/bin/env python3
''' 
RogueOne - This framework will work wherever 
Python 3 & Tkinter have been installed.
'''

import RogueOne.Console as Console
import RogueOne.Planet as Planet
import RogueOne.Ship as Ship
import RogueOne.Alien as Alien
import RogueOne.Resource as Resource
from RogueOne.Events import EventGUI as Game

console = Console.ConsoleApplication()
ship = Ship.ShipOne(Console.PLAYER, '#', 1, 20)
alien = Alien.Alien("Alien", "֍", 20, 1, console.width, console.height)
planet = Planet.PlanetOne("Home World", 'h', 3, 15)
resource = Resource.PlayerResource("Credit", '$', 5, 10)

console.add_mover(ship)
console.add_mover(alien)
console.add_marker(planet)
console.add_resource(resource)

game = Game()
game.mainloop(console)
