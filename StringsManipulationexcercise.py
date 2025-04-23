from ctypes.macholib.framework import framework_info

string="hello"
print(string.upper())
print(string.lower())

#################

string1="Hello"
string2="World!"
print(string1+" "+ string2)

##############
word="Python"
print(word[:3])

#################
full_name =input("Please enter your full name : ")
part=full_name.split()

first_name=part[0]
last_name=part[-1]
print(first_name)

###################
new_string="Automation"
reverse_string=new_string[::-1]
print(reverse_string)

##############

name=input("Please enter your full name :")
separate=name.split()

if len(separate)>1:
    firstname=separate[0]
    lastname=separate[-1]
    middlename="".join(separate[1:-1])
    if len(separate)>2:
        print(middlename)
    else:
        print("There is no middle name")
    print(firstname)
else:
    print("Please enter your full name")


