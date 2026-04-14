##Main File??

#Importing State Stacks
"""
This section can be used to import stacks representing other trail systems if one desired
"""
import MDStack
import GAStack
import NCTNStack
import VAStack
import WVStack
import PAStack
import NJStack
import NYStack
import CTStack
import MAStack
import VTStack
import NHStack
import MEStack
"""
The global AbvStack creates an enviroment that stores the abbreviations of every state used.
It could be rewritten to diffrent abreviations if applied to a diffeent systeam
"""
AbvStack = ["GA","NCTN","VA","WV","MD","PA","NJ","NY","CT","MA","VT","NH","ME"]
"""
StackStack contains all of the State's stacks so that they may be manipulated individually.
Other stack segments could be uploaded here to use another trail, just remember to type .Stack or .(however you have them stored)
This will prevent some massive headaches!
"""
StackStack = [GAStack.Stack,NCTNStack.Stack,VAStack.Stack,WVStack.Stack,MDStack.Stack,PAStack.Stack,NJStack.Stack,NYStack.Stack,CTStack.Stack,MAStack.Stack,VTStack.Stack,NHStack.Stack,MEStack.Stack]
#ATStack = [GAStack.Stack + NCTNStack.Stack]
"""
AtStack is the stack used to observe the entire AT on a large scale, you would also need to add every segment's Stacks here.
"""
ATStack = []
ATStack += GAStack.Stack
ATStack += NCTNStack.Stack
ATStack += VAStack.Stack
ATStack += WVStack.Stack
ATStack += MDStack.Stack
ATStack += PAStack.Stack
ATStack += NJStack.Stack
ATStack += NYStack.Stack
ATStack += CTStack.Stack
ATStack += MAStack.Stack
ATStack += VTStack.Stack
ATStack += NHStack.Stack
ATStack += MEStack.Stack

#call function
#MDStack.Test_Print()
#MDStack.MD_Sumary()




## Stack_Sum with Arguments - Works (V3) took remebering to call the stack within the file GAStack to get it working :(
def Stack_Sum(Stack=ATStack,Abv="The entire AT"):
    
    Stack_Len = len(Stack)
    print(Abv,"has a total of:", Stack_Len, "availible lots on the AT. The respective lots are:")
    for i in range ((Stack_Len)):
        print (i+1,Stack[i])
    Dist_Stack = []
    Name_Stack = []
    for i in range ((Stack_Len)):
        result = Stack[i].split("-")
        Dist_Stack.append(float(result[0]))
        Name_Stack.append(result[1])
    Stack_Sum = 0
    for i in range ((Stack_Len)):
        Stack_Sum += Dist_Stack[i]
    print("There are", round(Stack_Sum, 2), "total trail miles in",Abv)
    return Name_Stack##


##Function for finding ideal trailhead within a distance from a stated trailhead
# dist represents the total distance the hiker is comfortable with walking
# Stack represents the state that will be being hiked
# TH represents the trailhead that the hiker will be starting from
def THTrad(dist,Stack,TH):
#    print("index",n)
    print("You could go up to",Nlimit(dist,Stack,TH),"trailheads north and up to",Slimit(dist,Stack,TH), "trailheads south") # Function to find how many trailheads south one can go

def Nlimit(dist,Stack,index):
    x=0
    tot=0
    for i in range (len(Stack)):
        result = (Stack[index+(i)].split("-"))
#        print(result[0])
        x += float(result[0])
        if x>dist:
            break
        tot+=1
    return tot

def Slimit(dist,Stack,index):
    x=0
    tot=0
    for i in range (len(Stack)):
        result = (Stack[index-(i)].split("-"))
#        print("s",result[0])
        x += float(result[0])
        if x>dist:
            break
        tot+=1
    return tot

## Function for finding ideal route of a given distance in a state
def StateDist(dist,Stack):
    start=0
#    tot1=0
    STot2 = []
    tot2=0
    for i in range (len(Stack)-1):
        STot1 = []
        tot1=0
        for i in range (len(Stack)):##Start of code to find path within distance
            result = (Stack[(i+start)].split("-"))
#            print("Itteration", start,result[0]) - Test Value
            tot1 += float(result[0])
            if tot1>dist:
                fin = (i-1)
                tot1 -= float(result[0])
                break ##End of code to find distance
        if ((dist-tot1)>(dist-tot2)) and ((dist-tot2)!=0):
            tot1=0
        else:
            STot2 = [start, tot1, fin]
            tot2=tot1
        start +=1
#        print(tot2)
#        print("s",STot2) - Test Values
    return STot2




##Front end function, recives user input and executes commands
def FrontRunner ():
    print("Hello and welcome to my best attempt at a trail manager for the the AT, with any luck, you'll be able to enjoy the AT like I have using the following options!")
    print("(1) for just a summary of the trails \n(2) if you would like to plan a traditional hike from a given trailhead\n(3) if you would like to plan a leapfrog hike from a given trailhead")
    print("(4) for the traditional route that best matches your distance in a given state\n(5) for the leapfrog route that best matches your distance in a given state.")
    num = eval(input())
    if num==1:
        SumRunner()
    elif num==2:
        TradRunner()
    elif num==3:
        LeapRunner()
    elif num==4:
        TradState()
    elif num==5:
        LeapState()
    else:
        print("I'm sorry, that was not an accaptable response, please try to enter a number")
        FrontRunner()
    
def SumRunner():
    print("This is the Trail Summary Command Center, please view the follwing options carefully!")
    for i in range (3):
        print ("Please press", (i+1), "to see the summary for",AbvStack[i])
    num = eval(input("Enter any diffent number to see the entire AT:"))
    print(num)
    if (num> 0) &(num<=3):
        Stack_Sum(StackStack[num-1],AbvStack[num-1])
    else:
        Stack_Sum()

