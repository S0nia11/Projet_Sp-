import streamlit as st
import os

def accueil():
    st.title('Page d\'accueil')
    st.write('Bienvenue dans notre application !')
    try:
        image_path = os.path.join(os.path.dirname(__file__), 'tennis.jpg')
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True)
        else:
            st.error(f"Image non trouvée : {image_path}")
    except Exception as e:
        st.error(f"Erreur lors du chargement de l'image : {e}")

def graphiques():
    st.title('Page des graphiques')
    st.write('Ici, vous verrez des graphiques réalisés.')
    try:
        image_path = os.path.join(os.path.dirname(__file__), 'OIP.jpg')
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True)
        else:
            st.error(f"Image non trouvée : {image_path}")
    except Exception as e:
        st.error(f"Erreur lors du chargement de l'image : {e}")

def modeles_ml():
    st.title('Page des modèles de ML')
    st.write('Ici, vous verrez les modèles réalisés et leurs résultats.')
    try:
        image_path = os.path.join(os.path.dirname(__file__), 'img.jpg')
        if os.path.exists(image_path):
            st.image(image_path, use_column_width=True)
        else:
            st.error(f"Image non trouvée : {image_path}")
    except Exception as e:
        st.error(f"Erreur lors du chargement de l'image : {e}")

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