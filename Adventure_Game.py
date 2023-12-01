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
    mapchoice = input("Would You Like A Map This Play-through? ").upper()
    if mapchoice == "Y" or "YES" or "TRUE":
        maptoggle = True
    else:
        continue
    if maptoggle:
        arcade.open_window(192 * 4, 108 * 4, "Mansion Map",resizable=True)#Map
        arcade.set_background_color(arcade.color.WHITE_SMOKE)
        arcade.start_render()

        point_list = ((21, 20), (96, 10), (171, 20), (181, 53), (171, 86), (96, 96), (21, 86), (11, 53))
        arcade.draw_polygon_outline(point_list, arcade.color.BLACK, 1)
        print(arcade.get_display_size())
        print(arcade.get_window())
        print(arcade.get_scaling_factor())
        #arcade.set_window(window=)
        arcade.finish_render()
        arcade.run()

    userchoice = input("Which Direction Would You Like To Go? ")

