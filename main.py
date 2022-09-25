print("Welcome to detect world you need 1 person to play along with you")
name1=input("Please put the first persons name in : ")
name2=input("Please put the second person who is playing along with "+name1)
who=input("Now! who is going to put the wod for the othe to guess Note put it as player1 or player2 it is case sensitive")
print(f'{who} come in front of the screen and the other player has to close their eyes')
word=input(f"{who} , Now, type the world you want other to guess it can be of only 5 letters")
numberofword=len(word)
print(f"there are {numberofword} words in the word given")
first=word[0]
second=word[1]
fifth=word[4]
answer=input(f'{first} {second} ___  ___ {fifth}')

