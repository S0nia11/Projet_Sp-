import streamlit as st

def accueil():
    st.title('Page d\'accueil')
    st.write('Bienvenue dans notre application !')

def graphiques():
    st.title('Page des graphiques')
    st.write('Ici, vous verrez des graphiques sur les performances des joueurs. Les graphiques seront ajoutés ultérieurement.')

def modeles_ml():
    st.title('Page des modèles de ML')
    st.write('Ici, vous verrez les modèles de prédiction et leurs résultats. Les modèles seront ajoutés ultérieurement.')

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