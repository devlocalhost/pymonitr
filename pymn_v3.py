from psutil import virtual_memory, cpu_freq, disk_usage, cpu_percent, cpu_count, swap_memory
from subprocess import check_output
from termcolor import colored
from time import sleep
from sys import exit
from os import system

CPU_MODEL = check_output("lscpu | grep 'Model name' | cut -f 2 -d ':' | awk '{$1=$1}1' | tr '\n', ' '", shell=True, text=True)
ARCH_TYPE = check_output("uname -m | tr '\n', ' '", shell=True, text=True)
CLUSTERS = check_output("lscpu | grep 'Socket(s)' | cut -f 2 -d ':' | awk '{$1=$1}1' | tr '\n', ' '", shell=True, text=True)
CORES_PER_CLUSTER = check_output("lscpu | grep 'Core(s) per socket' | cut -f 2 -d ':' | awk '{$1=$1}1' | tr '\n', ' '", shell=True, text=True)
THREADS_PER_CORE = check_output("lscpu | grep 'Thread(s) per core' | cut -f 2 -d ':' | awk '{$1=$1}1' | tr '\n', ' '", shell=True, text=True)


def readable_format(fsize, units=[' bytes',' KB',' MB',' GB',' TB', ' PB', ' EB']):
	return "{:.2f}{}".format(float(fsize), units[0]) if fsize < 1024 else readable_format(fsize / 1024, units[1:])

