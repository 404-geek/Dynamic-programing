import collections

def get(s, pat):
    need = collections.Counter(pat)
    left, right, i, j, missing = 0, 0, 0, 0, len(pat)

    while right<len(s):

        if need[s[right]] > 0:
            missing -= 1
        need[s[right]]  -= 1
        # print(need)
        # print(right)
        right+=1

        while missing == 0:
            print('inside while')
            if j==0 or right-left < j-i:
                i,j = left,right
            need[s[left]]+=1
            if need[s[left]]>0: missing+=1
            left+=1

    return s[i:j]


print(get("this is a test string","tist"))