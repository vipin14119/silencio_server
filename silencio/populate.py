from os import getcwd
from silencio.models import Location

f = open(getcwd()+"/silencio/data.txt")
datas = f.read().split("\n")
for data in datas:
    if len(data) > 20:
        print data.split(" == ")
        Location(name=data[0], mac=data[1]).save()


print "SCRIPT DONE"
