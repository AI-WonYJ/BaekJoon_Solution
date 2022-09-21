from datetime import datetime

now = datetime.now()
current_time = now.strftime('%Y-%m-%d')
print(current_time)