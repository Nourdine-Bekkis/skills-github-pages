
# SupportBotGPT

Bot d'assistance informatique pour Microsoft Teams et Web, avec création automatique de tickets via GLPI.

## Lancement local

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Déploiement
- Azure App Service (Python 3.10+)
- Ajouter les variables d'environnement depuis `.env`

## Intégration Teams
1. Utiliser `teams-package/manifest.json`
2. Remplacer les ID et URL dans le manifeste
3. Importer le `.zip` dans le [Developer Portal Teams](https://dev.teams.microsoft.com/)

## Web
- Intégrable en iframe ou via un frontend custom appelant `/api/messages`
