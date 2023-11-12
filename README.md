
# README

## User Guide

### Déploiement du tableau de bord

1. Assurez-vous d'avoir installé Python et les bibliothèques nécessaires comme `dash`, `dash_bootstrap_components`, `pandas`, etc.
2. Placez tous les fichiers dans un dossier unique.
3. Ouvrez un terminal ou une invite de commandes et naviguez jusqu'au dossier contenant les fichiers.
4. Exécutez la commande suivante pour démarrer le serveur Dash et afficher le tableau de bord:
   ```
   python main.py
   ```
5. Ouvrez un navigateur et accédez à l'URL affichée dans la console (généralement `http://127.0.0.1:8050/`).
6. Vous pouvez maintenant interagir avec le tableau de bord et explorer les différents graphiques et cartes.

### Utilisation du tableau de bord

- Sélectionnez un département pour voir les prix moyens du carburant.
- Explorez la carte thermique pour voir la distribution des prix du carburant en France.
- Utilisez l'histogramme pour comprendre la distribution des prix des différents types de carburants.
- D'autres visualisations peuvent également être disponibles en fonction des modules inclus.

## Rapport d'analyse
## Rapport d'analyse

### INTRO
Notre projet porte sur le prix des carburants pour automobiles en 2022, les données de 2023 n'étant pas encore complètes. Les informations ont été collectées sur [data.gouv.fr](https://data.gouv.fr), émises par le Ministère de l'Economie, des Finances et de la Souveraineté industrielle et numérique. Ce sujet a été choisi pour son importance quotidienne dans la vie des Français, notamment en ce qui concerne la localisation des stations-service et les prix des carburants. Notre Dashboard est une page web analysant les stations-services en France, leurs adresses, les carburants proposés, leurs tarifs, et l'historique des prix annuels par département.

### DETAILS TECHNIQUES (PYTHON)
#### 1-) Fichiers utilisés
- Le fichier `PrixCarburants_annuel_2022.xml` en format XML, converti en CSV pour l'exploitation avec Pandas. Il comprend les catégories `locations`, `code_postals`, `gas_types`, `dates`, et `prices`.
- Le fichier CSV `prix-des-carburants-en-france-flux-instantané-v2.csv`, déjà dans le format nécessaire.
- Le fichier `departements.geojson`, utilisé pour les visualisations géographiques.

#### 2-) Visualisations par département (fuel_prices.py)
Utilisation des bibliothèques Folium et Pandas pour afficher une carte de la France avec un zoom automatique sur le département choisi. Les stations sont indiquées par des "pins" affichant des informations détaillées.

#### 3-) Carte de la densité des stations services (gas_station.density.py)
Création d'une carte indiquant la densité des stations-services par département, utilisant les librairies Pandas, Geopandas, et Folium.

#### 4-) Graphique classique de prix pour chaque carburant (graph.py)
Graphique des prix des carburants au cours de l'année 2022, réalisé avec Plotly, affichant les données en fonction de la date et du prix.

#### 5-) Heatmap du prix de chaque carburant par département (heat_map.py)
Heatmaps pour les six types de carburants, affichant le prix moyen par département avec des variations de couleur.

#### 6-) Histogramme des prix des carburants (fuel_histogram.py)
Histogramme comparant les prix des six carburants, utilisant Pandas et Plotly pour l'analyse et la visualisation.

#### 7-) Le Dashboard (main.py)
Construction d'un dashboard avec Dash, Bootstrap, DCC, et HTML, présentant toutes les visualisations et informations précédemment citées.

### COMMENTAIRES SUR LES DONNÉES VISUALISÉES (PYTHON/R)

#### - PRIX DU CARBURANT PAR DÉPARTEMENT
Carte interactive affichant les stations-service par département, avec détails sur les carburants et les prix.

#### - DENSITÉ DES STATIONS SERVICES
Carte montrant la densité des stations-services par département, avec une corrélation visible avec les densités de population.

#### - PRIX DU CARBURANT AU FIL DU TEMPS
Analyse des prix des différents carburants en 2022, montrant l'impact de la guerre en Ukraine et d'autres facteurs globaux sur les prix.

#### - PRIX MOYEN DU CARBURANT PAR DÉPARTEMENT (HEATMAP)
Visualisation des prix moyens des carburants par département, avec des disparités régionales notables.

#### - HISTOGRAMME DES PRIX DES CARBURANTS
Comparaison des prix des carburants à travers un histogramme, soulignant la différence de popularité et de prix entre eux.

### CONCLUSIONS GÉNÉRALES DU PROJET
L'analyse des données sur les prix et la distribution des carburants en France révèle des tendances et modèles significatifs. L'utilisation de cartes interactives, de graphiques et d'histogrammes offre une compréhension détaillée des variations géographiques et temporelles des prix, mettant en lumière l'impact d'événements mondiaux et les disparités régionales, tout en fournissant des insights sur les habitudes de consommation et les influences socio-économiques et environnementales sur le marché des carburants en France.


## Developer Guide

### Architecture du code

Le code est organisé en plusieurs modules:

- **main.py**: Point d'entrée principal pour le tableau de bord. Il importe et utilise des fonctions des autres fichiers pour générer le tableau de bord.
- **fuel_histogram.py**: Génère un histogramme des prix du carburant.
- **fuel_prices.py**: Crée une carte montrant les prix moyens du carburant par département.
- **gas_station_density.py**: Montre la densité des stations-service.
- **graph.py**: Produit des graphiques pour diverses analyses.
- **heat_map.py**: Crée une carte thermique pour la distribution des prix du carburant.
- **xml_to_csv.py**: Convertit les données au format XML en CSV.

### Modifier ou étendre le code

1. Pour ajouter une nouvelle visualisation, créez un nouveau fichier `.py` pour cette visualisation et définissez les fonctions nécessaires.
2. Importez ces fonctions dans `main.py` et intégrez-les dans la mise en page Dash ou ajoutez des callbacks pour la mise à jour interactive.
3. Pour modifier une visualisation existante, trouvez le fichier correspondant et apportez les modifications nécessaires. Assurez-vous de tester les modifications avant de les intégrer dans le tableau de bord principal.
