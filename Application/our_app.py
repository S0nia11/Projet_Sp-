import streamlit as st
import os
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string});
            background-size: cover;
        }}
        .white-text {{
            color: white;
        }}
        .content {{
            position: relative;
        }}
        .images {{
            text-align: center;
        }}
        .images img {{
            margin: 20px; /* Ajustez selon vos préférences */
            max-width: 80%; /* Ajustez selon vos préférences */
            height: auto;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def accueil():
    add_bg_from_local(os.path.join('static', 'tennis.jpg'))
    
    st.markdown("""
    <div class="content">
        <div class="left-text">
            <h1 class="white-text">Page d'accueil</h1>
            <p class="white-text">Bienvenue dans notre application de tennis !</p>
        </div>
        <div class="images">
            <img src="data:image/png;base64,{}" class="img1">
        </div>
        <div class="images">
            <img src="data:image/png;base64,{}" class="img2">
        </div>
    </div>
    """.format(
        base64.b64encode(open('static/img1.jpg', "rb").read()).decode(),
        base64.b64encode(open('static/img2.jpg', "rb").read()).decode()
    ), unsafe_allow_html=True)

def graphiques():
    add_bg_from_local(os.path.join('static', 'wt.webp'))
    st.markdown('<h1 class="white-text">Page des graphiques</h1>', unsafe_allow_html=True)
    st.markdown('<p class="white-text">Ici, vous verrez des graphiques réalisés.</p>', unsafe_allow_html=True)

def modeles_ml():
    add_bg_from_local(os.path.join('static', 'img.jpg'))
    st.markdown('<h1 class="white-text">Page des modèles de ML</h1>', unsafe_allow_html=True)
    st.markdown('<p class="white-text">Ici, vous verrez les modèles réalisés et leurs résultats.</p>', unsafe_allow_html=True)

def main():
    st.sidebar.title('Menu')
    page = st.sidebar.selectbox('Sélectionnez une page', ['Accueil', 'Graphiques', 'Modèles'])

    if page == 'Accueil':
        accueil()
    elif page == 'Graphiques':
        graphiques()
    elif page == 'Modèles':
        modeles_ml()

if __name__ == '__main__':
    main()