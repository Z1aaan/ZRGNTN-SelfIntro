# Zhean Ganituen        - @Z1aaan
# March 28, 2022
# Created using: Ren'Py - https://www.renpy.org
# Credits to: sutemo    - https://sutemo.itch.io (for the character sprites)


define z = Character("Zhean", color="#0080ff") #Cyan text color for Zhean

define x = Character("Miss J.", color="#FFFFFF") #White text color for Miss J.

define me = Character("IRL Zhean", color="#FF0000") 

# TODO: For show commands
# `mj` at left
# `zhean` at right
# `me` at center

label start:    
    # The background music
    play music "audio/bgm_ambient.mp3"
    
    scene bg schoolfront
    
    play sound "audio/sfx_footsteps.mp3" volume 1.5
    
    "After a five week break, it is the first day of the third trimester in De La Salle University - Integrated School."
    
    "Zhean's kinda bummed out, because he's back to reality after a really, really long break."
    
    "But he can't really do anything, so he's gonna have to suck it up and buck up."

    scene bg schoolhall
    
    "His third class for the day is his Computational Thinking course, that starts at 12.45 and ends at 14.15."
    
    play sound "audio/sfx_schoolBell.mp3" volume 0.5 #WTH this sfx is TOO LOUD
         
    "Guess he's late again... smh"
    
    scene bg classroom
    
    show mj smile at left
    
    x "Hi class, welcome to your Computational Thinking course."
    
    x "I am Miss J., and I will be your instructor for this course."
    
    show mj delight at left
    
    x "Before we begin with everything, let us introduce ourselves! \nI have already introduced myself, so it is now your turn!"
    
    show mj annoyed at left
    
    x "The first person in my list is Mr. Z- Sh- 'Zean'?, can you go in front and introduce yourself?"
menu:
    "Yes":
        jump main2
    "No":
        jump choice1_no
    
label choice1_no:
    hide mj 
    hide zhean
    
    show me smirk
    
    me "I know, I know... I'm breaking the fourth wall here..."
    
    show me angry
    
    me "But you can't do that!"
    
    show me eyeroll
    
    me "C'mon man... I used up a lot of my time to make this!"
    
    show me disappoint
    
    me "I will pretend that did not happen, and your choice was 'Yes'."
    
    me "Tsk... Hope you learn next time..."
    
    hide me

label main2:
    
    show mj delight at left
    
    x "Nice! Can you come up here 'Zean'"
    
    show zhean nervous at right
    
    show mj smile at left
    
    x "Okay, you may now start introducing yourself."
    
    
    z "Hi I am Zhean..."
    
    show zhean nervouslaugh at right
    
    z "And don't worry, A LOT of people mispronounce my name on the first meeting..."
    
    z "Though my name has no specific pronunciation."
    
    z "Some people pronounce it as Shaun, “Zee-yan”, “Zeen”." 
    
    show zhean laugh at right
    
    z "But most people pronounce it as “J-ean”, as in the french pronunciation of Jean."
    
label interests:    
    
    show mj smile at left
    
    x "What are you interested in, Zhean?"
    
    show zhean nervous at right
menu:    
    "Video Games":
        jump choice2_VG
    "Sitcoms":
        jump choice2_SC
    "I am very uninterested in everything...":
        jump choice2_NO
    
label choice2_VG:
    hide mj fade
    
    show zhean smile at right
    
    z "I guess I am interested in video games."
    
    z "I did compete in the game Overwatch with a Korean team, but I had to quit due to a wrist injury I got while competing."

    hide mj
    
    hide zhean
    
    show me disappoint
    
    me "Breaking the fourth wall again... Wrist pain sucks btw."
    
    show me smirk
   
    me "Okay bye now!"
        
    hide me
    
    show zhean laugh at right
    
    jump main3
    
label choice2_SC:
    hide mj smile
    
    show zhean smile at right
    
    z "Well I am interested in sitcoms, such as the Big Bang Theory, Modern Family, The Good Place, and Schitts Creek."
    
    z "But... Unlike the general sitcom enjoyer, I find Friends and How I Met Your Mother... a snoozefest"
    
    hide mj

    hide zhean
    
    show me smirk
    
    me "Breaking the fourth wall, yet again... Yeah I said it Friends and HIMYM is boring... Fight me!"
    
    show me smile
    
    me "Okay bye now!"
    
    hide me 
    
    show zhean smile at right
    
    jump main3

label choice2_NO:
    show mj annoyed at left
    
    show zhean smirk at right
    
    x "..."
    
    x "Uhm..."
    
    show mj angry at left
    
    x "I DO NOT know what to say after that, but okay... I guess?"    
    
label main3:
    
    show mj smile at left
    
    x "Okay!"
    x "Cool..."
    x "What is something people do not know about you?"
    
    show zhean smile at right
    
menu:
    "I have never watched anime":
        jump choice3_ANIME
    "I Enjoy classical music":
        jump choice3_CM
        
label choice3_ANIME:
    hide mj
    
    show zhean laugh at right
    
    z "It's not something people do not know about me, but it is more of something people get baffled about when they meet me."
    
    show zhean smile at right
    
    z "Is that I have never and don't plan on watching Anime."
    
    hide zhean
    
    show me smirk
    
    me "Kind of ironic how this project is created in a visual novel style."
    
    show me eyeroll
    
    me "Which is quite popular in Japan and the anime culture."
    
    me "But sure... You DON'T watch anime..."
    
    show me disappoint
    
    me "Talk to your collection of Horror Manga"
    
    hide me
    
    show zhean laugh at right
    
    z "I guess it baffles people, because I look like an anime enjoyer or weaboo."
    
    jump main4
    
label choice3_CM:
    hide mj
    
    show zhean smile at right
    z "I guess... something people don't know about me is..."
    
    z "I am a fan of classical music..."
    
    z "To be honest it's quite contrasting with the music I typically enjoy and listen to."
    
    show zhean laugh at right
    
    z "Such as The Strokes, Playboi Carti, Arctic Monkeys, and The Voidz."
    
    z "But yeah! I do really enjoy classical music."
    
    jump main4
    
label main4:
    show mj delight at left
    
    show zhean nervouslaugh at right 
    
    x "Well..."
    
    x "That was very interesting, thank you for that!"
    
    z "Thank you miss!"
    
    hide zhean
    
    x "Okay..."
    
    x "Next student on my list is..."
    
    hide mj
    
    scene bg black
    
    show me smile
    
    me "Credits:\nCreated using Python and the game engine Ren'Py"
    
    me "Thanks to: sutemo (sutemo.itch.io) for the character sprites!"
    
    me "GitHub Repo and Itch.io project pages are in the README"
    
    show me smirk
    
    me "You know, there were some choices you did not get to pick!"
    
    show me smile
    
    me "You can play again so that you can know a little bit more about me!"
menu:
    "Play Again":
        jump start
    "Go Away Thanks":
        jump bye

label bye:
    show me eyeroll
    me "K."