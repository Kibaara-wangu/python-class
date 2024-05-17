def tasks(*kwargs):
    for i in kwargs:
        if i in range(1,4):
            print("The task is most important")
        elif i in range(4,7):
           print("The task is more important")
        elif i in range (7,11):
            print("The task is less important")
        else:
            print("javascript practice") 

tasks("kotlin practice","mary","john")