#!/usr/bin/env python3

# Created by: Patrice Pat-Odita
# Created on: Jan 09, 2023
# This program is the "Space Aliens" program on the pybadge

import stage
import ugame



def game_scene():

    # this is the main scene for space alien
    #image bank for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    #set the background to image 0 in the image bank
    #   and the size
    background = stage.Grid(image_bank_background, 10, 8)
    # updates the sprite in every frame
    ship = stage.Sprite(image_bank_sprites, 4, 75, 66)

    # creates a stage background and sets the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    #sets the layers of all the sprites and items to show up in order
    game.layers = [ship] + [background]

    #renders all sprites
    game.render_block()

    #repeat forever game loop

    while True:
        # gets user input
        # updates the game logic
        
        # redraw sprite
        game.render_sprites([ship])
        game.tick()



if __name__ == "__main__":
    game_scene()

