import random

## list comprehension

numbers = [1, 2, 3, 4, 5]

# twice
twice_numbers = [num * 2 for num in numbers]
print(twice_numbers)

# with conditions
even_numbers = [num for num in numbers if num%2 == 0]
odd_numbers = [num for num in numbers if num%2 != 0]
print(even_numbers)
print(odd_numbers)

# intersect
intersect = [num for num in numbers if num in twice_numbers]
print(intersect)

# finding odd numbers using different
diff_odd_numbers = [num for num in numbers if not num in even_numbers]
print(diff_odd_numbers)

## dictionary comprehension
students = ["Alex", "Bob", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student:random.randint(1, 100) for student in students}
print(student_scores)
passed_student = {student:score for (student, score) in student_scores.items() if score > 60}
print(passed_student)