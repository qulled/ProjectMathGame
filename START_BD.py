import configparser


def start_bd():
    config = configparser.ConfigParser()
    config.read('BD.py')
    config['DEFAULT']['life'] = '3'
    config['DEFAULT']['lvl'] = '1'
    config['DEFAULT']['lvl_progress'] = '0'

    with open('BD.py', 'w') as configfile:
        config.write(configfile)
    return
