from psutil import virtual_memory, cpu_freq, disk_usage, cpu_percent, cpu_count, swap_memory
from argparse import ArgumentParser
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

flag = ArgumentParser()
flag.add_argument("-refresh", type=int, default=1, help='How many seconds should the program refresh the stats (Default is 1). Example: pymn.py -refresh 2. Float numbers are not allowed.')

retime = flag.parse_args()

def readable_format(fsize, units=[' bytes',' KB',' MB',' GB',' TB', ' PB', ' EB']):
	return "{:.2f}{}".format(float(fsize), units[0]) if fsize < 1024 else readable_format(fsize / 1024, units[1:])

system('clear')
print(colored(' -- PyMonitr -- ', 'blue', attrs=['bold']))
sleep(2)
system('clear')

print('.')
sleep(0.25)
system('clear')
print('..')
sleep(0.25)
system('clear')
print('...')
sleep(0.25)
system('clear')

while True:
	ram = virtual_memory()
	cpu = cpu_freq(percpu=True)
	storage = disk_usage('/')
	swap = swap_memory()

	total_ram = readable_format(ram[0])
	free_ram = readable_format(ram[1])
	used_ram = ram[0] - ram[1]

	percent_used_ram = ram.percent
	percent_free_ram_unformatted = percent_used_ram - 100
	percent_free_ram = abs(percent_free_ram_unformatted)

	total_swap = readable_format(swap[0])
	used_swap = readable_format(swap[1])
	free_swap = readable_format(swap[2])

	percent_used_swap = swap.percent
	percent_free_swap = abs(percent_used_swap - 100)

	total_storage = readable_format(storage[0])
	used_storage = readable_format(storage[1])
	free_storage = readable_format(storage[2])

	percent_used_storage = storage.percent
	percent_free_storage = percent_used_storage - 100

	print(colored('<===== [Storage] =====>', 'blue', attrs=['bold']))
	print(colored(f'Total: {total_storage}', 'green', attrs=['bold']))
	print(colored(f'Used: {used_storage} | {percent_used_storage}%', 'yellow', attrs=['bold']))
	print(colored(f'Free: {free_storage} | {abs(percent_free_storage)}%', 'red', attrs=['bold']))
	print(colored('<======= [RAM] =======>', 'blue', attrs=['bold']))
	print(colored(f'Total: {total_ram}', 'green', attrs=['bold']))
	print(colored(f'Used: {readable_format(used_ram)} | {percent_used_ram}%', 'yellow', attrs=['bold']))
	print(colored(f'Free: {free_ram} | {percent_free_ram:.1f}%', 'red', attrs=['bold']))
	print(colored('<====== [Swap] =======>', 'blue', attrs=['bold']))
	print(colored(f'Total: {total_swap}', 'green', attrs=['bold']))
	print(colored(f'Used: {used_swap} | {percent_used_swap}%', 'yellow', attrs=['bold']))
	print(colored(f'Free: {free_swap} | {percent_free_swap:.1f}%', 'red', attrs=['bold']))
	print(colored('<======= [CPU] =======>', 'blue', attrs=['bold']))
	print(colored(f'Usage: {cpu_percent()}%', 'green', attrs=['bold']))
	print(colored(f'Total cores: {cpu_count()}', 'yellow', attrs=['bold']))
	print(colored(f'Clusters: {CLUSTERS}', 'red', attrs=['bold']))
	print(colored(f'Cores per cluster: {CORES_PER_CLUSTER}', 'green', attrs=['bold']))
	print(colored(f'Threads per core: {THREADS_PER_CORE}', 'yellow', attrs=['bold']))

	corenum = 0

	for core in cpu:
		for ccore in range(1):
			corenum += 1
			
		print(colored(f'Core {corenum} frequency: {core[0]} GHz', 'red', attrs=['bold']))

	print(colored(f'Architecture type: {ARCH_TYPE}', 'magenta', attrs=['bold']))
	print(colored(f'CPU model/name: {CPU_MODEL}', 'blue', attrs=['bold']))

	try:
		sleep(retime.refresh)

	except KeyboardInterrupt:
		exit()

	system('clear')