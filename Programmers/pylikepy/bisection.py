
mylist = [1, 2, 3, 7, 9, 11, 33]

# 00


def bisect00(a, x, lo=0, hi=None):
    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo


print(bisect00(mylist, 3))

# 01
import bisect
print(bisect.bisect(mylist, 3))


# 00과 01의 출력값이 다르다. 알아보자.
