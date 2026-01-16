playlist = ["hukum","annuale malee","na ready","smooth operator"];

print(playlist[0]);
playlist.append(" du du du du max verstappen")
playlist.insert(2,"enn maima peru da anjalai")
playlist.remove("enn maima peru da anjalai")
# playlist.pop()
# playlist.reverse()
print(playlist.count("na ready"))  

print(playlist[0:2])
print(playlist[2:])
print(playlist[:2])
print(playlist[-2:])

# list itreation 
locations= ["Tiruppur","coimbatore","chennai","erode","salem"]

for i in locations:
    print(i)
#checking
if "Coimbatore" in locations:
    print("yes")
else :
    print("No")

#updating the location mutable 

locations[1]='Trichy'
print(locations)
#merging
special = ["clothes","temple","captial","Bedsheet","manogo"]

mixed = locations+special;
print(mixed)

for i,location in enumerate(mixed):
    print(f"{i } {location}")


a  = [1,2,3,4,5]

b= a[:]
print(b)
c = a.copy()
print(c)
a.extend([6,7])
a.pop()
del a [2]
# a.clear()
ab=a.count(5)
print(ab)
# print (a is b)
# print (a is c)
print(a)

list = [["ubar","airport", 4.5 ,"coimabtore"]]
for travller ,pickup,time,drop in list: 
    print(f"traveller {travller} pickup locaton is {pickup} timing is {time} drop location is {drop} ")
   