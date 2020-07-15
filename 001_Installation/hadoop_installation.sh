##"In this file, we will be downloading and installing the Hadoop software"

#!/bin/sh


sudo apt-get update

mkdir hadoop3

cd hadoop3

sudo apt install ssh

sudo apt install pdsh

echo "export PDSH_RCMD_TYPE=ssh" >> /home/frederick/.bash_profile

sudo apt-get install openssh-server openssh-client

ssh-keygen -t rsa -P ""

cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

chmod 0600 ~/.ssh/authorized_keys

sudo apt-get install rsync

ssh localhost

ssh-add 

sudo apt-get update

touch /home/frederick/.bash_profile

echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> /home/frederick/.bash_profile
echo "export PATH=$PATH:$JAVA_HOME/bin" >> /home/frederick/.bash_profile

sudo wget https://archive.apache.org/dist/hadoop/common/hadoop-3.1.3/hadoop-3.1.3.tar.gz

tar -zxvf hadoop-3.1.3.tar.gz

rm hadoop-3.1.3.tar.gz

cd /home/frederick/hadoop3/hadoop-3.1.3

mkdir hdfs

cd /home/frederick/hadoop3/hadoop-3.1.3/hdfs

mkdir datanode 

mkdir namenode

cd /home/frederick/hadoop3/hadoop-3.1.3/etc/hadoop

echo "export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64" >> hadoop-env.sh

echo "<configuration>
<property>
  <name>fs.default.name</name>
    <value>hdfs://localhost:9000</value>
</property>
</configuration>" >> core-site.xml


echo "<configuration>
<property>
 <name>dfs.replication</name>
 <value>1</value>
</property>

<property>
  <name>dfs.name.dir</name>
    <value>file:///home/frederick/hadoop3/hadoop-3.1.3/hdfs/namenode</value>
</property>

<property>
  <name>dfs.data.dir</name>
    <value>file:///home/frederick/hadoop3/hadoop-3.1.3/hdfs/datanode</value>
</property>
</configuration>" >> hdfs-site.xml


echo "<configuration>
 <property>
  <name>mapreduce.framework.name</name>
   <value>yarn</value>
 </property>
</configuration>" >> mapred-site.xml


echo "<configuration>
 <property>
  <name>yarn.nodemanager.aux-services</name>
    <value>mapreduce_shuffle</value>
 </property>
</configuration>" >> yarn-site.xml

cd 

echo "export HADOOP_HOME=/home/frederick/hadoop3/hadoop-3.1.3" >> .bash_profile
echo "export HADOOP_INSTALL=$HADOOP_HOME" >> .bash_profile
echo "export HADOOP_MAPRED_HOME=$HADOOP_HOME" >> .bash_profile
echo "export HADOOP_COMMON_HOME=$HADOOP_HOME" >> .bash_profile
echo "export HADOOP_HDFS_HOME=$HADOOP_HOME" >> .bash_profile
echo "export YARN_HOME=$HADOOP_HOME" >> .bash_profile
echo "export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native" >> .bash_profile
echo "export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin" >> .bash_profile

#Due to limited premissions, this is used to increase it

sudo chmod 777 -R /home/frederick/hadoop3/hadoop-3.1.3/

echo "source .bash_profile" >> .bashrc
