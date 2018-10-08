
# Manny Pagan
# Sept 24th Python Course
# Assignment 3
# Due: Oct 8th



## Problem 2: If You're Cold, Sit in a Corner. It's 90 Degrees!
### Skill you're practicing: Writing `while` loops.
# Wow! It's 90 degrees Fahrenheit and you are sweating buckets! Luckily you have air conditioning, but it's really old and kind of finicky. It cools the room by three degrees and shuts off, so you have to keep turning it back on until the temperature gets to where you want it to be. Seventy five sounds much more pleasant than 90, so that's what you're shooting for.

def temp_change():
    temperature = 90
    while temperature > 75:
        print("Temperature is " + str(temperature) + " - crank the AC!")
        temperature -= 3
    if temperature == 75:
        print(str(temperature) + " Ahh, that's better.")
temp_change()
