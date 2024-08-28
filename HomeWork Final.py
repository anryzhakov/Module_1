# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Дополнительное практическое задание по модулю: "Базовые структуры данных."

grades_list = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students_set = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Создаем заготовку списка усредненных оценок
average_grades_list = [1, 2, 3, 4, 5]
# Преобразуем словарь имен студентов в список для последующей обработки
students_list = list(students_set)
# Сортируем список студентов по алфавиту
students_list_sorted = sorted(students_list)
#print(students_list_sorted)
# Определяем длину списка оценок
N = len(grades_list)
# В цикле вычисляем усредненную оценку каждого студента
while N > 0:
    N = N - 1
    average_grades_list[N] = float(round((sum(grades_list[N])) / (len(grades_list[N])), 1))

# Создаем упорядоченный перечень студентов и их средний бал
dictionary = dict(zip(students_list, average_grades_list))
print(dictionary)



