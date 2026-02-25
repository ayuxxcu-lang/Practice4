from datetime import datetime, timedelta

# 1. Subtract 5 days
today = datetime.now()
five_days_ago = today - timedelta(days=5)
print("5 days ago:", five_days_ago)

# 2. Yesterday, Today, Tomorrow
print("Yesterday:", today - timedelta(days=1))
print("Today:", today)
print("Tomorrow:", today + timedelta(days=1))

# 3. Drop microseconds
print("Without microseconds:", today.replace(microsecond=0))

# 4. Difference in seconds
date1 = datetime(2026, 2, 20, 10, 0, 0)
date2 = datetime(2026, 2, 25, 12, 30, 0)
print("Seconds difference:", (date2 - date1).total_seconds())