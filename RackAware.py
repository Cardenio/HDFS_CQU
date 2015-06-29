#!/usr/bin/python
#-*-coding:utf-8 -*-
import sys
rack = {
"node1":"rack1",
"node2":"rack2",
"node3":"rack3",
"node4":"rack4",
"222.198.132.209":"rack1",
"222.198.132.208":"rack2",
"222.198.132.207":"rack3",
"222.198.132.210":"rack4"
}

if __name__=="__main__":
  print "/"+rack.get(sys.argv[1],"rack0")
