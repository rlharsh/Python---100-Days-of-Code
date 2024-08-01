# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/4e31e198-3cbb-4dae-aad9-c0d99be60fa2?sl=78555e13-d113-4d5a-b665-6575a6185b97&st=hzMUDF7hRx7MhXXymdpjbUnqEzO51wRp
# Write your code below this line 👇
def prime_checker(number):
    if number <= 100:
        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    print("It's not a prime number.")
                    return
            print("It's a prime number.")
        else:
            print("It's not a prime number.")
    else:
        print("This program only accepts numbers up to 100.")

# Write your code above this line 👆

#Do NOT change any of the code below👇
n = int(input()) # Check this number
prime_checker(number=n)
