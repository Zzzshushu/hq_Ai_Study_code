"""list1=[1,2,3,4,5,5]
list2=[4,5,6,7,8,5]

list1=set(list1)
list2=set(list2)

set1=set(list1)&set(list2)
print(set1)"""
from tokenize import group

group_a=set(['apple','banana','orange','grape'])
group_b=set(['banana','grape','watermelon'])
group_c=set(['orange','peach'])

print(group_a)
print((group_a&group_b)-group_c)
set1=((group_a-group_b)-group_c)|(group_c-(group_a-group_b))|((group_b-(group_a-group_c)))

print(set1)