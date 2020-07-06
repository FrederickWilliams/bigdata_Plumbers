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

touch .bash_profile.sh

echo "JAVA_HOME=/opt/jdk1.8.0_221" >> .bash_profile.sh
echo "export PATH=$PATH:$JAVA_HOME/bin" >> .bash_profile.sh

sudo wget https://www.python.org/ftp/python/3.7.7/Python-3.7.7.tgz

tar -zxvf Python-3.7.7.tgz

rm Python-3.7.7.tgz

echo "PYTHON_HOME=/opt/Python-3.7.7" >> .bash_profile.sh
echo "export PATH=$PATH:$PYTHON_HOME/bin" >> .bash_profile.sh

sudo wget https://downloads.lightbend.com/scala/2.11.8/scala-2.11.8.tgz

tar -zxvf scala-2.11.8.tgz

rm scala-2.11.8.tgz

echo "SCALA_HOME=/opt/scala-2.11.8" >> .bash_profile.sh
echo "export PATH=$PATH:$SCALA_HOME/bin" >> .bash_profile.sh

sudo wget https://piccolo.link/sbt-1.3.13.tgz

tar -zxvf sbt-1.3.13.tgz

rm sbt-1.3.13.tgz

echo "SBT_HOME=/opt/sbt-1.3.13" >> .bash_profile.sh
echo "export PATH=$PATH:$SBT_HOME/bin" >> .bash_profile.sh
















