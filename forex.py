from forex_python.converter import CurrencyRates
from datetime import datetime, date, time


def get_history():
    try:
        with open('history.txt', 'r') as f:
            history = f.readlines()
        return history
    except:
        print('нет истории ;(')
        return None


def input_value():
    while True:
        try:
            text = ("ваша сумма:")
            a = float(input(text))
            if a >= 0:
                return a
            raise ValueError
        except ValueError:
            print("плохой ввод ;(")


def convert(input_val, ouput_val, amount, date=datetime.now()):
    c = CurrencyRates()
    itog = c.convert(input_val, ouput_val, amount, date)
    with open('history.txt', 'a') as f:
        history = 'конвертировал {} {} в {} по курсу {} и получил {} {}\n'.format(
            amount, input_val, ouput_val, c.get_rate(input_val, ouput_val), itog, ouput_val)
        f.write(history)
    return itog


def get_datetime():
    year = int(input('год:'))
    month = int(input('месяц:'))
    day = int(input('день:'))
    date = datetime(year, month, day)
    return date


def main():
    try:
        input_val = input('откуда (код валюты):')
        output_cur = input('куда (код валюты):')
        amount = input_value()

        if (input('исторический курс("y" - да):') == 'y'):
            date = get_datetime()
            print('получили ', convert(input_val, output_cur, amount, date), output_cur)
        else:
            print('получили ', convert(input_val, output_cur, amount), output_cur)
    except:
        print('что-то пошло не так ;( \n')
        main()


main()
# print(get_history())
