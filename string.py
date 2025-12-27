''' 
word = " Hello world"
print(word[4])
print(word[1:3])
print(word[3:4])
print(word[5:])
print(word.upper())
print(word.lower())
print(word.strip()) #trim the extra space 
print(word.replace("world","python"))
print(word.split())
print(len(word))
print(word*4)
animal = "horse"
legs = 4
print(animal[:2]*legs)
a=10
b=10
print(a+b)
val1 =int( input("Enter the value 1 "))
val2 = int(input("Enter the value 2 "))
print(val1+val2)
'''

mobile = "9944754778"
maksed = mobile[:2]+"******"+mobile[-2:]
print(maksed)
song = "shape OF you"
artist = "justin Biber"

formatted =f"{song.title()}-{artist.title()}"
print(formatted)


location = "Tiruppur-periyarcolony"
fixedlocation = location.replace("periyarcolony","Balamuragnagar")
print(fixedlocation)
message = 'your booking id is : UB6767.please keep it safe'
bookingSide= message.split(":")[1].split(".")[0].strip();
# booking_id = bookingSide.split(".")[0]
# print(booking_id)
print(bookingSide)
promo_msg = 'use zomoto100 to get 100 off on your first day of your order';

coupon_code = promo_msg.split("use")[1].split('to')[0,3].strip();

print(coupon_code)