# series | list , tuple , str , set , dict

se=set()

se={5}
print(type({}))
print(type({5}))

#hashed -> not ordered, not duplicated, and not indexed -- you can loop on it

se ={5,8,9,545,1,545,5,4,5,8}
print(se)
for i in se:
    print(i)

c={1,2}
a={1,2,1,4}
b={9,8,1}

# print(a.intersection(c))#العناصر اللتي تتقاطع مع c
# print(a.difference(c))#العناصر الغير مشتركة
# print(a.union(c))#كل العناصر
# print(c.issubset(a))#هل c هي مجموعة فرعية من a
# print(c.issuperset(a))

lst=[5,6,9,8,2,2,4,8,5,7,8,6,4]
lst2=[8,9,5,78,15,21,3]

lst=list(set(lst))
print(lst)

lst3=list(set(lst).intersection(set(lst2)))

a.add(10)
a.difference_update(c)#شال المختلفات


#dict
dct={}
#key - vlaue
#key is hashed, value can be anything
#بنتعامل مع ال key زي ما بنتعامل مع الset

#ما يتقدر تعمل index للkey
#key is not ordered and not duplicated
#key must be immutable type

dct={#templiting
    'name':"Ahmad",
    'name':"Ahmad",
    'Age':19

}

print(dct['name'])

for i in dct:
    print(i)

for i in dct.values():
    print(i)

for k,v in dct.items():
    print(k,v)

#frequancy array

st="The sky blushed in shades of gold as the sun dipped below the horizon. A soft breeze carried the scent of blooming jasmine through the quiet streets."

dct={}

for i in st:
    if i in dct:
        dct[i]+=1
    else:
        dct[i]=1

print(dct)