
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
Nous décidons d’afficher en premier lieu d’afficher une carte de la France qui zoome automatiquement avec le département choisi. Nous avons utilisé la bibliothèque folium ainsi que la bibliothèque pandas pour exploiter les données du fichier csv. Sur la carte, nous avons des “pins” avec la localisation des différentes stations, et les informations telles que l’adresse postale, la ville,  les carburants disponibles ainsi que leur prix et enfin la date de dernière mise à jour. 


#### 3-) Carte de la densité des stations services (gas_station.density.py)
Ici, afin d’afficher la carte des densités des stations services par rapport aux départements. Nous utilisons les librairies python pandas, pour la lecture du fichier csv pour le nombre de stations services, geopandas pour lire et exploiter les données du fichier geojson pour les informations sur les départements et enfin folium pour la carte et la personnalisation de l’affichage pour la visualisation. Nous rentrons les coordonnées de la France afin que la carte s’y affiche par défaut. La carte affiche les différents départements français et plus la densité est élevée, plus la 
couleur verte devient foncée. 

#### 4-) Graphique classique de prix pour chaque carburant (graph.py)
Pour visualiser le prix de chaque carburant individuellement, nous créons un graphique avec en abscisse la date de janvier à décembre 2022 et en ordonnée le prix en euro. Nous utilisons la librairie python plotly. On a une barre de sélection afin de choisir le carburant qui nous intéresse. Ici, le graphique n’a pas été compliqué à réaliser mais a une utilité extrêmement importante. 

#### 5-) Heatmap du prix de chaque carburant par département (heat_map.py)
Nous avons ici affiché côte à côte les six carburants avec la heatmap de leur prix par département. Les couleurs vont du jaune au rouge en fonction du prix. Bien évidemment, le choix de ces couleurs a été effectué pour représenter une métaphore de la carte de la météo. Pour ce faire, nous utilisons les librairies pandas, geopandas et folium, comme expliqué précédemment pour la carte de la densité des stations services. Nous mettons les coordonnées de la France avec un zoom à 5 pour directement afficher le territoire français entier. Malheureusement, l’incrément du zoom n’étant pas très précis, nous voyons également en partie les autres pays limitrophes. Bien sûr, seule la France est prise en compte donc cela n’altère pas la 

#### 6-) Histogramme des prix des carburants (fuel_histogram.py)
Après avoir affiché les précédentes façons de visualiser les relations entre les carburants et les stations services avec pour facteurs le prix, la localisation ou encore la date, l’heure est venue de réaliser un histogramme qui compare ces six carburants. Ici, nous allons analyser les données avec pour abscisse le prix (‘Price’) et pour l’ordonnée le nombre d’observations (‘Frequency’) pour chaque tarif (le nombre de stations service qui pratiquent ce prix). Nous avons fait appel aux librairies Pandas et Plotly. En lisant le fichier csv avec Pandas, nous récupérons les données relatives aux carburants puis avec Plotly nous traçons l’histogramme en précisant les axes. 

#### 7-) Le Dashboard (main.py)
Enfin, nous allons parler de notre programme “main.py”. Notre but est de créer un dashboard avec affiché dessus toutes les informations et graphiques citées précédemment. Pour créer un dashboard, nous utilisons bien entendu la librairie dash, avec également les extensions bootstrap, dcc et l’html pour construire cette page. On utilise également pandas pour charger les données des deux documents en format csv. Nous importons les six programmes dont les cinq sur les graphiques ainsi que  le dernier qui lui sert à convertir les fichiers xml en csv. Nous utilisons les fonctions propres à Dash pour créer et personnaliser le layout de la page, à partir de “Row” et de “Card”. L’utilisation ici du html est nécessaire pour les textes. Le bootstrap permet d’utiliser un thème. Une fois le code “main.py” éxécuté, un lien web s’affiche sur le TERMINAL. Sur VsCode, si l’on passe le curseur de la souris dessus, il suffit de cliquer sur “Follow Link” pour que le Dashboard s’affiche dans le navigateur. La page peut être rechargée et il est possible de naviguer en utilisant le scroll de la souris ainsi que la barre verticale située à droite de la page. De plus, chaque carte peut être zoomée ou dézoomée manuellement selon nos envies. Enfin, les menus déroulants sont fait pour que l’on puisse sélectionner soit le département soit le carburant en fonction du graphique ou de la carte, avec la possibilité de cliquer sur n’importe quelle station service pour la première carte. Un rafraichissement de la page permet de réinitialiser les choix effectués. 

### COMMENTAIRES SUR LES DONNÉES VISUALISÉES (PYTHON/R)

