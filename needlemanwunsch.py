import numpy as np
import argparse

def calc_score(string1, string2, similar, not_similar, i, j):
    if string1[i] == string2[j]:
        result = similar
    else:
        result = not_similar
    return result

def needleman(string1, string2, distance, similar, not_similar):
    len1 = len(string1)
    len2 = len(string2)

    matrix = np.zeros((len1+1, len2+1))
    for i in range(0,len1+1):
        matrix[i][0] = distance * i
    for j in range(0,len2+1):
        matrix[0][j] = distance * j

    for i in range(1,len1+1):
        for j in range(1,len2+1):
            case1 = matrix[i-1][j-1] + calc_score(string1, string2, similar, not_similar, i-1, j-1)
            case2 = matrix[i-1][j] + distance
            case3 = matrix[i][j-1] + distance
            matrix[i,j] = max([case1,case2,case3])

    align1 = []
    align2 = []
    space = []

    i, j = len1, len2

    while (i > 0 or j > 0):
        if i > 0 and matrix[i, j] == (matrix[i-1, j-1] + calc_score(string1, string2, similar, not_similar, i-1, j-1)):
            align1.append(string1[i-1])
            align2.append(string2[j-1])
            space.append("*")
            i -=1
            j -=1
        elif i > 0 and matrix[i, j] == matrix[i-1, j] + distance:
            align1.append(string1[i-1])
            align2.append("-")
            space.append(" ")
            i -=1
        else:
            align1.append("-")
            align2.append(string2[j-1])
            space.append(" ")
            j -=1

    align1.reverse()
    align2.reverse()
    space.reverse()
    
    return "".join(align1), "".join(align2), "".join(space)

"""string1 = str(input("Erste Sequenz eingeben: "))
string2 = str(input("Zweite Sequenz eingeben: "))
distance = int(input("Distanz eingeben: "))
similar = int(input("Match Score eingeben: "))
not_similar = int(input("Mismatch Score eingeben: "))
aligned_string1, aligned_string2, spacer = needleman(string1, string2, distance, similar, not_similar)
print("Optimale Ausrichtung:")
print(aligned_string1 + "\n" + spacer + "\n" + aligned_string2)"""

def main():
    parser = argparse.ArgumentParser(description="Needleman-Wunsch-Algorithmus zur Sequenzalignment")
    parser.add_argument("sequence1", help="Erste Sequenz")
    parser.add_argument("sequence2", help="Zweite Sequenz")
    parser.add_argument("--distance", type=int, default=3, help="Distanzwert (Standard: -3)")
    parser.add_argument("--match", type=int, default=10, help="Match Score (Standard: 10)")
    parser.add_argument("--mismatch", type=int, default=-2, help="Mismatch Score (Standard: -5)")
    args = parser.parse_args()

    aligned_string1, aligned_string2, spacer = needleman(args.sequence1, args.sequence2, args.distance, args.match, args.mismatch)
    print("Optimale Ausrichtung:")
    print(aligned_string1 + "\n" + spacer + "\n" + aligned_string2)

if __name__ == "__main__":
    main()