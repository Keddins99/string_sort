def string_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key.lower() < lst[j].lower():
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
