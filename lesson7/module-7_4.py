team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 18015.2
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
    #Использование %:
print('В команде Мастера кода участников: %s !' % team1_num)
print('Итого сегодня в командах участников: %s и %s !'%(team1_num, team2_num))

    #Использование format():
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} с !'.format(team2_time))

    # Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'победа команды Мастера кода'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'победа команды Волшебники Данных'
else:
    challenge_result = 'Ничья'
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {score_1 + score_2} задач, в среднем по'
      f' {round((team1_time + team2_time)/(score_2 + score_1),1)} секунды на задачу!')

