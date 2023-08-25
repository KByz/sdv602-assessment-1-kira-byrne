from enum import Enum
"""_summary_

Take string containing a proposed command produce a list of tokens
"""
_explore_tokens = set(['north', 'south', 'east', 'west', 'look', 'fight', 'use', 'up', 'down', 'talk',
                    'leave', 'enter', 'attack', 'potion']) #set valid tokens for explore state.

_combat_tokens = set(['attack', 'potion']) #set valid tokens for combat state

#perhaps add the combat tokens back into the original set and create a check at Troll that if the player uses attack they reduce in health and the troll reduces in health.

# _white_space = set('\t', '\r', '\n', ' ')


def valid_list(p_input_string):

    """
    Takes a string, that is a sequence of command and operators 
    separated by "white space" characaters 
    returns a list of valid tokens - in order 

    Args:
        p_input_string (string): a string of characters 
    """
    result = []
    for astring in p_input_string.split():
        if astring.lower() in _explore_tokens or astring in _combat_tokens:
            result += [astring] 

    return result
"""
If check "is command in vocab tokens, if not, in comabat token?"

"""