system('clear')
print(colored(' -- PyMonitr -- ', 'blue', attrs=['bold']))
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

	total_ram = readable_format(ram[0])
	used_ram = ram[0] - ram[1]
	free_ram = readable_format(ram[1])

	percent_used_ram = ram.percent
	percent_free_ram = abs(percent_used_ram)

	total_swap = readable_format(swap[0])
	used_swap = readable_format(swap[1])
	free_swap = readable_format(swap[2])

	percent_used_swap = swap.percent
	percent_free_swap = abs(percent_used_swap)

	total_storage = readable_format(storage[0])
	used_storage = readable_format(storage[1])
	free_storage = readable_format(storage[2])

	percent_used_storage = storage.percent
	percent_free_storage = abs(percent_used_storage)

	print(colored('|===== [Storage] =====|', 'green', attrs=['bold']))
	print(colored(f'Total: {total_storage}', 'blue', attrs=['bold']))

	if int(percent_used_storage) in range(0, 50):
		print(colored(f'Used: {used_storage} | {percent_used_storage}%', 'green', attrs=['bold']))

	elif int(percent_used_storage) in range(51, 80):
		print(colored(f'Used: {used_storage} | {percent_used_storage}%', 'yellow', attrs=['bold']))

	elif int(percent_used_storage) in range(81, 90):
		print(colored(f'Used: {used_storage} | {percent_used_storage}%', 'red', attrs=['bold']))

	elif int(percent_used_storage) in range(91, 101):
		print(colored(f'Used: {used_storage} | {percent_used_storage}% | STORAGE USAGE IS TOO HIGH!!', 'magenta', attrs=['bold', 'blink']))

	if int(percent_free_storage) in range(0, 50):
		print(colored(f'Free: {free_storage} | {percent_free_storage - 100:.1f}%', 'green', attrs=['bold']))

	elif int(percent_free_storage) in range(51, 80):
		print(colored(f'Free: {free_storage} | {percent_free_storage - 100:.1f}%', 'yellow', attrs=['bold']))

	elif int(percent_free_storage) in range(81, 90):
		print(colored(f'Free: {free_storage} | {percent_free_storage - 100:.1f}%', 'red', attrs=['bold']))

	elif int(percent_free_storage) in range(91, 101):
		print(colored(f'Free: {free_storage} | {percent_free_storage - 100:.1f}% | LOW STORAGE SPACE AVAILABLE!!', 'magenta', attrs=['bold', 'blink']))

	print(colored('|======= [RAM] =======|', 'green', attrs=['bold']))
	print(colored(f'Total: {total_ram}', 'blue', attrs=['bold']))

	if int(percent_used_ram) in range(0, 50):
		print(colored(f'Used: {readable_format(used_ram)} | {percent_used_ram}%', 'green', attrs=['bold']))

	elif int(percent_used_ram) in range(51, 80):
		print(colored(f'Used: {readable_format(used_ram)} | {percent_used_ram}%', 'yellow', attrs=['bold']))

	elif int(percent_used_ram) in range(81, 90):
		print(colored(f'Used: {readable_format(used_ram)} | {percent_used_ram}%', 'red', attrs=['bold']))

	elif int(percent_used_ram) in range(91, 101):
		print(colored(f'Used: {readable_format(used_ram)} | {percent_used_ram}% | RAM USAGE IS TOO HIGH!!', 'magenta', attrs=['bold', 'blink']))

	if int(percent_free_ram) in range(0, 50):
		print(colored(f'Free: {free_ram} | {percent_free_ram - 100:.1f}%', 'green', attrs=['bold']))

	elif int(percent_free_ram) in range(51, 80):
		print(colored(f'Free: {free_ram} | {percent_free_ram - 100:.1f}%', 'yellow', attrs=['bold']))

	elif int(percent_free_ram) in range(81, 90):
		print(colored(f'Free: {free_ram} | {percent_free_ram - 100:.1f}%', 'red', attrs=['bold']))

	elif int(percent_free_ram) in range(91, 101):
		print(colored(f'Free: {free_ram} | {percent_free_ram - 100:.1f}% | LOW RAM MEMORY AVAILABLE', 'magenta', attrs=['bold', 'blink']))

	print(colored('|====== [Swap] =======|', 'green', attrs=['bold']))
	print(colored(f'Total: {total_swap}', 'blue', attrs=['bold']))

	if int(percent_used_swap) in range(0, 50):
		print(colored(f'Used: {used_swap} | {percent_used_swap}%', 'green', attrs=['bold']))

	elif int(percent_used_swap) in range(51, 80):
		print(colored(f'Used: {used_swap} | {percent_used_swap}%', 'yellow', attrs=['bold']))

	elif int(percent_used_swap) in range(81, 90):
		print(colored(f'Used: {used_swap} | {percent_used_swap}%', 'red', attrs=['bold']))

	elif int(percent_used_swap) in range(91, 101):
		print(colored(f'Used: {used_swap} | {percent_used_swap}% | SWAP USAGE IS TOO HIGH!!', 'magenta', attrs=['bold', 'blink']))

	if int(percent_free_swap) in range(0, 50):
		print(colored(f'Free: {free_swap} | {percent_free_swap - 100:.1f}%', 'green', attrs=['bold']))

	elif int(percent_free_swap) in range(51, 80):
		print(colored(f'Free: {free_swap} | {percent_free_swap - 100:.1f}%', 'yellow', attrs=['bold']))

	elif int(percent_free_swap) in range(81, 90):
		print(colored(f'Free: {free_swap} | {percent_free_swap - 100:.1f}%', 'red', attrs=['bold']))

	elif int(percent_free_swap) in range(91, 101):
		print(colored(f'Free: {free_swap} | {percent_free_swap - 100:.1f}% | LOW SWAP MEMORY AVAILABLE!!', 'magenta', attrs=['bold', 'blink']))

	print(colored('|======= [CPU] =======|', 'green', attrs=['bold']))

	cpu_perc = cpu_percent()

	if int(cpu_perc) in range(0, 50):
		print(colored(f'Usage: {cpu_perc}%', 'green', attrs=['bold']))

	elif int(cpu_perc) in range(51, 80):
		print(colored(f'Usage: {cpu_perc}%', 'yellow', attrs=['bold']))

	elif int(cpu_perc) in range(81, 90):
		print(colored(f'Usage: {cpu_perc}%', 'red', attrs=['bold']))

	elif int(cpu_perc) in range(91, 101):
		print(colored(f'Usage: {cpu_perc}% | RAM USAGE IS TOO HIGH!!', 'magenta', attrs=['bold', 'blink']))

	print(colored(f'Total cores: {cpu_count()}', attrs=['bold']))
	print(colored(f'Clusters: {CLUSTERS}', attrs=['bold']))
	print(colored(f'Cores per cluster: {CORES_PER_CLUSTER}', attrs=['bold']))
	print(colored(f'Threads per core: {THREADS_PER_CORE}', attrs=['bold']))

	corenum = 0

	for core in cpu:
		for ccore in range(1):
			corenum += 1
			
		print(colored(f'Core {corenum} frequency: {core[0]} GHz', attrs=['bold']))

	print(colored(f'Architecture type: {ARCH_TYPE}', attrs=['bold']))
	print(colored(f'CPU model/name: {CPU_MODEL}', attrs=['bold']))

	try:
		sleep(0.5)

	except KeyboardInterrupt:
		exit()

	system('clear')