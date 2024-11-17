import random 
#snakes dictionary .It has snake head values on keys  and tail values on values
snakes={97:25, 92:70, 86:54, 62:37,53:33, 47:5, 38:15, 29:9}
#LADDER dictionary .It has ladder bottom values  on keys  and ladder top values on values
ladders={2:23,8:34,20:77,32:68,41:79,74:88,82:100}
print("ladders:")
for k in ladders.keys():
	print(k,"-->",ladders[k])
print("\nsnakes:")	
for k in snakes.keys():
	print(k,"-->",snakes[k])
#reading the player names into the dictionary and intialising values zero
def readData(n):
	dict={}
	for i in range(n):
		name=input("enter the player name:")
		dict[name]=0
	return dict

#logic function for incrementing and decrementing player position
def implement(players):
	for  x in players:
		print("\n",x,end="")
		click=input("...click ENTER to roll the die:")
		num=random.randint(1,6)
		print("your number is ",num)
		players[x]+=num
		pos=players[x]
		

#checking player position have snake or  not			
		if pos in snakes.keys():
			print("you stepped on SNAKE...")
			pos=players[x] =snakes[pos]
			

#checking player position have ladder or  not			
			
		if pos in ladders.keys():
			print("you stepped on LADDER ...")
			pos=players[x]=ladders[pos]

#checking player position  greater than are equal to 100

		if pos>=100:
			if pos==100:
				print("your position  :",players[x])
				print("\nwinner is...",x)
				return x
			else:
				players[x]-=num
				print("\n\nyour get high value than required value..\nnot considered...")
		print("your position  :",players[x])
		

#main function
num=int(input("enter the numner of players:"))
if num<1:
	print("\ndont give values as negative and zero")
	exit()
dict=readData(num)
winner=None
#Loop for repeating rounds
while(winner ==None):
			winner=implement(dict)#calling main logic
print("-"*25)			
print("\nCongrats....",winner.upper())
print("\n-"*25)				
			
		

		