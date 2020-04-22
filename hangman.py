
box_character = u'\u2610'

import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import re

chance1img=mpimg.imread('1stchance.png')
chance2img=mpimg.imread('2ndchance.png')
chance3img=mpimg.imread('3rdchance.png')
chance4img=mpimg.imread('4rthchance.png')
chance5img=mpimg.imread('5thchance.png')
chance6img=mpimg.imread('6thchance.png')
chance7img=mpimg.imread('7thchance.png')
chance8img=mpimg.imread('8thchance.png')

imagearray=[chance8img,chance7img,chance6img,chance5img,chance4img,chance3img,chance2img,chance1img]

class Player():

    def __init__(self,name,score,wongivingword,wondecoding):
        self.score=score
        self.name = name
        self.wongivingword = wongivingword
        self.wondecoding = wondecoding

def checkstars(string):

    a = 10

    for letter in string:
        if letter == u'\u2610':
            a = 20
            return 0
            break
            
    if a==10:

        return 1

def replaceletter(string,index,letter):
    
    if index==len(string)-1:
        b = string[0:index]
        newstring = b+letter
    elif index==0:
        c = string[index+1:]
        newstring = letter + c
    else:
        b,c =string[0:index],string[index+1:]
        newstring=b+letter+c
    return newstring

def eachround(player):
    
    chances = 7
    
    if player == 1:
        play=player1
        receiver = player2
    elif player == -1:
        play=player2
        receiver = player1
        
    while True:
 
        ask = 'Write down your word, {} \n'.format(play.name.upper())
        word_by_the_user = input(ask)

        if len(word_by_the_user) == 0:
            print('Give atleast a letter, This is not accepted {}'.format(play.name))
        elif re.match(r"[A-Za-z ]+$",word_by_the_user):
            word_by_the_user = word_by_the_user.upper()
            break
        else:
            print('\n')
            print('Give only Words, nothing else {}'.format(play.name))

    for i in range(0,50):
        print(' \n')
    
    displaystring = []
    
    for letter in word_by_the_user:
        if letter==' ':
            displaystring.append(' ')
        else:
            displaystring.append(box_character)
            
    displaystring = ''.join(displaystring)
    print('\n')
    print('\t{}'.format(displaystring))
    print('\n')

    result=1
    selected_words = []

    while result>0:

        imgindex = 7-chances
        imgplot = plt.imshow(imagearray[imgindex])
        plt.axis('off')
        plt.show()

        if chances==0:
            print('The man is hanged:( {} wins!'.format(play.name))
            print('The Answer is {}'.format(word_by_the_user.upper()))
            play.score = play.score + 1
            result = 0
            break

        guess_letter_ask = 'Give your guess, {} \n'.format(receiver.name.upper())
        guess_letter = input(guess_letter_ask)
        guess_letter = guess_letter.upper()
        
        if len(guess_letter)!= 1:
            print('Give only a single letter {}'.format(receiver.name))
            continue
        if not guess_letter.isalpha():
            print('Give only letter {}'.format(receiver.name))
            continue 
        if guess_letter in selected_words:
            print('Sorry,{}. You\'ve already selected this letter, choose an another one'.format(receiver.name.upper()))
            continue

        answer = guess_letter in word_by_the_user

        selected_words.append(guess_letter)    
        
        if answer == False:
            chances = chances - 1
            print('\n')
            print('\t{}'.format(displaystring))
            print('\n')

        else:
            for i in range(0,len(word_by_the_user)):
                if word_by_the_user[i]==guess_letter:
                    displaystring=replaceletter(displaystring,i,guess_letter)
            print('\n')
            print('\t{}'.format(displaystring))
            print('\n')
          
        winorlose = checkstars(displaystring)

        if winorlose == 1:
            print('\n')
            print('{} wins!'.format(receiver.name))
            print('\n')
            receiver.score = receiver.score+1
            break
print('\n')
print('\t\tLet\'s play Hangman!')
while True:
    askPlayer1 = 'Player 1 : How would you want to be called?\n'
    player1name = input(askPlayer1)  
    if len(player1name) == 0:
        print('Please type again')
    else:
        break
while True:
    askPlayer2 = 'Player 2 : How would you want to be called?\n'
    player2name = input(askPlayer2)  
    if len(player2name) == 0:
        print('Please type again')
    else:
        break
while True: 
    askRounds = 'For How many rounds do you want to play?\n'
    rounds = input(askRounds)
    if rounds.isdigit():
        rounds=int(rounds)
        break
    else:
        print('Please enter only numbers')

player1=Player(name=player1name,score=0,wongivingword=0,wondecoding=0)
player2=Player(name=player2name,score=0,wongivingword=0,wondecoding=0)
   
playerindex=1

for i in range(0,2*rounds):
    j = int(i/2 + 1)
    print('\n')
    print('ROUND {}'.format(j))
    print('\n')
    eachround(playerindex)
    playerindex=playerindex*-1

print('\n')
print('\tSCOREBOARD')
print('Player name\tScore\n')
print('{}\t\t{}\n'.format(player1.name,player1.score))
print('{}\t{}\n'.format(player2.name,player2.score))