# files
#open read close - modify - open write close

file=open("new.txt",mode='r')
data=file.read()
file.close()
print(data)
data=data+"I added this"


file=open("new.txt",mode='w')
file.write(data)
file.close()