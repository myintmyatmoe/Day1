scores = [55, 80, 35, 90, 65]

scores.append(75)
scores[1]=85
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Average score: {sum(scores)/len(scores)}")
print(scores)

for score in scores:
    if score >=80 :
        print (score)