<div align="center">
  <img src="icon.png" alt="Logo INTER-CYBORG.IA" width="180">  <h1>INTER-CYBORG.IA</h1>  <p><strong>Un assistant d'intelligence artificielle modulaire et évolutif.</strong></p>
</div>---

Présentation

INTER-CYBORG.IA est un projet expérimental développé en Python. Son objectif est de construire une architecture modulaire capable de communiquer avec des modèles d'intelligence artificielle, de gérer l'authentification et de traiter les conversations.

Le projet évoluera progressivement vers un moteur central chargé de coordonner ses différents composants.

Objectifs

- Organiser la communication avec différents modèles d'intelligence artificielle.
- Séparer la gestion de l'authentification.
- Centraliser la logique du projet dans un moteur appelé "core".
- Conserver l'historique des conversations.
- Faciliter l'ajout de nouvelles fonctionnalités.
- Améliorer la fiabilité grâce aux tests automatisés.

État du développement

Fonctionnalité| État
Communication avec une API d'IA| Prototype fonctionnel
Sélection du modèle| Implémentation initiale
Authentification séparée| Structure initiale
Historique conversationnel| Implémentation initiale
Moteur central "core"| En développement
Gestion des erreurs| À améliorer
Conversations indépendantes| À développer

Le projet est encore expérimental. Certaines fonctionnalités restent à développer et l'architecture peut évoluer.

Technologies

- Python : langage principal.
- Requests : communication HTTP avec l'API.
- Git : gestion des versions.
- API d'intelligence artificielle : accès aux modèles.

Organisation du projet

INTER-CYBORG.IA/
├── auth/
│   ├── __init__.py
│   ├── headers_auth.py
│   └── token_auth.py
├── core/
│   └── animations/
├── tests/
│   ├── __init__.py
│   ├── test_ai_cors.py
│   ├── test_token_verif_import.py
│   └── test_token_verif_result.py
├── ai_cors.py
├── description.txt
├── requirements.txt
├── CHANGELOG.md
└── README.md

Cette arborescence présente les principaux éléments du projet et pourra être mise à jour au fil du développement.

Installation

1. Récupérer le projet

git clone https://github.com/inza57765-sketch/INTER-CYBORG-IA.git
cd INTER-CYBORG-IA

2. Installer les dépendances

pip install -r requirements.txt

3. Configurer l'authentification

Configure les informations d'authentification requises avant d'utiliser les fonctionnalités qui communiquent avec l'API.

Sécurité : ne publie jamais tes jetons d'API, tes mots de passe ou tes fichiers contenant des secrets.

Tests

Le dossier "tests/" contient des tests destinés à vérifier certains composants du projet.

Pour lancer le test du prototype :

python -m tests.test_ai_cors

Ce test peut nécessiter une authentification valide et une connexion à l'API.

Feuille de route

- [ ] Développer le moteur central "core_module".
- [ ] Séparer la sélection des modèles de la communication HTTP.
- [ ] Améliorer la gestion des erreurs.
- [ ] Organiser la mémoire conversationnelle.
- [ ] Renforcer les tests automatisés.
- [ ] Documenter le projet pour les futurs contributeurs.

Contributions

Les suggestions, signalements de problèmes et propositions d'amélioration sont les bienvenus.

Le projet étant expérimental, toute contribution devrait tenir compte de son architecture actuelle et de son évolution.

Auteur

CYBER TchaK

Développement indépendant autour de Python et de l'intelligence artificielle.

Licence

La licence du projet reste à définir. Avant toute réutilisation ou redistribution du code, renseigne-toi sur les conditions applicables.

---

<div align="center">
  <p><strong>INTER-CYBORG.IA</strong></p>
  <p>L'IA au service de vos idées.</p>
</div>
