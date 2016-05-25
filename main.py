from function import *
from time import *


def main():
    # sort1()
    # sort3()
    # create_txt()
    # print(open_txt()[0])
    print('   ')
'''
    t1 = time()
    # new_list = qsort(open_txt())
    new_list = shell_sort(open_txt())
    print('Сортировка - ' + str(time() - t1))
    t2 = time()
    create_sort_txt(new_list)
    print('Создания new_txt - ' + str(time() - t2))
'''

if __name__ == '__main__':
    print('Команды:\n1 - выбрать файл для сортировки\next - Выход')
    while True:
        my_command = input()
        if my_command == '1':
            file = input('Введите названия файла:')
            print('Идёт процесс сортировки...')
            t1 = time()
            new_list = shell_sort(open_txt(file=file))
            print('Сортировка - ' + str(time() - t1))
            t2 = time()
            create_sort_txt(new_list)
            print('Создания new_txt - ' + str(time() - t2) + '\nПроцесс закончен.')

        elif my_command == 'ext':
            print('До свидания')
            break
    # main()
