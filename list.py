list=[1,2,3,5,5]
freq={}
for i in list:
     freq[i]=freq.get(i,0)+1
print(freq)