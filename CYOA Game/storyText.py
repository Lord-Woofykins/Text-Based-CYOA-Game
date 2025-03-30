scenes = {
    #Scene 1
    "scene1": {
        "text": ["You wake up in a small rental unit, your little abode where you have been forced to retreat to after your parents kicked you from their home.", "BLUE"],
        "options": {
            "option1": "Get out of bed and look around",
            "option2": "Stay in bed",
            "option3": "Cry",
            "option4": "Take a walk outside",
            "optionText": "What will you do? (1-4) "
        }
    },
    "scene1-1": {
        "text": ["You decide to take a proactive step towards a brighter future, and get out of bed. You look around your small room, and see the mess that you have been living in. Your mother's voice echoes in your mind, 'Stop living like a pig!' she would say. You chuckle to yourself, turn your back on the dump that is your room and sit down at your computer."],
        "bool": "See Specs? (y/n)"
    },
    "scene1-1-True": {
        "text": ["9800x3d, 5090D (You aren’t Chinese or anything, it's just that the global version was sold out), 128gb Ram, 2tb SSD"],
        "item": "screwdriver",
        "move": "scene2"
    },
    "scene1-1-False": {
        "text": ["How disappointing."],
        "move": "scene2"
    },
    "scene1-2": {
        "text": ["To take your mind off of your depressing life as a uni student working minimum wage at McDonalds, you pick up your phone and start doomscrolling down political rabbit holes and engulfing yourself in social media hate bubbles"],
        "move": "scene2"
    },
    "scene1-3": {
        "text": ["You cry. For a very long time."],
        "move": "scene2"
    },
    "scene1-4": {
        "text": ["You decide to take a walk outside, and as you walk through the park, you see a group of people gathered together, holding signs and chanting slogans. You are intrigued, and you decide to join them. You feel a sense of belonging and purpose as you march with the group, someone even offered you a sandwich, and you realize that you have found your calling as an activist."],
        "item": "sandwich",
        "move": "scene2"
    },
    
    #Scene 2
    "scene2": {
        "text": ["You become fixated on the idea that you can change anything. It all starts with you."],
        "options": {
            "option1": "Go through a get rich quick scheme.",
            "option2": "Solve climate change, it can't be that hard.",
            "optionText": "What kind of difference will you make? (1-2) ",
        }
    },

    #Beginning of political path
    "scene2-1": {
        "text": ["After going down a get rich quick scheme, you begin to realise that the influencial game is easier than you realise."],
        "options": {
            "option1": "Online",
            "option2": "Joining the local political party",
            "optionText": "How do you want to become popular? (1-2) "
        }
    },
    "scene2-1-1": {
        "text": ["You retreat to your parent’s basement to write hate speech on twitter and reddit."],
        "move": "scene2-1-2"
    },
    "scene2-1-2": {
        "text": ["While you are on one of your more radical rants, someone who thinks they know soooooo much better decides to challenge your opinions."],
        "challengeSpeech": "Challenge them?",
    },
    "scene2-2": {
        "text": ["You come up with a few key solutions"],
        "options": {
            "option1": "Recycling",
            "option2": "Renewables",
            "option3": "Replace coal with nuclear",
            "optionText": "What will you pick?"
        }
    },
    "scene2-2-1": {
        "text": ["After much deliberation, you come up with a resolve that everyone must recycle. You start a campaign to educate the masses on the importance of recycling, and you even go as far as to start a recycling program in your community. Noone cared though, so you try something else."],
        "move": "scene2-2"
    },
    "scene2-2-2": {
        "text": ["Renewables must be the future, you think to yourself. There's amazing profit to be had in the energy industry, but that's when it hits you that the renewables market is already saturated. You decide to try something else."],
        "move": "scene2-2"
    },
    "scene2-2-3": {
        "text": ["Replace coal with nuclear. You think to yourself, 'It's so simple, why hasn't anyone thought of this before?' You convince your best friend to help you, as well as a bunch of extremists from Twitter (aka Elon media) and Instagram to help you and decide to protest at the council office for change."],
        "move": "scene3B"
    },

    #Scene 3A
    "scene3A": {
        "text": ["A political party offers you the chance of a lifetime to join their legions as a proud supporter. However, hours of scrolling TikTok have given you a better idea. You decide to join as a double agent, bent on exposing their corruption."],
        "move": "scene3A-1"
    },

    #Scene 3B
    "scene3B": {
        "text": ["While setting up, a passer by starts bugging you to let him join. However, you already have a full party. Kick out your best friend for him?"],
        "bool": "Kick out best friend?"
    },
    "scene3B-True": {
        "text": ["Your friend is super mad, and grumbles to himself about how he should’ve stayed at uni instead of joining you. He will remember this."],
        "harderPoliticalEnding": True,
        "move": "scene3-True-1"
    },
    "scene3B-False": {
        "text": ["You tell the passerby that you already have a full party. He shows you a briefcase of cash, before turning to walk away."],
        "opportunity": ["screwdriver", "Stab and rob him with the screwdriver? (y/n)"]
    },
    "scene3B-False-1": {
        "text": ["You are successful in your plight, and gain thousands of dollars. Unfortunartely, your ltt screwdriver is broken. Linus will remember this.", "GREEN"],
        "item": "briefcase",
        "removeItem": "screwdriver",
        "move": "scene4B"
    },
    "scene3B-False-2": {
        "text": ["You are unsuccessful in your plight, and the passerby is furious. Your screwdriver is stolen by the man, and you are slightly hurt.", "RED"],
        "removeItem": "screwdriver",
        "health": -20,
        "move": "scene3B-False-3"
    },
    "scene3B-False-3": {
        "text": ["The man gets away, but that’s ok because after all it’s all about the friends we made along the way."],
        "move": "scene4B"
    },

    #Scene 4A

    #Scene 4B
    "scene4B": {
        "text": ["You continue to set up, and together with your friend begin your “peaceful” protest. While you are chanting on your megaphone, a nimby shows up and initiates a fight."],
        "challengeFight": "You get up and make towards them and realise that there's no going back now as they turn towards you."
    },
}