## Function used to recommend traditional hikes to a hiker
# StateInd represents the state the hiker would like to start in
# TH Represents the trailhead the hiker would like to start at
def TradRunner():
    print("This is the summary center for a traditional style hike, please use the options below to determine your state")
    for i in range (13):
        print ("Please press", (i+1), "to see the summary for",AbvStack[i])
    StateInd = eval(input())
    print("You've selected:", AbvStack[StateInd-1])
    if (StateInd> 0) &(StateInd<=3):
        Stack_Sum(StackStack[StateInd-1],AbvStack[StateInd-1])
    else:
        print("Incorrect input, please try one of the numbers again")
        TradRunner()
    TH = eval(input("Please enter the number that appeared besides the trailhead you would like to start at"))
    if TH<=(len(StackStack[StateInd-1])):#input protection for the trailhead secion, if sucessful request distance and call calculator, if not, start the runner command again
        dist = eval(input("Now enter the desired total milage for the trip:"))
        THTrad(dist/2,StackStack[StateInd-1],TH)
    else:
        TradRunner()
def LeapRunner():
    print("This is the summary center for a leapfrog style hike, please use the options below to determine your state")
    for i in range (13):
        print ("Please press", (i+1), "to see the summary for",AbvStack[i])
    StateInd = eval(input())
    print("You've selected:", AbvStack[StateInd-1])
    if (StateInd> 0) &(StateInd<=3):
        Stack_Sum(StackStack[StateInd-1],AbvStack[StateInd-1])
    else:
        print("Incorrect input, please try one of the numbers again")
        LeapRunner()
    TH = eval(input("Please enter the number that appeared besides the trailhead you would like to start at"))
    if TH<=(len(StackStack[StateInd-1])):#input protection for the trailhead secion, if sucessful request distance and call calculator, if not, start the runner command again
        dist = eval(input("Now enter the desired total milage for the trip:"))
        THTrad(dist,StackStack[StateInd-1],TH)
    else:
        LeapRunner()
        
##Funtion designed to find ideal leap style hike given distance and state
def LeapState():
    print("This is the summary potion for a leapfrog style hike given a state and an ideal distance")
    for i in range (13):
        print ("Please press", (i+1), "to see the summary for",AbvStack[i])
    StateInd = eval(input())
    print("You've selected:", AbvStack[StateInd-1])
    dist = eval(input("Now please enter your desired distance in miles"))
    InfoStack = StateDist(dist,StackStack[StateInd-1])
    print("The ideal hike for you starts at trail marker", InfoStack[0], ", ends at trail marker", InfoStack[2], "and is a total distance of", round(InfoStack[1],2), "miles")

def TradState():
    print("This is the summary potion for a traditional style hike given a state and an ideal distance")
    for i in range (13):
        print ("Please press", (i+1), "to see the summary for",AbvStack[i])
    StateInd = eval(input())
    print("You've selected:", AbvStack[StateInd-1])
    dist = eval(input("Now please enter your desired distance in miles"))
    InfoStack = StateDist((dist/2),StackStack[StateInd-1])
    print("The ideal hike for you starts at trail marker", InfoStack[0], ", will double back at trail marker", InfoStack[2], "and will have you travel a total distance of", (round(InfoStack[1],2)*2), "miles")
   
    
    

#FrontRunner()
Stack_Sum() #- Useful for verifying additions made to stacks
#StateTrad(15,StackStack[0])
#THTrad(20, StackStack[0],5)
#TradState() 

## Previous versions and notes
"""
##Attempting to see if I can host the summary command on main - (V1) Outdated and phased out for code with more general wording
print (MDStack.MD_Stack)
Len = len(MDStack.MD_Stack)
#print(Len)
def MD_Sumary():    
    print("MD has a total of:", Len, "availible lots on the AT. The respective lots are:")
    for i in range ((Len)):
        print (i+1,MD_Stack[i])
    #print("The total distance of the AT in MD is roughly:") - Test Value
    result = MD_Stack[0].split("-")
    #print(result) - Test Value
    MDist_Stack = []
    MDName_Stack = []
    for i in range ((Len)):
        result = MD_Stack[i].split("-")
        MDist_Stack.append(float(result[0]))
        MDName_Stack.append(result[1])
    #print(MDist_Stack,MDName_Stack)- Test Value
    MD_Sum = 0
    for i in range ((Len)):
        MD_Sum += MDist_Stack[i]
    print("There are", round(MD_Sum, 2), "total trail miles in MD")

MD_Sumary()"""

##Stack sume w/o Arguments - Works (V2)- phased out to call stack in argument
"""
def Stack_Sum():
    Stack_Len = len(GAStack.Stack)
    print("GA has a total of:", Stack_Len, "availible lots on the AT. The respective lots are:")
    for i in range ((Stack_Len)):
        print (i+1,GAStack.Stack[i])
    Dist_Stack = []
    Name_Stack = []
    for i in range ((Stack_Len)):
        result = GAStack.Stack[i].split("-")
        Dist_Stack.append(float(result[0]))
        Name_Stack.append(result[1])
    Stack_Sum = 0
    for i in range ((Stack_Len)):
        Stack_Sum += Dist_Stack[i]
    print("There are", round(Stack_Sum, 2), "total trail miles in GA")

Stack_Sum()
"""
#does this work?-yes
## MD had trouble due to specific terms already being in use
### We will attempt to build GA Stack to prevent this! then determine if useful-it has been useful so far! ##Update- It was useful!
