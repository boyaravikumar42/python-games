#Number game
print("\t\tR-U-L-E-S=>\n--> The alphabates in the list have internally 1 to 9 values\n --> Enter the two alphabates from the list\n-->It will display their internal values like range ")
print("-->enter third choice from the shown list. if its internal value is with in first two choices then your the winner else you loss game")
d={}
for i in range(1,11):
	d[chr(75+i)]=11-i
l=set()
for k,v in d.items():
	l.add(k)
print()
print(l)
print()
print("\t\tEnter your choices from the list")
print()
n1=input("enter the first choice:")
print()
n2=input('enter the second choice:')
print()
if d[n1]>d[n2]:
	temp=d[n1]
	d[n1]=d[n2]
	d[n2]=temp	
print("\t\tYOUR RANGE :",end='') 
print("  ",d[n1],'    to   ',d[n2])
print()
if d[n2]==d[n1]+1:
		print("\tsorry..you loss the game")
		exit()
l.remove(n1)
l.remove(n2)
print(l)
print()
print('\t\t\'_\' ...BEST OF LUCK.... \'_\'')
print()
n= input("enter your last choice: ")
if d[n]<d[n2] and d[n]>d[n1]:
	print('congrats ....\5')
	print()
	print("you won the game")
	print()
	print(" guessed number is",d[n])
	print()
else:
	print("sorry..you loss the game...")
	print()
	print(" guessed number is",d[n])
	print()
	flag=input("enter zero to exit the game: ")

