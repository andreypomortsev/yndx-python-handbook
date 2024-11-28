import json
from sys import stdin

DEFAULT_ENCODING = {"encoding": "UTF-8"}

student_answers = [line.rstrip("\n") for line in stdin]

with open("scoring.json", "r", **DEFAULT_ENCODING) as json_file:
    scoring = json.load(json_file)

student_grade = 0
index = 0

for problem in scoring:
    point_per_test = problem["points"] // len(problem["tests"])

    for test in problem["tests"]:
        studen_answer = student_answers[index]
        right_answer = test["pattern"]

        if studen_answer == right_answer:
            student_grade += point_per_test
        index += 1

print(student_grade)
