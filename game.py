""" 
A comment describing the game module
"""
import PySimpleGUI as sg


import cmd_parser.command_parser as cm


def make_a_window():
    """
    Creates a game window

    Returns:
        window: the handle to the game window
    """

    sg.theme('Dark Red 2')  # please make your windows
    prompt_input = [sg.Text('Enter your command', font='Any 14'), sg.Input(
        key='-IN-', size=(20, 1), font='Any 14')]
    buttons = [sg.Button('Enter',  bind_return_key=True), sg.Button('Exit')]
    command_col = sg.Column([prompt_input, buttons], element_justification='r')
    layout = [[sg.Image(r'images/forest.png', size=(100, 100), key="-IMG-"), sg.Text(cm.show_current_place(), size=(300, 8), font='Any 12', key='-OUTPUT-')],
              [command_col]]

    return sg.Window('Dungeon Crawler', layout, size=(740, 400))


if __name__ == "__main__":
    #define various gamestates to be called in the window loop
    #define window loop for main gameplay

    window = make_a_window()
    game_state = 'explore' #set explore state in story more
    game_state = 'combat' #set combat state when player encounters troll
    game_state = 'game_over' #set game over state when player dies or finishes the game

    while True:
        event, values = window.read() #values of event are read and printed in the window
        print(event) 
        if event == 'Enter':
            current_story = cm.game_play(values['-IN-'].lower()) #checks for lower case letters in valid tokens


            window['-OUTPUT-'].update(current_story) #updates the output window with the current story
            window['-IN-'].update("") #removes input when enter is pressed
            window['-IMG-'].update(cm.game_places[cm.game_state]
                                   ['Image'], size=(100, 100)) #set consistent image size

            pass
        elif event == 'Exit' or event is None or event == sg.WIN_CLOSED: # A persisent window - stays until "Exit" is pressed
            break
        else:
            pass

    window.close() #close window on exit