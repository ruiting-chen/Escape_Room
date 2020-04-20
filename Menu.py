# Date created: 19/04/10
# Date last modified: 19/04/12
# Description: Menu of Escape Room Game


# Ask for an action from user.
print("You can take 4 actions in this game:")
print("\tSearch\n\tUse\n\tTake\n\tTansform")
ask = input("\nWhat action do you want to take?").lower().strip()
if ask == "search":
    print("Search!")
elif ask == "use":
    print("Use!")
elif ask == "take":
    print("Take!")
elif ask == "transform":
    print("Transform!")
else:
    print("Invalid action!")
