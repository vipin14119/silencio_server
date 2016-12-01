from os import getcwd
from silencio.models import Location

f = open(getcwd()+"/silencio/data.txt")
datas = f.read().split("\n")
for data in datas:
    if len(data) > 20:
        a = data.split(" == ")
        # print a[0]
        # print a[1]
        print('locationsMap.put("'+a[1]+'", "'+a[0]+'");')
        # Location(name=a[0], mac=a[1]).save()

print "SCRIPT DONE"
