def swap(l, a, b):
    tmp = l[a]
    l[a] = l[b]
    l[b] = tmp


def partition(input_list, lo, hi):
    pivot = input_list[lo]
    left_mark = lo + 1
    right_mark = hi
    done = False
    while not done:
        while left_mark <= right_mark and input_list[left_mark] <= pivot:
            left_mark += 1
        while input_list[right_mark] >= pivot and right_mark >= left_mark:
            right_mark -= 1
        if right_mark < left_mark:
            done = True
        else:
            swap(input_list, lo, right_mark)
    return pivot


def quick_sort_aux(input_list, lo, hi):
    if lo < hi:
        pivot = partition(input_list, lo, hi)
        quick_sort_aux(input_list, lo, pivot - 1)
        quick_sort_aux(input_list, pivot + 1, hi)
    return input_list


def quick_sort(input_list):
    quick_sort_aux(input_list, 0, len(input_list) - 1)


if __name__ == "__main__":
    quick_sort([2, 34, 6, 234, 1, 78, 3,
                9, -12, -23, -13, 54, -12])
