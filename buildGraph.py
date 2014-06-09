#! /usr/bin/python

import plotly.plotly as py
from plotly.graph_objs import *

#username = "rpural"
#api_key = "7abemi2v86"

#py = plotly.plotly(username=username, key=api_key)

def extract(filename, timestamp, temp):
  data = open( filename, 'r' )

  for line in data:
    ts, t = line.split( ',' )
    ts = ts.strip( '"' )
    t = float( t )
    timestamp.append( ts )
    temp.append( t )

  data.close()

udtimestamp = []
udtemp = []

extract( '/home/ubuntu/cpuTemp/cpuTemp.log', udtimestamp, udtemp )

r2timestamp = []
r2temp = []

extract( '/home/ubuntu/cpuTemp/cpuTemp.rpural', r2timestamp, r2temp )

r3timestamp = []
r3temp = []

extract( '/home/ubuntu/cpuTemp/cpuTemp.rpural2', r3timestamp, r3temp )

r4timestamp = []
r4temp = []

extract( '/home/ubuntu/cpuTemp/rmTemp.log', r4timestamp, r4temp )

layout = { 'title': 'CPU Temperture (Farenheit)',
	   'xaxis': { 'title': "Date / Time" },
	   'yaxis': { 'title': "Temp (F)" },
	   'legend': { 'x': 0, 'y': 0 } }

trace1 = { 'x': udtimestamp,
	   'y': udtemp,
	   'name': 'uDoo',
	   'type': 'scatter',
	   'mode': 'lines' }

trace2 = { 'x': r2timestamp,
	   'y': r2temp,
	   'name': 'RasPi 1',
	   'type': 'scatter',
	   'mode': 'lines' }

trace3 = { 'x': r3timestamp,
	   'y': r3temp,
	   'name': 'RasPi 2',
	   'type': 'scatter',
	   'mode': 'lines' }

trace4 = { 'x': r4timestamp,
	   'y': r4temp,
	   'name': 'Rm Temp',
	   'type': 'scatter',
	   'mode': 'lines' }

response = py.plot([trace1, trace2, trace3, trace4], layout=layout, filename='uDooTemp', fileopt='overwrite')
# filename = response['filename']
#url = response['url']
#print filename, " - ", url
print response
