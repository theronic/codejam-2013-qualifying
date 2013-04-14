import bisect

def isPalindrome(n): # my naive impl.
    s = str(n)
    return s[::-1] == s

def is_palindrome_2(s): # via http://stackoverflow.com/a/11367380/198927
    return all(s[i] == s[-(i + 1)] for i in range(len(s)//2))

def compute(fair, a, b):
    leftIndex = bisect.bisect_left(fair, %.*ea)
    rightIndex = bisect.bisect_right(fair, b)
    return rightIndex - leftIndex

#count to 10^50, so that the maximum square will be 10^100
max = 10**50

# store fair numbers in a list
fair = []

for x in range(1,max+1):
    if isPalindrome(x):
        square = x*x
        if isPalindrome(square):
            fair.append(square)

fair = sorted(fair) # make sure list is sorted

for i in range(int(input())):
    a, b = map(int, input().split())
    print("Case #%d: %s" % (i+1, compute(fair, a, b)))