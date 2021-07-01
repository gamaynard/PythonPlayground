## NamingDemo.py

## Import the simple GUI library
import PySimpleGUI as sg

## Set the color theme
sg.theme('NeutralBlue')

## Create a layout
layout = [
  [sg.Text('Global Identifier (NEFSC or External):'), sg.Input(key="Global")],
  [sg.Text('Grouping identifier (Program Name):'), sg.Input(key="Program")],
  [sg.Text('Data Explanation (?):'), sg.Input(key="Explain")],
  [sg.Text('Spatial Scale (SELECT FROM LIST):'), sg.Input(key="Spatial")],
  [sg.Text('Temporal Resolution (SELECT FROM LIST):'),sg.Input(key="Temp")],
  [sg.Text('Start Date:'),sg.Input(key="Start")],
  [sg.Text('End Date:'),sg.Input(key="End")],
  [sg.Text('Version:'),sg.Input(key="v")],
  [sg.Button('Read'),sg.Exit()]
]

## Create a window
window=sg.Window('ERDDAP Dataset Name Generator',layout)

## Event loop to monitor inputs
while True:
  event, values = window.read()
  print(event, values)
  if event == sg.WIN_CLOSED or event == "Exit":
    break
  
window.close()
