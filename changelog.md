# Changelog

#### Version: 1
1. Added colors,
2. Added: **Cores per cluster, Threads per core, Architecture type**

#### Version: 2
1. **Colors now match the usage. For example, if CPU usage is between 0 between 50 the color will be green, 51 - 80 yellow, and 81+ red and the text will flash too,**
2. **Changed start animation logo speed from 2 to 1**

#### Version: 3
1. **Changed colors of: 
	+ Total cores,
	+ Clusters,
	+ Cores per cluster,
	+ Threads per core,
	+ Core * frequency,
	+ Architecture type and CPU model/name to white**

#### Version: 4
1. **Fixed the annoying "minus (-)" thing, where it would usually show up on the "Free" fields (such as free storage etc),**
2. **Changed colors of:
	+ Total cores,
	+ Clusters,
	+ Cores per cluster,
	+ Threads per core,
	+ Core * frequency,
	+ Architecture type and CPU model/name to some random ones**

#### Version: 5
1. **Removed cluster field**

#### Version: 6
1. **Changed & added new colors,**
2. **Removed core frequency field,**
3. **Before the status colors were: 
	+ 0-50 green,
	+ 50-80 yellow,
	+ 80+ red,
	now its:
	+ 0-50 green,
	+ 50-80 yellow,
	+ 80-90 orange & 90+ red,**
4. **Removed dot animation**

#### Version: 7
1. **Added the version while starting the program,**
2. **Added CPU temperature, which MIGHT NOT be accurate, because im using a laptop that has 1 core (yes, 1 core, im not joking...). The program also reads the "/sys/class/thermal/thermal_zone0/temp" file to get the temperature. If you have any better idea to do this, you can open a issue or something *idk lol***

#### Version: 8
1. **1) Added CPU vendor & new color,**
2. **Added arguments/flags to control refresh time for the stats,**
3. **Added a exception in case CPU temperature cannot be read,**
4. **The program now will ask you to install the required packages incase you havent installed them, which are: [psutil](https://pypi.org/project/psutil/) and [colorhex](https://pypi.org/project/colorhex/)**