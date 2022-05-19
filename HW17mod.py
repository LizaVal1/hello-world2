list_numbers = [int(x) for x in input("Введите числа от 1 до 999 в любом порядке, через пробел: ").split()]
print(list_numbers ) #чтоб видеть список

while True:
    try:
        element = int(input("Введите число от 1 до 999: "))
        if element < 0 or element > 999:
            raise Exception
        break
    except ValueError:
        print("Нужно ввести число!")
    except Exception:
        print("Неправильный диапазон!")

list_numbers.append(element)
print(list_numbers) #новый список, в который добавили число

def merge_sort(list_numbers):
    if len(list_numbers) < 2:
        return list_numbers[:]
    else:
        middle = len(list_numbers) // 2
        left = merge_sort(list_numbers[:middle])
        right = merge_sort(list_numbers[middle:])
        return merge(left, right)
        print (merge)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1

    return result

print(merge_sort(list_numbers)) #отсортированный новый список


def binary_search(list_numbers, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False
    middle = (right + left) // 2
    if list_numbers[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < list_numbers[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(list_numbers, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(list_numbers, element, middle + 1, right)


print(binary_search(list_numbers, element, 0,  len(list_numbers)))