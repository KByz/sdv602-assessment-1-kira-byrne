"""_summary_
Manages the commands - may not be the best name at this time

"""
# import typing
import cmd_parser.token as token
import inventory.items as inventory
import status.health as health
#import combat.combat_sys as combat
from combat.combat_sys import combat

# Game commands


def move(game_place):
    """_summary_

    Args:
        game_place (_type_): _description_

    Returns:
        _type_: _description_
    """
    global game_state
    global game_state

    location = game_place[1]
    if location == 'Troll':
        game_state = 'combat'
    game_state = location

    story_result = show_current_place()

    return story_result

def exit(game_place):
     """
     _summary_

     result returns the game is over message

     """
     result = f'You have been slain by the troll! Game Over!'
     return result 

def talk_to_hermit(game_place):
    """_summary_
        Hermit gives an amulet
        ( inventory update add)
    Args:
        game_place (_type_): _description_
    Returns:
        _type_: _description_
    """
    inventory.collect_item("key")
    return move(game_place)

def talk_to_guard(game_place):
    """_summary_
        The guard gives the player a quest scroll
        ( inventory update add)
    Args:
        game_place (_type_): _description_
    Returns:
        _type_: _description_
    """
    inventory.collect_item("quest_scroll")
    return move(game_place)

def guard_check(game_place):
    result = ""
    if inventory.has_item('quest_scroll'):
            result = move([move, 'Guard_2'])
    elif inventory.has_item('troll_head'):
            result = move([move, 'Guard_3'])
    else:
        result = move([move, 'Guard'])
    return result


def talk_to_smithy(game_place):
    """_summary_
        The smithy gives the player armour, a sword, and a tinder pouch for torch lighting
        ( inventory update add)
    Args:
        game_place (_type_): _description_
    Returns:
        _type_: _description_
    """
    inventory.collect_item("armour")
    inventory.collect_item("sword")
    return move(game_place)

def talk_to_druid(game_place):
    """_summary_
        The druid gives the player a health potion and a torch kit
        ( inventory update add)
    Args:
        game_place (_type_): _description_
    Returns:
        _type_: _description_
    """
    inventory.collect_item('potion'),
    #find out how to add two items in one instance
    inventory.collect_item('torch')
    return move(game_place)

def troll_head(game_place):
     inventory.collect_item('troll_head')
     return move(game_place)

def enter_castle(game_place):
    result = ""
    if inventory.has_item('key'):
        result = move(game_place)
    else:
        result = "Visit the hermit to recieve a key to enter the castle.\n"+show_current_place()
    return result

def smithy_check(game_place):
    result = ""
    if inventory.has_item('quest_scroll'):
            result = move([move, 'Smithy_2'])
    else:
        result = move([move, 'Smithy_1'])
    return result

def druid_check(game_place):
    result = ""
    if inventory.has_item('potion'):
            result = move([move, 'Druid_2'])
    else:
        result = move([move, 'Druid_1'])
    return result

def combat_check(game_place):
     result = ""
     if game_places == 'Troll':
            result = game_state.combat

def cave_check(game_place):
    result = ""
    if inventory.has_item('torch'):
            result = move([move, 'Cave_Lit'])
    else:
        result = move([move, 'Cave_Dark'])
    return result
