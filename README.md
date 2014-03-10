udootemp
========

Perl and Python code to collect CPU and room temp, and plot the values over time via Plot.ly

Files comprising this package:

logTemp.pl - A perl script to capture the CPU temperture of the uDoo or Raspberry Pi board.
	This script is called via cron once each 15 minutes on the monitored machines.

logRmTemp.py - A python script to capture the room temperture via a one-wire device.
	This script is called via cron once each 15 minutes on the Raspberry Pi with the
	sensor for the room temperature.

buildGraph.py - Reads timestamped CPU temp logs from three different processors, and a
	room temperture log, and graphs the values against time using plot.ly

createGraph.sh - Simple bash script to scp the three external files used to the uDoo 
	machine, and create the graph using buildGraph.py. This script is called
	on demand to create a new version of the graph on plot.ly

A sample of the plot can be found at https://plot.ly/~rpural/11/

