
Main Structure
BEGIN(Main) Escape Room Game:
    display INSTRUCTION
    print "Are you Ready to Start the game?"
    if "Yes":
        Health = 1
        allow Game Start

    if Health is 1 and allow Game Start:
        BEGIN game
    elif Health not 1 and allow Game Start:
        print " Game Over you Died. Do you wan to try again?"
        if Input is "yes":
            Health = 1
            else:
            END (Main) Rpg Game

INSTRUCTION Code
print Game title
print Basic Game Setting
print Possible Actions
print Help Options


Possible Actions Code


Game Code 
