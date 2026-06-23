# import calendar
# yy=2025
# mm=2
# print(calendar.month(yy,mm))
# -----------------------------------------------------------------------
import calendar

yy = 2025
mm = 9
highlight_day = 27

# Get the calendar as a string
cal_text = calendar.month(yy, mm)

# Convert the day number to string and pad with space to match formatting
day_str = f"{highlight_day:2}"  # e.g. "14"
highlighted = f"[{day_str}]"    # e.g. "[14]"

# Replace only the first match of the day
cal_text = cal_text.replace(day_str, highlighted, 1)

print(cal_text)
