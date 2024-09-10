import streamlit as st
from transformers import pipeline

# Charger le pipeline pour la traduction dyula-français
pipe = pipeline("text2text-generation", model="Kimmy7/dyula-french-model")

# Ajouter du CSS personnalisé
st.markdown("""
    <style>
        body {
            background-color: #e8f4f8;
            color: #333;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            text-align: center;
            padding: 0;
            margin: 0;
        }
        .title {
            color: #008CBA;
            font-size: 2.5em;
            margin: 20px 0;
            font-weight: bold;
            display: inline-block;
            padding: 10px;
            border: 4px solid #008CBA; /* Couleur de la bordure */
            border-radius: 8px; /* Bordure arrondie */
            background-color: #f9f9f9; /* Couleur de fond pour le titre */
        }
        .text-area {
            width: 80%;
            margin: auto;
            padding: 15px;
            border-radius: 10px;
            border: 2px solid #008CBA;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            font-size: 1.2em;
            resize: vertical;
            margin-top: 40px; /* Augmenter l'espace au-dessus du champ de texte */
        }
        .button {
            background-color: #008CBA;
            color: white;
            padding: 12px 24px;
            border: none;
            border-radius: 10px;
            cursor: pointer;
            font-size: 1.2em;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: background-color 0.3s, transform 0.2s;
            margin-top: 20px;
        }
        .button:hover {
            background-color: #005f6a;
            transform: scale(1.05);
        }
        .footer {
            margin-top: 40px;
            padding: 20px;
            color: #555;
            font-size: 1em;
            border-top: 1px solid #ccc;
        }
        .footer a {
            color: #008CBA;
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
input_text = st.text_area("Entrez du texte en Dyula :", "", key="input_text", help="Saisissez ici le texte en Dyula que vous souhaitez traduire.", placeholder="Ecrivez ici...", 
    height=150)

# Bouton pour lancer la traduction
if st.button("Traduire", key="translate_button", help="Cliquez ici pour traduire le texte"):
    if input_text:
        # Traduire le texte
        translations = pipe(input_text)
        # Afficher la traduction
        st.write("**Traduction en Français :**")
        st.write(f"<div style='font-size: 1.5em; color: #333;'>{translations[0]['generated_text']}</div>", unsafe_allow_html=True)
    else:
        st.error("Veuillez entrer du texte en Dyula pour la traduction.")

# Pied de page
st.markdown('<div class="footer">Développé avec ❤️ par Groupe4. Pour en savoir plus, visitez <a href="https://github.com/SySamba/NLP.git" target="_blank">notre projet GitHub</a>.</div>', unsafe_allow_html=True)
