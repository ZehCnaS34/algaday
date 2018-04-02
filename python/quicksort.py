def swap(lst, i, j):
    lst[i], lst[j] = lst[j], lst[i]


def parition(lst, lo, hi):
    p = lst[hi]
    i = lo - 1

    print lst[lo: hi+1], p

    for j in xrange(lo, hi):
        if lst[j] < p:
            i += 1
            swap(lst, i, j)

    swap(lst, i+1, hi)

    print '---'
    print lst[lo: hi+1], p

    return i+1


def quick_sort(lst, lo, hi):
    if lo < hi:
        p = parition(lst, lo, hi)
        quick_sort(lst, lo, p - 1)
        quick_sort(lst, p + 1, hi)


if __name__ == '__main__':
    from random import shuffle
    a = range(10)
    shuffle(a)

    quick_sort(a, 0, len(a)-1)

    print a
