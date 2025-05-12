# APP_AI - Application Streamlit

Découvrez APP_AI, votre alliée intelligente deux-en-un : elle vous aide à anticiper les variations du cours de l’action Tesla et à évaluer avec fiabilité la résistance du béton à la compression. Une seule application, deux puissants leviers de décision.

---

## 🚀 Exécution locale

### 📦 Prérequis

- Python 3.8+
- pip

### 📁 Structure du projet

```
project/
├── .streamlit
├── src/
│   ├── app_streamlit.py
│   └── style.css
    └── images
    └── concrete.csv
    └── dataCC.csv
    └── modelML.pkl
    
├── requirements.txt
└── README.md
```

---

### 🔧 Installation

1. Clonez le dépôt :

```bash
git clone https://github.com/votre-utilisateur/nom-du-repo.git
cd nom-du-repo
```

2. Créez un environnement virtuel (optionnel mais recommandé) :

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Installez les dépendances :

```bash
pip install -r requirements.txt
```

---

### ▶️ Lancer l'application

Exécutez :

```bash
streamlit run src/app_streamlit.py
```

L'application s'ouvrira automatiquement dans votre navigateur à l'adresse :  
`http://localhost:8501`

---

## 🐳 Optionnel : Exécution avec Docker

### 🏗️ Construire l'image

```bash
docker build -t beton-app .
```

### ▶️ Lancer le conteneur

```bash
docker run -p 8501:8501 beton-app
```

---

## 📄 Contenu du fichier `requirements.txt`

```txt
streamlit
pandas
scikit-learn
numpy
altair
joblib
```

> Ajoutez ici toute autre bibliothèque utilisée par votre projet.

---

## 📞 Contact

Pour toute question, ouvrez une issue ou contactez-moi à `alotsechristy@gmail.com`.
