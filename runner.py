"""
This script downloads the files open data files into the local repository.
Keep adding the energy data files into the files list

"""
# Import required packages
import subprocess
import os
import time

# List of URLs of the datasources
files = ["http://en.openei.org/datasets/files/961/pub/EPLUS_TMY2_RESIDENTIAL_BASE.zip"]

# Set the download command
command = "wget"

# List of parallel processes
processess = set()

# Maximum number of processes
max_processoes = 4

# Download the datasources
for file in files:
	processess.add(subprocess.Popen([command, file]))
	if len(processess) >=max_processoes:
		os.wait()
		processess.difference_update([p for p in processess if p.poll() is not None])
