import easygui as eg
title = 'SHREK HERE'
buttone = "SAY GOODBYE TO YOUR OGRELORD"

answer=eg.buttonbox(msg="Do you like shrek?",title="Ultimate Question",choices=('yes','no','the answer is ogrely obvious'))

if answer == 'yes':
    words = 'YOU UNDERSTAND MY OGREPOWERED SKILLS'
elif answer == 'no':
    words = "FOR YOU IT'S ALL OGRE NOW!"
    title = "SHREK HERE AND I'M TICKED OFF"
    buttone = "APOLOGISE TO YOUR OGRELORD"
else:
    words = "YOU ARE THE ULTIMATE SHREKTIFIER"

eg.msgbox(words,title,buttone)
