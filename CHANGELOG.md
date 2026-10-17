Historique des modifications — INTER-CYBORG.IA

Ce document retrace les évolutions notables du projet.

Les fonctionnalités annoncées comme prévues ne sont pas considérées comme implémentées tant qu'elles n'ont pas été développées et vérifiées.

[Non publié]

Documentation

- Clarification des prérequis nécessaires à l'utilisation du projet.
- Ajout des informations relatives au compte Groq et à la clé API.
- Explication de la configuration actuelle de la variable "GROK_API".
- Distinction entre Groq et Grok afin d'éviter toute confusion.
- Amélioration des instructions d'installation et d'utilisation.
- Correction de la présentation du README.
- Correction des noms de fichiers "__init__.py" dans la documentation d'architecture.
- Harmonisation des descriptions avec l'état actuel du prototype.

À améliorer

- Renforcer la gestion des erreurs réseau et HTTP.
- Améliorer la validation des réponses de l'API.
- Organiser la gestion des conversations indépendantes.
- Développer des tests automatisés complémentaires.
- Préparer progressivement l'évolution vers une architecture orientée objet.
- Harmoniser les noms des variables de configuration.
- Maintenir la documentation synchronisée avec le code.

[0.1.0] — 2026-10-16

Ajouté

- Premier prototype Python de communication avec un modèle d'intelligence artificielle.
- Fonction "choice_models()" pour envoyer des messages à un modèle sélectionné.
- Communication HTTP avec la bibliothèque "requests".
- Intégration du module d'authentification "auth/".
- Historique conversationnel temporaire utilisant les rôles "user" et "assistant".
- Récupération du contenu des réponses du modèle.
- Premiers tests consacrés à l'authentification.
- Structure initiale organisée autour des modules "auth/", "core/" et "tests/".

Modifié

- Déplacement de la fonction "choice_models()" de "ai_cors.py" vers "core/core_module.py".
- Ajout de "core/__init__.py" pour exposer "choice_models" depuis le paquet "core".
- Adaptation du test interactif dans "tests/test_choice_models.py".
- Mise à jour de l'organisation des fichiers d'authentification.

Supprimé

- Ancien fichier "ai_cors.py", remplacé par "core/core_module.py".
- Ancien test interactif "tests/test_ai_cors.py", remplacé par "tests/test_choice_models.py".

Limites connues

- L'historique conversationnel est conservé uniquement en mémoire vive.
- Les appels à la fonction partagent actuellement le même historique.
- La gestion des erreurs réseau et HTTP reste à renforcer.
- L'architecture orientée objet n'est pas encore implémentée.
- La gestion de plusieurs conversations indépendantes reste à développer.
