fp=open('catalog.txt','r')
lines=fp.readlines()
fp.close()

i_code=1
items={}

for line in lines:
    iName,price,bQty=line.split(',')
    items[i_code]={'name':iName,'price':int(price),'bQty':bQty}
    i_code+=1
