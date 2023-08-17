import numpy as np

"""TODO: Funktionen verkleinern oder ganz auslassen """
"""TODO: Config-Datei und Programm soll per Terminal funktionieren"""

def create_matrix(len1, len2, distance):
    matrix = np.zeros((len1+1, len2+1))
    for i in range(0,len1+1):
            matrix[i][0] = distance * i
    for j in range(0,len2+1):
        matrix[0][j] = distance * j
    return matrix

def calc_score(string1, string2, similar, not_similar, i, j):
    if string1[i] == string2[j]:
        result = similar
    else:
        result = not_similar
    return result

def eval_matrix(matrix, string1, string2, len1, len2, distance, similar, not_similar):
    for i in range(1,len1+1):
        for j in range(1,len2+1):
            c1 = matrix[i-1][j-1] + calc_score(string1, string2, similar, not_similar, i-1, j-1)
            c2 = matrix[i-1][j] + distance
            c3 = matrix[i][j-1] + distance
            matrix[i,j] = max([c1,c2,c3])
    return matrix

def traceback(matrix, string1, string2, distance, similar, not_similar):
    x = []
    y = []
    space = []
    i, j = len(string1), len(string2)
    
    """while i > 0 and j > 0:
        if matrix[i, j] == matrix[i-1, j-1] + calc_score(string1, string2, similar, not_similar, i-1, j-1):
            x.append(string1[i-1])
            y.append(string2[j-1])
            i -= 1
            j -= 1
        elif matrix[i, j] == matrix[i-1, j] + distance:
            x.append(string1[i-1])
            y.append("-")
            i -= 1
        else:
            x.append("-")
            y.append(string2[j-1])
            j -= 1
    
    while i > 0:
        x.append(string1[i-1])
        y.append("-")
        i -= 1
    
    while j > 0:
        x.append("-")
        y.append(string2[j-1])
        j -= 1"""
    
    while (i > 0 or j > 0):
        if i > 0 and matrix[i, j] == matrix[i-1, j-1] + calc_score(string1, string2, similar, not_similar, i-1, j-1):
            x.append(string1[i-1])
            y.append(string2[j-1])
            space.append("*")
            i -=1
            j -=1
        elif i > 0 and matrix[i, j] == matrix[i-1, j] + distance:
            x.append(string1[i-1])
            y.append("-")
            space.append(" ")
            i -=1
        else:
            x.append("-")
            y.append(string2[j-1])
            space.append(" ")
            j -=1

    x.reverse()
    y.reverse()
    space.reverse()
    print(matrix)
    return "".join(x), "".join(y), "".join(space)

string1 = "GTTTACCGTGT"
string2 = "GTAGGTCGTAA"
len1 = len(string1)
len2 = len(string2)
distance = 3
similar = 10
not_similar = -2
matrix = create_matrix(len1, len2, distance)
eval_matrix(matrix, string1, string2, len1, len2, distance, similar, not_similar)
aligned_string1, aligned_string2, space= traceback(matrix, string1, string2, distance, similar, not_similar)
print("Optimale Ausrichtung:")
print(aligned_string1)
print(space)
print(aligned_string2)