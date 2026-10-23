scores = [45,70,85,30,90,35]
total = 0
numpass = 0
numfail = 0
for score in scores:
 total += score
 if score >= 40:
     numpass += 1
 else:
     numfail += 1

average = total / len(scores)
print("Total:", total)
print("Average:", average)
print(f"Number of Pass: {numpass}")
print(f"Number of fail: {numfail}")

