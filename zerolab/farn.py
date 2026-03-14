# c = float(input())
# f = (c * 9/5) + 32
# print(f)

nums=[1,2,1,2,1,2,3]
hashmap={}
n=len(nums)
result=[]
for i in range(n):
    hashmap[nums[i]]=hashmap.get(nums[i],0)+1
print(hashmap)
print(hashmap.get(5,0))
print(hashmap.values())