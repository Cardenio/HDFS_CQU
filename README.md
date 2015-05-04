# HDFS_CQU
...
Maven编译
cd /hadoop-2.6.0-src/hadoop-hdfs-project/hadoop-hdfs \n
mvn package -Pdist -DskipTests -Dtar \n

将Target目录下生成的 \n
hadoop-hdfs-2.6.0.jar \n 
hadoop-hdfs-2.6.0-tests.jar \n
复制到已经配置好的hadoop-2.6.0/share/hadoop/hdfs/ \n
hadoop namenode -format \n
./start-all.sh \n


