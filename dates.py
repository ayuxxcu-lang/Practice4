# dates.py

import datetime

# Create date object
now = datetime.datetime.now()
print("Current date and time:", now)

# Format date
formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

# Time difference
future = datetime.datetime(2026, 1, 1)
difference = future - now
print("Days until 2026:", difference.days)