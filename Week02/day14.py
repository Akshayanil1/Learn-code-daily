students = [
    {"name": "John", "school_id": 2001, "scores": [89, 67, 90, 45, 78]},
    {"name": "Tony", "school_id": 2002, "scores": [81, 67, 90, 75, 98]},
    {"name": "Robin", "school_id": 2003, "scores": [59, 63, 98, 47, 70]},
    {"name": "George", "school_id": 2004, "scores": [69, 57, 80, 90, 73]}
]
def calculate_sum(scores):
    total = 0
    for number in scores:
        total += number
    return total
def find_top_student(student_list):
    top_student = None
    highest_score = 0
    for student in student_list:
        total_score = sum(student["scores"])
        if total_score > highest_score:
            highest_score = total_score
            top_student = student
    return top_student


# def find_top_student(student_list):
#     if not student_list:
#         return None
#     top_student = student_list[0]
#     for current_student in student_list:
#         if current_student["scores"] > top_student["scores"]:
#             top_student = current_student
#     return top_student

star_performer = find_top_student(students)
if star_performer:
    print(f"The star performer is: {star_performer['name']}")
    print(f"Their amazing score was: {sum(star_performer['scores'])}")
else:
    print("No students list found.")
        
    


    