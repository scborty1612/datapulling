"""
This script (as of now) just read one of the CSV data files
and place the data into a pandas dataframe. Later, additional stuffs
will be added there.

"""
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

import numpy as np
import os

def processDataFile(dataFile = None):
	"""
	Process the energy datafile
	"""
	df = pd.read_csv(dataFile, parse_dates = ['Date/Time'], index_col='Date/Time')
	dataLen = 500

	# Check the columns name
	print df.columns.values


	_, ax = plt.subplots(figsize=[10, 5])
	# df['Electricity:Facility [kWh](Hourly)'][:dataLen].plot()
	# df['General:ExteriorLights:Electricity [kWh](Hourly)'][:dataLen].plot()
	sns.regplot(df['Electricity:Facility [kWh](Hourly)'], df['General:ExteriorLights:Electricity [kWh](Hourly)'],)
	plt.show()


def directoryWalker(dirName = None):
	"""Walk through the directory 
	to scan the data (CSV) files
	"""
	dataFiles = []

	try:
		for fileName in os.listdir(dirName):

			# Check whether its a csv file
			if not fileName.endswith(".csv"):
				continue

			file_info = fileName.split("_")
			state = file_info[1]
			res_info = file_info[2].split(".")
			location = "-".join([str(v) for v in res_info[:-2]])

			dataFiles.append({'state': state, 'location': location, 'data': dirName+fileName})

		df = pd.DataFrame(data = dataFiles)
	except Exception as e:
		print "Directory is not valid"
		print e
		return None
	
	return df


def main():

	dataFiles = ["USA_CA_Bakersfield.723840_TMY2.csv"]

	for dataFile in dataFiles:
		processDataFile(dataFile = "data/"+dataFile)

	# dirName = "EPLUS_TMY2_RESIDENTIAL_BASE"

	# df = directoryWalker(dirName=dirName)

	# if df is not None:
	# 	print df[df['state']=='CA'][:2]
	# else:
	# 	print "None"

if __name__ == "__main__":
	main()
