#
# #while
# #flage
#
#
# count=0
# n=5
# for i in range(1,n+1):#O(n)
#     if n%i==0:
#         count+=1
#
# if count==2:
#     print("prime")
# else:
#     print('not prime')
#
#
# count=0
# n=5
# flag=False
# for i in range(1,n+1):#O(n)
#     if n%i==0:
#         flag = True
#         break
#
# if flag:
#     print("prime")
# else:
#     print('not prime')
# # ----------------------------------------------------------
# for i in range(51):#O(50)
#     if i==40:#O(50)
#         continue#O(1)
#     print(i)#O(49)
#
# #total(O(150))
#
# for i in range(40):##40
#     print(i)#40
# for i in range(41,50):#9
#     print(i)#9
# #total(O(98))
#
# #اول وحدة كود اقل لكن تكلفة اكبر الثانية كود اكبر لكن تكلفة اقل

x=int(input('Enter a number: '))
i=2
flag=False
while x%i!=0:
    i+=1

if i==x:
    print('prime')
else:
    print('not prime')