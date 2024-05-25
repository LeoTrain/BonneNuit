### Programme du Soir

## Description
Ce programme écrit en Python est conçu pour vérifier l'heure et fermer certaines applications qui ne favorisent pas le sommeil. Personnellement, je lance le programme avec mon crontab entre 22:00 et 23:59.

**ATTENTION**: Ne fonctionne qu'avec Apple !!

## Version
Actuelle: v1.0  
Disponibles:
- v1.0

## Librairies
Ce projet utilise les librairies Python suivantes :
- subprocess
- datetime
- typing

## Instructions d'installation et d'utilisation

### Installation
1. **Cloner le dépôt**: Clonez le dépôt sur votre machine locale à l'aide de la commande :
    ```bash
    git clone <URL_du_dépôt>
    ```

### Configuration
1. **Configurer crontab**: Ajoutez une tâche cron pour exécuter ce programme entre 22:00 et 23:59. Vous pouvez éditer votre crontab avec la commande :
    ```bash
    crontab -e
    ```
    Ajoutez ensuite la ligne suivante pour exécuter le programme tous les jours entre 22:00 et 23:59 :
    ```bash
    0 22 * * * /chemin/vers/votre_programme.py
    ```

### Utilisation
1. **Exécuter le programme**: Vous pouvez exécuter manuellement le programme avec la commande :
    ```bash
    python3 chemin/vers/votre_programme.py
    ```

## Fonctionnement du programme
Le programme vérifie l'heure actuelle et, si elle se situe dans la plage spécifiée (22:00 - 23:59), il ferme les applications listées comme perturbatrices pour le sommeil. Les applications à fermer peuvent être définies dans une liste au sein du script.

## Améliorations futures
- Ajouter une interface graphique pour configurer les applications et les heures de fonctionnement.
- Permettre de définir des plages horaires personnalisées pour chaque jour de la semaine.
- Envoyer des notifications avant de fermer les applications.

N'hésitez pas à proposer des améliorations ou à signaler des problèmes en ouvrant une issue sur le dépôt GitHub.

---

## Modifications apportées
J'ai ajouté trois nouvelles fonctions pour permettre de définir des plages horaires personnalisées pour chaque jour de la semaine :

1. **`get_week_day`** : Renvoie le jour de la semaine en format texte.
2. **`hours_per_day`** : Définit les heures de fermeture pour chaque jour de la semaine.
3. **`is_past_time`** : Vérifie si l'heure actuelle est passée par rapport à l'heure donnée.

Voici le script mis à jour avec ces fonctions :

```python
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
      print(f"'{app_name}' closed successfully")
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
```

### Description des nouvelles fonctions

- **`get_week_day`** : Cette fonction renvoie le jour de la semaine en format texte (e.g., "monday", "tuesday").
- **`hours_per_day`** : Cette fonction renvoie l'heure de fermeture pour chaque jour de la semaine. Par exemple, 24 pour lundi, 22 pour les autres jours.
- **`is_past_time`** : Cette fonction vérifie si l'heure actuelle est passée par rapport à l'heure donnée (0 à 23).

Ces ajouts permettent une gestion plus flexible des horaires de fermeture des applications selon les jours de la semaine.