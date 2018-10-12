# Dynamic-programing
stre = "aabbccbbdccde"

data = list(stre)
temp = list(stre)
i=j=count=0

while i < len(temp):
    k = i
    print(data[j]+"     "+temp[i]+"      "+str(j)+"     "+str(i))

    if data[j] == temp[i]:
        count+=1
        print("Count="+str(count))
        i+=1
    else:
        print("Inside Else")

        if count%2 == 0:
            print("Inside if even")
            del data[j:j+count]
            count = 0
            j = data.index(temp[i])
            i = k
        else:
            print("Inside if odd")
            i = k
            j = count
            count = 0




