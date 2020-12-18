from sys import argv

script_name, hours, pay, prem = argv

print(f'Ваша заработная плата составляет: {(int(hours) * int(pay)) + int(prem)}')

