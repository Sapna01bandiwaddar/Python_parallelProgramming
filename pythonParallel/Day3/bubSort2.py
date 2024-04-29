def bubbleSort(lst):
    size = len(lst)

    for i in range(size):
        for j in range(size-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

if '__main__' == __name__:
    from sys import argv, exit
    from random import randint
    from time import perf_counter

    if len(argv) <= 1:
        print("pass size")
        exit(1)

    size = int(argv[1])
    lst = [randint(1,size * 10) for _ in range(size)]

    start = perf_counter()
    print("List before sorting:", lst)
    bubbleSort(lst)
    print("List after sorting:", lst)
    end = perf_counter()

    print("Time elapsed: ", round(end - start, 6))