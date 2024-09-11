import streamlit as st
import pickle

# Charger le modèle de traduction dyula-français à partir du fichier .pkl
try:
    with open('dyula_french_model.pkl', 'rb') as f:
        pipe = pickle.load(f)
except Exception as e:
    st.error(f"Erreur lors du chargement du modèle : {e}")

# Ajouter du CSS personnalisé
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

        body {
            background-color: #f0f8ff;
            color: #333;
            font-family: 'Poppins', sans-serif;
            text-align: center;
            margin: 0;
            padding: 0;
        }

        .title {
            color: #4CAF50;
            font-size: 3em;
            margin: 20px 0;
            font-weight: 600;
            background-color: #ffffff;
            border-radius: 10px;
            padding: 10px 20px;
            display: inline-block;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }

        textarea {
            width: 70% !important;
            margin: 30px auto !important;
            padding: 15px !important;
            border-radius: 10px !important;
            border: 2px solid #4CAF50 !important;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1) !important;
            font-size: 1.1em !important;
        }

        .button {
            background-color: #4CAF50;
            color: white;
            padding: 15px 30px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 1.2em;
            margin-top: 20px;
            transition: background-color 0.3s, transform 0.2s;
        }

        .button:hover {
            background-color: #45a049;
            transform: scale(1.05);
        }

        .footer {
            margin-top: 50px;
            color: #777;
            font-size: 1em;
        }

        .footer a {
            color: #4CAF50;
            text-decoration: none;
        }

        .footer a:hover {
            text-decoration: underline;
        }

    </style>
""", unsafe_allow_html=True)

# Titre de l'application
st.markdown('<h1 class="title">Traduction Dyula - Français</h1>', unsafe_allow_html=True)

# Champ de texte pour l'entrée utilisateur
input_text = st.text_area("Entrez du texte en Dyula :", "", key="input_text", 
    help="Saisissez ici le texte en Dyula que vous souhaitez traduire.", 
    placeholder="Ecrivez ici...", 
    height=150)

# Bouton pour lancer la traduction
if st.button("Traduire", key="translate_button"):
    if input_text:
        try:
            # Traduire le texte en utilisant le modèle chargé depuis le fichier .pkl
            translations = pipe(input_text)
            # Afficher la traduction
            st.write("**Traduction en Français :**")
            st.write(f"<div style='font-size: 1.5em; color: #333;'>{translations[0]['generated_text']}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Erreur lors de la traduction : {e}")
    else:
        st.error("Veuillez entrer du texte en Dyula pour la traduction.")

# Pied de page
st.markdown('<div class="footer">Développé avec ❤️ par Groupe4. Pour en savoir plus, visitez <a href="https://github.com/SySamba/NLP.git" target="_blank">notre projet GitHub</a>.</div>', unsafe_allow_html=True)
