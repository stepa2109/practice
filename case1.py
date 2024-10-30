def sum_negative_between_max_min(arr):
    if len(arr) < 2:
        return 0

    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))

    if max_index == min_index:
        return 0

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    negative_sum = sum(x for x in arr[min_index + 1:max_index] if x < 0)
    return negative_sum

if __name__ == "__main__":
    array = [int(x) for x in input("Введите элементы массива через пробел: ").split()]
    result = sum_negative_between_max_min(array)
    print(f"Сумма отрицательных элементов между максимальным и минимальным: {result}")
