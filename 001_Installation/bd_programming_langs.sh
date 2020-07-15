"""
In this file, we will be downloading and installing Java, Python, and Scala to be use in the Hadoop ecosystem. Also, SBT will be install to act as a compilier for Scala.
"""
#!/bin/sh

mkdir opt 

cd opt

sudo wget -O jdk-8u221-linux-x64.tar.gz \
-c --content-disposition \
"https://javadl.oracle.com/webapps/download/AutoDL?BundleId=239835_230deb18db3e4014bb8e3e8324f81b43"

tar -zxvf jdk-8u221-linux-x64.tar.gz

rm jdk-8u221-linux-x64.tar.gz

touch /home/frederick/.bash_profile2

echo "JAVA_HOME=/home/frederick/hadoop3/jdk1.8.0_221" >> /home/frederick/.bash_profile2
echo "export PATH=$PATH:$JAVA_HOME/bin" >> /home/frederick/.bash_profile2

sudo wget https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tgz

tar -zxvf Python-3.7.7.tgz

rm Python-3.7.7.tgz

echo "PYTHON_HOME=/home/frederick/hadoop3/Python-3.7.7" >> /home/frederick/.bash_profile2
echo "export PATH=$PATH:$PYTHON_HOME/bin" >> /home/frederick/.bash_profile2

sudo wget https://downloads.lightbend.com/scala/2.11.8/scala-2.11.8.tgz

tar -zxvf scala-2.11.8.tgz

rm scala-2.11.8.tgz

echo "SCALA_HOME=/home/frederick/hadoop3/scala-2.11.8" >> /home/frederick/.bash_profile2
echo "export PATH=$PATH:$SCALA_HOME/bin" >> /home/frederick/.bash_profile2

sudo wget https://piccolo.link/sbt-1.3.13.tgz

tar -zxvf sbt-1.3.13.tgz

rm sbt-1.3.13.tgz

echo "SBT_HOME=/home/frederick/hadoop3/sbt-1.3.13" >> /home/frederick/.bash_profile2
echo "export PATH=$PATH:$SBT_HOME/bin" >> /home/frederick/.bash_profile2

cd 

echo "source .bash_profile2" >> .bashrc

