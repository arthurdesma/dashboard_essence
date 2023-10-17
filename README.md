
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

Le tableau de bord fournit une analyse complète des prix du carburant en France. Voici quelques conclusions clés:

- Les prix du carburant varient considérablement d'un département à l'autre.
- Certains types de carburant, comme le diesel, peuvent avoir des prix plus stables, tandis que d'autres, comme l'essence, peuvent varier davantage.
- La densité des stations-service dans une région donnée peut influencer les prix du carburant.
- D'autres analyses et visualisations détaillées sont disponibles dans le tableau de bord lui-même.

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
