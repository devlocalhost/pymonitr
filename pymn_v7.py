from psutil import virtual_memory, cpu_freq, disk_usage, cpu_percent, cpu_count, swap_memory
from subprocess import check_output
from colorhex import colorex, BOLD, BLINKING, UNDERLINE, ITALIC
from time import sleep
from sys import exit
from os import system

CPU_MODEL = check_output("lscpu | grep 'Model name' | cut -f 2 -d ':' | awk '{$1=$1}1' | tr '\n', ' '", shell=True, text=True)
ARCH_TYPE = check_output("uname -m | tr '\n', ' '", shell=True, text=True)
VERSION = 'v7'

def convertbytes(fsize, units=[' bytes',' KB',' MB',' GB',' TB', ' PB', ' EB']):
	return "{:.2f}{}".format(float(fsize), units[0]) if fsize < 1024 else convertbytes(fsize / 1024, units[1:])

system('clear')
print(colorex(f' -- [PyMonitr {VERSION}] -- ', '7289da', style=BOLD))
sleep(1)
system('clear')

print('.')
sleep(0.15)
system('clear')
print('..')
sleep(0.15)
system('clear')
print('...')
sleep(0.15)
system('clear')

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

	print(colorex('|===== [Storage] =====|', 'CAD3c8', style=BOLD))
	print(colorex(f'Total: {total_storage}', '7289da', style=BOLD))

	if int(percent_used_storage) in range(0, 50):
		print(colorex(f'Used: {used_storage} | {percent_used_storage}%', '43b581', style=BOLD))

	elif int(percent_used_storage) in range(50, 80):
		print(colorex(f'Used: {used_storage} | {percent_used_storage}%', 'fdcc4b', style=BOLD))

	elif int(percent_used_storage) in range(80, 90):
		print(colorex(f'Used: {used_storage} | {percent_used_storage}%', 'fa8231', style=BOLD))

	elif int(percent_used_storage) in range(90, 101):
		print(colorex(f'Used: {used_storage} | {percent_used_storage}% | ', 'f04947', style=BOLD), end=colorex('STORAGE USAGE IS TOO HIGH!!\n', 'f04947', style=[BLINKING, BOLD]))

	if int(percent_free_storage) in range(0, 50):
		print(colorex(f'Free: {free_storage} | {percent_free_storage - 100:.1f}%', '43b581', style=BOLD).replace('-', ''))

	elif int(percent_free_storage) in range(50, 80):
		print(colorex(f'Free: {free_storage} | {percent_free_storage - 100:.1f}%', 'fdcc4b', style=BOLD).replace('-', ''))

	elif int(percent_free_storage) in range(80, 90):
		print(colorex(f'Free: {free_storage} | {percent_free_storage - 100:.1f}%', 'fa8231', style=BOLD).replace('-', ''))

	elif int(percent_free_storage) in range(90, 101):
		print(colorex(f'Free: {free_storage} | {percent_free_storage - 100:.1f}% | ', 'f04947', style=BOLD), end=colorex('LOW STORAGE SPACE AVAILABLE!!\n', 'f04947', style=[BLINKING, BOLD]))

	print(colorex('|======= [RAM] =======|', 'CAD3c8', style=BOLD))
	print(colorex(f'Total: {total_ram}', '7289da', style=BOLD))

	if int(percent_used_ram) in range(0, 50):
		print(colorex(f'Used: {convertbytes(used_ram)} | {percent_used_ram}%', '43b581', style=BOLD))

	elif int(percent_used_ram) in range(50, 80):
		print(colorex(f'Used: {convertbytes(used_ram)} | {percent_used_ram}%', 'fdcc4b', style=BOLD))

	elif int(percent_used_ram) in range(80, 90):
		print(colorex(f'Used: {convertbytes(used_ram)} | {percent_used_ram}%', 'fa8231', style=BOLD))

	elif int(percent_used_ram) in range(90, 101):
		print(colorex(f'Used: {convertbytes(used_ram)} | {percent_used_ram}% | ', 'f04947', style=BOLD), end=colorex('RAM USAGE IS TOO HIGH!!\n', 'f04947', style=[BLINKING, BOLD]))

	if int(percent_free_ram) in range(0, 50):
		print(colorex(f'Free: {free_ram} | {percent_free_ram - 100:.1f}%', '43b581', style=BOLD).replace('-', ''))

	elif int(percent_free_ram) in range(50, 80):
		print(colorex(f'Free: {free_ram} | {percent_free_ram - 100:.1f}%', 'fdcc4b', style=BOLD).replace('-', ''))

	elif int(percent_free_ram) in range(80, 90):
		print(colorex(f'Free: {free_ram} | {percent_free_ram - 100:.1f}%', 'fa8231', style=BOLD).replace('-', ''))

	elif int(percent_free_ram) in range(90, 101):
		print(colorex(f'Free: {free_ram} | {percent_free_ram - 100:.1f}% | ', 'f04947', style=BOLD), end=colorex('LOW RAM MEMORY AVAILABLE!!\n', 'f04947', style=[BLINKING, BOLD]))

	print(colorex('|====== [Swap] =======|', 'CAD3c8', style=BOLD))
	print(colorex(f'Total: {total_swap}', '7289da', style=BOLD))

	if int(percent_used_swap) in range(0, 50):
		print(colorex(f'Used: {used_swap} | {percent_used_swap}%', '43b581', style=BOLD))

	elif int(percent_used_swap) in range(50, 80):
		print(colorex(f'Used: {used_swap} | {percent_used_swap}%', 'fdcc4b', style=BOLD))

	elif int(percent_used_swap) in range(80, 90):
		print(colorex(f'Used: {used_swap} | {percent_used_swap}%', 'fa8231', style=BOLD))

	elif int(percent_used_swap) in range(90, 101):
		print(colorex(f'Used: {used_swap} | {percent_used_swap}% | ', 'f04947', style=BOLD), end=colorex('SWAP USAGE IS TOO HIGH!!\n', 'f04947', style=[BLINKING, BOLD]))

	if int(percent_free_swap) in range(0, 50):
		print(colorex(f'Free: {free_swap} | {percent_free_swap - 100:.1f}%', '43b581', style=BOLD).replace('-', ''))

	elif int(percent_free_swap) in range(50, 80):
		print(colorex(f'Free: {free_swap} | {percent_free_swap - 100:.1f}%', 'fdcc4b', style=BOLD).replace('-', ''))

	elif int(percent_free_swap) in range(80, 90):
		print(colorex(f'Free: {free_swap} | {percent_free_swap - 100:.1f}%', 'fa8231', style=BOLD).replace('-', ''))

	elif int(percent_free_swap) in range(90, 101):
		print(colorex(f'Free: {free_swap} | {percent_free_swap - 100:.1f}% | ', 'f04947', style=BOLD), end=colorex('LOW SWAP MEMORY AVAILABLE!!\n', 'f04947', style=[BLINKING, BOLD]))

	print(colorex('|======= [CPU] =======|', 'CAD3c8', style=BOLD))

	cpu_perc = cpu_percent()

	if int(cpu_perc) in range(0, 50):
		print(colorex(f'Usage: {cpu_perc}%', '43b581', style=BOLD))

	elif int(cpu_perc) in range(50, 80):
		print(colorex(f'Usage: {cpu_perc}%', 'fdcc4b', style=BOLD))

	elif int(cpu_perc) in range(80, 90):
		print(colorex(f'Usage: {cpu_perc}%', 'fa8231', style=BOLD))

	elif int(cpu_perc) in range(90, 101):
		print(colorex(f'Usage: {cpu_perc}% | ', 'f04947', style=BOLD), end=colorex('CPU USAGE IS TOO HIGH!!\n', 'f04947', style=[BLINKING, BOLD]))

	with open(r"/sys/class/thermal/thermal_zone0/temp") as ctemp:
		cputemp = str(float(ctemp.readline()) / 1000)[:-2]

		if int(cputemp) in range(0, 50):
			print(colorex(f'Temperature: {cputemp} °C', '43b581', style=BOLD))

		elif int(cputemp) in range(50, 80):
			print(colorex(f'Temperature: {cputemp} °C', 'fdcc4b', style=BOLD))

		elif int(cputemp) in range(80, 90):
			print(colorex(f'Temperature: {cputemp} °C', 'fa8231', style=BOLD))

		elif int(cputemp) in range(90, 200):
			print(colorex(f'Temperature: {cputemp} °C | ', 'f04947', style=BOLD), end=colorex('CPU TEMPERATURE IS TOO HIGH!!\n', 'f04947', style=[BLINKING, BOLD]))

	print(colorex(f'Total cores: {cpu_count()}', '82589f', style=BOLD))
	print(colorex(f'Architecture type: {ARCH_TYPE}', 'ccae62', style=BOLD))
	print(colorex(f'CPU model/name: {CPU_MODEL}', 'FEA47F', style=BOLD))

	try:
		sleep(1)

	except KeyboardInterrupt:
		exit()

	system('clear')