
numpass =0

def calculate_total(scores):
    
    return sum(scores)

def calculate_average(scores):
    if len(scores)== 0:
        return 0
    return sum(scores)/len(scores)


# def classify_grade(scores):
#     if scores < 0 or scores > 100:
#         return "Invalid"
#     elif scores>=80:
#         return "Grade A"
#     elif scores>=60 or scores<=80:
#         return "Grade B"
#     elif scores>=40 or scores<=60:
#         return "Grade C"
#     elif scores>=20 or scores<=40:
#         return "Grade D"
#     else:
#         return "Grade E"
    
def count_pass_scores(scores):
   if scores>=40:
       numpass +=1
       return numpass
   
scores = [23,45,67,89,48,90]
total_score = calculate_total(scores)
average_score = calculate_average(scores)
# for score in scores:
#     print(f"{scores} {classify_grade(scores)}")
number_of_pass = count_pass_scores(scores)

print(total_score)
print(average_score)
print(number_of_pass)
        
    
