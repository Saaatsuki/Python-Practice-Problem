students = {
    'Alice': 85,
    'Bob': 92,
    'Charlie': 88,
    'David': 90,
    'Eva': 95
}

sorted_students = sorted(students.items() , key=lambda x:x[1],reverse=True)

top_3 = sorted_students[:3]

for name , score in top_3:
    print(f"{name} : {score}")