"""
Define troll health & attack 
"""
import types
_troll_health: int = 300 #set troll health points
_troll_attack: int = 50 #set troll attack points

def get():
    return _troll_health #return troll's health to window 


def reduce(pValue): #reduce value of troll's health when called
    global _troll_health
    _troll_health -= pValue

"""
Define player health & attack 
"""

    
_player_health: int = 400 #set player health points
_player_attack: int = 25 #set player attack power

def get():
    return _player_health #call to return player health to window.


def reduce(pValue):
    global _player_health #reduce value of player health when called
    _player_health -= pValue


def increase(pValue): #increase value of player health when called
    global _player_health
    _player_health += pValue