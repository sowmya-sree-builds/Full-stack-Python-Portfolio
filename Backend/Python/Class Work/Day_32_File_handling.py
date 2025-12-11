# # file hadnling
# # creating files
# # reading files
# # updating files
# # deleting files

# #  why files?
# #   to store data permanently until we remove it.

# # 1. begineer level ->> txt files.
# #  to open the file --> open(path,mode)
# a=45
# print(a)
# x = open('.\Day_32_Sample.txt','r')
# op = x.read()
# print(op)
# op1 = x.readline()
# op2 = x.readline()

# print(op1,op2)

# print(x.closed)
# x.close()
# print(x.closed)

# i = 1
# for i in x:
#     if i == 2 or i == 5:
#         print(i)
#     i+=1

# op = x.readlimes()
# print(op)

# write mode - 

f = open('basic.txt','w')
f.write("hello world")
# f.close()       old approach 


# in write mode if file is not available then it will create

with open('basic.txt','r') as f:
    op = f.read()
    print(op)
print(f.closed)

with open('basic.txt','r') as f:
    f.writelines(['1','2','3','4'])

# w mode -- re write the content in the file.
# a mode -- update the exsisting file with new data
# r mode -- read mode
# r+     -- read+write
# w+     -- write+read
# a+     -- apppend + read   



# json.load
# json.dump

# ip='simha'
# with open('./data.json','r') as f:
#     data = json.load(f)
#     print(data,type(data))
#     data.append(``)