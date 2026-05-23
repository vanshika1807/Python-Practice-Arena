s = [1,2,2,2,33,44,44,44,44,44,6,7,8,9]

for i in set(s):
    if s.count(i)>1:
        print("Duplicate: ",i)