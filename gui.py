import PySimpleGUI as sg
import time
import threading
from Node import Node
node = Node()

layout = [[sg.Text(node.wallet.pubkey)], [sg.Text("Balance: "), sg.Text(0)], [sg.Text('Reciever'), sg.InputText(), sg.Button("Send")], [
    sg.Button("Mine"), sg.Button("Stop Mining")
]]

# Create the window
window = sg.Window("BierCoin", layout)
#
abort = False

stop = False


def mine():
    while True:
        if abort:
            time.sleep(1)
            if stop:
                break
            continue
        if stop:
            break
        node.start_mining()


# Create an event loop
x = threading.Thread(target=mine, args=())
first_time = True


while True:
    event, values = window.read()

    if event == "Mine":
        abort = False
        if first_time:
            x.start()
            first_time = False
    if event == "Stop Mining":
        abort = True
    if event == sg.WIN_CLOSED:
        stop = True
        break

window.close()
