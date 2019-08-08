import csv
uids1 = []
uids2 = []

with open("tbimsform1.csv") as file:
    csv_reader = csv.reader(file, delimiter=',')

    for row in csv_reader:
        uids1.append(row[1])

with open("tbimsform2.csv") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        uids2.append(row[1])

numOverlap = 0
for person in uids1:
    if person in uids2:
        numOverlap += 1

print(numOverlap)
#15068 of the UIDs in tbimsform1 are also present in form2
if numOverlap == len(uids1):
    print("tbimsform1 people are all in tbimsform2 as well")

    