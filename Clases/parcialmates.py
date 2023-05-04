C=[]
for i in range(26,45):
    for j in range(3,8):
        a = i%j
        if  a == 0:
            C.append(a)
        print(len(C))