
# Manny Pagan
# Sept 24th Python Course
# Assignment 3
# Due: Oct 8th



disney_characters = ["simba", "ariel", "pumba", "flounder", "nala", "ursula", "scar", "flotsam", "timon"]
# vowels = ['a', 'e', 'i', 'o', 'u']

def isVowel(disney_characters):
    for character in disney_characters:
        if any(u.lower() in 'u' for u in character):
            print(character + " U are so Uniquely U!")
        elif any(i.lower() in 'i' for i in character):
            print(character + " I bet you're Impressively Intelligent!")
        elif any(o.lower() in 'o' for o in character):
            print(character + " O My! How Original!")
        else:
            print(character + "...ehh, a's and e's are so ordinary.")
isVowel(disney_characters)
