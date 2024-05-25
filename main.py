import subprocess
from datetime import datetime
from typing import List

def is_past_time(time:int) -> bool:
  if 0 <= time <= 23:
    return datetime.now().hour >= time
  else:
    raise ValueError("Time must be between 0 and 23")

def get_open_apps() -> List:
  script = '''
  tell application "System Events"
      set openApps to name of every process whose background only is false
  end tell
  return openApps
  '''
  try:
    process = subprocess.Popen(['osascript', '-e', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if process.returncode != 0:
      print(f"Error when retrieving open applications: {error.decode('utf-8')}")
      return []

    apps = output.decode('utf-8').strip().split(', ')
    return apps
  except Exception as e:
    print(f"Exception while executing osascript : {e}")
    return []

def close_application(app_name) -> None:
  script = f'''
  tell application "{app_name}"
      quit
  end tell
  '''
  try:
    process = subprocess.Popen(['osascript', '-e', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if process.returncode == 0:
      print(f"'{app_name}' closed sucessfully")
    else:
      print(f"Error while closing '{app_name}': {error.decode('utf-8')}")
  except Exception as e:
    print(f"Exception while closing '{app_name}' : {e}")

def get_week_day() -> str:
  day_int = datetime.now().weekday()
  day = [day_name for day_name, day_number in days_dict.items() if day_number == day_int][0]
  return day

def hours_per_day(day: str) -> int:
  days = [name for name, _ in days_dict.items()]
  if day in days:
    if day == "monday":
      hours = 24
    elif day == "tuesday":
      hours = 22
    elif day == "wednesday":
      hours = 22
    elif day == "thursday":
      hours = 22
    elif day == "friday":
      hours = 22
    elif day == "saturday":
      hours = 22
    else:
      hours = 22
    return hours
  else:
    print(f"""
Error, wrong input: day:str
{days}
          """)
    return 0

def main():
  open_apps = get_open_apps()
  closing_hour = hours_per_day(get_week_day())
  if is_past_time(closing_hour):
    for banned_app in banned_apps:
      if banned_app in open_apps:
        close_application(banned_app)

banned_apps = ['Arc', 
               'Safari', 
               'Firefox', 
               'Music', 
               'Steam', 
               'DeSmuME'
               ]

days_dict = {
  "monday": 0,
  "tuesday": 1,
  "wednesday": 2,
  "thursday": 3,
  "friday": 4,
  "saturday": 5,
  "sunday": 6
}   

if __name__ == "__main__":
  main()