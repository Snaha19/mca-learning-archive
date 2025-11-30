#count consecutive block increase
count=1
no_block=1
max_block_len=1
block_len=1

while count<=8:
    num=int(input("enter num"))
    if count==1:
        value1=num
    else:
        if num>value1:
            block_len+=1
            value1=num
        else:
            no_block+=1
            if(block_len>max_block_len):
                max_block_len=block_len
            block_len=1
            value1=num
    count+=1
if(block_len>max_block_len):
    max_block_len=block_len
print("no of block :",no_block)
print("no of max block :",max_block_len)
