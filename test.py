import os, time
from urllib.request import urlopen
while True:
    print("Choose Test File Size : \n1 : 100MB\n2 : 1000MB")
    inputvalue = input("#")
    if inputvalue == "1":
        value = "100"
        break
    elif inputvalue == "2":
        value = "1000"
        break
    else:
        print("Input error. Please try again.")
list1 = ["hnd-jp-ping.vultr.com","sgp-ping.vultr.com","syd-au-ping.vultr.com","fra-de-ping.vultr.com","ams-nl-ping.vultr.com","lon-gb-ping.vultr.com","par-fr-ping.vultr.com","wa-us-ping.vultr.com","sjo-ca-us-ping.vultr.com","lax-ca-us-ping.vultr.com","il-us-ping.vultr.com","tx-us-ping.vultr.com","nj-us-ping.vultr.com","ga-us-ping.vultr.com","fl-us-ping.vultr.com"]
list2 = []
dict1 = {"timeToServer":{}}
dict2 = {"serverToArea":{'hnd-jp-ping.vultr.com': 'Tokyo', 'sgp-ping.vultr.com': 'Singapore', 'syd-au-ping.vultr.com': 'Sydney', 'fra-de-ping.vultr.com': 'Frankfurt', 'ams-nl-ping.vultr.com': 'Amsterdam', 'lon-gb-ping.vultr.com': 'London', 'par-fr-ping.vultr.com': 'Paris', 'wa-us-ping.vultr.com': 'Seattle', 'sjo-ca-us-ping.vultr.com': 'Silicon', 'lax-ca-us-ping.vultr.com': 'Los Angeles', 'il-us-ping.vultr.com': 'Chicago', 'tx-us-ping.vultr.com': 'Dallas', 'nj-us-ping.vultr.com': 'New York', 'ga-us-ping.vultr.com': 'Atlanta', 'fl-us-ping.vultr.com': 'Miami'}}

for i in list1:
    print("Testing Area : " + dict2["serverToArea"][str(i)])
    print("Testing Server : " + i)
    start = time.time()
    data = urlopen("http://" + i + "/vultr.com." + value + "MB.bin").read()
    end = time.time()
    print("Spent Times : " + str(end - start))
    print("\n")
    list2.append(end - start)
    dict1["timeToServer"][str(end - start)] = i

maxdata = max(list2)
mindata = min(list2)
print("\n")
print("Fastest Area : " + str(dict2["serverToArea"][dict1["timeToServer"][str(mindata)]]))
print("Fastest Server : " + str(dict1["timeToServer"][str(mindata)]))
print("Spent Times : " + str(mindata) + " seconds")
print("\n\n")
print("Lowest Area : " + str(dict2["serverToArea"][dict1["timeToServer"][str(maxdata)]]))
print("Lowest Server : " + str(dict1["timeToServer"][str(maxdata)]))
print("Spent Times : " + str(maxdata) + " seconds")