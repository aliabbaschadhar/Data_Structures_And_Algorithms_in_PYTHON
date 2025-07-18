num = 899234
reservedNum = num
while reservedNum>0 : 
  last_digit= reservedNum%10
  print(last_digit,end="")
  reservedNum = reservedNum//10
