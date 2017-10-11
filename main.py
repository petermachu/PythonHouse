from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on every wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

closet = Room("Closet")
closet.set_description("A small closet filled with cleaning supplies.")

hallway = Room("Hallway")
hallway.set_description ("A long hallway lined with paintings."

cellar = Room("Cellar")
cellar.set_description ("A dark smelly room littered with rotting food that emits a powerful odour.")

wine_cellar = Room("Wine Cellar")
wine_cellar.set_description ("A nearly pitch black room with empty wineracks along the walls and broken glass on the floor.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
hallway.link_room(ballroom, "south")
ballroom.link_room(hallway, "north")
hallway.link_room(closet, "west")
closet.link_room(hallway, "east")
cellar.link_room(kitchen, "up")
kitchen.link_room(cellar, "below")
cellar.link_room(wine_cellar, "east")
wine_cellar.link_room(cellar, "west")
                         
current_room = kitchen

while True:
    print ("\n")
    current_room.get_details()
    command = raw_input("> ")
    current_room = current_room.move(command)

