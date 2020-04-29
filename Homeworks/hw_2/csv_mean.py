import csv

def avg() -> str:
    #присваваем пустые переменные для каждого из столбиков файла
    id = 0
    sum_h = 0
    sum_w = 0
    #открываем файл
    with open('hw.csv') as file:
        reader = csv.reader(file)
        next(reader)
        #циклом проходимся по файлу
        for row in reader:
            id += 1
            sum_h += float(row[1])
            sum_w += float(row[2])
        #Расчет + округление(round) реузльтата до второго символа после запятой
        # 1 фунт = 0,453592
        # 1 дюйм = 2,54
        avg_h = round((sum_h / id) * 2.54, 2)
        avg_w = round((sum_w / id) * 0.453592, 2)
        result = f'{avg_h}, {avg_w}'
        return str(result)