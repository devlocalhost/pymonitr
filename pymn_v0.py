from psutil import virtual_memory, cpu_freq, disk_usage, cpu_percent, cpu_count, swap_memory
from time import sleep
from sys import exit
from os import system

def readable_format(fsize, units=[' bytes',' KB',' MB',' GB',' TB', ' PB', ' EB']):
	return "{:.2f}{}".format(float(fsize), units[0]) if fsize < 1024 else readable_format(fsize / 1024, units[1:])

system('clear')
print(' -- PyMonitr -- ')
sleep(1)
system('clear')

print('.')
sleep(0.5)
system('clear')
print('..')
sleep(0.5)
system('clear')
print('...')
sleep(0.5)
system('clear')

while True:
	ram = virtual_memory()
	cpu = cpu_freq(percpu=True)
	storage = disk_usage('/')
	swap = swap_memory()

	total_ram = readable_format(ram[0])
	used_ram = readable_format(ram[3])
	free_ram = readable_format(ram[1])
	percent_used_ram = ram.percent
	percent_free_ram_unformatted = percent_used_ram - 100
	percent_free_ram = abs(percent_free_ram_unformatted)

	total_swap = readable_format(swap[0])
	used_swap = readable_format(swap[1])
	free_swap = readable_format(swap[2])
	percent_used_swap = swap.percent
	percent_free_swap = percent_used_swap - 100

	total_storage = readable_format(storage[0])
	used_storage = readable_format(storage[1])
	free_storage = readable_format(storage[2])
	percent_used_storage = storage.percent
	percent_free_storage = percent_used_storage - 100

	print('========= Storage =========')
	print(f'Total: {total_storage}')
	print(f'Used: {used_storage} | {percent_used_storage}%')
	print(f'Free: {free_storage} | {abs(percent_free_storage)}%')
	print('=========== RAM ===========')
	print(f'Total: {total_ram}')
	print(f'Used: {used_ram} | {percent_used_ram}%')
	print(f'Free: {free_ram} | {percent_free_ram:.1f}%')
	print('========== Swap ===========')
	print(f'Total: {total_swap}')
	print(f'Used: {used_swap} | {percent_used_swap}%')
	print(f'Free: {free_swap} | {abs(percent_free_swap)}%')
	print('=========== CPU ===========')
	print(f'Total cores: {cpu_count()}')
	print(f'Usage: {cpu_percent()}%')
	
	corenum = 0

	for core in cpu:
		for ccore in range(1):
			corenum += 1
			
		print(f'Core {corenum} frequency: {core[0]}')
	print('===========================')

	try:
		sleep(1)

	except KeyboardInterrupt:
		exit()

	system('clear')