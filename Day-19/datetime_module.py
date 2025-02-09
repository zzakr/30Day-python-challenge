from datetime import datetime

current_time = datetime.now()
print("Current date and time:", current_time)

formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted_time)
