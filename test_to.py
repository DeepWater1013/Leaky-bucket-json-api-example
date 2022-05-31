lst = [1,2,3,4,5,6,7,8,9,11,1,123,123,123,124,325,325]
n = 5
for i in range(0, len(lst), n):
    print(lst[i:i + n])