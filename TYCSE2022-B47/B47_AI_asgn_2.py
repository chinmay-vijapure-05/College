print("We have 2 ROOMS and 1 Vacuum cleaner\nEnter 0 if room is clean and 1 if room is dirty")
print("ROOM_A",end=" : ")
rA=int(input())
print("ROOM_B",end=" : ")
rB=int(input())

print("Enter A if vacuum cleaner is in ROOM_A and B if vacuum cleaner is in ROOM_B\nWhich room is vacuum cleaner currently in : ")
vc = input()

cost=0
if(vc=='A'):
    # print("Vacuum cleaner present in ROOM_1")
    if(rA == 1):
        print("Cleaned Room A")
        cost+=1 # cleaning cost
        rA=0
    elif(rB==1):
        print("Moved to Room B\nCleaned Room B")
        cost += 2 # cleaning + movement cost
        rB=0
elif (vc == 'B'):
    # print("Vacuum cleaner present in ROOM_2")
    if (rB == 1):
        print("Cleaned Room B")
        cost += 1  # cleaning cost
        rB=0
    elif (rA == 1):
        print("Room B is clean\nMoved to Room A\nCleaned Room A")
        cost += 2  # cleaning + movement cost
        rA=0
print("\nCost of cleaning 2 rooms : ",cost)


'''
simple reflex
utility
model
--> goal 
learning
'''