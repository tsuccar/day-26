names = ['Alex', 'Beth', 'Carolina', 'Dave', 'Eleanor', 'Freddie']
import random

students_scores = {student: random.randint(1, 100) for student in names}

# passed_students = {item:students_scores[item] for item in students_scores if students_scores[item] > 60}

passed_students = {key:value for (key,value) in students_scores.items() if value > 60}
print(students_scores)
print(passed_students)
input_text = "i'm a disco dancer"
input_list = input_text.split()
result = {key:len(key) for key in input_list}

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {key:(value * 9/5) + 32 for (key,value) in weather_c.items()}