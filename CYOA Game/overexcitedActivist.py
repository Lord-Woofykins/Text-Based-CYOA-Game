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

def challengeSpeechContest():
    messagePrinter("Threadit            r/Politics")
    username = inputHandler("Choose your username: ")
    print()
    messagePrinter("Threadit            r/Politics")
    messagePrinter(f"{username}: I hate cheese! #CheeseIsBad")
    messagePrinter("| 1. Upvote (21) | 2. Downvote (7) | 3. Comments (4) |")
    print()

    messagePrinter("Comments:")
    messagePrinter("1. I agree, cheese is the worst!")
    messagePrinter("2. I'm chonky and like cheese, but I respect your opinion.")
    messagePrinter("3. u/CheeseVigilante42: Oh. Oh, you hate cheese? You just wake up in the morning and decide to be objectively wrong? CHEESE IS THE BACKBONE OF SOCIETY. You think you’re better than the entirety of France? THAN THE GRANDMA IN ITALY HANDMAKING MOZZARELLA RIGHT NOW? I bet your fridge is just air and despair. #CheeseIsLife")

    messagePrinter("1 reply:")
    response = inputHandler("Open? (y/n) ")
    if response == "y":
        messagePrinter("u/Chonky: I hope you choke on a cracker. I hope you get a paper cut on your tongue. I hope you step on a lego. I hope you get a splinter under your fingernail. I hope you get a popcorn kernel stuck in the back of your throat. I hope you get a blister. I hope you get a pimple in your ear. I hope you get a mosquito bite on your eyelid. I hope you get a sunburn on your scalp. I hope you get a cramp in your foot. I hope you get a headache. I hope you get a stomach ache. I hope you get a toothache. I hope you get a brain freeze.")
    print()
    
    messagePrinter("Speech Contest!" + "\n" + "Write the best (angriest) speech possible!")
    print()
    
    speechScore = 0
    speech = input("Speech: ")
    #Scoring added for length
    if len(speech.split()) > 50:
        speechScore += 2
    elif len(speech.split()) >= 30:
        speechScore += 1
    #Scoring added for keywords
    keywords = ["cheese", "hate", "anger", "rage", "disgust", "pooky", "france", "italy", "mozzarella", "grandma", "backbone", "society", "wrong", "despair", "life"]
    for keyword in keywords:
        if keyword in speech.lower():
            speechScore += 1
    speechScore += speech.count("!") + speech.count("?") #Scoring added for punctuation
        
    if speechScore < 6:
        messagePrinter("u/CheeseVigilante42: And THERE IT IS, folks! He crumbles.")
        if len(speech.split()) < 30:
            messagePrinter("u/CheeseVigilante42: Imagine not even bothering to write a proper length comeback.")
        elif "cheese" not in speech.lower():
            messagePrinter("u/CheeseVigilante42: Didn't even mention cheese.")
        elif speech.count("!") == 0:
            messagePrinter("u/CheeseVigilante42: No exclamation points? No ALL CAPS? No insults? You call that a speech?")
        elif speech.count("?") == 0:
            messagePrinter("u/CheeseVigilante42: No rhetorical questions? No insults? You call that a speech?")
        elif len(speech.split()) < 50:
            messagePrinter("u/CheeseVigilante42: Could've spent more time on that one instead of rage quitting.")
        print()
        messagePrinter("You have lost the speech contest. Words hurt.")
        response = inputHandler("Try again? (y/n) ")
        while response != "y" and response != "n":
            response = inputHandler("Try again? (y/n) ")
        if response == "n":
            global scene 
            scene = "end"
        else:
            challengeSpeechContest()


# Print messages with a delay between letters
def messagePrinter(message):
    for letter in message:
        if letter == " ":
            time.sleep(writeDelay + writeDelay * spaceDelayMultiplier)    
        print(letter, end="", flush=True)
        time.sleep(writeDelay)
    print()

#Setting keybinds and interacting with the player's responses
def keyBindHandler():
    global inventoryBind, healthBind #Accessing the global variables to change them
    response = input("Change key bindings? (y/n)").lower()
    while response != "y" and response != "n": #Checking if the response is either y or n
        messagePrinter("Please enter a valid response.")
        response = input("Change key bindings? (y/n)").lower()

    if response == "y": #Checking if the user wants to change the keybinds
        inventoryBind = input("Inventory: ")

        #Making sure the keybinds are unique of each other and important options
        while inventoryBind in ["1", "2", "3", "4", "", "True", "False"]:
            messagePrinter(f"[{inventoryBind}] is already bound to an option, please choose another key.")
            inventoryBind = input("Inventory: ")
        healthBind = input("Health: ")
        while healthBind in ["1", "2", "3", "4", "", "True", "False", inventoryBind]:
            if healthBind == inventoryBind:
                messagePrinter(f"[{inventoryBind}] is already bound to inventory, please choose another key.")
            elif healthBind in ["1", "2", "3", "4", "", "True", "False"]:
                messagePrinter(f"[{healthBind}] is already bound to an option, please choose another key.")
            healthBind = input("Health: ")
        messagePrinter("Key bindings have been changed, your new key bindings are:")
        messagePrinter(f"Inventory: [{inventoryBind}]" + "\n" + f"Health: [{healthBind}]" + "\n")
    return response

