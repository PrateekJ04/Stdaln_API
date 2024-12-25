from datetime import datetime

now=datetime.now()
now_formatted=datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
print(now_formatted)
print(now)