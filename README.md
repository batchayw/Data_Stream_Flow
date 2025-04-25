# Data_Stream_Flow
**Construction d'une pipeline robuste, automatisé et surveillé, allant de l’ingestion des données CSV à leur visualisation en temps réel, avec une gestion efficace des erreurs et des performances.**

##### Voici les étapes détaillées de réalisation du projet, structurées selon votre liste, en français et de manière concise:

***1. Remote CSV Data***
- Configurez une tâche dans Apache Airflow pour importer des fichiers CSV depuis une source distante (via URL, API ou serveur distant).

***2. Traitement avec Pandas et Spark***
- Utilisez Pandas pour nettoyer et transformer les données (suppression des doublons, gestion des valeurs manquantes, etc.).
- Utilisez Spark pour un traitement distribué si le volume de données est important (ex: agrégation ou filtrage, etc.).

***3. Enregistrement du traitement dans un fichier CSV***
- Enregistrez les données traitées par Pandas et Spark dans un fichier CSV local ou accessible pour les étapes suivantes.

***4. Utilisation de Spark Streaming pour lire le fichier CSV traité***
- Configurez Spark Streaming 1 pour lire le fichier CSV en continu et le diffuser comme un flux de données.

***5. Utilisation de ce fichier CSV par Python pour générer les données***
- Créez un script Python (Python Data Generator) qui lit le fichier CSV et génère des données supplémentaires ou simulées (par exemple, en ajoutant des champs calculés).

***6. Publication de ces données dans un topic Kafka***
- Publiez les données générées par le script Python dans un topic Kafka spécifique via une tâche Airflow.

***7. Configuration de Kafka pour recevoir les données générées et ZooKeeper pour gérer la coordination de Kaf***ka
- Configurez un topic Kafka pour recevoir les données.
- Assurez-vous que ZooKeeper est opérationnel pour gérer la coordination et la distribution des messages dans Kafka.

***8. Utilisation de Spark Streaming pour consommer les données du topic Kafka***
- Configurez Spark Streaming 2 pour consommer les données du topic Kafka en temps réel.

***9. Stockage des données traitées dans MinIO (Configuration de MinIO pour recevoir les données de Spark Streaming 2)***
- Configurez MinIO pour stocker les données issues de Spark Streaming 2.
- Organisez les données dans MinIO (ex: par date ou type, sous forme de fichiers Parquet ou JSON).

***10. Configuration ELK pour visualiser les données en temps réel (graphiques de tendances, cartes, ou métriques)***
- Configurez Elasticsearch pour indexer les données depuis MinIO.
- Connectez Kibana à Elasticsearch et créez des visualisations (graphiques de tendances, cartes, métriques).

***11. Définition d’un DAG (Directed Acyclic Graph) qui orchestre toutes les étapes avec des dépendances entre les tâches***
- Créez un DAG dans Airflow pour orchestrer les étapes 1 à 10.
- Définissez les dépendances (ex: le traitement Pandas doit se terminer avant Spark Streaming).

***12. Configuration des intervalles de planification (toutes les heures), avec ajout des mécanismes de gestion d’erreurs (réessais)***
- Planifiez le DAG pour s’exécuter toutes les heures.
- Ajoutez des mécanismes de gestion d’erreurs dans Airflow (ex: réessayer 3 fois en cas d’échec).

***13. Test et Validation***
- Testez chaque composant individuellement (Pandas, Spark, Kafka, MinIO, ELK).
- Exécutez le DAG complet dans Airflow pour valider le pipeline de bout en bout.
- Vérifiez que les données sont correctement visualisées dans Kibana.

***14. Surveillez les performances du pipeline via les journaux d’Airflow, Kafka, et Spark***
- Consultez les journaux d’Airflow, Kafka, et Spark pour surveiller les performances et détecter les goulots d’étranglement.

***15. Configurez des alertes pour détecter les anomalies (via Airflow)***
- Configurez des alertes dans Airflow pour signaler les échecs ou anomalies (envoi d’un e-mail ou notification Slack).

