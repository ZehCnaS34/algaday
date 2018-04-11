from random import shuffle

def merge(a, b):
    result = []

    while a and b:
        if a[0] <= b[0]:
            result.append(a[0])
            a = a[1:]
        else:
            result.append(b[0])
            b = b[1:]

    if a:
        result = result + a

    if b:
        result = result + b

    return result


def merge_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst

    middle = n / 2

    left = lst[:middle]
    right = lst[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)



if __name__ == '__main__':
    a = range(10)
    shuffle(a)

    print a
    print merge_sort(a)




