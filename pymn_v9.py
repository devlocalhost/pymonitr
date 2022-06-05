#!/usr/bin/env python3

from os import system, popen
from sys import exit
from time import sleep
from random import choice
from argparse import ArgumentParser
from datetime import timedelta, datetime
from threading import Thread
from subprocess import check_output

try:
    from psutil import virtual_memory, cpu_freq, disk_usage, cpu_percent, cpu_count, swap_memory, getloadavg, net_io_counters
    from colorhex import colorex, BOLD, BLINKING
    from cursor import hide, show

except ModuleNotFoundError:
    system('clear')
    print('psutil, colorhex and cursor are not installed. please run pip3 install colorhex psutil cursor, and run the program again')
    exit()

CPU_MODEL = check_output("lscpu | grep 'Model name' | cut -f 2 -d ':' | awk '{$1=$1}1' | tr '\n', ' '", shell=True, text=True)
ARCH_TYPE = check_output("uname -m | tr '\n', ' '", shell=True, text=True)
CPU_CACHE = check_output("cat /proc/cpuinfo | grep 'cache size' | cut -f 2 -d ':' | awk '{$1=$1}1' | tr '\n', ' '", shell=True, text=True)

extime = datetime.now().strftime('%I:%M:%S %p')

VERSION = 'v9'
COLORLIST = ['7289da', '43b581', 'fdcc4b', 'fa8231', 'f04947', 'd892e2', '82589f', 'ccae62', 'FEA47F'] 

flag = ArgumentParser(f'python3 pymn_{VERSION}.py')

flag.add_argument('-r', type=float, default=1, help='How many seconds should the program refresh the stats (Default is 1). Example: pymn.py -r 2. Float numbers are not allowed.')
flag.add_argument('-v', help='Displays the programs version.', action='store_true')

fl_str = flag.parse_args()

if fl_str.v:
    system('clear')
    print(colorex('PyMonitr version: ', '7289da', style=BOLD), end=colorex(f'{VERSION}\n', '43b581', style=BOLD))
    exit()

def convertbytes(fsize, units=(' bytes',' KB',' MB',' GB',' TB')):
    return "{:.2f}{}".format(float(fsize), units[0]) if fsize < 1024 else convertbytes(fsize / 1024, units[1:])

def convert_to_seconds(sec):
    UNITS = {'s':'seconds', 'm':'minutes', 'h':'hours', 'd':'days', 'w':'weeks'}
    return int(timedelta(**{UNITS.get(m.group('unit').lower(), 'seconds'): int(m.group('val')) for m in re.finditer(r'(?P<val>\d+)(?P<unit>[smhdw]?)', sec, flags=re.I)}).total_seconds())

def getcputemp():
    try:
        with open(r"/sys/class/thermal/thermal_zone0/temp") as ctemp: # or cat /sys/class/hwmon/hwmon0/temp1_input
            return float(ctemp.readline()) / 1000

    except OSError:
        try:
            with open(r"/sys/class/hwmon/hwmon0/temp1_input") as ctemp: # or cat /sys/class/hwmon/hwmon0/temp1_input
                return float(ctemp.readline()) / 1000

        except OSError:
            return None

