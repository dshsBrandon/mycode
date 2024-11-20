#!/usr/bin/env python3

# Dictionary of Marvel characters
marvelchars = {
    "Starlord": {
        "real name": "peter quill",
        "powers": "dance moves",
        "archenemy": "Thanos"
    },
    "Mystique": {
        "real name": "raven darkholme",
        "powers": "shape shifter",
        "archenemy": "Professor X"
    },
    "Hulk": {
        "real name": "bruce banner",
        "powers": "super strength",
        "archenemy": "adrenaline"
    }
}

# Get user input
char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk): ").capitalize()
char_stat = input("What statistic do you want to know about? (real name, powers, archenemy): ").lower()

# Extract the appropriate value from the dictionary

# Starlord stats
if char_name == "Starlord":
    if char_stat == "real name":
        value = marvelchars["Starlord"]["real name"].title()
    elif char_stat == "powers":
        value = marvelchars["Starlord"]["powers"]
    elif char_stat == "archenemy":
        value = marvelchars["Starlord"]["archenemy"]
    else:
        value = "Statistic not found."

# Mystique stats
elif char_name == "Mystique":
    if char_stat == "real name":
        value = marvelchars["Mystique"]["real name"].title()
    elif char_stat == "powers":
        value = marvelchars["Mystique"]["powers"]
    elif char_stat == "archenemy":
        value = marvelchars["Mystique"]["archenemy"]
    else:
        value = "Statistic not found."

# Hulk stats
elif char_name == "Hulk":
    if char_stat == "real name":
        value = marvelchars["Hulk"]["real name"].title()
    elif char_stat == "powers":
        value = marvelchars["Hulk"]["powers"]
    elif char_stat == "archenemy":
        value = marvelchars["Hulk"]["archenemy"]
    else:
        value = "Statistic not found."

# Default value
else:
    value = "Character not found."

# Print the output
print(f"{char_name}'s {char_stat} is: {value}")

