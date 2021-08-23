from answerdef import answer_def
from answernumdef import answer_num_def
from random import randint
from START_BD import start_bd
print("Здравствуйте! Вы хотите поучаствовать в математической игре?")
print("Нажмите д/н и подтвердите выбор нажатием клавиши Enter")
vote = input()
if vote != 'д':
    print("Очень жаль! Будем ждать Вас в следующий раз!")
    exit()
elif vote == 'д':  # Начало игры. Первый уровень.
    start_bd()
    with open('start.txt', encoding='utf-8') as inf:
        for line in inf:
            line = line.strip()
            print(line)
answer_def('д')
answernum1, answernum2 = randint(1, 100), randint(1, 100)
print("Следующий вопрос. Укажите сумму чисел", answernum1, "и", answernum2)
answer_num_def(answernum1+answernum2)
answernum1, answernum2 = randint(-100, 100), randint(-100, 100)
print("Следующий вопрос. Укажите разность чисел", answernum1, "и", answernum2)
answer_num_def(answernum1 + answernum2)
print("Пифагор - это имя человека, деятельность которого была от части связана с Геометрией?")
answer_def('д')
print("Правда ли, что у равнобедренного треугольника все стороны равны?")
answer_def('н')
answernum1, answernum2, answernum3 = randint(1, 9), randint(1, 9), randint(1, 20),
print("""Решите уравнение.""", "(", answernum1, "+", answernum2, ") в квадрате, умножено на", answernum3)
answer_num_def((answernum1 + answernum2)**2 * answernum3)
