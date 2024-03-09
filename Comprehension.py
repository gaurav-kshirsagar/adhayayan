# Comprehension

#List Comprehension:
# without comprehension:
sample_list = []
for i  in range(1,11):
    if i % 2 == 0:
        sample_list.append(i)
    else:
        sample_list.append(i+100)

print("sample_list=",sample_list)

#with comprehension:

sample_list = [i if i % 2 == 0 else i+100 for i in range(1,11)]
print("sample_list",sample_list)

#without comprehension:
li1 = ['a','b']
li2 = ['10','20']

out = []

for i in li1:
    for j in li2:
        out.append(i+' '+j)
print(out)

#with comprehension:
new_list = [i+' '+j for i in li1 for j in li2]
print('new_list= ',new_list)

#Dictionary Comprehension:

#without comprehension:
sample_dict = {}
for i in range(1,11):
    if i % 2 == 0:
        sample_dict[i]= i*i
    else:
        sample_dict[i]=i
print('sample_dict= ',sample_dict)

#with comprehension:
new_dict = {i:i*i if i%2 else i for i in range(1,11)}
print('new_dict',new_dict)

