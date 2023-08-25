"""
Define troll health & attack 
"""

import types
import cmd_parser.command_parser as cmd
import status.health as health

def troll(): #WIP
    global _troll_health
    global _troll_attack

_troll_health: int = 300
_troll_attack: int = 50

def get():
    return _troll_health


def reduce(pValue):
    global _troll_health
    _troll_health -= pValue

def get():
    return _troll_health

"""
Define player health & attack 
"""
_player_health: int = 410
_player_attack: int = 25

def get():
    return _player_health


def reduce(pValue):
    global _player_health
    _player_health -= pValue


def increase(pValue):
    global _player_health
    _player_health += pValue

def sword(pValue):
    global _player_attack
    _player_attack += pValue

"""
Define combat system
"""

def combat(pPlace):
    global _player_health
    global _player_attack
    global _troll_health
    global _troll_attack

    result = ""
    pCommand = pPlace[1]
    print(pPlace, 'INSIDE COMBAT')
    if pCommand == 'attack':
        health._troll_health -= health._player_attack
        health._player_health -= health._troll_attack
        if health._troll_health <= 0: #Check for troll's health, when less than or euqal to 0, move to next stage in game
            result = cmd.move([cmd.move, 'Troll_Dead'])
        elif health._player_health <= 0:
            #cmd.game_state = 'game_over' #check for player health, if less than or equal to 0, return 'game over'
            result = 'You have been slain by the troll! Game Over!' + cmd.move([cmd.move, 'Game_Over'])
        else:
            result = 'You attacked the troll\n' + cmd.move([cmd.move, 'Troll_Fight'])
    elif pCommand == 'potion':
        health. _player_health += 500
        result = 'You have restored your health!' + cmd.move([cmd.move, 'Troll_Fight'])
    else:
        result = 'You cannot do that here.' + cmd.move([cmd.move, 'Troll_Fight'])

    return result
 #IF attack, troll health - player attack
#check if troll health = <0, if yes, set game location to "dead_troll", set game state back to explore.
    # set game state to explore, call cmd.move([cmd.move, 'Troll_Dead'])
     #if troll health is > 0, minus troll attack from player health
    #check if player health = 0, if yes, return game_over string.
#return player health and troll health


