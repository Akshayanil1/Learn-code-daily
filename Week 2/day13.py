# def calculate_sum (student_list):
#     total = 0
#     for number in student_list:
#         total += number
#     return total
    
# # Akshay = [89, 67, 90, 45, 78]
# # print(f"Sum of Akshay's scores: {calculate_sum(Akshay)}")
# # Abijith = [89, 97, 70, 85, 88]
# # print(f"Sum of Abijith's scores: {calculate_sum(Abijith)}")
# # Abishek = [79, 87, 90, 95, 78]
# # print(f"Sum of Abishek's scores: {calculate_sum(Abishek)}")

# report = [
#     {
#         "name": "Akshay",
#         "scores": [89, 67, 90, 45, 78]
#     },
#     {
#         "name": "Abijith",
#         "scores": [89, 97, 70, 85, 88]
#     },
#     {
#         "name": "Abishek",
#         "scores": [79, 87, 90, 95, 78]
#     }
# ]

# for student in report:
#     student_name = student["name"]
#     student_scores = student["scores"]
#     print(f"{student_name}'s scores: {calculate_sum(student_scores)}")

def calculate_sum(student_list):
    total = 0
    for number in student_list:
        total += number
    return total

report = [
    {"name": "Akshay", "scores": [89, 67, 90, 45, 78]},
    {"name": "Abijith", "scores": [89, 97, 70, 85, 88]},
    {"name": "Abishek", "scores": [79, 87, 90, 95, 78]}
]

for student in report:
    student_name = student["name"]
    student_scores = student["scores"]
    print(f"{student_name}'s scores: {calculate_sum(student_scores)}")