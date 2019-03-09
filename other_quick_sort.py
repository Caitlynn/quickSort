def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        split_point = partition(alist, first, last)

        quickSortHelper(alist, first, split_point - 1)
        quickSortHelper(alist, split_point + 1, last)


def partition(alist, first, last):
    pivot_value = alist[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and alist[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while alist[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = alist[left_mark]
            alist[left_mark] = alist[right_mark]
            alist[right_mark] = temp

    temp = alist[first]
    alist[first] = alist[right_mark]
    alist[right_mark] = temp

    return right_mark


alist = [2, 34, 6, 234, 1, 78, 3, 9, -12, -23, -13, 54, -12]
quickSort(alist)
print(alist)
