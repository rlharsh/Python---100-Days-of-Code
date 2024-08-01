# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/69cffc56-5ac8-4b20-b067-b7ac13386989?sl=ab3946cf-d481-4015-a374-2f1390f31054&st=KgNgmOQAmEicKT1FZTkeepKeBVoagBBD

student_scores = input().split()

highest_score = 0
for n in range(0, len(student_scores)):
    if (int(student_scores[n]) > highest_score):
        highest_score = int(student_scores[n])

print(f"The highest score in the class is: {highest_score}")
