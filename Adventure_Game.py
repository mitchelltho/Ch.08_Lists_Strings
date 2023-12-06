'''
ADVENTURE GAME (4pts)
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import arcade
import random

def showmap1():
    arcade.open_window(int(192 * 5), int(108 * 5), "Mansion Map Floor 1", resizable=True, antialiasing=True)  # Map
    arcade.set_background_color(arcade.color.WHITE_SMOKE)
    arcade.start_render()
    Window = arcade.get_window()

    arcade.Window.set_size(Window, 192 * 5, 108 * 5)
    arcade.Window.set_viewport(Window, 0, 192, 0, 108)

    point_list = ((21, 20), (96, 10), (171, 20), (181, 53), (171, 86), (96, 96), (21, 86), (11, 53))
    arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 1)
    arcade.draw_line(64, 14, 64, 92, arcade.color.BLACK, 1)
    arcade.draw_line(128, 14, 128, 92, arcade.color.BLACK, 1)
    arcade.draw_line(16, 36, 176, 36, arcade.color.BLACK, 1)
    arcade.draw_line(17, 72, 175, 72, arcade.color.BLACK, 1)
    # print(arcade.get_display_size()) # Testing
    # print(arcade.get_window()) # Testing
    # print(arcade.get_scaling_factor()) # Testing

    arcade.Window.center_window(Window)
    arcade.finish_render()
    arcade.run()

userchoice = ""
player_floor = 1


input("Welcome To Adventure Game(Temp) Press Enter To Continue ")
playing = True
while playing:
    print("Go North")
    print("Go East")
    print("Go South")
    print("Go West")
    print("Q. Quit")
    print("M. Map")
    print("Stairs. Use Stairs")
    input("What Would You Like To Do? ").upper()
    if userchoice == "Q":
        playing = False
        break

    if userchoice == "M":
        if player_floor == 1:
            showmap1()
        elif player_floor == 2:
            showmap2()
        elif player_floor == "A":
            showmapA()
        elif player_floor == "B":
            showmapB()
        continue



'''
idea list:
"You've Forced yourself against the east wall so many times you made a hole and vaulted through it into the east room" 
^maybe 16 times will do? ?secret ending or item maybe? maybe just a fun joke room with nothing in it?^
^^maybe something along the lines of "It's Empty... What did you expect?"^^
^^^thinking bottom right room of the mansion is a good candidate, top right too, just not center right for sure^^^
MAKE DEFINITIONS AND COMMENT


Keep This List Post Development Just To See
'''