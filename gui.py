import PySimpleGUI as sg
import threading
from Node import Node
layout = [[sg.Text("Balance: "), sg.Text(0)], [sg.Text('Reciever'), sg.InputText(), sg.Button("Send")], [
    sg.Button("Mine"), sg.Button("Stop Mining")
]]

# Create the window
window = sg.Window("BierCoin", layout)

abort = False


def threadtest():
    for x in range(1, 10000):
        if abort:
            break
        print(x)


# Create an event loop
while True:
    event, values = window.read()

    if event == "Mine":
        abort = False
        x = threading.Thread(target=threadtest, args=())
        x.start()
    if event == "Stop Mining":
        abort = True
    if event == sg.WIN_CLOSED:
        break

window.close()
