#General Python Imports
import os
import pygame

#My Imports
import Entity
import Map
import Deck
import Card
import Entity

def main():
    print("Welcome to Swordsalot.")
    board = Map.Board(4, 7, 4)
    board.display()



if __name__ == '__main__':
    main()