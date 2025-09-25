#str- immutable
#list- mutable


#tuple - is a immutabile list

# lst=[]
# tpl=(5)
#
# lst.append(5)
# lst.append(10)
# #tpl.append() cant append because it is immutable
# #insted we can do this:
# tpl=(tpl,)+(65,4)
# print(tpl)
#
# #packing, unpacking
#
# x=1,0,5,6,10
# a,b,c,d,e=x
# a,*_,e=x#ال * لعمل باكيج
# print(type(x))
# print(x)
# print(a, _,e)
# # a,*_,e=x
#
#
# a=5
# x=6
# print(a,x)
# a,x=x,a
# print(a,x)

#string ,lists,tuples,dictionaries ,sets --> collections /series
#1-working in the for loop
#2- indexing ,slicing, strides

if __name__=='__main__':
    # # st="lkjnekle;gmertlk;gmerg"
    # # st='ergregregregerg\''
    # # st = '\t'
    st='this is a string with a newline character \n'
    # print(st)
    # print(st.upper())
    # print(st)#immutable #call by value
    # st=st.upper()
    #
    # lst=[5]
    # print(lst)
    # lst.append(6)
    # print(lst)#mutable #call by reference


    #working feature in time
    #refactoting: optimize the code
    #design pattern, immutability
    #goal:protect the original data from being changed
    #by default: any object is mutable, unless it is clearly specified immutable
    #immutable: str, int, float, tuple,frozenset
    #mutable:list,dict,set

    # print(st.upper())
    # print(st.lower())
    # print(st.count(" "))
    # print(st.find('z'))
    # print(st.rfind('z'))
    # print(st.index('a'))
    # print(st.split())
    # print(st.endswith("this"))#هل ينتهي ب
    # print(st.startswith("This"))#هل يبدا ب
    # print(st.replace('a','b'))
    # print(st.replace('a','b',__count=1))#first appearance
    # print(st)
    # print(st.strip(' 0123456789'))#بنظف عن اليمين وعن اليسار
    # print(st.isalnum())#هل هي ارقام واحرف فقط؟
    # print(st.isalpha())#هل هي فقط احرف؟
    # print(st.isdigit())#هل هي فقط ارقام؟
    # print(st.islower())
    # print('a')
    # print(chr(97))#97+26 -a-z
    # print(ord('a'))#65 +26 -A-Z

    # st='AAAA'
    # for i in range(65,65+26):
    #     for j in range(65, 65 + 26):
    #         for k in range(65, 65 + 26):
    #             for h in range(65, 65 + 26):
    #                 print(chr(i)+chr(j)+chr(k)+chr(h))




    #list vs array
    #array: single datatype ,limited operation, memory efficient,fast
    #list: multiple datatype ,dynamic,memory inefficient, slow

    # for i in range(5):
    #     print()
    #     for j in range(i):
    #         print('#',end='')
    # for i in range(5):
    #     print('#'*i)
    # print()
    # x=5
    # for i in range(5):
    #     print('#'*x)
    #     x-=1


    # str='The quick brown fox jumped over the lazy dog'
    # maxl=''
    # for i in str.split():
    #     if len(i)>len(maxl):
    #         maxl=i
    #
    # print(maxl)
    #
    # print(max(str.split(),key=len))
    # print(sorted(str.split(),key=len))

    # nums=[1,2,3,4,5,6,7,8,9,10]
    # n=int(input('enter n:'))
    # print(nums[n:]+nums[:n])
    # nums = [1,2,3,4,5,6,7,8,9,10,1,5,7,10]
    # notd=0
    # for i in nums:
    #     if nums.count(i)==1:
    #         notd+=1
    #
    #
    # print(notd)
    #
    # nums=[1,2,3,4,5,6,7,8,9,10,1,5,7,10]
    # un=[]
    # dub=[]
    #
    # for i in nums:
    #     if i in dub:
    #         continue
    #     if i not in un:
    #         un.append(i)
    #     else:
    #         dub.append(i)
    #         un.remove(i)
    #
    # print(un)
    # print(dub)
    #

    st='this is khaled'
    lis=[]
    l=[]
    for i in st:
        if i not in l:
            l.append([i,st.count(i)])


    print(l)


