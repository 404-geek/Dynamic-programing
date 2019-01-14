
def maxapples(arr,rows,cols):
    for i,idi in enumerate(range(0,rows)):
        for j,idj in enumerate(range(0,cols)):
            leftweight = -1
            rightweight = -1

            leftweight = 0 if i-1<0 else arr[idi-1][idj]
            rightweight = 0 if i-1 < 0 else arr[idi][idj-1]

            arr[idi][idj] = max(leftweight,rightweight)
            print (arr)

    print(arr)


if __name__ == "__main__":
    garden = [[1, 2, 3],[6, 7, 10],[4, 2, 10]]
    numrows = len(garden)
    numcols = len(garden[0])
    maxapples(garden,numrows,numcols)



