#!/usr/bin/env python3

# Challenge list
challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

# Trial list
trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

# Nightmare list
nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def first():
    # Extract the strings for the first challenge
    eyes = challenge[2][1]
    goggles = challenge[2][0]
    nothing = challenge[3]

    # Print out the result
    print(f"My {eyes}! The {goggles} do {nothing}!")

def second():
    # Extract the strings for the second challenge
    a = trial[2]["goggles"]
    b = trial[2]["eyes"]
    c = trial[-1] # trial[3]

    # Print out the result
    print(f"My {a}! The {b} do {c}!")

def third():
    #Extract the strings for the third challenge
    x = nightmare[0]["user"]["name"]["first"]
    y = nightmare[0]["kumquat"]
    z = nightmare[0]["d"]

    # Print out the result
    print(f"My {x}! The {y} do {z}!")

first()
second()
third()
