import configparser

config = configparser.ConfigParser()
config.read('BD.py')


def answer_num_def(answersumm):
    respond = int(input())
    if respond == answersumm:
        config.read('BD.py')
        config['DEFAULT']['lvl_progress'] = str(int(config['DEFAULT']['lvl_progress']) + 25)
        if int(config['DEFAULT']['lvl_progress']) >= 100:
            config['DEFAULT']['lvl'] = str(int(config['DEFAULT']['lvl']) + 1)
            config['DEFAULT']['lvl_progress'] = '0'
        with open('BD.py', 'w') as configfile:
            config.write(configfile)
        print('''Ответ верный! % прогресса уровня увеличен на 25''', '\n',
              '''Ваш уровень:''', config['DEFAULT']['lvl'], '''прогресс уровня -''', config['DEFAULT']['lvl_progress'],
              '''%, количество попыток -''', config['DEFAULT']['life'])
        return
    else:
        config.read('BD.py')
        config['DEFAULT']['life'] = str(int(config['DEFAULT']['life']) - 1)
        with open('BD.py', 'w') as configfile:
            config.write(configfile)
        if config['DEFAULT']['life'] == '0':
            print('''Вы исчерпали все свои попытки! Игра окончена.''')
            exit()
        else:
            print("Ответ не верный. Количество попыток уменьшилось на 1")
            print("Ваш уровень:", config['DEFAULT']['lvl'], "прогресс уровня -", config['DEFAULT']['lvl_progress'],
                  "%, количество попыток -", config['DEFAULT']['life'])
        return
