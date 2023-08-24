"""
Define troll health & attack 
"""

import types
import cmd_parser.command_parser as cmd

def troll():
    global _troll_health
    global _troll_attack

_troll_health: int = 300
_troll_attack: int = 50

def get():
    return _troll_health


def reduce(pValue):
    global _troll_health
    _troll_health -= pValue

"""
Define player health & attack 
"""

    
_player_health: int = 810
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

def combat(pCommand):
    global _player_health
    global _player_attack
    global _troll_health
    global _troll_attack
    if pCommand == 'attack':
        _troll_health -= _player_attack
        _player_health -= _troll_attack
        if _troll_health <= 0:
            cmd.move(['Troll_Dead'])
            cmd.game_state = 'explore'
        elif _player_health <= 0:
            cmd.game_state = 'game_over'
            return 'You have been slain by the troll!'
        else:
            return 'You strike the troll with a mighty blow, but she strikes back with vicious claws.'
    elif pCommand == 'potion':
        _player_health += 500
        _player_health -= _troll_attack
        if _player_health <= 0:
            cmd.game_state = 'game_over'
            return 'You have been slain by the troll! Game Over!'
        else:
            return 'You have restored your health!'
    else:
        return 'You cannot do that here.'
 #IF attack, troll health - player attack
#check if troll health = <0, if yes, set game location to "dead_troll", set game state back to explore.
    # set game state to explore, call cmd.move([cmd.move, 'Troll_Dead'])
     #if troll health is > 0, minus troll attack from player health
    #check if player health = 0, if yes, return game_over string.
#return player health and troll health


