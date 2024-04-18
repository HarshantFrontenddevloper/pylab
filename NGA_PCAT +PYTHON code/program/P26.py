# records  = [["chi", 20.0], ["beta", 50.0], ["alpha", 50.0]]

# output : The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are
# alpha
# beta

scores = []
records = []
names = []

for _ in range(int(input())):
 name = input()
 score = float(input())
 scores.append(score)
 records.append([name, score])

for record in records:
 if record[1] == sorted(set(scores))[1]:
  names.append(record[0])



print("=================OutPut Below===================")
for name in sorted(names):
 print(name)