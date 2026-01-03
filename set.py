# set1 = {1,2,3,4,6,7,8,9,10}
# print(set1)
# set2 = {1,1,2,2,3,3,4,5,5}
# set2.add(6)
# print(set2.remove(3))
# print(set2.discard(9))
# print(set2)
# print(set2[2])

# setA = {1,2,True,3,"praveen"}
# setB= {3,4,False,True,5,"surya","praveen"}

# print(setA|setB) # unioun join the all the values from the both set and remove the dplicate value 

# uni = {1,3,2,4,2,5}

# 
# uni.clear()
# del uni

# print(uni)

# set_Order = {"praveen","surya","tharun","srikanth","premkesh"}
# for i in set_Order:
#     print(i)
# print("sury" not in set_Order)
# print("surya" in set_Order)
# set_order1=["lando","max","lec","hamliton","oscar"]
# set_Order.add("kishore")
# set_Order.discard("srikanth1")
# # set_Order.discard("maxsss")
# set_Order.update(set_order1)
# x = set_Order.pop()
# print(x)
# print(set_Order)

# name1 = {"praveen","surya","prem"}
# name2 = {"tharun","srikanth","Praveen"}
# name3 = name1.union(name2)
# print(name3)
# nameList = ["praveen","surya","prem"]
# print(set(nameList))

# cities = {"chennai","banglore","hyd"}
# cities1 = {"hyd","mumbai","manglore"}

# print(cities.union(cities1))
# print(cities.intersection(cities1))
# print(cities1.difference(cities))
# cities.add("covai")
# print(cities)

fav_place = frozenset({"chennai","kovai","trichy","ooty","kodai"})
fav_place.remove("chennai")

print(fav_place)
