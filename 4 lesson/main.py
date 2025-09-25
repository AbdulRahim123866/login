# statement
# 1- executable جملة تنفيذية
# 2- definitionجملة تعريفية


# keyword vs built-in function
# input=5
# print(input)
#convention - PEP_reduce team conflicts
#dont use built in function names
#use _ only for dummy viriable
#all names should ba small and seperated by _
#class names use camel case #thisIsMyClass
#any variable starts with _ or __used for special purpose variable
#_x=3 special usage
#__x=3 special usege
#_=3 dummy
#===============================

#Operation -
#Arithmatic , **,*,/,//,+.-,%
#comparision operation ,>,<,>=,<=,==,!=
# print(5==5.0)
#Anytihng #Bool
#Logical ,and,or ,npt# bool,same type
# print(5 and 6)
# identity -is ,not is #works on the pointer level
# x=5
# print(type(x)is int)
#membership - in , not in # work on the pointer level
# print('a' in 'abcd')
#
# for i in 'abcd':
#     pass# keyword do noting #planceholder
#
# #BitWise :>>, <<, ^ | & ~
# print(5<<2)
# print(5 | 2)
# print(~5)

# #Assignment #the variable is already defined
# x=1
# x+=5#=x=x+5


# mark=int(input("Enter th mark: "))
# print(mark*4 //100)

# x=5*2-1 **3/5%2
# x='qqqaA'
# count=0
# for i in range(len(x)):
#     if x[i].upper()=='A':
#         count+=1

# print(count)
# x='this this is my name'
# count=0
# for i in x.split():
#     if i=='this':
#         count+=1
#
# print(count)
# x=input("enter anything: ").strip()
# count=1
# for i in x:
#     if i==' ':
#         count+=1
# print(count)
# ins=input("Enter text: ")
# cp=""
# flage=False
# loc=0
# end=0
# #cleaning
# for i in range(len(ins)):
#     if ins[i]not in ' 1234567890' and flage==False:
#         loc=i
#         flag=True
# for i in range (len(ins)):
#     if ins[i] not in ' 1234567890' and flage ==False:
#         loc=i
#         flage=True
#
# end =0
# flage=False
# for i in range (len(ins[::-1])):
#     if int[-i]not in '1234567890'and flage ==False:
#         end=i
#         flage=True
#
# print(loc ,end)
# print(ins[loc:-end+1])
ins = input("Enter text: ")
flage = False
loc = 0

# إيجاد أول حرف غير رقم أو مسافة من البداية
for i in range(len(ins)):
    if ins[i] not in ' 1234567890' and flage == False:
        loc = i
        flage = True

# إيجاد أول حرف غير رقم أو مسافة من النهاية (باستخدام السلسلة المعكوسة)
end = 0
flage = False
for i in range(len(ins[::-1])):
    if ins[::-1][i] not in '1234567890 ' and flage == False:
        end = i
        flage = True

print("Start index:", loc)
print("End index from end:", end)

# طباعة الجزء الحرفي فقط
print(ins[loc:len(ins)-end])


x=input('enter string : ')
v='aeiuo'
count=0
for i in x:
    if i in v:
        count+=1

print(count)