#### - PRIX DU CARBURANT PAR DÉPARTEMENT
Tout d'abord, nous avons une carte interactive ainsi qu'une barre de choix afin de choisir le département souhaité. Une fois le département déterminé, la carte affichera alors chaque station service recensée avec un "pin" sur leur localisation exacte. Si on clique sur l'une d'entre elle, nous pouvons voir l'adresse (ex 20 route de Cannes), la ville (ex Opio), les carburants disponibles (ex Gazole/SP95/E85/SP98), le prix (ex 2.11 €/L de Gazole), avec la date de dernière mise à jour. 

#### - DENSITÉ DES STATIONS SERVICES
Nous avons une carte de la densité des stations services par département en France. L'intensité de la couleur varie en fonction de la densité de station service par département, allant de 19(le plus clair) à 280(le plus foncé). Nous pouvons voir que, sans surprise, les départements les plus foncés ont donc le plus grand nombre de stations services. Si l'on compare cette carte à la carte des densités de population en France, on distingue les mêmes tendances, avec en prime la fameuse "diagonale du vide" qui est facile à deviner. Les départements ayant la plus grande concentration de stations services sont : Nord/Pas-de-Calais/Gironde/Haute-Garonne/Bouches-du-Rhône/Rhône/Seine-et-Marne. 

#### - PRIX DU CARBURANT AU FIL DU TEMPS
Afin de mieux visualiser les données de prix, nous avons décidé d'afficher la courbe de prix du carburant tout au long de l'année 2022, avec la date en abscisse et les prix en ordonnée. Les carburants répertoriés sont : E10/E85/GPLC/GAZOLE/SP95/SP98. Malgré les spécificités de chaque carburant et les différents véhicules qui les utilisent, nous remarquons que les courbes de prix, bien qu'ayant des tarifs différents, ont plus ou moins les mêmes allures :
une hausse très forte aux alentours de mars 2022 pour tous les carburants, avec parfois un extremum local. Cela peut-être corrélé avec la guerre entre l'Ukraine et la Russie. En effet, à cette époque, nous avions bel et bien constaté que le prix des carburants avait fortement augmenté peu après cet évènement. Il y a aussi une forte baisse des tarifs aux alentours de septembre 2022, créant un minimum local. Cela s'applique également pour tous les carburants. Enfin, il y a une forte hausse des prix aux alentours de juillet pour certains carburants tels que l'E10, le Gazole, le SP95, le SP98. Concernant l'E85, il y a également une légère tendance de hausse mais elle est bien moins marquée et le phénomène dure plus longtemps, de juillet à septembre 2022.

#### - PRIX MOYEN DU CARBURANT PAR DÉPARTEMENT (HEATMAP)
Pour les 6 différents types de carburants nous avons décidé de créer des cartes interactives avec le prix moyen de chaque carburant par département. Plus la couleur est foncée, plus le tarif est élevé. Nous constatons que pour chaque carburant, les tendances sont différentes : pour le SP95, le SP98 et le Gazole, les prix sont homogènes dans la plupart des départements, surtout concernant le SP95. Néanmoins, pour le E10, et E85 ainsi que le GPLC les tarifs sont assez hétérogènes. Une tendance se dessine cependant : ces carburants sont moins chers dans les départements à l'ouest de la France. 

#### - HISTOGRAMME DES PRIX DES CARBURANTS
Nous voulons à présent comparer les prix des différents carburants et la meilleure façon d’obtenir la meilleure visualisation est de tous les représenter en même temps. C’est pour cela que nous avons utilisé un histogramme. Tout d’abord, nous voyons que 2 carburants ont un prix au litre bien inférieur aux 4 autres. Ce sont l’E85 et le GPLC. Nous pouvons constater que l’E85 est bien plus fréquent que le GPLC (plus de 2000 observations contre quelques centaines. Les 4 autres carburants ont un prix au litre situé entre 1,9 et 2,1 euro au litre. Les carburants les plus utilisés sont de loin le SP98 et le Gazole. L’E10, le SP95 et l’E10 sont bien moins populaires. 

### CONCLUSIONS GÉNÉRALES DU PROJET
La visualisation et l'analyse des données relatives aux prix et à la distribution des carburants en France révèlent des tendances et des modèles significatifs. L'utilisation de cartes interactives pour examiner les prix du carburant par département et la densité des stations-service fournit une compréhension détaillée de la distribution géographique et des variations de prix. Les tendances des prix du carburant au fil du temps en 2022 démontrent l'impact d'événements mondiaux tels que la guerre en Ukraine, avec des hausses et baisses notables. La comparaison des prix moyens des différents carburants à travers des heatmaps illustre des disparités régionales, tandis que l'analyse des histogrammes met en évidence la variabilité des prix et la popularité relative des différents types de carburants. Ces observations fournissent des insights précieux non seulement sur les habitudes de consommation de carburant, mais aussi sur les facteurs socio-économiques et environnementaux qui influencent le marché du carburant en France.


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
