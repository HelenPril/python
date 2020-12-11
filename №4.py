a = input().split()
for ind, el in enumerate(a):
    if len(el) <= 10:
        print(ind, el)
    else:
        print(ind, el[:10])