# Описание кода Main.py
Этот код представленый в файле main.py написан на Python и состоит из трех функций и блока if __name__ == "__main__":.

1. fill_array_with_random_values(size): Эта функция заполняет массив случайными значениями от 1 до 100. Размер массива определяется параметром size.

2. print_array(array): Эта функция выводит массив на экран. Она принимает массив в качестве аргумента и выводит его на экран.

3. main(): Эта функция является основной точкой входа в программу. Она запрашивает у пользователя размер массива, затем заполняет массив случайными значениями и выводит его на экран с помощью функции print_array().

4. if __name__ == "__main__":: Этот блок кода позволяет запускать код только при прямом выполнении этого файла, а не при импорте модуля. Если файл импортируется как модуль в другой программе, то блок if __name__ == "__main__": не будет выполнен.

# Описание кода Main2.py
Этот код представленый в файле main.py написан на Python и состоит из трех функций и блока if __name__ == "__main__":.

1. Импортирует необходимые модули: random для генерации случайных чисел и datetime для работы с датами.

2. Определяет списки:

  * last_names и first_names для русских фамилий и имен соответственно.

  * subjects для предметов.

  * teachers для ФИО преподавателей.

3. Определяет функцию generate_birthdate(), которая генерирует случайную дату рождения студента в диапазоне от 2000 до 2005 года.

4. Определяет функцию generate_zachetka(), которая генерирует зачетку студента с случайным количеством предметов, датами экзаменов и ФИО преподавателей.

5. Генерирует список из 20 студентов с помощью цикла for. Для каждого студента выбираются случайные фамилия, имя, дата рождения и зачетка.

6. Определяет функцию print_students(students), которая выводит информацию о студентах и их зачетках.

7. Вызывает функцию print_students(students) для вывода информации о студентах.

8. Находит самого младшего и самого старшего студента с помощью функций max() и min(), используя ключ lambda для сравнения дат рождения.

9. Выводит информацию о самом младшем и самом старшем студенте.
