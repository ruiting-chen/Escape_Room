Health = 0

MAIN STRUCTURE Code
begin(Main Structure):
    global Health
    display INSTRUCTION
    if ready to start:
        Health = 1
        allow Game Start
    if Health is 1 and allow Game Start:
        begin MAIN
    elif Health not 1 and allow Game Start:
        print " Game Over you Failed to Escape. Do you wan to try again?"
        if Input is "yes":
            Health = 1
        else:
            end MAIN

INSTRUCTION Code
print Game title: Escape Room
print Basic Game Setting/Purpose
    You are locked inside a house by the aliens. You have to escape the house
    before they come back to do experiments on you. There are two guards
    outside the house. They poor eye sight, but they have very good hearings.
    So keep quiet! You should search for tools in the house that can help
    you escape as fast as possible.
print Possible Actions
    You can input four actions to play the game:
    search (search for items in furniture to help you escape )
    use (use an item in your inventory)
    take (add items from furniture to your inventory)
    transform (change item to another shape)
print Help Options

MAIN Code
    Initialize
    get INPUT action from player
    when input Search or search
        Ask: where do you want to search?
        verify if the name of the furniture is in the house
        if yes:
            FUNITURE.search
        else:
            warning: furniture not in the room
            print out name of furniture in the house

    when input Use or use
        Ask: what do you want to use?
        verify if the name of the item is in inventory
        if yes:
            Ask: what do you want to use it on?
            verify if the name of the target is in room
            if yes:
                ITEM.use(target)
            else:
                warning: target not in the room
        else:
            warning: you do not have this item

    when input Take or take
        This is only functional after you just searched a furniture
        Ask: what do you want to take?
        verify if the name of the item is in the furniture being searched
        if yes:
            ITEM.take
        else:
            warning: you cannot reach this item

    when input Transform or transform
        Ask: what do you want to transform?
        if item is "Paper Clip":
            transform to pointy, thin shape
            add TransformedPaperClip to ITEM class
            add TransformedPaperClip to inventory
        else:
            warning: you cannot transform this item

    when input is not the four actions
        warning: This action is not valid.
        print out the possible actions and ask player to enter one of them

class ME
attribute
    inventory

class FUNITURE
    attribute
        name
        items
    method
        add_item(item_name)
            items.append(item_name)
        search
            for item in items:
                print(item)

Different furniture in the room include:
sofa
cupboard
shelf
painting
window
box (hidden in painting)


class ITEM
    attribute
        name
        belong_to_funiture
        can_be_used_on
    method
        take
            furnitue.removeItem
            me.addItem
        use
            validate target with can_be_used_on
            if True:
                useItem
            else:
                display warning
        useItem
            blank method

Different items in the room include:
painting piece (under sofa)
matches (under sofa)
ice cube (on shelf)
hammer (on cupboard)
photo (on cupboard)
paper clip (hidden inside painting)
bomb (inside box)

Some special function performed by different items in the ITEM class
class key extend ITEM
    useItem
        Open door, success
        end MAIN

class PaintingPiece extend ITEM
    useItem
        Painting disappear, shown hidden shelf
        add hidden shelf to FUNITURE

class hammer extend ITEM
    useItem
        if target == "Ice cube":
            Broke Ice cube, but aliens heard you. You are caught. You failed.
            Health = 0
        if target == "Window"
            Broke window, but aliens heard you. You are caught. You failed.
            Health = 0

class mathes extend ITEM
    useItem
        Ice cube melt, got key.
        me.addKey

class bomb extend ITEM
    useItem
        Bomb exploded, you died.
        Health = 0

class TransformedPaperClip extend ITEM
    useItem
        Open door, success
        end MAIN
