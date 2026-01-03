user = {
    "Name":"Praveen",
    "Age":21,
    "Gender":"Male",
    "isMarried":False,
    "Stack":"Python",
    "Skills":["Html","css","Js","Bootstrap","React js","Git","Github","database","python"]
    # "Stack":"Python"
}
# user.pop("isMarried")
# print(user["Skills"][5])
print(user["Skills"].append("SQl"))
user["Skills"].extend(["Mongo DB","Typescprit"])
print(user)
for skills in user["Skills"]:
    print(skills)

# user1 = user.copy()
# print(user1)
# print(user)
# for key,values in  user.items():
#     print(f"{key} = {values}")
# for X in  user:
#     print(user[X])
# print(user.update({"Stack":"Java"}))
# print(user)
# print(user['Name'])
# print(user.get("Gender"))
# print(len(user))
# print(user["Skills"])
# print(user.keys())
# user['Age']=22
# print(user.values())
# print(user.items())
# if "Age" in user:
# print("yes the  age is extist")
# dicMeth = dict(name="praveen",Age=21,Gender="Male",isMarried=False,)
# print(type(dicMeth))

