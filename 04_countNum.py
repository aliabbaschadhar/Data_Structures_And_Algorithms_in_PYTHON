from math import log10
num = 889239
reservedNum = num
count = 0 
while reservedNum>0:
  reservedNum= reservedNum//10 # Whole time complexity depends on this line 
  # If there is a division in any algo and the algo depends on that division 
  # like if reservedNum//5 then no of loops would increase then it will take more time.
  # then T.C will be of O(log(division)(n)) like here O(log10(n))
  count+=1
print(count)
# Log10 count
logCount = int(log10(num)+1)
print(logCount)
# string count 
strCount = len(str(num))
print(strCount) 