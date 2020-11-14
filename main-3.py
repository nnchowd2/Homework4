# Name: Nafisa Chowdhury
# PSID: 11591144

def selection_sort_descend_trace(numbers):
    for i in range(len(numbers) - 1):
        index_smallest = i
        for j in range(i + 1, len(numbers)):
            if numbers[j] > numbers[index_smallest]:
                index_smallest = j

        temp = numbers[i]
        numbers[i] = numbers[index_smallest]
        numbers[index_smallest] = temp

        for num in numbers:
            print(num, end=" ")
        print()


if __name__ == "__main__":
    numbers = []
    number = input()
    for num in number.split():
        numbers.append(int(num))
    selection_sort_descend_trace(numbers)
