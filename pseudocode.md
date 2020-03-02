Health = 0
Search_time = 0
Search_hidden = 0
Search_box = 0

MAIN STRUCTURE Code
begin(Main) Escape Room Game:
    globel Health
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
            END (Main) Rpg Game

INSTRUCTION Code
print Game title
print Basic Game Setting
print Possible Actions
print Help Options

MAIN Code
    Initialize
    get INPUT
    when Search
        get furnitue name
        validate furniture name
        FUNITURE.search
    when Use
        get item name
        validate item name
        get target name
        validate target name
        ITEM.use(target)
    when Take
        get item name
        validate item name
        ITEM.take
    when Trans
        get item name
        if item == "Paper Clip":
            transform to pointy, thin shape
            add TransformedPaperClip to ITEM
            me.addTransformedPaperClip
        else:
            warning

class ME
attribute
    items

class FUNITURE
    attribute
        name
        items
    method
        search
            for item in items:
                print(item)

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

class key extend ITEM
    useItem
        if target == "Door":
            Open door, success
            end Main

class PaintingPiece extend ITEM
    useItem
        if target == "Painting":
            Painting disapear, shown hidden shelf
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
        if target == "Ice cube":
            Ice cube melt, got key
            me.addKey

class TransformedPaperClip extend ITEM
    useItem
        if target == "Door":
            Open door, success
            end Main
