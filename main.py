#imports
import webbrowser
import random
import time

#actual code of the "game"
time.sleep(2)
print("Welcome to AmogUs! This is basically Among Us, but with... drum roll... COMMAND PROMPT! I don't know how this will work well without being in 2d/3d, but here it is anyway!")
print("While we're at it, would you like... let's just say... good ambience for this game? (Y/N) Also, if you want ambience music you have to run pip install webbrower in command prompt. If it doesn't work then :(")
ambience_input = input("")
if ambience_input == ("Y"):
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=MGnObcTv6CA')
else:
    print("Ok no ambience music then ;(")
time.sleep(2)
print("The round will begin in three seconds.")
time.sleep(2)
print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)

Sabotages = ['LIGHTS HAVE BEEN SABOTAGED', 'REACTOR HAS BEEN SABOTAGED', 'COMMUNICATIONS ARE SABOTAGED', 'OXYGEN HAS BEEN SABOTAGED', 'SEIMSIC TREMORS HAVE BEEN SABOTAGED', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...', 'Nice! No sabotage. At least not yet...']


print("Type IMPOSTOR if you want to be an impostor :D. Otherwise, type CREWMATE.")
role_input = input("")
time.sleep(1)
#Impostor Code
if role_input == ("IMPOSTOR"):
    sabotage_input = input("")
    print("Type SABOTAGE to sabotage the ship!")
    if sabotage_input == ("SABOTAGE"):
        print("Which sabotage? (LIGHTS/REACTOR/COMMUNICATIONS/OXYGEN/SEISMIC TREMORS")
        sabotage_input = input("")
        if sabotage_input == ("LIGHTS"):
            print("LIGHTS ARE SABOTAGED.")
        if sabotage_input == ("REACTOR"):
            print("REACTOR IS SABOTAGED.")
        if sabotage_input == ("COMMUNICATIONS"):
            print("COMMUNICATIONS ARE SABOTAGED.")
        if sabotage_input == ("OXYGEN"):
            print("OXYGEN IS SABOTAGED.")
        if sabotage_input == ("SEISMIC TREMORS"):
            print("SEISMIC TREMORS ARE SABOTAGED.")    

#Crewmate Code

if role_input == ("CREWMATE"):
    print("Type TASK to do your tasks!")
    direction_input = input("")
    if direction_input == ("TASK"):

        task_input = input("")
        if task_input == ("FIX NAVS"):
            print("Fixing navs...")
            time.sleep(3)
            print(random.choice(Sabotages)) 