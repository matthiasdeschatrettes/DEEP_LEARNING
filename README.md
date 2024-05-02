
# Tableau de bord pour l'analyse des données de location de logements

Ce README fournit des informations détaillées sur le déploiement et l'utilisation du tableau de bord, les perspectives tirées de l'analyse des données, et un guide pour les développeurs intéressés par la compréhension, la modification ou l'extension du code.

## Guide de l'utilisateur

### Déploiement

1. **Prérequis** : Assurez-vous que Python est installé sur votre machine ainsi que les bibliothèques suivantes :
   - `dash`
   - `plotly`
   - `pandas`
   - `dash_bootstrap_components`
   Installez-les via pip si ce n'est pas déjà fait :
   ```bash
   pip install dash plotly pandas dash-bootstrap-components
   ```

2. **Téléchargement des données** :
   Exécutez le script `get_data.py` pour télécharger les données nécessaires :
   ```bash
   python get_data.py
   ```

3. **Démarrage du tableau de bord** :
   Naviguez vers le répertoire contenant `main.py` et exécutez :
   ```bash
   python main.py
   ```
   Accédez au tableau de bord via votre navigateur web à l'adresse `http://127.0.0.1:8050`.

### Utilisation

- **Interaction avec le tableau de bord** :
  Utilisez les menus déroulants pour sélectionner différentes catégories de données et observez comment les visualisations se mettent à jour en conséquence.
  - **Histogramme** : Montre la distribution des prix des locations.
  - **Carte de géolocalisation** : Affiche les emplacements sur une carte en fonction des données de location.

## Rapport d'analyse

L'analyse des données sur les locations de logements a fourni les perspectives suivantes :
- Les prix moyens de location varient considérablement selon les zones.
- Les prix de location sont plus élevés dans les centres urbains par rapport aux zones rurales.
- Les logements plus grands commandent des prix de location plus élevés, comme en témoignent les données.

## Guide du développeur

### Architecture

- **main.py** : Contient toute la logique du serveur et les callbacks nécessaires pour exécuter l'application Dash.
- **get_data.py** : Script utilisé pour télécharger le jeu de données utilisé par l'application.

### Extension du code

Pour étendre le tableau de bord :
- Ajoutez des callbacks et des graphiques supplémentaires dans `main.py`.
- Modifiez `get_data.py` pour télécharger des jeux de données supplémentaires si nécessaire.

### Modification du code

- Pour changer la source de données ou ajouter de nouveaux composants visuels, mettez à jour le `data_path` dans `main.py` et ajustez les fonctions de callback en conséquence.

N'hésitez pas à fork ce projet et à apporter vos propres modifications comme bon vous semble.
