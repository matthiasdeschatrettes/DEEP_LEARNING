PROJET PREDICTION DE LOYERS


Objectif du projet :

Prédire le prix des loyers en fonction de la surface, du nombre de pièce et de l'agglomération.
Dans notre dataset ces informations sont recoupées par groupement d'habitations.
Nous travaillerons donc avec des moyennes.
Par exemple sur un immeuble ou un quartier on aura le loyer moyen, la surface moyenne et le nombre de pièce moyen.



Étapes pour lancer le projet :


1 - Installer Python et les Dépendances :

Python doit être installé. Vous pouvez télécharger Python depuis python.org.
Installez les dépendances nécessaires en exécutant le fichier requirements.txt.
Ouvrez un terminal ou une invite de commande et naviguez jusqu'au dossier contenant les fichiers du projet.
Exécutez la commande suivante :

pip install -r requirements.txt


2 - Lancer l'Application Streamlit :

Dans le même terminal, lancez l'application en utilisant Streamlit avec la commande :

streamlit run main.py

Streamlit devrait automatiquement ouvrir l'application dans ton navigateur par défaut.
Si ce n'est pas le cas, il affichera une URL que vous pourrez copier et coller dans votre navigateur pour accéder à l'application.


3 - Interagir avec l'Application :

Utilise les widgets sur l'interface pour interagir avec les données, voir les graphiques, et faire des prédictions de loyers en fonction des entrées que vous fournirez.


4 - Vérifier le Modèle de Deep Learning :

Si vous voulez tester le modèle de deep learning, assurez-vous que le fichier de données et le modèle entraîné (loyer_model.h5) sont correctement configurés et accessibles par le script deeplearning.py. Vous pouvez exécuter ce script séparément pour voir les prédictions de loyer basées sur les données d'entrée.


5 - Visualiser et Analyser les Résultats :

Histogrammes et Graphiques : Observez les distributions et autres visualisations générées par l'application.
Prédictions de Loyer : Testez le modèle de prédiction en entrant différentes valeurs de surface pour voir comment le loyer prédit varie.


