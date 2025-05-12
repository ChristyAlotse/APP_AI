import streamlit as st
import pandas as pd
import numpy as np
import joblib
from PIL import Image


# 🔧 CONFIG
st.set_page_config(page_title="APP_AI", layout="centered")

st.markdown(
    """
    <style>
    /* Cible le conteneur principal de Streamlit */
    .stApp {
        background: linear-gradient(-45deg, #1E1E1E, #2C2C2C, #1E1E1E, #2C2C2C);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 🎨 THEME DARK CSS LOCAL (optionnel mais recommandé)
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

local_css("style.css")
remote_css("https://fonts.googleapis.com/css2?family=Roboto&display=swap")

img1 = Image.open("images/app_ai.png")
img1 = img1.resize((300, 300))  # largeur=200px, hauteur=100px
st.sidebar.image(img1)
#st.sidebar.image("images/image_side_bar.png", width=200)

# 📷 IMAGES
image_paths = {
    "home": "images/app_ai1.png",
    "ml": "images/image_ML.png",
    "dl": "images/image_DL.png",
    "tesla_courbe" : "images/image_tesla_courbe.png"
}

# 🔢 MENU
menu = ["🏠 Accueil", "🤖 Machine Learning", "🧠 Deep Learning", "👤 À propos de moi"]
choice = st.sidebar.selectbox("Menu", menu)

# 🏠 PAGE D'ACCUEIL
if choice == "🏠 Accueil":
    img2 = Image.open(image_paths["home"])
    img2 = img2.resize((900, 400))  # largeur=200px, hauteur=100px
    st.image(img2)
    
    #st.image(image_paths["home"], width=400)
    #st.title("APP_AI")
    st.markdown('---')
    st.subheader("Bienvenue dans notre application d'Intelligence Artificielle")
    st.markdown('---')
    st.markdown("Découvrez APP_AI, votre alliée intelligente deux-en-un : elle vous aide à anticiper les variations du cours de l’action Tesla et à évaluer avec fiabilité la résistance du béton à la compression. Une seule application, deux puissants leviers de décision.")

# 🤖 PAGE MACHINE LEARNING
elif choice == "🤖 Machine Learning":
    
    img3 = Image.open(image_paths["ml"])
    img3 = img3.resize((900, 400))  # largeur=200px, hauteur=100px
    st.image(img3)
    
    st.title("Prédiction avec un modèle de ML")
    tab1,tab2 = st.tabs([":clipboard: Data",
                                  "🔮 Prediction"])
    
    with tab1:
        st.subheader("Loaded Dataset")
        data = pd.read_csv('concrete.csv')
        st.write(data)
        
    with tab2:
        st.subheader("Make a prediction")
        #st.write("Veuillez remplir chacun des champs ci dessous à fin de prédire la capacité de résistance de votre béton à l'issue d'une compression ")
    

        with st.form("Form 1"):
            st.markdown("**Veuillez remplir les champs suivants :**")
            
            col1,col2 = st.columns(2)
            cement = col1.number_input("Cement (kg/m3)", min_value=0.0)
            slag = col2.number_input("Blast Furnace Slag (kg/m3)", min_value=0.0)
            col3,col4 = st.columns(2)
            ash = col3.number_input("Fly Ash (kg/m3)", min_value=0.0)
            water = col4.number_input("Water (kg/m3)", min_value=0.0)
            col5,col6 = st.columns(2)
            superplastic = col5.number_input("Superplasticizer (kg/m3)", min_value=0.0)
            coarseagg = col6.number_input("Coarse Aggregate (kg/m3)", min_value=0.0)
            col7,col8 = st.columns(2)
            fineagg = col7.number_input("Fine Aggregate (kg/m3)", min_value=0.0)
            age = col8.number_input("Age (jours)", min_value=0.0)
                
            st_state = st.form_submit_button("📊 Prédire la résistance du béton")

            if st_state:
                if not all([cement, slag, ash, water, superplastic, coarseagg, fineagg, age]):
                    st.warning("Merci de remplir tous les champs.")
                else:
                    model = joblib.load(open("modelML.pkl", "rb"))  
                    df = pd.DataFrame({'cement': [cement],
                                       'slag': [slag],
                                       'ash': [ash],
                                       'water': [water],
                                       'superplastic': [superplastic],
                                       'coarseagg': [coarseagg],
                                       'fineagg': [fineagg],
                                       'age': [age]})
                    prediction = model.predict(df)
                    st.success(f"Résistance prédite : **{prediction[0]:.2f} MPa**")

# 🧠 PAGE DEEP LEARNING
elif choice == "🧠 Deep Learning":

    img = Image.open("images/image_dl.png")
    img = img.resize((1000, 500))  # largeur=200px, hauteur=100px
    st.image(img)
    st.title("Deep Learning")
    #st.info("La fonctionnalité Deep Learning arrive bientôt...")
    tab1, tab2, tab3 = st.tabs([
        "📈 Visualisation", 
        "🧠 Performances & Métriques", 
        "🔮 Prédictions"
    ])
    
    with tab1:
        st.markdown("### 📊 Données des trois dernières années")
        df = pd.read_csv("dataCC.csv")
        st.dataframe(df, use_container_width=True)
        
        st.markdown("### 📉 Cours de l'action Tesla")
        st.image(image_paths["tesla_courbe"], use_column_width=True)

    with tab2:
        st.markdown("### ⚙️ Performances du modèle")
        st.image("images/loss1.png", caption="Courbe de perte", use_column_width=True)

        st.markdown("---")
        st.markdown("### 📐 Métriques du modèle")
        col1, col2 = st.columns(2)
        col1.metric("🔹 MSE", "16.7222")
        col2.metric("🔹 MAE", "12.6825")
        
        col3, col4 = st.columns(2)
        col3.metric("🔹 R² Score", "0.9462")

        st.markdown("---")
        st.markdown("### 🆚 Valeurs Réelles vs Prédites")
        st.image("images/valeurs reels vs predit1.png", use_column_width=True)

        st.markdown("### 📊 Distribution des erreurs")
        st.image("images/erreur1.png", use_column_width=True)

    with tab3:
        st.markdown("### 🔮 Prédictions : Deux Semaines dans le Futur")
        st.image("images/pred_proch_semaines1.png", use_column_width=True)

# 👤 À PROPOS
elif choice == "👤 À propos de moi":
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("images/me.jpg")
    with col2:
        st.subheader("ALOTSE Christy")
        st.text("Data Scientist")
        st.write("Spécialisée dans le traitement, l’analyse et la visualisation des données, ainsi que dans la conception, l’optimisation et le déploiement de modèles de machine learning, tout en gardant un ancrage solide dans le cœur de métier.")
    
    st.markdown("💼 [LinkedIn](https://www.linkedin.com/in/christy-alotse)")
    st.markdown("📧 [Me contacter](mailto:marinaparker223@gmail.com)")
