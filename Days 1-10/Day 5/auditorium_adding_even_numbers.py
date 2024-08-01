# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/c8a70cc6-7b64-42ad-880b-e2034e8cb8bc?sl=6ca26e31-59e7-48b8-bd61-29aa4578dee3&st=dxa8zt7S8lJSxMK4Sf9f2ajskeJOrcsk
target = int(input())
final_total = 0
for number in range(0, target + 1):
    if number % 2 == 0:
        final_total += number
print(final_total)

final_total = 0
for number in range(0, target + 1, 2):
    final_total += number
print(final_total)
