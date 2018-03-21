s = 'azcbobobegghakl'
long_sub_str=''
for i in range(1,len(s)-1):
  temp =s[i-1]
  while s[i] >= temp[-1]:
    temp+=s[i]
    i+=1
    if i > len(s)-1:
      break
  if len(long_sub_str) < len(temp):
    long_sub_str =temp
   
print ('Longest substring is :',long_sub_str)
