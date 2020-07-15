##"In this file, we will be downloading and installing the Hadoop software"

#!/bin/sh

echo "Starting up the HDFS"

echo 

echo

echo "Checking for updates"

echo

echo

sudo apt-get update

echo "Run the .bash_profile"

source .bash_profile

echo

echo

echo "Call the HDFS"

echo 

echo

hdfs namenode -format 

echo 

echo

echo "Start the HDFS-sh(s)"

start-dfs.sh

start-yarn.sh

echo

echo

echo "Check JPS Status"

jps
