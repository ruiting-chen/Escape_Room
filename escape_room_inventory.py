# Date created: 20/02/13
# Date last modified: 20/02/13
# Description: Inventory for Escape Room

# Create 2 lists, tools and special_tools, with initial elements.
tools = ['Flower', 'Time extender']
special_tools = ['Seed']
print(tools)
print(f"{special_tools}\n")

# Changing elements in tools list.
# Delete 'Flaower' and add 'Matches', 'Hammer', 'Key', 'Paper clip'.
del tools[0]
print(tools)
tools.append('Matches')
print(tools)
tools.insert(1, 'Hammer')
print(tools)
tools.append('Key')
print(tools)
tools.append('Paper clip')
print(f"{tools}\n")

# Changing elements in special_tools list.
# Pull 'Time extenter' from tools list and insert it in special_tools list.
# Remove 'Seed' and add 'Invisible Cloak' to special_tools list.
special_tools.append(tools.pop(0))
print(tools)
print(special_tools)
special_tools.remove('Seed')
print(special_tools)
special_tools.append('Invisible Cloak')
print(f"{special_tools}\n")

# Changeing the order of elements in tools and special_tools list.
# Put tools list in alphabetical order.
# Present tools list in reverse alphabetical order.
# Reverse the order of elements in special_tools list.
tools.sort()
print(tools)
print(sorted(tools, reverse=True))
special_tools.reverse()
print(f"{special_tools}\n")

# Count the amount of elements in tools and special_tools list.
print(len(tools))
print(f"{len(special_tools)}\n")

# Print out the elements in both lists with a statement.
for tool in tools:
    print(f"{tool} is a tool.")
for st in special_tools:
    print(f"{st} is a special tool.")
