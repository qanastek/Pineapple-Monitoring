# TODO LIST :

- [ ] Collecte d’information (sonde) - Client side
    - [x] Renvoie en Json pour l'API
    - [x] Avec --display afficher les informations de la machine
    - [x] Marche sur Linux
    - [ ] Marche sur Windows 
    - [ ] Marche sur Mac
- [ ] Détecteur de situation de crise - Server side
    - [x] Récupère les données de la sonde
    - [x] Détecte les problèmes suivants (Cpu load, Disk usage, Swap usage, Memory usage, Connected users)
    - [x] Envoie un email en cas de crise à yanis.labrak@alumni.univ-avignon.fr
    - [ ] Module d’affichage dans le terminal des informations pour toutes les machines connues à l'aide de la librairie "TOP"
    - [x] Affiche les critères de situation de crises dans le terminale
    - [x] Les critères de situation de crise sont configurable via terminale
    - [x] Contenu de l’e-mail paramétrable
    - [x] Envoie des email via le serveur smtp de gmail
- [ ] Communication (in)  - Server side
    - [x]  Setup le serveur Flask
    - [x]  Renvoie une réponse au client si la requête vers l'API à bien fonctionné
        - [x] Si la requête est POST cela revoie un code 200
        - [x] Si la requête est autre chose que POST cela revoie un code 405
    - [ ] Vérifier que les données reçus sont complètes et bien au format JSON
        - [ ] Renvoie un code érreur si les données sont incomplètes ou éronnées 
    - [x] Traiter les données :
        - [x] Lancé le programme de détection de crise avec les données en paramètres
- [ ] Communication (out)  - Client side
    - [x] Créer un programme qui gère tout coté client (Collecte, Empaquetage et Envoie)
    - [ ] Automatisé avec CRON l'exécution de ce programe
    - [ ] Un module qui récupère et sauvegarde les informations

- [ ] Graphe
- [ ] First install send infos about the computer like the cpus cores, hostname or hardrive capacity

# TODO LIST A VAL :

- [x] Faire pineapple dans dossier d'installation
- [x] Finir le AUtoInstall.sh
