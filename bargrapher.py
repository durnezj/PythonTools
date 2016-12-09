import os
import sys

class Disk:
    def __init__(self, name, total, used, mountpoint,percent):
        self.name = name
        self.total = total
        self.used = used
        self.mountpoint = mountpoint
        self.percent = int(percent)

    def __str__(self):
        graph = self.name + " on " + self.mountpoint+ "\n"
        graph += "["
        bars = 100
        for i in range(self.percent):
            graph+="|"
            bars -= 1
        for i in range(bars):
            graph+=" "
        graph += "]"
        graph += "\t"+str(self.used)+" of "+str(self.total)+" used" + "\t"
        return graph + "\n"



tmp = os.popen("df").read()

lines = tmp.split("\n")
header = lines[0]
disks = []
i = 1
while i in range(lines.__len__()-1):
    line = lines[i].split()
    print(Disk(line[0],line[1],line[2],line[5],line[4].replace("%",'')))

    i += 1
