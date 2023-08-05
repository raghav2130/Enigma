from machine import Enigma
import PySimpleGUI as sg

def main():
    enigma = Enigma()

    layout = [
        [sg.Text('Enter the text to encrypt:')],
        [sg.Input(key='-TEXT-')],
        [sg.Button('Encrypt'), sg.Button('Reset')],
        [sg.Output(size=(50, 10))]
    ]

    window = sg.Window('Enigma Machine', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        if event == 'Encrypt':
            text = values['-TEXT-']
            encrypted_text = enigma.encrypt(text)
            print(f"Encrypted Text: {encrypted_text}")
        elif event == 'Reset':
            window['-TEXT-'].update('')

    window.close()


if __name__ == "__main__":
    main()
