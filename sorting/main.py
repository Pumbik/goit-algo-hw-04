import timeit
import random

# 1. Сортування вставками (Insertion Sort)
def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


# 2. Сортування злиттям (Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    # Сполучаємо два списки в один відсортований
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Додаємо залишки (якщо якісь елементи залишилися)
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


if __name__ == "__main__":
    sizes = [100, 1000, 5000, 10000]

    print(f"{'Algorithm':<20} | {'Size':<10} | {'Time (sec)':<15}")
    print("-" * 50)

    for size in sizes:
        data = [random.randint(0, 100_000) for _ in range(size)]

        # 1. Замір Insertion Sort
        if size <= 10000: 
            time_insertion = timeit.timeit(lambda: insertion_sort(data[:]), number=5)
            print(f"{'Insertion Sort':<20} | {size:<10} | {time_insertion:.5f}")
        else:
            print(f"{'Insertion Sort':<20} | {size:<10} | {'Skipped (too slow)':<15}")

        # 2. Замір Merge Sort
        time_merge = timeit.timeit(lambda: merge_sort(data[:]), number=5)
        print(f"{'Merge Sort':<20} | {size:<10} | {time_merge:.5f}")

        # 3. Замір Timsort (sorted)
        time_timsort = timeit.timeit(lambda: sorted(data[:]), number=5)
        print(f"{'Timsort (Built-in)':<20} | {size:<10} | {time_timsort:.5f}")
        
        print("-" * 50)