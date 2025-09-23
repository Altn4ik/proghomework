input_line=input('фрукты через запятую').split(', ')
cap_fruits=[]
for fruit in input_line:
    cap_fruits.append(fruit.capitalize())
print(cap_fruits)
def delete_repeats(fruit_list:list):
    return list(set(input_line))
sorted_fruits= sorted(input_line)


fruit_count_dict={f: sorted_fruits.count(f) for f in sorted_fruits}
print('Fruit dictionary:',fruit_count_dict)

maxfruit=''
maxcount=0
for key, value in fruit_count_dict.items():
    if value > maxcount:
        maxcount=value
        maxfruit=key

print(fruit_count_dict.keys())

for check_fruin in ['Banana', 'Mango']:
    if check_fruin.lower() in input_line:
        print('e')
    else:
        print('n')

N=input()
a = input_line[:N]
a.sort()





