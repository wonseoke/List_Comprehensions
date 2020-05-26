# total_comprehension.py

my_numbers = [1, 2, 3, 4, 5, 6, 7]
print("--------------")
print("ORIGINAL LIST:", my_numbers)

print("--------------")
print("TOTAL COMPREHENSION...")

# TODO: write python code here


mapped_list = []
for i in my_numbers:
    mapped_list.append(i * 100)

print("--------------")
print("Mapped List: " + str(mapped_list))


f_list1 = []
for i in my_numbers:
    if i > 3:
        f_list1.append(i)

print("--------------")
print("FILTERED LIST W/ MATCHES: " + str(f_list1))


f_list2 = []
for i in my_numbers:
    if i > 8:
        f_list2.append(i)
print("--------------")
print("FILTERED LIST W/ MATCHES: " + str(f_list2))



mf_list = []
for i in mapped_list:
    if i > 399:
        mf_list.append(i)

print("--------------")
print("MAPPED AND FILTERED LIST: " + str(mf_list))