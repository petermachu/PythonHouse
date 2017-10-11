# PythonHouse
Creating a collection of rooms and items in python.

I'm learning Object-Oriented Programming in Python on Futurelearn.com

Please help me add more rooms and link them together.

Add rooms by adding the following code to main.py:

newroom = Room("Insert New Room Name")

newroom.set_description("Insert New Room Description.")

Link rooms by adding the following code to main.py:

firstroom.link_room(roomtolinkto, "direction to link")

roomtolinkto.link_room(firstroom, "opposite direction to direction to link")

Please note that links only go one way so you have to repeat the process in the opposite direction.

Example:

kitchen = Room("Kitchen")

kitchen.set_description("A dank and dirty room buzzing with flies.")

kitchen.link_room(dining_hall, "south")

dining_hall.link_room(kitchen, "north")


Move through the house here: https://trinket.io/python/c0bf3c7c32
