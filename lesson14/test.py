

# Files
# open read close - modify - open write close
file = open("new.txt", mode='br')
data = file.read()
file.close()

print(data)
# data = data + " I added this"
#
#
# file = open("new.txt", mode='wt')
# file.write(data)
# file.close()