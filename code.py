#!/usr/bin/env python3

# Created by: Patrice Pat-Odita
# Created on: Jan 09, 2023
# This program is the "Space Aliens" program on the pybadge

import stage
import ugame

import constants

def game_scene():

    # this is the main scene for space alien
    # saves images and sprites for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")
    # set the background to image 0 in the image bank
    # and the size
    background = stage.Grid(image_bank_background, 10, 8)
    # updates the sprite in every frame
    ship = stage.Sprite(image_bank_sprites, 4, 75, 66)

    # creates a stage background and sets the frame rate to 120fps
    game = stage.Stage(ugame.display, 120)

    #sets the layers of all the sprites and items to show up in order
    game.layers = [ship] + [background]

    #renders all sprites
    game.render_block()

    #repeat forever game loop

    while True:
        # gets user input
        keys = ugame.buttons.get_pressed()

        # Assigns key to specific task and display's command
        if keys & ugame.K_X != 0:
            print("A")
        if keys & ugame.K_O != 0:
            print("B")
        # sets the start button to start the game
        if keys & ugame.K_START != 0:
            print("Start Game")
        # sets the select button to select options in the game
        if keys & ugame.K_SELECT != 0:
            print("select")
        
       # sets the right button to move the sprite to the right by 1
        if keys & ugame.K_RIGHT != 0:
            if ship.x < (constants.SCREEN_X - constants.SPRITE_SIZE):
                ship.move((ship.x + constants.SPRITE_MOVEMENT_SPEED),ship.y)
            else:
                ship.move((constants.SCREEN_X - constants.SPRITE_SIZE), ship.y)

       # sets the left button to move the sprite left by 1
        if keys & ugame.K_LEFT != 0:
            if ship.x > 0:
                ship.move((ship.x - constants.SPRITE_MOVEMENT_SPEED), ship.y)
            else:
                ship.move(0, ship.y)

        # sets the up button to move the sprite upward by 1
        if keys & ugame.K_UP != 0:
            pass

        # sets the down button to move the sprite down by 1
        if keys & ugame.K_DOWN != 0:
            pass

            
        # updates the game logic
        
        # redraw sprite
        game.render_sprites([ship])
        game.tick()



if __name__ == "__main__":
    game_scene()

