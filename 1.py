import time
import random

number = random.randint(0,3)
message = ['Не буди лихо, пока оно тихо.',
            "Друг познается в беде.",
            "В тихом омуте черти водятся.",
            'В гостях хорошо, а дома лучше.']

print('Проверка скорости набора текста. Введите следующую фразу. Я засеку время.')
time.sleep(2)
print('На старт...')
time.sleep(1)
print('Внимание.')
time.sleep(1)
print('Начали!')
print(message[number])

start_time = time.time()
anser = input()

if anser == message[number]:
    end_time = time.time()
    user_time = end_time - start_time
else:
    print("Вы допустили как минимум одну ошибку")
    for i in range(message[number]):
        if message[number][i]==anser[i]:
            i+1
        else:
            print(f'Вы ошиблись и написали "{message[number][i]}" вместо "{anser[i]}"')
            i+1
    
    


print(f'Вы ввели {len(message[number])} символов за {user_time} секунд')
print(f'Это {len(message[number])/user_time} символов в секунду')