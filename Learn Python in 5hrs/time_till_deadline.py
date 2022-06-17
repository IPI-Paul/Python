from datetime import datetime
import re

regex = re.compile(r"(.*[^\s*])(\s*:\s*)(.*[^\s*])")
user_input = input("Enter your goal with a deadline separated by a colon\n")
input_list = list(regex.match(user_input).group(1, 3))

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d/%m/%Y")
today_date = datetime.today()
time_till = deadline_date - today_date
hours_till = int(time_till.total_seconds() / 60 / 60)

# print(f"Dear user! Time remaining for your goal: {goal} is {time_till.days} days")
print(f"Dear user! Time remaining for your goal: {goal} is {hours_till} hours")
