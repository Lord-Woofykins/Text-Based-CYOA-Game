scenes = {
    #Scene 1
    "scene1": {
        "text": "You wake up in a small rental unit, your little abode where you have been forced to retreat to after your parents kicked you from their home.",
        "options": {
            "option1": "Get out of bed and look around",
            "option2": "Stay in bed",
            "option3": "Cry",
            "option4": "Take a walk outside",
            "optionText": "What will you do? (1-4) "
        }
    },
    "scene1-1": {
        "text": "You decide to take a proactive step towards a brighter future, and get out of bed. You look around your small room, and see the mess that you have been living in. Your mother's voice echoes in your mind, 'Stop living like a pig!' she would say. You chuckle to yourself, turn your back on the dump that is your room and sit down at your computer.",
        "bool": "See Specs? (y/n)"
    },
    "scene1-1-True": {
        "text": "9800x3d, 5090D (You aren’t Chinese or anything, it's just that the global version was sold out), 128gb Ram, 2tb SSD",
        "item": "screwdriver",
        "move": "scene2"
    },
    "scene1-1-False": {
        "text": "How disappointing.",
        "move": "scene2"
    },
    "scene1-2": {
        "text": "To take your mind off of your depressing life as a uni student working minimum wage at McDonalds, you pick up your phone and start doomscrolling down political rabbit holes and engulfing yourself in social media hate bubbles",
        "move": "scene2"
    },
    "scene1-3": {
        "text": "You cry. For a very long time.",
        "move": "scene2"
    },
    "scene1-4": {
        "text": "You decide to take a walk outside, and as you walk through the park, you see a group of people gathered together, holding signs and chanting slogans. You are intrigued, and you decide to join them. You feel a sense of belonging and purpose as you march with the group, someone even offered you a sandwich, and you realize that you have found your calling as an activist.",
        "move": "scene2"
    },
    
    #Scene 2
    "scene2": {
        "text": "You become fixated on the idea that you can change anything. It all starts with you.",
        "options": {
            "option1": "Go through a get rich quick scheme.",
            "option2": "Solve climate change, it can't be that hard.",
            "optionText": "What kind of difference will you make?",
        }
    },

    #Beginning of political path
    "scene2-1": {
        "text"
    },
    "scene2-2": {
        "text": "You come up with a few key solutions",
        "options": {
            "option1": "Recycling",
            "option2": "Renewables",
            "option3": "Replace coal with nuclear",
            "optionText": "What will you pick?"
        }
    },
    "scene2-2-1": {
        "text": "After much deliberation, you come up with a resolve that everyone must recycle. You start a campaign to educate the masses on the importance of recycling, and you even go as far as to start a recycling program in your community. Noone cared though, so you try something else.",
        "move": "scene2-2"
    },
    "scene2-2-2": {
        "text": "Renewables must be the future, you think to yourself. There's amazing profit to be had in the energy industry, but that's when it hits you that the renewables market is already saturated. You decide to try something else.",
        "move": "scene2-2"
    },
    "scene2-2-3": {
        "text": "Replace coal with nuclear. You think to yourself, 'It's so simple, why hasn't anyone thought of this before?' You convince your best friend to help you, as well as a bunch of extremists from Twitter (aka Elon media) and Instagram to help you and decide to protest at the council office for change.",
        "move": "scene3"
    },

    #Scene 3
    "scene3": {
        "text": "While setting up, a passer by starts bugging you to let him join. However, you already have a full party. Kick out your best friend for him?",
        "bool": "Kick out best friend?"
    },
    "scene3-True": {
        "text": "Your friend is super mad, and grumbles to himself about how he should’ve stayed at uni instead of joining you. He will remember this.",
        "harderPoliticalEnding": True,
        "move": "scene3-True-1"
    },
    "scene3-False": {
        "text": "You tell the passerby that you already have a full party, and he walks away.",
        "move": "scene4"
    },
}