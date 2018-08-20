redo=1
while redo == 1:
    import random
    
    #first sentence praising student
    x=random.randint(0,8)
    y=random.randint(0,8)
    if y == x: 
        y=random.randint(0,8)    
    adjectivecomments=["great", "fantastic", "super", "excellent", "outstanding", "top notch", "first class", "supreme", "wonderful"]
    adjective1=adjectivecomments[x]
    adjective2=adjectivecomments[y]
    
    # how they have been improving
    
    x=random.randint(0,8)
    improvmentarea=["work", "writting", "focus", "spoken English", "handwritting", "grammar", "punctuation", "spelling", "handwriting"]
    x=random.randint(0,3)
    howitimproves=["has been getting better and better", "has been improving by leaps and bounds", "has gotten better", "is even better than last week"]
    improvementmessage= "His/Her " + improvmentarea[x] + " " + howitimproves[x]
    
    #should improve
    x=random.randint(0,8)
    shouldimprovemessage="I would like to see him/her work a little harder on his/her " + improvmentarea[x]
    
    #second statement offering criticism
    x=random.randint(0,4)
    betterhabitcomments=["try a little harder", "work more slowly", "work more carefuly", "pay closer attention", "follow instructions more closely"]
    betterhabit=betterhabitcomments[x]
    
    #encouragement
    x=random.randint(0,4)
    encourementcomment=["You can do it!", "Way to go!", "You've got this!", "Great!", "Keep it up!"]
    encouragement= encourementcomment[x]
    
    #changes the beginning of the improvement message
    improve= ". S/he could do even better if s/he would "
    
    #comment format so that they arent as conspicuously computer generated
    x==random.randint (0,3)
    if x==0:
        print ("(name) is a " + adjective1 + " student. And his/her work is " + adjective2+ ". S/he could do even better if s/he would " + betterhabit + ". " + encouragement)
    elif x==1:
        print ("(name) is a " + adjective1 + " student. " + improvementmessage + ". S/he could do even better if s/he would " + betterhabit + ". " + encouragement)
    elif x==2:
        print ("(name) is a " + adjective1 + " student. "+ improvementmessage + shouldimprovemessage
               + betterhabit + ". " + encouragement)
    else: 
        print ("(name) is a " + adjective1 + " student. And his/her work is " + adjective2+ ". " + shouldimprovemessage + ". " + encouragement)
     
    from tkinter import *
    import tkinter.messagebox
    

    root= Tk()
    root.overrideredirect(1)
    root.withdraw()    
    
    
    
    answer = tkinter.messagebox.askquestion("(name) is a " + adjective1 + " student. And his/her work is " + adjective2+ ". S/he could do even better if s/he would " + betterhabit + ". " + encouragement)
                       
    
    if answer == 'yes':
        redo=1    
    else:
        redo=0
