'''
ADVENTURE GAME (4pts)
-----------------
1.) Use the pseudo-code on the website to help you set up the basic move through the house program
2.) Print off a physical map for players to use with your program
3.) Expand your program to make it a real adventure game

'''
import arcade
import random

userchoice = ""

input("Welcome To Adventure Game(Temp) Press Enter To Continue ")
playing = True
while playing:
    if userchoice == "Q":
        playing = False
        break
    mapchoice = input("Would You Like A Map This Play-through? (You'll Have To Size It Up Manually) {for now} ").upper()
    if mapchoice == "Y" or "YES" or "TRUE":
        maptoggle = True
    else:
        continue
    if maptoggle:
        arcade.open_window(192, 108, "Mansion Map Floor 1",resizable=True)#Map
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        arcade.start_render()

        point_list = ((21, 20), (96, 10), (171, 20), (181, 53), (171, 86), (96, 96), (21, 86), (11, 53))
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 1)
        arcade.draw_line(64, 14, 64, 92, arcade.color.BLACK, 1)
        arcade.draw_line(128, 14, 128, 92, arcade.color.BLACK, 1)
        arcade.draw_line(16, 36, 176, 36, arcade.color.BLACK, 1)
        arcade.draw_line(16, 72, 176, 72, arcade.color.BLACK, 1)
        print(arcade.get_display_size())
        print(arcade.get_window())
        print(arcade.get_scaling_factor())
        arcade.screen_to_isometric_grid(400, 400, 1920, 1080, 20, 20)
        arcade.finish_render()
        arcade.run()

    userchoice = input("Which Direction Would You Like To Go? ")

'''
idea list:
"You've Forced yourself against the east wall so many times you made a hole and vaulted through it into the east room" 
^maybe 16 times will do? ?secret ending or item maybe? maybe just a fun joke room with nothing in it?^
^^maybe something along the lines of "It's Empty... What did you expect?"^^
^^^thinking bottom right room of the mansion is a good candidate, top right too, just not center right for sure^^^



'''