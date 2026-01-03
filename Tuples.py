# t1 = (1,2,3,4,4,5,5)
# print(t1)
# l1 =[1,2,2,3,3,4,5]
# print(tuple(l1))

# t2 = ("praveen","surya","prem","mani")
# for i in t2:
#     print(i)

# t3 = ("praveen",2.4,True,(21,"indian",False),["surya",3.4,True])

# for i in t3:
#     print(i)
# a=[10,20,30]
# print(max(a))

tup=(0,1,2,3,4,5,6,7,8,9,10)
tup1=(11,12,13,14,15,16,17,18,19,20)
print(tup[0:2])
print(tup[:5])
print(tup[5:])
print(tup[4:8])
# print(tup+tup1)
tup2 = tup[4:8]+tup1[4:8]
print(tup2)
tup3= (1,2,3,4,5,6)
tupList=(list(tup3))
print(type(tupList))
# print(tupList.push(7))

about_me =  [("praveen","front end developer","Html","css","bootstrap","js","react js","version control","database","python")]


for name, role, tool1, tool2, tool3, tool4, tool5, tool6, tool7, tool8, in about_me:
    print(
        f"My name is {name}, I am a {role}, I know "
        f"{tool1}, {tool2}, {tool3}, {tool4}, {tool5}, {tool6}, {tool7}, {tool8}"
    )

names=("praveen","surya","tharun","vikram","praveen","kathir")

print(names.count("praveen"))
print(names.index("kathir"))