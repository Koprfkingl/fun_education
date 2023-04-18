# every proper app needs fancy gui to confuse users. this is it

"""
author: Michal Sykora
date: 17.4.2023
license: free garbage ®
"""

import threading
import time

# imports
import PySimpleGUI as sg


def long_operation(how_long):
    # convert given time in minutest to time in seconds
    how_long = int(how_long) * 60
    time.sleep(10)
    # reduce remaining time
    how_long = how_long - 10
    return how_long


def gui(theme: str = ''):
    sg.theme(theme)  # Add a touch of color
    sitting_countdown = ''
    drinking_countdown = ''

    # All the stuff inside your window.
    layout = [
        # sitting
        [sg.Text('Sitting counter - do not sit longer than hour.')],
        [sg.Text('Enter time'), sg.InputText(), sg.Button('RUN')],
        [sg.Text('Sitting countdown: '), sg.Text(sitting_countdown, key='sitting')],
        # drinking
        [sg.Text('Drinking counter - do not dry out.')],
        [sg.Text('Enter time'), sg.InputText(), sg.Button('RUN')],
        [sg.Text('Drinking countdown:'), sg.Text(drinking_countdown, key='drinking')]]

    # Create the Window
    window = sg.Window(f'Health timer - theme: {theme}', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

        # sitting button "RUN" pressed
        if event == 'RUN':
            # create thread for wait loop
            thread = threading.Thread(target=long_operation)
            thread.start()

            # iterate until remaining time == 0
            while True:

                # obtain user choice
                how_long = int(values[0])
                if how_long > 0:
                    # wait 10s
                    how_long = long_operation(how_long)
                    # show wait counter in the window
                    window['sitting'].update(how_long)
                    window.refresh()

        # drinking button "RUN" pressed
        if event == 'RUN0':
            drinking_countdown = values[1]
            drinking_output = calculations.timer(drinking_countdown)
            print('drinking countdown is ', drinking_output)
            window['drinking'].update(drinking_output)

    window.close()


gui()

'''
available graphical themes:
['Black', 
'BlueMono', 'BluePurple', 
'BrightColors', 
'BrownBlue', 
'Dark', 'Dark2', 
'DarkAmber', 
'DarkBlack', 'DarkBlack1', 
'DarkBlue', 'DarkBlue1', 'DarkBlue10', 
'DarkBlue11', 'DarkBlue12', 'DarkBlue13', 
'DarkBlue14', 'DarkBlue15', 'DarkBlue16', 
'DarkBlue17', 'DarkBlue2', 'DarkBlue3', 
'DarkBlue4', 'DarkBlue5', 'DarkBlue6', 
'DarkBlue7', 'DarkBlue8', 'DarkBlue9', 
'DarkBrown', 'DarkBrown1', 'DarkBrown2', 
'DarkBrown3', 'DarkBrown4', 'DarkBrown5', 
'DarkBrown6', 'DarkBrown7', 
'DarkGreen', 'DarkGreen1', 'DarkGreen2', 
'DarkGreen3', 'DarkGreen4', 'DarkGreen5', 
'DarkGreen6', 'DarkGreen7', 
'DarkGrey', 'DarkGrey1', 'DarkGrey10', 
'DarkGrey11', 'DarkGrey12', 'DarkGrey13', 
'DarkGrey14', 'DarkGrey15', 'DarkGrey2', 
'DarkGrey3', 'DarkGrey4', 'DarkGrey5', 
'DarkGrey6', 'DarkGrey7', 'DarkGrey8', 
'DarkGrey9', 
'DarkPurple', 'DarkPurple1', 'DarkPurple2', 
'DarkPurple3', 'DarkPurple4', 'DarkPurple5', 
'DarkPurple6', 'DarkPurple7', 
'DarkRed', 'DarkRed1', 'DarkRed2', 
'DarkTanBlue', 
'DarkTeal', 'DarkTeal1', 'DarkTeal10', 
'DarkTeal11', 'DarkTeal12', 'DarkTeal2', 
'DarkTeal3', 'DarkTeal4', 'DarkTeal5', 
'DarkTeal6', 'DarkTeal7', 'DarkTeal8', 
'DarkTeal9', 
'Default', 'Default1', 'DefaultNoMoreNagging', 
'GrayGrayGray', 
'Green', 'GreenMono', 'GreenTan', 
'HotDogStand', 
'Kayak', 
'LightBlue', 'LightBlue1', 'LightBlue2', 
'LightBlue3', 'LightBlue4', 'LightBlue5', 
'LightBlue6', 'LightBlue7', 
'LightBrown', 'LightBrown1', 'LightBrown10', 
'LightBrown11', 'LightBrown12', 'LightBrown13', 
'LightBrown2', 'LightBrown3', 'LightBrown4', 
'LightBrown5', 'LightBrown6', 'LightBrown7', 
'LightBrown8', 'LightBrown9', 
'LightGray1', 
'LightGreen', 'LightGreen1', 'LightGreen10', 
'LightGreen2', 'LightGreen3', 'LightGreen4', 
'LightGreen5', 'LightGreen6', 'LightGreen7', 
'LightGreen8', 'LightGreen9', 
'LightGrey', 'LightGrey1', 'LightGrey2', 
'LightGrey3', 'LightGrey4', 'LightGrey5', 
'LightGrey6', 
'LightPurple', 
'LightTeal', 
'LightYellow', 
'Material1', 'Material2', 
'NeutralBlue', 
'Purple', 
'Python', 'PythonPlus', 
'Reddit', 
'Reds', 
'SandyBeach', 
'SystemDefault', 'SystemDefault1', 'SystemDefaultForReal', 
'Tan', 'TanBlue', 
'TealMono', 
'Topanga']
'''
