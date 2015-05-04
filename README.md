# HDFS_CQU
...
Maven编译
cd /hadoop-2.6.0-src/hadoop-hdfs-project/hadoop-hdfs
mvn package -Pdist -DskipTests -Dtar

将Target目录下生成的
hadoop-hdfs-2.6.0.jar
hadoop-hdfs-2.6.0-tests.jar
复制到已经配置好的hadoop-2.6.0/share/hadoop/hdfs/
hadoop namenode -format
./start-all.sh


