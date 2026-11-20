def zip_longest_lists(*lists, fill=None):


    Примеры:
        zip_longest_lists([1, 2], [3])        -> [(1, 3), (2, None)]
        zip_longest_lists([], [1, 2], fill="x") -> [("x", 1), ("x", 2)]
    """
    if not lists:
        return []

    max_len = max(len(lst) for lst in lists)
    result = []

    for i in range(max_len):
        row = []
        for lst in lists:
            if i < len(lst):
                row.append(lst[i])
            else:
                row.append(fill)
        result.append(tuple(row))

    return result
