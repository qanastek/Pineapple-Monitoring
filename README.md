# :pineapple: Pineapple-Monitoring

Projet d’administration système 2018 - 2019 // CERI

## Informations auteurs :

Auteurs :
* Labrak Yanis
* Vougeot Valentin

Etablissement :

Université d'Avignon - CERI

Licence 2 Informatique - Groupe 4

## Notation enseignant :

- [ ] Collecte d'information
    - [x] Créer la sonde
    - [ ] Mettre en place 3 sondes sur des VM avec CRON
- [x] Stockage & Collecte Web
    - [x] Stockage de données avec gestion d'historique
        - [x] Utilisation de standard (Json)
        - [x] Moteur de base de données (Sqlite)
    - [x] Un parseur web
    - [x] Mettre une nouvelle machine sur le réseau nécéssite aucune modification manuelle
        - [x] Auto dependencies install
        - [x] Auto install + CRON table
- [x] Affichage & Alerte
    - [x] Detection de crise
    - [x] Envoie de mail
    - [x] Module d'affichage
        - [ ] Terminale
        - [ ] Graphique rrdTools
        - [x] En ligne
    - [x] Critaires de situation de crise configurable (En ligne)
    - [x] Contenue de l'email configurable (En ligne)
    - [x] Envoie d'email par serveur SMTP Gmail    
- [x] Communication
    - [x] Module de réception (API avec flask)
    - [x] Module récupération et sauvegarde des informations (Protocole POST)
    - [x] Affiche l'historique sous forme de graphique
    - [x] Affichage web

## Topologie :

![Diagramme](./mermaid-diagram.svg)
