def turn_matrix(mx): #Функция поворота матрицы
    mx = list(map(lambda x: list(x), list(zip(*reversed(mx)))))
    return mx




def fill_row(row, mx): #Функция заполнения одного ряда
    max_mx = max(list(map(lambda x: max(x), mx))) + 1
    start = row.index(0)
    stop = row[start:].count(0)
    for _ in range(stop):
        row[start] = max_mx
        start += 1
        max_mx += 1
    return row




#Вводим размеры и создаем матрицу с нулями
size = input().split()
n = int(size[0])
m = int(size[1])
matrix = [[0] * m for _ in range(n)]

#Основной блок
for x in range(n*m):
    for i in range(len(matrix)-1):
        if 0 in matrix[i]:
            matrix[i] = fill_row(matrix[i], matrix)
            for _ in  range(3):
                matrix = turn_matrix(matrix)
            break
    if all(list(map(lambda x: 0 not in x, matrix))):
        break

#Поворачиваем матрицу, пока она не вернется в исходный формат
while matrix[0][0] != 1 or (n != int(size[0]) and m != int(size[1])):
    matrix = turn_matrix(matrix)

#Вывод матрицы
for ii in range(n):
    for jj in range(m):
        print(str(matrix[ii][jj]).ljust(3), end=" ")
    print()
