from fileinput import close
import json
import csv

#Task 1

code = b'r\xc3\xa9sum\xc3\xa9'

decode_utf = code.decode()
print(decode_utf)

latin_code = decode_utf.encode('latin1')
print(latin_code)

code_str = latin_code.decode('latin1')
print(code_str)

#Task 2

str_1 = input("1st string:")
str_2 = input("2nd string:")
str_3 = input("3rd string:")
str_4 = input("4th string:")

file = open('text.txt','w+')
file.write(str(str_1) + "\n" + str(str_2) + "\n")
file.close()

file = open('text.txt','a')
file.write(str(str_3) + "\n" + str(str_4))
file.close()

file = open('text.txt','r')
print(file.read())
file.close()

#Task 3

dict_1 = {
    111111: ('Yar', 30),
    222222: ('Misha', 25),
    333333: ('Vitold', 35),
    444444: ('Sara', 20)
}
print(dict_1)

with open('less_6.json', 'w') as write_file:
    json.dump(dict_1, write_file)

print(dict_1)