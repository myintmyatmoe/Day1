def calculate_Average(scores):
    if len(scores) == 0:
        return 0
    return sum(scores)/len(scores)
    
scores =[45,56,89]
result = calculate_Average(scores)
print(f"Result: {result}")
    
