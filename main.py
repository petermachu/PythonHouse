from room import Room

kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on every wall.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

hallway = Room("Hallway")
hallway.set_description ("A long hallway lined with paintings."

cellar = Room("Cellar")
cellar.set_description ("A dark smelly room littered with rotting food that emits a powerful odour.")

wine_cellar = Room("Wine Cellar")
wine_cellar.set_description ("A nearly pitch black room with empty wineracks along the walls and broken glass on the floor.")
                         
swimming_pool = Room("Swimming Pool")
swimming_pool.set_description ("A deep pool filled with distilled water with a tiny bit of chlorine and urine.")
                         
gym = Room("Gym")
gmy.set_description ("A huge room with a glass ceiling and one yoga ball in the center of the room.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
hallway.link_room(ballroom, "south")
ballroom.link_room(hallway, "north")
cellar.link_room(kitchen, "up")
kitchen.link_room(cellar, "below")
cellar.link_room(wine_cellar, "east")
wine_cellar.link_room(cellar, "west")
swimming_pool.link_room(ballroom, "east")
ballroom.link_room(swimming_pool, "west")
gym.link_room(swimming_pool, "down")
swimming_pool.link_room(gym, "up")                        
                         
current_room = kitchen

while True:
    print ("\n")
    current_room.get_details()
    command = raw_input("> ")
    current_room = current_room.move(command)

