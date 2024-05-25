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

def main():
  open_apps = get_open_apps()
  # banned_apps = ['Safari', 'Firefox', 'Music', 'Steam', 'DeSmuME']
  banned_apps = ['Obsidian']
  if is_past_time(12):
    for banned_app in banned_apps:
      if banned_app in open_apps:
        close_application(banned_app)
    

if __name__ == "__main__":
  main()