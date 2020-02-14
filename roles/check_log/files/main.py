#!/usr/bin/env python3

import os, time

def Parser(add_files, path_in, slow, fast, t, path_out):
    for i in add_files:
        big = 0 # Переменная - счетчик, в которой считается количество долгих запросов
        small = 0 # Переменная - счетчик, в которой считается количество быстрых запросов
        average_time_taken = 0 # Среднее время долгого запроса
        start_date = 0 # Дата начала цепочки долгих запросов
        start_time = 0 # Время начала цепочки долгих запросов
        finish_date = 0 # Дата окончания цепочки долгих запросов
        finish_time = 0 # Время окончания цепочки долгих запросов
        with open("{}/{}".format(path_in, i)) as f_in, open("{}/{}.output.log".format(path_out, i), "a") as f_out:
            f_out.write("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}\n".format('Start date', 'Start time', \
                                                                              'Finish date', 'Finish time', \
                                                                               'Length chain', 'Average time taken')) # Выводим начало таблицы
            f_in.readline() # Первую строку пропускаем
            for line in f_in:
                get_time = int(line.split()[-1]) # Получаем время запроса
                if (get_time >= t): # Если время запроса >= t
                    big += 1 # Инкремент счетчика долгих запросов
                    average_time_taken = average_time_taken + get_time # Сумма всех долгих запросов
                    if (big == 1): # Если это первый долгий запрос то
                        start_date = line.split()[0] # то получаем дату начала цепочки долгих запросов
                        start_time = line.split()[1] # и время начала цепочки долгих запросов
                    small = 0 # сбрасываем счетчик быстрых запросов, т.к. получили долгий запрос
                else:
                    small += 1 # Инкремент счетчика быстрых запросов
                    if (small == 1): # Если это первый в цепочке быстрых запросов
                        finish_date = line.split()[0] # то получаем дату окончания цепочки долгих запросов
                        finish_time = line.split()[1] # и время окончания цепочки долгих запросов
                    if (small >= fast): # Если количество быстрых запросов подряд больше или равно fast то
                        if (big >= slow): # Если долгих запросов больше slow то
                            f_out.write("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}\n".format(start_date, start_time, \
                                                                                              finish_date, finish_time, big, \
                                                                                               int(average_time_taken / big))) # делаем вывод
                        average_time_taken = 0 # то Сбрасываем сумму всех длинных запросов т.к. цепочка долгих запросов прервалась
                        big = 0 # то Сбрасываем счетчик долгих запросов т.к. цепочка долгих запросов прервалась
            if (big >= slow): # проверяем ещё раз т.к. в конце файла может не оказаться fast быстрых запросов
                f_out.write("{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}\n".format(start_date, start_time, \
                                                                                  finish_date, finish_time, big, \
                                                                                   int(average_time_taken / big)))


def CheckFiles(list_files, path_in, slow, fast, t, path_out):
    while 1:
        time.sleep (10)
        new_files = list(os.listdir (path_in))
        add_files = [f for f in new_files if not f in list_files]
        list_files = new_files
        if add_files:
            Parser(add_files, path_in, slow, fast, t, path_out)



if __name__ == "__main__":
    path_in = "./Input"
    path_out = "./Output"
    slow = 5 # Количество долгих запросов, после которых будет отслежена вся цепочка долгих запросах и выведена в файл
    fast = 5 # Количество быстрых запросов, после которого цепочка долгих запросов сбрасывается
    t = 5000 # Длительность запроса в миллисекундах, если запрос выполняется >= t - это долгий запрос
    list_files = list(os.listdir (path_in)) # список файлов в указанной директории
    CheckFiles(list_files, path_in, slow, fast, t, path_out)
