import csv
import numpy as np

cr = csv.reader(open('OPA\AP3-OPA - Aufgabe2.csv', "r"))
outputArray = []
oA = []

arr = list(range(100))  # adjust to needed
x = 0
for row in cr:
    arr[x] = row
    x += 1



startAtLine =1
spalte = 5
spalte_end = 8
endAtLine = 5


s = spalte
while s <= spalte_end:

    y = int(startAtLine)
    while y <= endAtLine:
        if arr[y][s] != '':
            oA.append(arr[y][s])
        y += 1

    a = 0
    while a < np.size(oA):
        amount = oA[a]
        maketrans = amount.maketrans
        amount = amount.translate(maketrans(",", "."))
        outputArray.append(amount)
        outputArray[a] = float(outputArray[a])
        a+=1


    print(outputArray)
    outputArray = []
    amount = []
    maketrans = []
    oA = []
    s += 1