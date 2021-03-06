# Date created: 20/03/10
# Date last modified: 20/03/12
# Description: Character info, Inventory and Location


# Character's basic information.
character = {
    'description': 'You are going to just be yourself in this game',
    'num_of_life': 1,
    'location': 'You are locked inside a house guared by aliens.',
    'objective': 'You goal is to escape the house as quickly as possible.'
}

# All inventory items and their description.
inventory = {
    'tools': {
        'matches': {
            'description': 'Can start fire'
            },
        'hammer': {
            'description': 'Can break things but could be loud'
            },
        'key': {
            'description': 'Can open the door'
            },
        'paper clip': {
            'description':
            'Made of thin, hard metal, not sure about its function'
            }
        },
    'special tools': {
        'invisible cloak': {
            'description': 'Can make your body invisible'
            },
        'time extender': {
            'description': 'Can increase the time you have to escape the room'
            }
        }
    }

# All location in the game and their descriptions.
location = {
    'sofa': {
        'description': 'It is in the middle of the room.'
        },
    'cupboard': {
        'description':
        'It is along the inner side of the room. It has 2 drawers.',
        'first drawer': 'some message',
        'second drawer': 'some message'
        },
    'shelf': {
        'description':
        'It is along the inner side of the room. It has 2 levels.',
        'first level': 'some message',
        'second level': 'some message'
        },
    'painting': {
        'description':
        'On the wall opposite to sofa. The painting is missing a corner.',
        'box': 'some message'
        },
    'window': {
        'description': 'It is on the wall opposite to shelf and cupboard.',
        },
    'door': {
        'description':
        'The door of the house. You need to escape out from here.',
        },
    }

# Print out basic character information.
# print("\nCHARACTER\n")
# print(f"Description: {character['description']}")
# print(f"Number of lives each game: {character['num_of_life']}")
# print(f"Location: {character['location']}")
# print(f"Objective: {character['objective']}\n\n")


# Print out all inventory and their descriptions.
# print("INVENTORY\n")
# for type_tool, tool_name in inventory.items():
#     print(f"{type_tool.title()}:")
#     for tool_name, tool_info in tool_name.items():
#         print(f"\t{tool_name.title()}:")
#         print(f"\tDescription: {tool_info['description']}\n")

# Print out all locations and their descriptions.
# print("\nLOCATIONS")
# for loc_name, detail in location.items():
#     print(f"\n\t{loc_name.title()}:")
#     print(f"\tDescription: {detail['description']}")
#     if loc_name == 'cupboard':
#         print(f"\tFirst drawer: {location['cupboard']['first drawer']}")
#         print(f"\tSecond drawer: {location['cupboard']['second drawer']}")
#     if loc_name == 'shelf':
#         print(f"\tFirst level: {detail['first level']}")
#         print(f"\tSecond Level: {detail['second level']}")
#     if loc_name == 'painting':
#         print(f"\tBox: {detail['box']}")

Health = 0
Search = 0
start = input("Do you want to start the game?").lower().strip()
if start == "yes":
    Health = 1

if Health == 1:
    print("\nYou can take 4 actions in this game:")
    print("\tSearch\n\tUse\n\tTake\n\tTansform")

while Health == 1:
    ask = input("\nWhat action do you want to take?").lower().strip()
    if ask == "search":
        Search = 1
        while Search == 1:
            a_search = input("\nWhere do you want to search?").lower().strip()
            if a_search in location.keys():
                print("\nYes")
                Search = 0
            else:
                print("\nThis location is not in the room.The valid locations are:")
                for _ in location:
                    print(f"\t{_}")
    elif ask == "use":
        a_use = input("\nwhat do you want to use?").lower().strip()
        if a_use in inventory.values():
            print("\nYes")
        else:
            print("\nThis item is not in the room. The valid items are:")
            for _, a in inventory.items():
                for b in a.keys():
                    print(f"\t{b}")
    elif ask == "take":
        print("Take")
    elif ask == "transform":
        print("Transform")
    else:
        print("\nInvalid Action!")
        print("Please enter a valid action word.\nValid actions:" +
        "\n\tSearch\n\tUse\n\tTake\n\tTansform")
