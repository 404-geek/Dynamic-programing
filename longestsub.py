def func():
    c = '11010111'
    numarr = list(map(int,list(c)))
    l = 0
    r = 2
    print(numarr[l:r])
    for i in range(0,len(numarr)):
        print(numarr[l:r])
        if numarr[l:r].count(1) == numarr[l:r].count(0) or (numarr[l:r].count(1)%2 == 0 and numarr[l:r].count(0)%2 == 0):
            r+=1
            count = len(numarr[l:r])
        else:
            l+=1

    print(count)

if __name__ == '__main__':
    func()
