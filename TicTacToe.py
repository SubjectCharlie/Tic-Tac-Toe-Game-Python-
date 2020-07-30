# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 11:12:33 2020

@author: SubjectCharlie
"""

#This is a basic game of Tic Tac Toe

import random
import sys

player = ''
computer = ''

Board = {'TOP-L': ' ', 'TOP-M': ' ', 'TOP-R': ' ', 'MID-L': ' ', 'MID-M': ' ', 
         'MID-R': ' ', 'BOTTOM-L': ' ', 'BOTTOM-M': ' ', 'BOTTOM-R': ' '}  #Board dict holds game area states

def displayBoard():
    print(Board.get('TOP-L', '?') + ' | ' + Board.get('TOP-M', '?') + ' | ' + Board.get('TOP-R', '?'))
    print('--|---|--')
    print(Board.get('MID-L', '?') + ' | ' + Board.get('MID-M', '?') + ' | ' + Board.get('MID-R', '?'))
    print('--|---|--')
    print(Board.get('BOTTOM-L', '?') + ' | ' + Board.get('BOTTOM-M', '?') + ' | ' + Board.get('BOTTOM-R', '?'))

def playGame():
    global player 
    global computer
    print('Time for a game of Tic-Tac-Toe!')
    print('Choose one: X or O')
    player = input()
    player = player.upper()
    if player == 'X':
        player = 'X'
        computer = 'O'
    elif player == 'O':
        player = 'O'
        computer = 'X'
    else:
        print('Your input was invalid. You are X.')
        player = 'X'
        computer = 'O'
    print('This is the current board. Space names include: TOP-M, MID-R, BOTTOM-L, and so on.')
    displayBoard()
    #do something here to loop turn and display with wincheck
    while True:
        Turn()
    
def Turn():
    global player
    global computer
    while True:
        print('Where do you want to play?')
        play = input()
        if play == 'TOP-L' or play == 'TOP-M' or play == 'TOP-R' or \
           play == 'MID-L' or play == 'MID-M' or play == 'MID-R' or \
           play == 'BOTTOM-L' or play == 'BOTTOM-M' or play == 'BOTTOM-R':
               if Board[play] == ' ':
                   break
               else:
                   print("You can't play there.")
        else:
             print('Your input should be in all caps. Example: MID-M')
    Board[play] = player
    displayBoard()
    print()
    WinCheck(player)
    while True:
        PCplay = random.choice(list(Board.keys()))
        PCplay = str(PCplay)
        if Board[PCplay] == ' ':
            Board[PCplay] = computer
            break
    displayBoard()
    WinCheck(computer)
    
def WinCheck(check):
    #this function will check after player and computer turns for game win/loss/tie
    if check == player:
        message = 'The game has ended. YOU WON!'
    elif check == computer:
        message = 'The game has ended. YOU LOST!'
    if Board['TOP-L'] == check and Board['TOP-M'] == check and Board['TOP-R'] == check:
        print(message)
        sys.exit()
    elif Board['MID-L'] == check and Board['MID-M'] == check and Board['MID-R'] == check:
        print(message)
        sys.exit()
    elif Board['BOTTOM-L'] == check and Board['BOTTOM-M'] == check and Board['BOTTOM-R'] == check:
        print(message)
        sys.exit()
    elif Board['TOP-L'] == check and Board['MID-M'] == check and Board['BOTTOM-R'] == check:
        print(message)
        sys.exit()
    elif Board['BOTTOM-L'] == check and Board['MID-M'] == check and Board['TOP-R'] == check:
        print(message)
        sys.exit()
    elif Board['TOP-L'] == check and Board['MID-L'] == check and Board['BOTTOM-L'] == check:
        print(message)
        sys.exit()
    elif Board['TOP-M'] == check and Board['MID-M'] == check and Board['BOTTOM-M'] == check:
        print(message)
        sys.exit()
    elif Board['TOP-R'] == check and Board['MID-R'] == check and Board['BOTTOM-R'] == check:
        print(message)
        sys.exit()
    elif Board['TOP-L'] != ' ' and Board['TOP-M'] != ' ' and Board['TOP-R'] != ' ' and \
         Board['MID-L'] != ' ' and Board['MID-M'] != ' ' and Board['BOTTOM-R'] != ' ' and \
         Board['BOTTOM-L'] != ' ' and Board['BOTTOM-M'] != ' ' and Board['BOTTOM-R'] != ' ':
            print('You have tied. Better luck next time!')
            sys.exit()

playGame()









