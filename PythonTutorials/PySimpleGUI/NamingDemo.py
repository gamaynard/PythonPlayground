## NamingDemo.py

## Import the simple GUI library
import PySimpleGUI as sg

## Set the color theme
sg.theme('NeutralBlue')

## Create a layout
layout = [
  ## The global identifier tells the user whether the data was collected by
  ## NEFSC, NOAA, or an external group
  [sg.Text('Global Identifier:'), sg.InputCombo(['NEFSC','NOAA','External'])],
  ## The grouping identifier is a unique project identifier
  ## I'm not quite sure how to control inputs to this field
  [sg.Text('Grouping identifier (Program Name):'),sg.Input(key="Program")],
  ## I assume the data explanation is the type of data being collected, whether
  ## that's temperature, depth, salinity, DO, etc., but maybe I'm wrong?
  [sg.Text('Data Explanation (?):'),sg.Input(key="Explain")],
  ## Not sure how to control this field. By spatial scale, do we mean
  ##    general: (e.g., local, regional, national, international) or
  ##    specific: (e.g., NW Atlantic, Gulf of Maine, Great South Channel)
  ## More information is needed to control inputs on this field
  [sg.Text('Spatial Scale:'),sg.Input(key="Spatial")],
  ## Temporal resolution is a drop down menu
  [sg.Text('Temporal Resolution:'),sg.InputCombo(["Minute","Hourly","Daily","Weekly","Monthly","Annually"])],
  ## Start date and end date are recorded as date values in the format
  ## yyyy-mm-dd 
  [sg.CalendarButton('Select Start Date', close_when_date_chosen=True, target='Start', location=(0,0), no_titlebar=False, format='%Y-%m-%d'),sg.Input(key='Start')],
  [sg.CalendarButton('Select End Date', close_when_date_chosen=True,  target='End', location=(0,0), no_titlebar=False, format='%Y-%m-%d'),sg.Input(key='End')],
  ## I'm not quite sure how to control version numbers, I guess that's up to the
  ## individual project?
  [sg.Text('Version:'),sg.Input(key="v")],
  [sg.Exit()]
]

## Create a window
window=sg.Window('ERDDAP Dataset Name Generator',layout)

## Event loop to monitor inputs
while True:
  event, values = window.read()
  print(event, values)
  if event == "Exit":
    dataName="_".join([values[0],values["Program"],values["Explain"],values["Spatial"],values[1],values["Start"],values["End"],values["v"]])
    sg.popup("Filename: {dataname[0]}")
window.close()
