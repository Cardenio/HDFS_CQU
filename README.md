# HDFS_CQU
...</br>

#import the source code of hadoop to eclipse
1.install maven</br>
use "mvn -v" to check</br>
2.install protobuf</br>
use "protoc --version" to check</br>
3.something need to be done</br>
add TestAvroSerialization.java to hadoop-common/src/test/java/org/apache/hadoop/io/serializer/avro/</br>
add TestProtos.java, TestRpcServiceProtos.java to hadoop-common/src/main/java/org/apache/hadoop/ipc/protobuf/</br>
cd hadoop-2.6.0-src/hadoop-maven-plugins/ </br>
mvn install</br>
cd hadoop-2.6.0-src/</br>
mvn eclipse:eclipse -DskipTests</br>
4.import</br>
in "hadoop-streaming" project build path </br>
rebuild the source link "hadoop-2.6.0-src/hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-resourcemanager/conf", remove the original one.</br>


#use maven to compile 
java 1.7</br>
mvn package -Pdist -DskipTests -Dtar</br>
java 1.8</br>
mvn package -Pdist -DskipTests -Dtar </br>
copy the *.jar from target/ in source code to share/ which used by hadoop.</br>

#what we have done now
1.put the data submitted by the client to HDFS in a certain positions.</br>
related class and method:</br>
NameNodeRpcServer:addBlock()------return type:LocatedBlock</br>
FSNamesystem:getAdditionalBlock()------return type:LocatedBlock</br>
BlockManager:chooseTarget4NewBlock()------return type:DatanodeStorageInfo[]</br>
BlockPlacementPolicyDefault:chooseTarget()------return type:DatanodeStorageInfo[]</br>
Host2NodeMap:getDatanodeByHost()------return type:DatanodeDescriptor</br>
Host2NodeMap:getDatanodeByXferAddr()------return type:DatanodeDescriptor</br>
DatanodeDescriptor:getStorageInfos()------return type:DatanodeStorageInfo[]</br>
2.use SSD as a datanode</br>
3.compute the time of map</br>
4.compute the time of getting split into buffer </br>



</br>
</br>





