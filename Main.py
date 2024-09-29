import random

def fill_array_with_random_values(size):
    return [random.randint(1, 100) for _ in range(size)]

def print_array(array):
    print("Массив:", array)

def main():
    size = int(input("Введите размер массива: "))
    array = fill_array_with_random_values(size)
    print_array(array)

if __name__ == "__main__":
    main()
