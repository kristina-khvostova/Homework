number_of_comleted_homework = 12
hours_spent = 1.5
course_name = 'Python'
time_per_one_task = (hours_spent / number_of_comleted_homework)
time_per_one_task_in_minutes = (time_per_one_task * 60) # интересно было попробовать перевести значение в минуты, используя переменную
print('Курс:', course_name)
print('Всего задач:', number_of_comleted_homework)
print('Затрачено часов:', hours_spent)
print('Среднее время выполнения:', time_per_one_task, 'ч. или', time_per_one_task_in_minutes, 'мин.')