import os
import time
from storyText import scenes

# Clear the terminal 
os.system("clear")

# Stats
itemTypes = {
    "weapon": ["screwdriver"],
    "money": ["wallet", "briefcase"],
    "food": ["apple", "sandwich"],
}

inventory = ["apple"]
health = 100

inventoryBind = "z"
healthBind = "x"

# Print statements below this point
print(os.getcwd())

writeDelay = 0.005
spaceDelayMultiplier = 1.1

# Functions below this point

# Print messages with a delay between letters
def messagePrinter(message):
    for letter in message:
        if letter == " ":
            time.sleep(writeDelay + writeDelay * spaceDelayMultiplier)    
        print(letter, end="", flush=True)
        time.sleep(writeDelay)
    print()

#Setting keybinds and interacting with the player
def keyBindHandler():
    global inventoryBind, healthBind
    response = input("Change key bindings? (y/n)").lower()
    while response != "y" and response != "n":
        messagePrinter("Please enter a valid response.")
        response = input("Change key bindings? (y/n)").lower()
    if response == "y":
        inventoryBind = input("Inventory: ")
        while inventoryBind in ["1", "2", "3", "4"]:
            messagePrinter(f"[{inventoryBind}] is already bound to an option, please choose another key.")
            inventoryBind = input("Inventory: ")
        healthBind = input("Health: ")
        while healthBind in ["1", "2", "3", "4", inventoryBind]:
            if healthBind == inventoryBind:
                messagePrinter(f"[{inventoryBind}] is already bound to inventory, please choose another key.")
            elif healthBind in ["1", "2", "3", "4"]:
                messagePrinter(f"[{healthBind}] is already bound to an option, please choose another key.")
            healthBind = input("Health: ")
        messagePrinter("Key bindings have been changed, your new key bindings are:")
        messagePrinter(f"Inventory: [{inventoryBind}]" + "\n" + f"Health: [{healthBind}]" + "\n")
    return response

# Display the current scene and its options
def displayScene(sceneKey):
    messagePrinter(sceneKey["text"])
    if "item" in sceneKey:
        inventory.append(sceneKey["item"])
        print()
        messagePrinter(f"A {sceneKey["item"]} has been added to you inventory!")
    if "options" in sceneKey:
        response = inputHandler(sceneKey)
        optionHandler(sceneKey, response)
    elif "bool" in sceneKey:
        response = inputHandler()
        boolHandler(sceneKey)
    elif "move" in sceneKey:
        moveScene(sceneKey)

def moveScene(sceneKey):
    global scene
    scene = sceneKey["move"]
    displayScene(scenes[scene])

#Handle inputting from the user and find next scene for booleans
def boolHandler(sceneKey):
    global scene
    try:
        print()
        choice = input(f"Bool: {sceneKey["bool"]} ").lower()
        if choice == 'y':
            scene = f"{scene}-True"
            displayScene(scenes[scene])
        elif choice == 'n':
            scene = f"{scene}-False"
            displayScene(scene)
        else:
            print("Please input either y/n.")
            boolHandler(sceneKey)
    except ValueError:
        os.system("clear")
        print("There was an error with inputting, please input either y/n.", "\n")
        boolHandler(sceneKey)


# Handle user input and navigate to the next scene
def optionHandler(sceneKey):
    global scene
    for key, option in sceneKey["options"].items():
        if key != "optionText":
            messagePrinter(f"{key.title()}: {option}")
    print()
    if "optionText" in sceneKey["options"]:
        choice = 0
        try:
            while choice not in range(1, len(sceneKey["options"])):
                choice = int(input(sceneKey["options"]["optionText"]))
                if choice not in range(1, len(sceneKey["options"])):
                    print("Please enter a valid option.")
            scene = f"{scene}-{choice}"
            displayScene(scenes[scene])
        except ValueError:
            os.system("clear")
            print("There was an error with inputting, please input a number.", "\n")
            optionHandler(sceneKey)

#Handle general inputting from the user
def inputHandler(inputText):
    response = input(inputText)
    if response == inventoryBind:
        if inventory:
            messagePrinter("Inventory:")
            print()
            for item in inventory:
                messagePrinter(item.strip().title())
            print()
        else:
            messagePrinter("Inventory is empty.")
        inputHandler(inputText)
    elif response == healthBind:
        messagePrinter(f"Health: {health}")
        inputHandler(inputText)

def intro():
    messagePrinter("Welcome To Overexcited Activist!" + "\n")
    time.sleep(0.2)
    messagePrinter("Controls:")
    messagePrinter(f"Inventory: [{inventoryBind}]" + "\n" + f"Health: [{healthBind}]" + "\n")
    time.sleep(0.2)
    response = keyBindHandler()
    if response != "n":
        response = input("Confirm bindings? (y) ").lower()
        while response != "y":
            keyBindHandler()
            response = input("Confirm bindings? Note: [n] will retain new bindings. (y/n) ").lower()
    inputHandler("Begin? ")
    os.system("clear")

# Game Loop
scene = "scene1"
intro()
while scene != "end":
    displayScene(scenes[scene])