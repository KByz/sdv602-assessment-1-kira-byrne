"""
Define troll health & attack 
"""

import types
_troll_health: int = 500
_troll_attack: int = 25

def get():
    return _troll_health


def reduce(pValue):
    global _troll_health
    _troll_health -= pValue

"""
Define player health & attack 
"""

    
_player_health: int = 500
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