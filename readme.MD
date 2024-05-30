# Application CRUD FastAPI

Ce projet est une application web simple utilisant FastAPI pour gérer des opérations CRUD (Create, Read, Update, Delete) sur des éléments (items) et des catégories.

## Prérequis

- Python 3.7+
- [Virtualenv](https://virtualenv.pypa.io/en/latest/)

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo
   ```

2. Créez et activez un environnement virtuel :

   - Sous Linux/MacOS :

     ```bash
     python -m venv env
     source env/bin/activate
     ```

   - Sous Windows :

     ```bash
     python -m venv env
     .\env\Scripts\activate
     ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Démarrez l'application :

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```


## Fonctionnalités

- **CRUD pour les Items :**
  - Créer un item
  - Lire les items (avec pagination)
  - Mettre à jour un item
  - Supprimer un item

- **CRUD pour les Catégories :**
  - Créer une catégorie
  - Lire les catégories (avec pagination)
  - Lire une catégorie spécifique

## Endpoints de l'API

### Items

- **POST** `/items/` : Créer un nouvel item
- **GET** `/items/` : Obtenir la liste des items
- **GET** `/items/{item_id}/` : Obtenir un item par ID
- **PUT** `/items/{item_id}/` : Mettre à jour un item par ID
- **DELETE** `/items/{item_id}/` : Supprimer un item par ID

### Catégories

- **POST** `/categories/` : Créer une nouvelle catégorie
- **GET** `/categories/` : Obtenir la liste des catégories
- **GET** `/categories/{category_id}/` : Obtenir une catégorie par ID

## Peuplement de la Base de Données

À l'initialisation, la base de données est peuplée avec des catégories et des items de base. Vous pouvez modifier le fichier `populate_db.py` pour ajouter ou modifier les données initiales.


## Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
