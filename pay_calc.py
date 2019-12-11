#©2019 Charles L. Arnold
#GNU GPL v3 licenced

from prettytable import PrettyTable
import os

os.system('cls' if os.name == 'nt' else 'clear')

print('''
	     "Pay Calculator"
	  ©2019 Charles L. Arnold
            GNU GPL v3 licenced''')

wage = float(input('\nEnter hourly wage: $'))
hours = float(input('\nEnter hours worked: '))
tax_ = float(input('\nEnter estimated tax percentage: %'))

ot = wage * 1.5

if hours >= 40:
  reg_hrs = 40
  ot_hrs = hours - reg_hrs
else:
  reg_hrs = hours
  ot_hrs = 0
    
reg_pay = wage * reg_hrs
ot_pay = ot * ot_hrs
gross = reg_pay + ot_pay

tax_per = tax_ / float(100)
tax = gross * tax_per

net = gross - tax

os.system('cls' if os.name == 'nt' else 'clear')

x = PrettyTable()
x.field_names = ['Straight Pay Info', ' ']
x.add_row(['Straight Wage', '${:.2f}/hr'.format(wage)])
x.add_row(['Straight Hours', '{} hours'.format(reg_hrs)])
x.add_row(['Straight Gross Pay', '${:.2f}'.format(reg_pay)])

y = PrettyTable()
y.field_names = ['Overtime Pay Info', ' ']
y.add_row(['Overtime Wage', '${:.2f}/hr'.format(ot)])
y.add_row(['Overtime Hours', '{} hours'.format(ot_hrs)])
y.add_row(['Overtime Gross Pay', '${:.2f}'.format(ot_pay)])

z = PrettyTable()
z.field_names = ['Total Pay Info', ' ']
z.add_row(['Total Hours', '{} hours'.format(hours)])
z.add_row(['Total Gross Pay', '${:.2f}'.format(gross)])
z.add_row(['Estimated Tax Withheld', '${:.2f}'.format(tax)])
z.add_row(['Estimated Net Pay', '${:.2f}'.format(net)])

print(x)
print(y)
print(z)
input()
