# Utiliser une image Python de base
FROM python:3.9-slim-buster

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier de dépendances
COPY requirements.txt .

# Installer les dépendances (avec pip)
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY LoanPridiction/ .

# Exposer le port 80
EXPOSE 80

# Commande pour démarrer l'application Flask
CMD ["python3", "app.py"]