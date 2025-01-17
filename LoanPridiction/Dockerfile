# Utiliser une image python de base
FROM python:3.9-slim-buster

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier de dépendances et l'installer
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier le reste de l'application
COPY . .

# Exposer le port 80
EXPOSE 80

# Démarrer l'application
CMD ["python", "app.py"]