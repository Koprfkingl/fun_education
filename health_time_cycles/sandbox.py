import threading
import time

import PySimpleGUI as sg


def long_operation():
    # dlouhá operace zde
    time.sleep(5)
    return "hotovo!"


def main():
    sg.theme('Dark Blue 3')
    layout = [[sg.Text('Stiskněte tlačítko pro spuštění operace.')],
              [sg.Button('Spuštění'), sg.Text(size=(15, 1), key='-OUTPUT-')]]
    window = sg.Window('Long Operation', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Spuštění':
            # vytvoření vlákna pro operaci
            thread = threading.Thread(target=long_operation)
            thread.start()
            result = thread.join()
            window['-OUTPUT-'].update(result)
        else:
            window['-OUTPUT-'].update('Probíhá operace.')

    window.close()


if __name__ == '__main__':
    main()
