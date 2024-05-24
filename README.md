# Programme du soir

## Description
Ce programme écrit en Python est conçu pour vérifier l'heure et fermer certaines applications qui ne favorisent pas le sommeil.

Personnellement, je lance le programme avec mon crontab entre 22:00 et 23:59.

ATTENTION: Ne fonctionne que avec Apple !!

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