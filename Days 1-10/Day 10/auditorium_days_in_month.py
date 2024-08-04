# URL: https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/79040aa6-f9d2-4493-9f92-52c26748ec3e?sl=c9278fb9-a6f0-492d-9547-fb79a3eadc76&st=xPEfb67hnFBbXQXPw9pBURtadKusnZIV

def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

# TODO: Add more code here 👇
def days_in_month(year=2022, month=2) -> int:
  """days_in_month Returns the total days within a given month.

  Args:
      year (int, optional): The year the user wants to check. Defaults to 2022.
      month (int, optional): The month the user wants to check. Defaults to 2.

  Returns:
      int: The total number of days in the month.
  """
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

  if is_leap(year) and month == 2:
      return(month_days[int(month - 1)] + 1)
  else:
      return(month_days[int(month - 1)])

#🚨 Do NOT change any of the code below
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
