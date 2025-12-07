# Merge Sort
def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

# проходимо по списках
def merge_k_lists(lists):
    if not lists:
        return []
    
    # список 1
    result = lists[0]

    # список 2+ ([1])
    for i in range(1, len(lists)):
        current_list = lists[i]

        result = merge(result, current_list)

    return result



lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)