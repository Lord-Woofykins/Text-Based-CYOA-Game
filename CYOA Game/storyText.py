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
            "optionText": "What will you pick? (1-3) "
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
    "scene3A-1": {
        "text": ["You join their party under the facade of an active citizen who wants the best for the party’s values. One day, upon promotion to the big leagues of the party, you walk into the senior office to notice a poster on the wall: A citizen may not injure a senior being or, through inaction, allow a senior being to come to harm. A citizen must obey the orders given it by senior beings except where such orders would conflict with the First Law. A citizen must protect its own existence as long as such protection does not conflict with the First or Second Law."],
        "bool": "Ignore the poster? (y/n) "
    },
    "scene3A-1-True": {
        "text": ["Further into the office, you notice an unlocked computer that is sitting inconspicuousky, such that only someone looking for anything ot of the ordinary would find it. Written on the monitor screen, a google maps location of a factory is open, alongside the words: 'Secret environmentally non-compliant factory protected by major donors'"],
        "move": "scene5B-2"
    },
    "scene3A-1-False": {
        "text": ["As you think about it, the place that you have been working in does seem kind of like a factory. You think back to all of the oddities that you overlooked over your time with the party. All of the 'favours' that the party had you do."],
        "move": "scene7B"
    },

    #Scene 3B
    "scene3B": {
        "text": ["While setting up, a passer by starts bugging you to let him join. However, you already have a full party. Kick out your best friend for him?"],
        "bool": "Kick out best friend? (y/n)"
    },
    "scene3B-True": {
        "text": ["Your friend is super mad, and grumbles to himself about how he should’ve stayed at uni instead of joining you. He will remember this."],
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
        "text": ["You continue to set up, and together with your friend begin your “peaceful” protest. While you are chanting on your megaphone, a angry looking person shows up and initiates a fight."],
        "challengeFight": "You get up and make towards them, however as they turn towards you a realisation comes over you that there's no going back now."
    },
    "scene4B-1": {
        "text": ["You lose, health depleted you are rushed to hospital. It was at this moment that you realised that Australia just abolished medicare because the internet said “it wastes too much money”"],
        "boolMoney": "Pay up? (y/n) ",
        "boolMoneyFail": "You don't have any money to give, so you end up dying in the hospital."
    },
    "scene4B-True": {
        "text": ["Luckily, you could afford healthcare, but it cost all of your money. Unfortunately what you find out when you get out of hospital makes you sick to your stomach."],
        "move": "scene5B"
    },
    "scene4B-2": {
        "text": ["You have defeated the nimby, and the crowd cheers. Looking at the fallen nimby, you feel a sense of satisfaction, but also a twinge of guilt. In their coat pocket, you find a wallet. You take it before handing him over to the ambulance."],
        "item": "wallet",
        "move": "scene5B"
    },
    "scene4B-3": {
        "text": ["You have won the fight, but at what cost?."],
        "move": "scene5B"
    },
    #Scene 5A

    #Scene 5B
    "scene5B": {
        "text": ["You come out of hospital to find out some terrible news. The media has covered your protest, however instead of focusing on the changes that you wanted to publicise, they “expose” you as unhinged radicalists."],
        "options": {
            "option1": "Respond to the media",
            "option2": "Sabotage a factory",
            "optionText": "You decide to take a more hands on approach. What is your next action? (1-2) "
        }
    },
    "scene5B-1": {
        "text": ["Let's correct their opinions.", "BLUE"],
        "move": "scene2-1-1"
    },
    "scene5B-2": {
        "text": ["You get everyone together to go out to an industrial park and to sabotage a factory there."],
        "options": {
            "option1": "Public Transport",
            "option2": "Private Dirty Automotive Vehicle",
            "optionText": "How do you get there? (1-2) "
        }
    },
    "scene5B-2-1": {
        "text": ["Public transport #1!!! On the way, you look out of the window and gain urban knowledge. +1 stealth boost."],
        "stealth": 1,
        "move": "scene6B"
    },
    "scene5B-2-2": {
        "text": ["You drive in your loud, emission creating car. This is a poor way to spend your time and it makes you tired. You lose 1 stealth."],
        "stealth": -1,
        "move": "scene6B"
    },
    #Scene 6A

    #Scene 6B
    "scene6B": {
        "text": ["You sneak into the factory, however you notice a guard nearby."],
        "challengeSneak": "You must attempt to sneak past the guard by entering 'sneak' at the right moment.",
    },
    "scene6B-Success": {
        "text": ["You stroll into the factory, very nonchalant, very demure, and hack the emissions data."],
        "move": "scene7B"
    },
    "scene6B-Fail": {
        "text": ["You are caught by the guard."],
        "boolMoney": "scene8B",
        "boolMoneyFail": "You are sent to jail for a long time."
    },
    "scene6B-Fail-True": {
        "text": ["Bribery always works, well done."],
        "move": "scene7B"
    },
    
    #scene7B
    "scene7B": {
        "text": ["What you see shocks you, and after fleeing the facility you leak the classified information, ensuring that the government finds out."],
        "move": "scene7B-1"
    },
    "scene7B-1": {
        "text": ["The government is so proud of your work and effort that they elect you as a parliment member. While you are voting, you give in to lobbyists for nuclear energy. Australia becomes a leading country in nuclear power."],
        "bool": "This is what you always wanted, right? (y/n)",
    },
    "scene7B-1-True": {
        "text": ["Isn’t this what you always wanted? You go along with the building of nuclear plants. Despite intense lobbying from the coal and gas companies, they end up closing down as intense US backed subsidies drive all energy competition out of the market."],
        "move": "scene7B-1-True-1"
    },
    "scene7B-1-False": { 
        "text": ["You have a change of heart. You see the error in your ways and decide to flee the city before it’s too late."],
        "countrysideEnding": True,
        "move": "scene8B"
    },
    "scene7B-1-True-1": {
        "text": ["All is well and good, because this is what you wanted, right? Nuclear volatility increased by 1"],
        "nuclearVolatility": 1,
        "move": "scene7B-1-True-2"
    },
    "scene7B-1-True-2": {
        "text": ["Nuclear meltdown is imminent provide calming words to cool it down!!!!!"],
        "challengeMeltdown": "Write 'calm' as many times as you can!",
    },
    "scene7B-1-True-2-1": {
        "text": ["Issue resolved. Signs of rebellion are beginning to show, but its all good because this is what you always wanted. Nuclear volatility increased by 1"],
        "nuclearVolatility": 1,
        "move": "scene7B-1-True-2-2"
    },
    "scene7B-1-True-2-2": {
        "text": ["Nuclear meltdown is imminent provide calming words to cool it down!!!!!"],
        "challengeMeltdown": "Write 'calm' as many times as you can!",
    },
    "scene7B-1-True-2-2-1": {
        "text": ["No problem, your quick thinking save the day yet again. It seems as though you were made for this job, right? Sitting around, doing nothing but approving nuclear proposals. Nuclear volatility increased by 1"],
        "nuclearVolatility": 1,
        "move": "scene7B-1-True-2-2-2"
    },
    "scene7B-1-True-2-2-2": {
        "text": ["Nuclear meltdown is imminent provide calming words to cool it down!!!!!"],
        "challengeMeltdown": "Write 'calm' as many times as you can!",
    },
    "scene7B-1-True-2-2-2-1": {
        "text": ["This must’ve just been what you always wanted after all. Unless? You hear an odd sound that seems kind of like a siren."],
        "move": "scene8B"
    },

    #Scene 8B
    "scene8B": {
        "text": ["A nuclear reactor blows up, and since they were all in such close proximity, a chain reaction happens."],
        #Peacefull ending
        "peacefullEnding": "You declare yourself the leader of a self proclaimed eco-state. Far away from the city, the nuclear meltdown doesn’t effect you and your group of survivors. Everyone lives in the forest, entirely off the grid in your green utopia. Zero carbon emissions required.",
        #Government bunker ending
        "mainEnding": "Acid rain falls overhead as the streets are showered in nuclear waste. The smoke in the air makes it difficult to breath as you run to the government bunker specifically made for this purpose under Parliament House. You ignore the fact that millions of lives are to perish any second as the lid of the bunker seals shut. But hey, if there’s no-one alive to create the carbon emissions, you got what you wanted after all. Right? Go you!"
    },
}