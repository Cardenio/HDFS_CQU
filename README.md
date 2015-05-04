# HDFS_CQU
...</br>

#Maven编译
cd /hadoop-2.6.0-src/hadoop-hdfs-project/hadoop-hdfs</br>
mvn package -Pdist -DskipTests -Dtar</br>

将Target目录下生成的</br>
hadoop-hdfs-2.6.0.jar</br>
hadoop-hdfs-2.6.0-tests.jar</br>
复制到已经配置好的hadoop-2.6.0/share/hadoop/hdfs/</br>

hadoop namenode -format</br>
./start-all.sh</br>