def fight(game_place):
    """

    Args:
        game_place (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Implement "fight"
    # Check inventory for a sword - if no sword go to blacksmith
    # If there is a sword then flip a random to decide if they win or lose
    # If they lose they lose health
    #    They die when health is zero. When they die,  empty inventory, game_state = Forest
    # If they win they can move into the Castle ...
    result = "You can not fight because you don\'t have a sword.\nGet a sword from the blacksmith\'s.\nFighting has not been implemented\n Can you implement it?"+show_current_place()

    return result

game_state = 'Forest'
game_places = {'Forest': {'Story': 'You are Agnmauða, an aspiring warrior.\nTo the south is the village caslte. To the North is the druid.\nTo the east is the blacksmith, and to the west is the cave.',
                          'North': (move, 'Druid_Hut'), 'South': (move, 'Castle'), 'West': (move, 'Cave'), 'East': (move, 'Blacksmith'), 'Image': 'images/forest.png'},
               'Cave': {'Story': 'You are at the cave.\nA low and foreboding howl \nblows through the entrance. \nTo the east is forest.',
                        'East':(move, 'Forest'), 'Enter': (cave_check,'Cave_Dark'), 'Image':'images/forest_circle.png'},
                'Cave_Dark': {'Story': 'The cave is pitch black on entry. You cannot see your own hand in front of your face \nYou cannot move forward without a source of light.',
                              'Leave': (move, 'Cave'), 'Image': 'images/forest_circle.png'},
                'Cave_Lit': {'Story': 'Shadows scatter accross the dripping stalactites. \nThe torch allows only a few feet of clear view in the cave. \nYou can hear a faint noise near by in the dark.',
                             'Look': (move, 'Frog'), 'Leave': (move, 'Cave'), 'Forward': (move,'Deep_Cave'), 'Image': 'images/forest_circle.png'},
                'Frog': {'Story': 'Approching the sound, you shine the torch over the surface of a smooth flowstone. \nA very tiny frog peers back at you with blackened eyes and throbbing throat. \nYou chuckle and take a breath before the frog lets out a loud croak, \nechoing through the cave.',
                         'Leave': (move, 'Deep_Cave'), 'Image': 'images/frog.png'},
                'Deep_Cave': {'Story': 'The unassuming frog hops away deeper into the cave. \nYour gaze follows its direction before panning up to see \ntwo glowing yellow eyes staring back at you. \nYour legs are paralised with fear. You can do nothing but look.',
                              'Look': (move, 'Troll'), 'Image': 'images/frog.png'},
                'Troll': {'Story': 'Stepping forth from the darkness, your torch illuminates the form of a \nsnarling cave troll. The towering creature lets forth an earth-shattering \nhowl, bashing the ground with clawed fists. \nIt is time to make your stand.',
                          'Fight': (move, 'Troll_Fight'), 'Image': 'images/frog.png'},
                'Troll_Fight': {'Story': 'The troll strikes at you with vicious claws. Attack or health with your potion.',
                                'Attack': (combat, 'attack'), 'Potion': (combat, 'potion'), 'Image': 'images/frog.png'},
                'Troll_Dead': {'Story': 'The troll drops to floor, lifeless and bloody.',
                               'Look': (move, 'Troll_Body'), 'Leave': (move, 'Cave'), 'Image': 'images/frog.png'},
                'Troll_Body': {'Story': 'You gaze over the troll before reching down to take your trophy. \nThe head of the troll does not come off easy \nbut you manage to take it with you.',
                               'Leave':(troll_head, 'Cave'), 'Image': 'images/frog.png'},
               'Castle': {'Story': 'You are at the castle.\nYou see a guard patroling the upper parapet.\nTo the north is forest.',
                          'North': (move, 'Forest'), 'Talk': (guard_check, 'Guard'), 'Image': 'images/frog.png'},
                'Guard': {'Story': 'The guard looks down at you, \n"Another aspiring warrior come to test their luck, eh? \nWell, lets see... There has been reports of strange noises \ncoming from the western cave. I task you with investigating it. \nGo see the blacksmith to the east for armaments. \nIt may pay to visit the druid in the north as well."',
                          'Leave': (talk_to_guard, 'Castle'), 'Image': 'images/frog.png'},
                'Guard_2': {'Story': 'The guard looks you over with a furrowed brow. \n"Get investigating!"',
                            'Leave': (move, 'Castle'), 'Image': 'images/frog.png'},
                'Guard_3': {'Story': 'As you approach the guard, he looks down to see a trail of blood dripping from your bag. \n "By Thor\'s beard, you\'ve done it! \nBy my honour as Thane, I name you Trollbane. \nTake your place in the meadhall and tell your tale."',
                            'Enter': (move, 'Game_Over'), 'Image': 'images/forest_circle.png'},
                'Blacksmith': {'Story': 'You see the workshop of the Blacksmith.\nThe booming sound of a hammer striking the anvil echos through the surrounding forest.',
                             'West': (move, 'Forest'), 'Enter': (smithy_check, 'Smithy_1'), 'Image': 'images/forest.png'},
                'Smithy_1': {'Story': 'The smithy before you is working hard on a sword.\n She looks up at you, unyielding in her work. \n "I only supply armourment to those who need it. \nCome back when youve got a battle to fight."',
                            'Leave': (move,'Blacksmith'), 'Image': 'images/forest.png'},
                'Smithy_2': {'Story': 'The smithy places her hammer down to eye you over with a smirk. \n"Guess you have a battle to fight." \nThe smithy hands you a set of armour and a sword. \n "Strike hard and strike true. May you return victorius."',
                             'Leave': (talk_to_smithy, 'Blacksmith'), 'Image': 'images/frog.png'},
                'Druid_Hut': {'Story': 'You come accross the druidic hut.\nThe scent of fresh potions brew from the chimney.',
                        'South': (move,'Forest'), 'Enter':(move, 'Druid'), 'Image': 'images/frog.png'},
                'Druid': {'Story': 'The hut is warm and full of magical energy. An old, beared druid rests by the fire.',
                            'Talk': (druid_check, 'Druid_1'), 'Leave':(move, 'Druid_Hut'), 'Image': 'images/forest_circle.png'},
                'Druid_1': {'Story': 'The druid gazes into the fire, smoking a long warden pipe. \n"Blood is on the air this night and devils play is at hand..." \nHe says lowly. "It is dangerous to go alone, take this." \nHe hands you a faintly glowing bottle filled with a vitalising red liquid \nand a tinder pouch for making a torch.',
                            'Leave': (talk_to_druid, 'Druid_Hut'), 'Image': 'images/frog.png'},
                'Druid_2': {'Story': 'The druid is resting soundly a sleep by the fire. \nThe roar of a dragon could not wake him.',
                            'Leave': (move, 'Druid_Hut'), 'Image': 'images/frog.png'},
                'Game_Over': {'Story': 'Game Over!', 'Exit': (exit, 'Exit' ), 'Image': 'images/frog.png'}
               }

def show_current_place():
    """Gets the story at the game_state place

    Returns:
        string: the story at the current place
    """
    global game_state # Lose health as you move
    return f"[Health={health.get()}]\n"+game_places[game_state]['Story']

 
def game_play(command_input):
    """
    Runs the game_play

    Args:
        command input string:
    Returns:
        string: the story at the current place, after an action
    """
    global game_state
    #split game states to check valid token vocab
    story_result = '' 
    valid_tokens = token.valid_list(command_input)
    print('COMMAND_INPUT' + command_input)
    """
    if game_place == 'Troll':
        return (game_state.combat)
    elif game_place != 'Troll':
        return (game_state.explore)
    """     

    if not valid_tokens:
        story_result = 'Can not understand that sorry\n'+show_current_place()
    else:
        for atoken in valid_tokens:
            game_place = game_places[game_state]
            the_place = atoken.capitalize()
            if the_place in game_place:
                place = game_place[the_place]
                story_result = place[0](place)  # Run the action
                print("game_place:", game_place, '\n', "game_state", game_state, '\n', "the_place", the_place, '\n', "story_result",  story_result)
            else:
                story_result = f"Can't {the_place} here\n"+show_current_place()
    return story_result
