
def crescentOrderArray1(rows, columns):
    # when we create a list like arr = [[]]*N
    # each row will have the same index 
    arr = [[] for i in range(rows)]
    count = 1
    for row in range(rows):
        for colum in range(columns):
            arr[row].extend([count])
            count = count + 1
    return arr 

#developed by tdelaney in https://stackoverflow.com/questions/75044504/2d-list-with-a-compact-nested-loop/75044634#75044634
def crescentOrderArray3(rows, columns):
    return [list(range(i, i+columns)) 
        for i in range(1, rows*columns+1, columns)]

#developed by Roniel López in https://stackoverflow.com/questions/75044504/2d-list-with-a-compact-nested-loop/75044634#75044634
def crescentOrderArray4(rows, columns):
    return [[i+j for i in range(1, columns+1)] for j in range(0, rows*columns, columns)]


print(crescentOrderArray4(9, 6))