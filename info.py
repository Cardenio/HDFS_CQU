import os
import sys

def TimeTrans(time):
        for i in (':', ','):
                time = time.replace(i,' ')
        timeList = time.split(" ")
        if len(timeList)<4:
                return -999
        H = int(timeList[0])
        M = int(timeList[1])
        S = int(timeList[2])
        MS = int(timeList[3])

        StandardTime = MS+S*1000+M*1000*60+H*1000*60*60

        return StandardTime

def sortedDictValues1(adict):
        items = adict.items()
        items.sort()
        return items


fh = open('syslog')


AttemptMapping= {}
ContainerAttemp = {}
ContainerHost = {}

HostList = []

Content = fh.readlines()
TaskHost = {}
for line in Content:
        if " on NM" in line:
                line = line.strip()
                lineSplits = line.split("TaskAttempt")
                attempt = lineSplits[2].split("[")[1].split("]")[0]
                container = lineSplits[2].split("[")[2].split(" ")[0]
                host = lineSplits[2].split("[")[3].split(":")[0]
                if host not in HostList:
                        HostList.append(host)
                #print attempt,container,host
                if container not in ContainerAttemp:
                        ContainerAttemp[container]=attempt
                if container not in ContainerHost:
                                                                                                                                                                                    1,1          顶端
                        ContainerHost[container]=host
                attemptType = attempt.split("_")[3]
                attemptTask = attempt.split("_")[4]
                attemptNumber  = attempt.split("_")[5]
                attempKey = attemptType+attemptTask
                if attempKey not in AttemptMapping:
                        AttemptMapping[attempKey] = []
                AttemptMapping[attempKey].append([int(attemptNumber),container])

ExcludeSet = []
for k,v in AttemptMapping.items():
        if len(v)>1:
                curMaxTrial = -1;
                for elem in v:
                        if elem[0]> curMaxTrial:
                                curMaxTrial = elem[0]
                for elem in v:
                        if elem[0]!=curMaxTrial:
                                ExcludeSet.append(elem[1])

#for elem in ExcludeSet:
#       del ContainerAttemp[elem]


AttemptDataPosition = {}

for line in Content:
        if "+maptask+++++++++" not in line:
                continue
        line = line.strip()
        lineList = line.split("+1")
        ClusterInfo = lineList[1].split("[")[1].split("]")[0]
        AttempInfo = lineList[1].split("---")[1]
        if AttempInfo not in AttemptDataPosition.keys():
                AttemptDataPosition[AttempInfo]=ClusterInfo





sortedDic = sortedDictValues1(ContainerAttemp)
for elem in sortedDic:
        k = elem[0]
        v = elem[1]
        if v.split("_")[3]=="m":
                print "Map task",v.split("_")[3]+v.split("_")[4],"run in",k.split("_")[0]+k.split("_")[4],"at",ContainerHost[k],"! Initial data at:",AttemptDataPosition[v]
                #print "Data in",AttemptDataPosition[v],"mapped to","task",v.split("_")[3]+v.split("_")[4],"allocated in",k.split("_")[0]+k.split("_")[4],"running at",ContainerHost[k],"starting from",StandardStartTime,"to",StandardEndTime
        else:

                print "Red task",v.split("_")[3]+v.split("_")[4],"run in",k.split("_")[0]+k.split("_")[4],"at",ContainerHost[k],"!"

print "-----------------------------------"



cmdAppStart = "head syslog | head -1 | cut -d \" \" -f 2"
AppStartTime = os.popen(cmdAppStart).read()
StandardAppStartTime = TimeTrans(AppStartTime)

sortedDic = sortedDictValues1(ContainerAttemp)

first = True

TotalSize = {}
TotalContinarTime = {}
for k,v in ContainerAttemp.items():
        TotalSize[k]=0
        TotalContinarTime[k]=0

for elem in sortedDic:
        #k: continar v: task
        k = elem[0]
        v = elem[1]
        cmdStart = "cat ../"+k+"/syslog | head -1 | cut -d \" \" -f 2"
        cmdEnd = "cat ../"+k+"/syslog | tail -1 | cut -d \" \" -f 2"

        containerFH = open("../"+k+"/syslog")
        content = containerFH.readlines()
        splitSize = 0
        for line in content:
                line = line.strip()
                if "Processing split" not in line:
                        continue
                splitSize = int(line.split("+")[1])

        StartTime = os.popen(cmdStart).read()
        EndTime = os.popen(cmdEnd).read()
                                           if first:
                if TimeTrans(StartTime)<StandardAppStartTime:
                        StandardAppStartTime = TimeTrans(StartTime)-1000
                first=False


        StandardStartTime = TimeTrans(StartTime)-StandardAppStartTime
        StandardEndTime = TimeTrans(EndTime)-StandardAppStartTime

        #print k,v,ContainerHost[k],StandardStartTime,StandardEndTime
        if v.split("_")[3]=="m":
                print "From",StandardStartTime,"to",StandardEndTime,"- Elapse Time:",int(StandardEndTime-StandardStartTime)/1000,". Map task",v.split("_")[3]+v.split("_")[4],"run in",k.split("_")[0]+k.split("_")[4],"at",ContainerHost[k],"! Initial data at:",AttemptDataPosition[v],v," size:",splitSize/1024/1024,"M"
                TotalSize[k] = TotalSize[k]+splitSize/1024/1024
                TotalContinarTime[k] = TotalContinarTime[k] + (StandardEndTime-StandardStartTime)
                #print "Data in",AttemptDataPosition[v],"mapped to","task",v.split("_")[3]+v.split("_")[4],"allocated in",k.split("_")[0]+k.split("_")[4],"running at",ContainerHost[k],"starting from",StandardStartTime,"to",StandardEndTime
        else:
                print "From",StandardStartTime,"to",StandardEndTime,"- Elapse Time:",int(StandardEndTime-StandardStartTime)/1000,". Red task",v.split("_")[3]+v.split("_")[4],"run in",k.split("_")[0]+k.split("_")[4],"at",ContainerHost[k],"!",v



HostTotalSize = {}
HostTotalTime = {}
for k,v in ContainerAttemp.items():
        if k in ContainerHost.keys() and "_r_" not in v:
                host = ContainerHost[k]
                if host not in HostTotalSize.keys():
                        HostTotalSize[host] = 0
                        HostTotalTime[host] = 0
                continarHost = host
                dataHost = AttemptDataPosition[v]
                if continarHost == dataHost:
                        HostTotalSize[host] = HostTotalSize[host] + TotalSize[k]
                        HostTotalTime[host] = HostTotalTime[host] + TotalContinarTime[k]
                print k,continarHost,v,dataHost


print "[",
for elem in HostList:
        #print "Host on", elem, "process",HostTotalSize[elem],"used", HostTotalTime[elem]
        print "(",elem,int(1000000*float(int(HostTotalSize[elem]))/int(HostTotalTime[elem])),")",
print "]"
                                                                                                                                                                                    178,1        底端
                                                                                                                                                         136,1-8       67%

                                                                                                                                                                                    46,1-8        34%
