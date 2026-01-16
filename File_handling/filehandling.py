# file = open("data.text" "mode")  # to create the a file or read file syantx
# 'r'  Read only (file must exist)
# 'w'  write only (overwrites or create)
# 'a' append only (adds to end of file )
# 'r+' Read and write (file must exist)
# 'w+' write and read (over rides or create )
# 'a+' append + read (creats if not exists)
# 'rb' read binary
# 'wb' write binary
# 'ab' append binary  

# file = open("filehand.txt",'w')
# file.write("This is the first line of the file handling \n")
# file.write("This is the second line of the file handling \n")
# file.close()
# file = open("filehand.txt",'r')
# content = file.read()
# print("File content :\n",content)
# file.close()

# file=open("filehand.txt",'w')
# file.write("hello world \n")
# file.write("hello world \n")
# file.write("hello world \n")
# file.write("hello world \n")
# file.close()
# file=open("filehand.txt",'r')
# next = file.read()
# print(next)
# file.close
# file = open("filehand.txt",'r')
# for line in file :
#     print(line.strip())
# file.close()

# with statement

# with open ("filehand.txt",'r') as file:
#     for line in file :
#      print(line.strip())

# ----------------------------------------

# feedback = input("Enter your feedback : ")

# with open('feedbackfile.txt','a') as feed : 
#     feed.write(feedback + '\n')
#     print("Thank you for your response")

# ---------------------------------------------------

# with open("filehand.txt",'r') as file:
#     for line in file :
#         print(line.strip())
# file = "filehand.txt"
# files = open(file,'r')
# read() method 
# print(files.read())
# readlines() method
# print(files.readlines()[4])
# readline() method
# for i in files.readlines():# give a line by line output inthe list
#     print(i)
# for i in files.readline(): # give a line by line output in the line 
#     print(i)
# print(files.readline())
# print(files.readline())
# # print(files.readline()[3])
# files.close()

with open('demopage.txt','w') as content :
    content.write("Hello world how are you this python one of the best languages \n")
    content.write("Hello world how are you this java one of the best languages \n")
    content.write("Hello world how are you this c one of the best languages \n")
    content.write("Hello world how are you this c++ one of the best languages \n")
    content.write("Hello world how are you this js one of the best languages \n")
    print("thank you for your response")
    
with open("demopage.txt",'r')as reading:
    print(reading.readlines())
    print(reading.tell())
    reading.seek(0) #go to page line that we mention
    print(reading.readlines())
# with open("demopage.txt",'w') as page :
#     page.write("Hello world how are you this python one of the best languages \n")

# with open("demopage.txt",'w') as page :
#     page.writelines("Hello world how are you this java one of the best languages""Hello world how are you this python one of the best languages""Hello world how are you this python one of the best languages")

#     print("thank you for your response")