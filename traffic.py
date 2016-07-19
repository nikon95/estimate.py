import re
import os

def fetchtraffic(name):
    
    link = "http://www.trafficestimate.com/" + name[:-1] #make link
    os.system("wget -O rec.html " + link)#call wget
    
    filed = open("rec.html","r")
    buf = filed.read()
    hits = re.findall("red.+/span", buf)
    if not hits:
        return "10,000"
    else:
        hits = re.findall(">[0-9|,]+<",hits[0])
        return hits[0][1:-1]


sitesfile = open("list.txt","rU")#input list
output = open("traffic.txt","w")#output list

buff = sitesfile.readlines()

for url in buff:
    output.write(fetchtraffic(url))
    output.write("\n")
    

sitesfile.close()
output.close()

