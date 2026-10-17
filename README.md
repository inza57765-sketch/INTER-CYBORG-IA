<div align="center">  <img src="icon.png" alt="Logo INTER-CYBORG.IA" width="180">  <h1>INTER-CYBORG.IA</h1>  <p><strong>Un assistant d'intelligence artificielle modulaire et évolutif.</strong></p>  <p>Un projet expérimental en Python consacré à la communication avec des modèles d'intelligence artificielle et à la gestion des conversations.</p></div>---

Présentation

INTER-CYBORG.IA est un projet expérimental développé en Python. Son objectif est de construire progressivement un assistant d'intelligence artificielle organisé en modules indépendants.

Le prototype actuel permet d'envoyer des messages à un modèle d'intelligence artificielle via l'API Groq, de préparer l'authentification nécessaire et de conserver temporairement l'historique des échanges pendant l'exécution du programme.

Le projet est toujours en développement. Certaines fonctionnalités sont opérationnelles dans le prototype, tandis que d'autres restent à améliorer ou à concevoir.

⚠️ Prérequis

Avant d'utiliser INTER-CYBORG.IA, vous devez disposer des éléments suivants :

- Python : pour exécuter le programme.
- Un compte Groq : pour accéder à la plateforme.
- Une clé API Groq valide : pour authentifier les requêtes.
- Une connexion Internet : pour communiquer avec l'API.
- Un modèle accessible sur Groq : le modèle choisi doit être disponible pour votre compte.

«Attention : Groq et Grok sont deux services différents. INTER-CYBORG.IA utilise actuellement l'API de Groq, et non celle de Grok développé par xAI.»

🔑 Obtenir une clé API Groq

Si vous ne possédez pas encore de clé API :

1. Rendez-vous sur la "console officielle de Groq" (https://console.groq.com/).
2. Créez un compte ou connectez-vous.
3. Accédez à la section de gestion des clés API.
4. Créez une clé API et conservez-la dans un endroit sécurisé.
5. Configurez cette clé dans le fichier ".env", comme expliqué dans la section suivante.

La disponibilité des modèles, les quotas et les conditions d'utilisation dépendent du service Groq et de votre compte.

Sécurité : ne publiez jamais votre clé API sur GitHub et ne la partagez pas.

Installation

1. Récupérer le projet

Depuis un terminal, exécutez :

git clone https://github.com/inza57765-sketch/INTER-CYBORG-IA.git
cd INTER-CYBORG-IA

2. Installer les dépendances

Installez les bibliothèques Python nécessaires :

python -m pip install -r requirements.txt

3. Configurer la clé API

Le projet recherche actuellement la clé API dans une variable d'environnement nommée "GROK_API", chargée depuis le fichier ".env" par "python-dotenv".

À la racine du projet, créez un fichier nommé ".env" contenant :

GROK_API=votre_cle_api_groq

Remplacez "votre_cle_api_groq" par votre véritable clé API Groq.

Ne mettez jamais votre véritable clé dans le code source, le README ou un dépôt public.

Le fichier ".env" doit rester ignoré par Git. Vérifiez également que votre clé n'a pas été ajoutée à l'historique du dépôt.

«Remarque technique : le nom actuel "GROK_API" est conservé pour rester compatible avec le code existant. Il s'agit bien ici d'une clé API Groq. Une harmonisation du nom de cette variable pourra être envisagée ultérieurement.»

Utilisation

Le paquet "core" expose actuellement la fonction "choice_models()".

Exemple :

from core import choice_models

response = choice_models(
    model="openai/gpt-oss-120b",
    user_message="Salut !"
)

print(response)

Cet exemple suppose que :

- les dépendances sont installées ;
- la clé API Groq est correctement configurée ;
- le modèle choisi est disponible ;
- la connexion Internet fonctionne.

Le modèle utilisé dans cet exemple est un identifiant de modèle configuré pour l'API Groq. Vérifiez sa disponibilité dans la documentation officielle de Groq avant de l'utiliser.

Lancer le test conversationnel

Pour démarrer l'interface interactive actuelle dans le terminal :

python -m tests.test_choice_models

Vous pourrez saisir plusieurs messages successifs et consulter les réponses du modèle.

Pour quitter, utilisez "Ctrl+C" dans un terminal qui prend en charge ce raccourci.

Ce programme est un test interactif du prototype, et non encore une application complète destinée au grand public.

Fonctionnalités actuelles

Fonctionnalité| État
Communication avec l'API Groq| Prototype implémenté
Sélection du modèle| Implémentation initiale
Authentification par clé API| Présente dans le code
Historique conversationnel temporaire| Implémenté dans le moteur actuel
Organisation en modules Python| En place
Gestion complète des erreurs réseau et HTTP| À améliorer
Conversations indépendantes| À développer
Mémoire persistante| Non implémentée
Architecture orientée objet| Envisagée

Cette liste décrit l'état du prototype et ne constitue pas une garantie de fonctionnement dans tous les environnements.

Organisation du projet

INTER-CYBORG.IA/
├── auth/
│   ├── __init__.py
│   ├── headers_auth.py
│   └── token_auth.py
├── core/
│   ├── __init__.py
│   ├── core_module.py
│   └── animations/
├── tests/
│   ├── __init__.py
│   ├── test_choice_models.py
│   ├── test_token_verif_import.py
│   └── test_token_verif_result.py
├── __init__.py
├── CHANGELOG.md
├── description.txt
├── icon.png
├── requirements.txt
└── README.md

Cette arborescence présente les principaux fichiers suivis par Git. Les fichiers personnels et les fichiers de configuration secrets ignorés par Git ne sont pas inclus.

Rôle des principaux modules

- "auth/" : regroupe les éléments liés à l'authentification et à la préparation des requêtes.
- "auth/token_auth.py" : charge la configuration et recherche la clé API dans l'environnement.
- "auth/headers_auth.py" : prépare les en-têtes HTTP d'authentification.
- "core/core_module.py" : contient la fonction "choice_models()", qui prépare et envoie les requêtes au modèle.
- "core/__init__.py" : expose "choice_models" pour faciliter son import.
- "tests/" : contient les tests du projet.
- "requirements.txt" : répertorie les dépendances Python.

Sécurité et limites

- La clé API doit rester confidentielle.
- Le fichier ".env" ne doit pas être publié.
- La fonction actuelle de vérification contrôle essentiellement la présence de la clé ; elle ne garantit pas que celle-ci est valide ou que le service est accessible.
- La gestion des erreurs réseau, HTTP et JSON doit être renforcée.
- L'historique conversationnel est partagé par les appels effectués dans le même processus Python.
- L'historique est perdu à l'arrêt du programme.
- Aucune mémoire persistante n'est actuellement implémentée.
- L'accès aux modèles et leurs limites dépendent du service Groq.

Feuille de route

- [ ] Renforcer la gestion des erreurs réseau et HTTP.
- [ ] Améliorer la validation des réponses de l'API.
- [ ] Organiser les historiques conversationnels.
- [ ] Préparer la gestion de plusieurs conversations indépendantes.
- [ ] Développer des tests automatisés complémentaires.
- [ ] Étudier progressivement le passage à une architecture orientée objet.
- [ ] Harmoniser les noms des variables de configuration.
- [ ] Maintenir la documentation à jour.

Contributions

Les suggestions, signalements de problèmes et propositions d'amélioration sont les bienvenus.

Toute contribution devrait préserver la cohérence entre le code, les tests et la documentation.

Auteur

CYBER TchaK

Développement indépendant autour de Python et de l'intelligence artificielle.

Licence

La licence du projet reste à définir.
