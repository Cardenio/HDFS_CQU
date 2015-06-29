# HDFS_CQU
...</br>

#import the source code of hadoop to eclipse
1.install maven</br>
use "mvn -v" to check</br>
2.install protobuf</br>
use "protoc --version" to check</br>
3.something need to be done</br>
add TestAvroSerialization.java to hadoop-common/src/test/java/org/apache/hadoop/io/serializer/avro/</br>
add TestProtos.java, TestRpcServiceProtos.java to hadoop-common/src/test/java/org/apache/hadoop/ipc/protobuf/</br>
cd hadoop-2.6.0-src/hadoop-maven-plugins/ </br>
mvn install</br>
cd hadoop-2.6.0-src/</br>
mvn eclipse:eclipse -DskipTests</br>
4.import</br>
in "hadoop-streaming" project build path </br>
rebuild the source link "hadoop-2.6.0-src/hadoop-yarn-project/hadoop-yarn/hadoop-yarn-server/hadoop-yarn-server-resourcemanager/conf", remove the original one.</br>

#import the source code of tachyon to eclipse
1.cd tachyon-0.6.4</br>
2.mvn eclipse:eclipse -DskipTests</br>
3.import and fix problems.</br>

#use maven to compile 
java 1.7</br>
mvn package -Pdist -DskipTests -Dtar</br>
java 1.8</br>
mvn package -Pdist -DskipTests -Dtar -Dadditionalparam=-Xdoclint:none </br>
copy the *.jar from target/ in source code to share/ which used by hadoop.</br>

#what we have done now
1.put the data submitted by the client to HDFS in a certain datanode.</br>
related class and method:</br>
NameNodeRpcServer:addBlock()------return type:LocatedBlock</br>
FSNamesystem:getAdditionalBlock()------return type:LocatedBlock</br>
BlockManager:chooseTarget4NewBlock()------return type:DatanodeStorageInfo[]</br>
BlockPlacementPolicyDefault:chooseTarget()------return type:DatanodeStorageInfo[]</br>
Host2NodeMap:getDatanodeByHost()------return type:DatanodeDescriptor</br>
Host2NodeMap:getDatanodeByXferAddr()------return type:DatanodeDescriptor</br>
DatanodeDescriptor:getStorageInfos()------return type:DatanodeStorageInfo[]</br>
2.use SSD, MEMORY as a datanode.</br>
3.do some tachyon experiments.
4.put the data submitted by the client to HDFS in some datanodes according to the proportion.</br>
1>make a proportion</br>
  static int count[] = { 8, 1, 1 };</br>
2>modify the chooseTarget method</br>
	public DatanodeStorageInfo[] inmemTarget(String srcPath, int numOfReplicas,</br>
			Node writer, List<DatanodeStorageInfo> chosenNodes,</br>
			boolean returnChosenNodes, Set<Node> excludedNodes, long blocksize,</br>
			final BlockStoragePolicy storagePolicy) {</br>

		if (count[0] != 0) {</br>
			DatanodeDescriptor Test1 = this.host2datanodeMap</br>
					.getDatanodeByHost("222.198.132.207");</br>
			DatanodeStorageInfo[] testTarget1 = Test1.getStorageInfos();</br>
			DatanodeStorageInfo[] testTarget = new DatanodeStorageInfo[1];</br> 
			testTarget[0] = testTarget1[0];</br>
			count[0]--;</br>
			return testTarget;</br>
		} else if (count[1] != 0) {</br>
			DatanodeDescriptor Test1 = this.host2datanodeMap</br>
					.getDatanodeByHost("222.198.132.210");</br>
  		DatanodeStorageInfo[] testTarget1 = Test1.getStorageInfos();</br>
			DatanodeStorageInfo[] testTarget = new DatanodeStorageInfo[1];</br> 
			testTarget[0] = testTarget1[0];</br>
			count[1]--;</br>
			return testTarget;</br>
		} else if (count[2] != 0) {</br>
			DatanodeDescriptor Test1 = this.host2datanodeMap</br>
					.getDatanodeByHost("222.198.132.208");</br>
			DatanodeStorageInfo[] testTarget1 = Test1.getStorageInfos();</br>
			DatanodeStorageInfo[] testTarget = new DatanodeStorageInfo[1]; </br>
			testTarget[0] = testTarget1[0];</br>
			count[2]--;</br>
			return testTarget;</br>
		}</br>
  	else {</br>
			count[0] = 8;</br>
			count[1] = 1;</br>
			count[2] = 1;</br>
			// get datanode by ip address</br>
			DatanodeDescriptor Test1 = this.host2datanodeMap</br>
					.getDatanodeByHost("222.198.132.207");</br>
			// get datanode by (ip, port)</br>
			// this.host2datanodeMap.getDatanodeByXferAddr("172.31.8.147",59010);</br>
			DatanodeStorageInfo[] testTarget1 = Test1.getStorageInfos();</br>
	  	DatanodeStorageInfo[] testTarget = new DatanodeStorageInfo[1]; </br>
			testTarget[0] = testTarget1[0];</br>
			count[0]--;</br>
			return testTarget;</br>
		}</br>
	}</br>

5.modify relax_locality to false in yarn_protos.proto to implement data locality.</br>
6.to set rack parameters "net.topology.script.file.name" in core.site.xml by using "RackAware.py"</br>

#some commands in hadoop
hadoop namenode -format</br>
hadoop fs -put file(s) file(d)</br>
hadoop fs -rm [-r] file</br>
hadoop fs -rm hdfs://node1(which namenode is located on):9000/*</br>
hadoop dfsadmin -safemode leave</br>
hadoop dfsadmin -report</br>

#compile a mapreduce program
bin/hadoop com.sun.tools.javac.Main *.java</br>
jar cf classname.jar *.class</br>


#what we are going to do
1.to find a relationship between containers and map tasks.</br>
2.do some benchmarks to show the different performance about memory and disk.</br>  


</br>
</br>





