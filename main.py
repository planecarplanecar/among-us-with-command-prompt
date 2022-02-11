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
#part 1 of 2 of the random role generator
role = ['|Crewmate| do your tasks, and save the ship!', '|Impostor| prevent the crew from completing their tasks, and sabotage the ship!']
time.sleep(3)
print("You are a/an: ")
time.sleep(1)
#part two of the role generator
print(random.choice(role)) 
role2 = random.choice(role)
if role2 == ("|Impostor| prevent the crew from completing their tasks, and sabotage the ship!"):
    eliminate_input = input("")
    print("Type SABOTAGE to sabotage the ship!")
    if eliminate_input == ("SABOTAGE"):
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