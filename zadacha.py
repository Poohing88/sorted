import json
import re


def sber_work():
    with open('operations.json', encoding='utf-8') as jsonfile:
        file = json.load(jsonfile)
        main_file = []
        for i in file:
            if i:
                if i['state'] == 'EXECUTED':
                    main_file.append(i)
            new_main_file = sorted(main_file, key=lambda k: k['date'])
        last_main_file = [new_main_file[-1], new_main_file[-2],
                          new_main_file[-3], new_main_file[-4], new_main_file[-5]]
        format_date = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
        format_from = '[a-zA-Zа-юА-Ю]* [a-zA-Zа-юА-Ю]*'
        read_number = '[0-9]*'
        for i in last_main_file:
            date = i['date']
            type_operation = i['description']
            try:
                from_money = i['from']
                type_operations = re.findall(format_from, from_money)
                number = re.findall(read_number, from_money)
                for a in number:
                    if a:
                        if len(a) == 16:
                            number = f'{a[0]}{a[1]}{a[2]}{a[3]} {a[4]}{a[5]}** **** {a[-4]}{a[-3]}{a[-2]}{a[-1]}'
                        else:
                            number = f'**{a[-4]}{a[-3]}{a[-2]}{a[-1]}'
            except KeyError:
                type_operations = ['Вклад']
                number = ''
            to_money = re.findall(read_number, i['to'])
            to_money = to_money[-2]
            to_number = f'Счет **{to_money[-4]}{to_money[-3]}{to_money[-2]}{to_money[-1]}'
            out_date = re.findall(format_date, date)
            tru_date = f'{out_date[0][-2]}{out_date[0][-1]}.{out_date[0][-5]}{out_date[0][-4]}.' \
                       f'{out_date[0][0]}{out_date[0][1]}{out_date[0][2]}{out_date[0][3]}'
            amount_money = i['operationAmount']['amount']
            currency = i['operationAmount']['currency']['name']
            answer = f'{tru_date} {type_operation}\n ' \
                     f'{type_operations[0]} {number} -> {to_number}\n' \
                     f' {amount_money} {currency} \n'
            print(answer)


sber_work()