def monitr():
    while True:
        ram = virtual_memory()
        cpu = cpu_freq(percpu=True)
        storage = disk_usage('/')
        swap = swap_memory()

        total_ram = convertbytes(ram[0])
        used_ram = ram[0] - ram[1]
        free_ram = convertbytes(ram[1])

        percent_used_ram = ram.percent
        percent_free_ram = abs(percent_used_ram)

        total_swap = convertbytes(swap[0])
        used_swap = convertbytes(swap[1])
        free_swap = convertbytes(swap[2])

        percent_used_swap = swap.percent
        percent_free_swap = abs(percent_used_swap)

        total_storage = convertbytes(storage[0])
        used_storage = convertbytes(storage[1])
        free_storage = convertbytes(storage[2])

        percent_used_storage = storage.percent
        percent_free_storage = abs(percent_used_storage)

        bytessent = net_io_counters()[0]
        bytesrevc = net_io_counters()[1]
        packetssent = net_io_counters()[2]
        packetsrevc = net_io_counters()[3]

        print(colorex(f'     [PyMonitr {VERSION}]', '7289da', style=BOLD))

        print(colorex('|===== [Network] =====|', 'CAD3c8', style=BOLD))

        print(colorex(f'Sent: {convertbytes(bytessent)}', '7289da', style=BOLD))
        print(colorex(f'Received: {convertbytes(bytesrevc)}', 'f04947', style=BOLD))
        print(colorex(f'Packets sent: {convertbytes(packetssent)}', '7289da', style=BOLD))
        print(colorex(f'Packets receive: {convertbytes(packetsrevc)}', 'f04947', style=BOLD))

        print(colorex('|===== [Storage] =====|', 'CAD3c8', style=BOLD))
        print(colorex(f'Total: {total_storage}', '7289da', style=BOLD))

        if int(percent_used_storage) in range(0, 50):
            print(colorex(f'Used: {used_storage} | {percent_used_storage}%', '43b581', style=BOLD).replace('-', ''))
            print(colorex(f'Free: {free_storage} | {percent_free_storage - 100:.1f}%', '43b581', style=BOLD).replace('-', ''))

        elif int(percent_used_storage) in range(50, 80):
            print(colorex(f'Used: {used_storage} | {percent_used_storage}%', 'fdcc4b', style=BOLD).replace('-', ''))
            print(colorex(f'Free: {free_storage} | {percent_free_storage - 100:.1f}%', 'fdcc4b', style=BOLD).replace('-', ''))

        elif int(percent_used_storage) in range(80, 90):
            print(colorex(f'Used: {used_storage} | {percent_used_storage}%', 'fa8231', style=BOLD).replace('-', ''))
            print(colorex(f'Free: {free_storage} | {percent_free_storage - 100:.1f}%', 'fa8231', style=BOLD).replace('-', ''))

        elif int(percent_used_storage) in range(90, 101):
            print(colorex(f'Used: {used_storage} | {percent_used_storage}% | ', 'f04947', style=BOLD), end=colorex('STORAGE USAGE IS TOO HIGH!!\n', 'f04947', style=[BLINKING, BOLD]).replace('-', ''))
            print(colorex(f'Free: {free_storage} | {percent_free_storage - 100:.1f}% | ', 'f04947', style=BOLD), end=colorex('LOW STORAGE SPACE AVAILABLE!!\n', 'f04947', style=[BLINKING, BOLD]).replace('-', ''))

        print(colorex('|======= [RAM] =======|', 'CAD3c8', style=BOLD))
        print(colorex(f'Total: {total_ram}', '7289da', style=BOLD))

        if int(percent_used_ram) in range(0, 50):
            print(colorex(f'Used: {convertbytes(used_ram)} | {percent_used_ram}%', '43b581', style=BOLD).replace('-', ''))
            print(colorex(f'Free: {free_ram} | {percent_free_ram - 100:.1f}%', '43b581', style=BOLD).replace('-', ''))

        elif int(percent_used_ram) in range(50, 80):
            print(colorex(f'Used: {convertbytes(used_ram)} | {percent_used_ram}%', 'fdcc4b', style=BOLD).replace('-', ''))
            print(colorex(f'Free: {free_ram} | {percent_free_ram - 100:.1f}%', 'fdcc4b', style=BOLD).replace('-', ''))

        elif int(percent_used_ram) in range(80, 90):
            print(colorex(f'Used: {convertbytes(used_ram)} | {percent_used_ram}%', 'fa8231', style=BOLD).replace('-', ''))
            print(colorex(f'Free: {free_ram} | {percent_free_ram - 100:.1f}%', 'fa8231', style=BOLD).replace('-', ''))

        elif int(percent_used_ram) in range(90, 101):
            print(colorex(f'Used: {convertbytes(used_ram)} | {percent_used_ram}% | ', 'f04947', style=BOLD), end=colorex('RAM USAGE IS TOO HIGH!!\n', 'f04947', style=[BLINKING, BOLD]).replace('-', ''))
            print(colorex(f'Free: {free_ram} | {percent_free_ram - 100:.1f}% | ', 'f04947', style=BOLD), end=colorex('LOW RAM MEMORY AVAILABLE!!\n', 'f04947', style=[BLINKING, BOLD]).replace('-', ''))

        print(colorex('|====== [Swap] =======|', 'CAD3c8', style=BOLD))
        print(colorex(f'Total: {total_swap}', '7289da', style=BOLD))

        if int(percent_used_swap) in range(0, 50):
            print(colorex(f'Used: {used_swap} | {percent_used_swap}%', '43b581', style=BOLD).replace('-', ''))
            print(colorex(f'Free: {free_swap} | {percent_free_swap - 100:.1f}%', '43b581', style=BOLD).replace('-', ''))

        elif int(percent_used_swap) in range(50, 80):
            print(colorex(f'Used: {used_swap} | {percent_used_swap}%', 'fdcc4b', style=BOLD).replace('-', ''))
            print(colorex(f'Free: {free_swap} | {percent_free_swap - 100:.1f}%', 'fdcc4b', style=BOLD).replace('-', ''))

        elif int(percent_used_swap) in range(80, 90):
            print(colorex(f'Used: {used_swap} | {percent_used_swap}%', 'fa8231', style=BOLD).replace('-', ''))
            print(colorex(f'Free: {free_swap} | {percent_free_swap - 100:.1f}%', 'fa8231', style=BOLD).replace('-', ''))

        elif int(percent_used_swap) in range(90, 101):
            print(colorex(f'Used: {used_swap} | {percent_used_swap}% | ', 'f04947', style=BOLD), end=colorex('SWAP USAGE IS TOO HIGH!!\n', 'f04947', style=[BLINKING, BOLD]).replace('-', ''))
            print(colorex(f'Free: {free_swap} | {percent_free_swap - 100:.1f}% | ', 'f04947', style=BOLD), end=colorex('LOW SWAP MEMORY AVAILABLE!!\n', 'f04947', style=[BLINKING, BOLD]).replace('-', ''))
            
        print(colorex('|======= [CPU] =======|', 'CAD3c8', style=BOLD))

        cpu_perc = cpu_percent()

        print(colorex(f'CPU model: {CPU_MODEL}', 'FEA47F', style=BOLD))

        if int(cpu_perc) in range(0, 50):
            print(colorex(f'Usage: {cpu_perc}%', '43b581', style=BOLD))

        elif int(cpu_perc) in range(50, 80):
            print(colorex(f'Usage: {cpu_perc}%', 'fdcc4b', style=BOLD))

        elif int(cpu_perc) in range(80, 90):
            print(colorex(f'Usage: {cpu_perc}%', 'fa8231', style=BOLD))

        elif int(cpu_perc) in range(90, 101):
            print(colorex(f'Usage: {cpu_perc}% | ', 'f04947', style=BOLD), end=colorex('CPU USAGE IS TOO HIGH!!\n', 'f04947', style=[BLINKING, BOLD]))

        if getcputemp() is None:
            print(colorex('Temperature: Could not read temperature', 'f04947', style=BOLD))

        elif int(getcputemp()) in range(int(float(0)), int(float(50))):
            print(colorex(f'Temperature: {getcputemp()} °C', '43b581', style=BOLD))

        elif int(getcputemp()) in range(int(float(50)), int(float(80))):
            print(colorex(f'Temperature: {getcputemp()} °C', 'fdcc4b', style=BOLD))

        elif int(getcputemp()) in range(int(float(80)), int(float(90))):
            print(colorex(f'Temperature: {getcputemp()} °C', 'fa8231', style=BOLD))

        elif int(getcputemp()) in range(int(float(90)), int(float(150))):
            print(colorex(f'Temperature: {getcputemp()} °C | ', 'f04947', style=BOLD), end=colorex('CPU TEMPERATURE IS TOO HIGH!!\n', 'f04947', style=[BLINKING, BOLD]))

        for freq in cpu:
            pass

        for i, percentage in enumerate(cpu_percent(percpu=True)):
            if int(percentage) in range(0, 50):
                print(colorex(f'Core {i + 1} frequency: {freq[0]} GHz | {percentage}%', '43b581', BOLD))

            elif int(percentage) in range(50, 80):
                print(colorex(f'Core {i + 1} frequency: {freq[0]} GHz | {percentage}%', 'fdcc4b', BOLD))

            elif int(percentage) in range(80, 90):
                print(colorex(f'Core {i + 1} frequency: {freq[0]} GHz | {percentage}%', 'fa8231', BOLD))

            elif int(percentage) in range(90, 101):
                print(colorex(f'Core {i + 1} frequency: {freq[0]} GHz | {percentage}%', 'f04947', BOLD))

        print(colorex(f'Architecture type: {ARCH_TYPE}|', 'BCA799', BOLD), end=colorex(f' Cache size: {CPU_CACHE}\n', 'D9D8C1', BOLD))

        if int(getloadavg()[0]) in range(int(float(0)), int(float(3))):
            print(colorex(f'Averange load (1, 5 and 10 mins): {getloadavg()[0]}, {getloadavg()[1]}, {getloadavg()[2]}', '43b581', style=BOLD))

        elif int(getloadavg()[0]) in range(int(float(3)), int(float(6))):
            print(colorex(f'Averange load (1, 5 and 10 mins: {getloadavg()[0]}, {getloadavg()[1]}, {getloadavg()[2]}', 'fdcc4b', style=BOLD))

        elif int(getloadavg()[0]) in range(int(float(6)), int(float(9))):
            print(colorex(f'Averange load (1, 5 and 10 mins): {getloadavg()[0]}, {getloadavg()[1]}, {getloadavg()[2]}', 'fa8231', style=BOLD))

        elif int(getloadavg()[0]) in range(int(float(9)), int(float(200))):
            print(colorex(f'Averange load (1, 5 and 10 mins): {getloadavg()[0]}. {getloadavg()[1]}. {getloadavg()[2]}', 'f04947', style=BOLD))
        
        print(colorex(f'Physical cores: {cpu_count(logical=False)}, ', '8da4ee', style=BOLD), end=colorex(f'Logical: {cpu_count(logical=True)}\n', 'e8b39d', style=BOLD))
        
        try:
            sleep(float(fl_str.r))

        except KeyboardInterrupt:
            show()
            exit()

        system('clear')

system('clear')
hide()
print(colorex(f' -- [PyMonitr {VERSION}] -- ', '7289da', style=BOLD))
print(colorex(' -- Report bugs on -- ', '7289da', style=[BOLD]))
print(colorex(' -- the github repo!! -- ', '7289da', style=[BOLD]))
hide()
sleep(2)
system('clear')

print(colorex('.', '7289da', style=[BOLD]))
hide()
sleep(0.15)
system('clear')
print(colorex('..', '7289da', style=[BOLD]))
hide()
sleep(0.15)
system('clear')
print(colorex('...', '7289da', style=[BOLD]))
hide()
sleep(0.15)
system('clear')
monitr()
