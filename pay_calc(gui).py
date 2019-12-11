#©2019 Charles L. Arnold
#GNU GPL v3 licenced

import PySimpleGUI as sg
import tkinter #required to run on Android
import urllib.request
import os

sg.change_look_and_feel('Kayak')

tab1_layout = [[sg.Txt('\nPay Calculator\n')],  
               [sg.Txt('-'*50)],
               [sg.Txt('Pay: $'), sg.In(size=(5,1), key='wage'), sg.Txt('/hr.')],          
	       [sg.In(size=(5,1), key='hours'), sg.Txt('Hours')],
	       [sg.Txt('Tax Percentage:'), sg.In(size=(3,1), key='percent'), sg.Txt('%')],     
	       [sg.Txt('-'*50)],
	       [sg.Txt('', size=(20,2), key='gross')],   
	       [sg.Txt('', size=(20,2), key='net')],   
	       [sg.Button('Calculate', bind_return_key=True), sg.Txt(' ', size=(8,3)), sg.Button('Exit')],
	       [sg.Txt(key='dis', size=(20,2))]]
            
tab2_layout = [[sg.Txt('\n©2019 Charles L. Arnold\n\nGNU GPL v3 licenced\n\nsource code and program are free to use, modify, and distribute as long as they remain free.\n', size=(25,11))],
	      [sg.Button('Download Source Code')],
	      [sg.Txt('', key='x', size=(24,5))]]

layout = [[sg.TabGroup([[sg.Tab(' Main ', tab1_layout), sg.Tab(' Licence ', tab2_layout)]])]]
window = sg.Window('Pay Calculator', layout) 

while True:
  event, values = window.read()
  if event is 'Download Source Code':
    d = os.getcwd()
    url = 'https://github.com/charleslarnold/Pay-Calculator/archive/master.zip'
    urllib.request.urlretrieve(url, d + '/pay_calc.zip')
    for i in range(100):
      sg.OneLineProgressMeter('Downloading', i+1, 100,  'key', 'downloading from Github')
    sg.popup('Download Complete')
    window['x'].update('\nfiles located in\n\n' + d + '/pay_calc.zip')
  elif event is 'Calculate':
    try:
      wage = float(values['wage'])
      hours = float(values['hours'])
      percent = float(values['percent'])
      
      if hours <= 40:
        gross = wage * hours
      else:
        pay = wage * 40
        ot_wage = wage * 1.5
        ot_hours = hours - 40
        ot_pay = ot_wage * ot_hours
        gross = pay + ot_pay

      tax_per = percent / float(100)
      tax = gross * tax_per
      net = gross - tax

      gross = 'Gross Pay: ${:.2f}'.format(gross)
      net = 'Net Pay: ${:.2f}*'.format(net)
      dis = '*estimated based on given tax percentage'
     
    except:
      gross = 'something went wrong'
      net = 'please try again'
      dis = ' '

    try:
      window['gross'].update(gross)
      window['net'].update(net)
      window['dis'].update(dis)

    except ValueError:
      pass
      
  else:
    break
