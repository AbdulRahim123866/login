# board=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# def map_loc_to_grid(loc: int):
#     for i in range(3):
#         for j in range(3):
#             if board[i][j]==loc:
#                 row,col=i+1,j+1
#
#     return f"row {row},col {col}"

# def map_loc_to_grid(loc: int):
#     row=loc//3
#     col=loc%3-1
#     if loc%3==0:
#         col=2
#         row-=1
#
#
#     return row,col
# def map_loc_to_grid(loc: int):
#     row = (loc - 1) // 3
#     col = (loc - 1) % 3
#
#     return row,col
#
# if __name__=='__main__':
#     print(map_loc_to_grid(1))
#     print(map_loc_to_grid(2))
#     print(map_loc_to_grid(4))
#     print(map_loc_to_grid(3))
#     print(map_loc_to_grid(5))
#     print(map_loc_to_grid(6))
#     print(map_loc_to_grid(7))
#     print(map_loc_to_grid(8))
#     print(map_loc_to_grid(9))
#     # row ,col =map_loc_to_grid(int(input('Enter a number on the board: ')))
#     # board[row][col]='X'

# def fac(n):
#     x=1
#     while n>1:
#         x*=n
#         n-=1
#     return x
# print(fac(5))

#bubble sort

# lst=[8,9,9,8,7,4,2,3]
# n=len(lst)
# for i in range(n//2):
#     lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]
#
#
# print(lst)
#
# lst=[8,9,9,8,7,4,2,3]
#
# def bubble_sort(lst:list):
#     lst =lst.copy()
#     for i in range(len(lst)):
#         for j in range(len(lst)-1):
#             if lst[j]>lst[j+1]:
#                 if lst[j]>lst[j+1]:
#                     lst[j],lst[j+1]=lst[j+1],lst[j]
#
#     return lst

# print(bubble_sort(lst))

# lst=[1,4,8,6,3,2,7,9]
#
# def bubble_sort(lst:list):
#     for i in range(len(lst)):
#         for j in range(len(lst)-i-1):
#             if lst[j]>lst[j+1]:
#                 lst[j],lst[j+1]=lst[j+1],lst[j]
#     return lst
#
#
# print(bubble_sort(lst))

# def broplem(lst:list):
#     n=len(lst)
#     for i in range(n):
#         for j in range(n-i-1):
#             if lst[j+1]>(lst[j]+1):
#                 lost=lst[j]+1
#     return lost
#
#
# print(broplem(lst))

# def find(lst):
#     lst.sort()
#     for i in range(len(lst)-1):
#         if lst[i]+1 != lst[i+1]:
#             return lst[i]+1
#
# lst=[1,3,7,9,2,4,6,8]
# print(find(lst))
#
# lst1=[5,7,3,4]
# lst2=[5,7,3,4]
#
# def compare(lst1,lst2):
#     for i in range(lst1):
#         if lst1[i]!=lst2[i]:
#             return False
#     return True


# st="this is my computer"

# def find_first_not_dublicated(st):
#     n=0
#     for i in range(len(st)):
#         for j in range(len(st)-1):
#             if st[i]==st[j+1]:
#                 n+=1
#                 if n==2:
#                     return st[i]
#
#     return False
#
# print(find_first_not_dublicated(st))   هاض كود غلط بس محاولة مني

# def find_first_duplicated(st):
#     seen = set()
#     for ch in st:
#         if ch in seen and ch != " ":
#             return ch
#         seen.add(ch)
#     return False
#
#
# print(find_first_duplicated(st))
# st="this is my computer"
#
# def find_first_duplicated(st:str):
#     for i in st:
#         if st.count(i)==1:
#             return i
#
#
# print(find_first_duplicated(st))


# Recursion - a function that call itself
# loop through function
# all loops can be converted to Recursion but not the opposite
# Recurion put the effort on the memory not the CPU


#base case
#stop
#input



def prenter(n):
    # print(n)
    if n==0:
        return 0
    return n+prenter(n-1)

print(prenter(10))


#TicTacToc / xo
#sudoko
#Bumb and Numbers
#Check for Balanced Pareantheses