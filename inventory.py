# Date created: 20/02/13
# Date last modified: 20/02/13
# Description: Inventory for Escape Room

tools = ['Flower', 'Time Extender']
special_tools = ['Seed']
print(tools)
print(f"{special_tools}\n")

special_tools.append(tools.pop(1))
print(tools)
print(f"{special_tools}\n")

del tools[0]
print(tools)
print(f"{special_tools}\n")

tools.append('Matches')
print(tools)
print(f"{special_tools}\n")

tools.insert(0,'Hammer')
print(tools)
print(f"{special_tools}\n")

tools.append('Key')
print(tools)
print(f"{special_tools}\n")

tools.append('Paper Clip')
print(tools)
print(f"{special_tools}\n")

special_tools.remove('Seed')
print(tools)
print(f"{special_tools}\n")

special_tools.append('Invisible Cloak')
print(tools)
print(f"{special_tools}\n")

tools.sort()
print(tools)
print(f"{special_tools}\n")

print(f"{sorted(tools, reverse=True)}\n")

special_tools.reverse()
print(tools)
print(f"{special_tools}\n")

print(len(tools))
print(f"{len(special_tools)}\n")

print("Your tools are: ")
for tool in tools:
    print(f"\t{tool}")

print("\nYour special tools are: ")
for a in special_tools:
    print(f"\t{a}")