def moveScene(sceneKey):
    global scene
    scene = sceneKey["move"]
    displayScene(scenes[scene])

#Handle inputting from the user and find next scene for booleans
def boolHandler(sceneKey):
    global scene
    try:
        print()
        choice = inputHandler(f"{sceneKey["bool"]} ").lower()
        if choice == 'y':
            scene = f"{scene}-True"
            displayScene(scenes[scene])
        elif choice == 'n':
            scene = f"{scene}-False"
            displayScene(scenes[scene])
        else:
            print("Please input either y/n.")
            boolHandler(sceneKey)
    except ValueError:
        os.system("clear")
        print("There was an error with inputting, please input either y/n.", "\n")
        boolHandler(sceneKey)


# Handle user input and navigate to the next scene
def optionHandler(sceneKey):
    global scene #Accessing the scene variable globally so that changes are kept
    choice = 0 #Setting the choice to 0 to trigger the while loop
    try:
        while choice not in range(1, len(sceneKey["options"])):
            choice = int(inputHandler(sceneKey["options"]["optionText"]))
            if choice not in range(1, len(sceneKey["options"])):
                print("Please enter a valid option.")
        scene = f"{scene}-{choice}"
        displayScene(scenes[scene])
    except ValueError:
        os.system("clear")
        print("There was an error with inputting, please input a number.", "\n")
        optionHandler(sceneKey)

# Display the current scene and its options
def displayScene(sceneKey):
    messagePrinter(sceneKey["text"]) #Displaying the text of the scene
    if "item" in sceneKey: #Adding any items to the inventory
        inventory.append(sceneKey["item"])
        print()
        messagePrinter(f"A {sceneKey["item"]} has been added to you inventory!")

    if "options" in sceneKey: # Checking if there are options to choose from
        #Displaying the options
        for key, option in sceneKey["options"].items():
            if key != "optionText":
                messagePrinter(f"{key.title()}: {option}")
        print()
        
        optionHandler(sceneKey) #Requesting input to trigger game progression

    elif "bool" in sceneKey: #Checking if there is a boolean to choose from
        boolHandler(sceneKey)

    elif "move" in sceneKey: #Move to the next scene
        moveScene(sceneKey)
    
    elif "challengeSpeech" in sceneKey:
        messagePrinter(sceneKey["challengeSpeech"])
        challengeSpeechContest()
    


#Handle general inputting from the user
def inputHandler(inputText):
    #Asking for input to trigger requested functions
    response = input(inputText)
    if response == inventoryBind: #Showing inventory contents
        if inventory:
            messagePrinter("Inventory:")
            print()
            for item in inventory:
                messagePrinter(item.strip().title())
            print()
        else:
            messagePrinter("Inventory is empty.")
        inputHandler(inputText)
    elif response == healthBind: #Showing health
        messagePrinter(f"Health: {health}")
        inputHandler(inputText)

    return response #Returning a response to be used by functions such as optionHandler or boolHandler


#Display opening text and handle calling of keybind function
def intro():
    #Displaying opening text & info
    messagePrinter("Welcome To Overexcited Activist!" + "\n")
    time.sleep(0.2)
    messagePrinter("Controls:")
    messagePrinter(f"Inventory: [{inventoryBind}]" + "\n" + f"Health: [{healthBind}]" + "\n")
    time.sleep(0.2)

    #Requesting changes to keybinds of inventory and health
    response = keyBindHandler()
    if response != "n": #Checking if confirmation is necessary
        response = input("Confirm bindings? (y) ").lower()
        while response != "y": #Looping until the user confirms the keybinds
            keyBindHandler()
            response = input("Confirm bindings? Note: [n] will retain new bindings. (y/n) ").lower()
    
    inputHandler("Begin? ") #Requesting input to begin the game
    os.system("clear")

# Game Loop
scene = "scene1" #Set the starting scene
intro() #Call into to the game
while scene != "end":
    displayScene(scenes[scene])