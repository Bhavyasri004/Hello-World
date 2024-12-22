import random
#specific images to show
Rock='''                @@@@@@@
                @@@@@@@        '''
paper='''                $$$$$$$
                $$$$$$$
                $$$$$$$
                $$$$$$$         '''
Scissor='''                H^H^H^H^H^
                H^H^H^H^H^
                H^H^H^H^H^      '''
#1aking input from user
image=[Rock,paper,Scissor]
userinput= int(input("Enter 3 numbers i.e is 0-Rock,1-Paper,2-Scissors"))
##if user input is out of range
if(userinput>=3 and userinput<0):
    print("Number not found1")
else:
    #taking  input from computer
    print(image[userinput])
    computerinput =random.randint(0,2)
    print("_Computer input is",computerinput)
    print(image[computerinput])
    if(computerinput==userinput):
        print("withdraw")
    elif(computerinput==0 and userinput==2):
        print("you `lose")
    elif(userinput==0 and computerinput==2):
        print("You Win")
    elif(computerinput>userinput):#if 0>1 or 1>2
        print("You lose")
    elif(userinput>computerinput):
        print("You Win")