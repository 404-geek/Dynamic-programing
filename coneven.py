# Dynamic-programing
stre = "aaabbbccbbdccde"
# stre = "dde"

b = list(stre)
n = list(stre)


def ret(data,temp):
    i = j = count = 0
    while i <= len(temp):
        if(i==len(temp)):
            # print("inside equals")
            # print(data)
            ret(data,data)
            break
        k = i
        # print(data[j]+"     "+temp[i]+"      "+str(j)+"     "+str(i))

        if data[j] == temp[i]:
            count+=1
            # print("Count="+str(count))
            i+=1

        else:
            # print("Inside Else")

            if count%2 == 0:
                # print("Inside if even")
                del data[j:j+count]
                if(len(data)==1):
                    return data
                    break
                count = 0
                j = data.index(temp[i])
                i = k
            else:
                # print("Inside if odd")
                i = k
                j = count
                count = 0

    return data


print(ret(b,n))


#
# data = list(stre)
# temp = list(stre)
# i=j=count=0
#
# while i < len(temp):
#     k = i
#     print(data[j]+"     "+temp[i]+"      "+str(j)+"     "+str(i))
#
#     if data[j] == temp[i]:
#         count+=1
#         print("Count="+str(count))
#         i+=1
#     else:
#         print("Inside Else")
#
#         if count%2 == 0:
#             print("Inside if even")
#             print (str(j)+"     "+str(j+count))
#             del data[j:j+count]
#             print (data)
#             count = 0
#             j = data.index(temp[i])
#             i = k
#         else:
#             print("Inside if odd")
#             i = k
#             j = count
#             count = 0
#
# # print(data)



