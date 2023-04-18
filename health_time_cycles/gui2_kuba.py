# kuba navrhnul pouziti modulu schedule

import PySimpleGUI as sg
import schedule


# update window
def update_sitting(window):
    window['sitting'].update('sit now')
    return schedule.CancelJob


def update_drinking(window):
    window['drinking'].update('drink now')
    return schedule.CancelJob


def gui(theme: str = ''):
    sg.theme(theme)  # Add a touch of color

    # All the stuff inside your window.
    layout = [
        # sitting
        [sg.Text('Sitting counter - do not sit longer than hour.')],
        [sg.Text('Enter time [min]'), sg.InputText(), sg.Button('RUN')],
        [sg.Text('Status: ', key='sitting')],
        [sg.Button('Reset')],
        # drinking
        [sg.Text('Drinking counter - do not dry out.')],
        [sg.Text('Enter time [min]'), sg.InputText(), sg.Button('RUN')],
        [sg.Text('Status:', key='drinking')],
        [sg.Button('Reset')]]

    # Create the Window
    window = sg.Window(f'Health timer - theme: {theme}', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read(timeout=100)
        if event == sg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
            break

        if event == 'RUN':
            # obtain user value
            how_long = int(values[0])

            # run the job after given time
            schedule.every(how_long).seconds.do(update_sitting, window=window)

        if event == 'RUN0':
            # obtain user value
            how_long_drink = int(values[1])

            # run the job after given time
            schedule.every(how_long_drink).seconds.do(update_drinking, window=window)

        schedule.run_pending()

        if event == 'Reset':
            # empty scheduled job
            # reset status message
            window['sitting'].update('')

        if event == 'Reset1':
            # reset status message
            window['drinking'].update('')


gui()
