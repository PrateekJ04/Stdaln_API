
# avg_marks=65.96666
# print(f"The average marks obtained by student is: {avg_marks:.2f}")

query_marks= float(input()),float(input()),float(input())
marks=list(query_marks)
print(marks)
avg_marks=sum(marks)/len(marks)
print(f"Avg marks of student: {avg_marks:.2f}")