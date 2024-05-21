import streamlit as st
import os
import base64
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string});
            background-size: cover;
            color: white;
        }}
        .content {{
            position: relative;
            color: white;
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
        <div class="images">
            <img src="data:image/png;base64,{}" class="photo-act">
        </div>
    </div>
    """.format(
        base64.b64encode(open('static/img1.jpg', "rb").read()).decode(),
        base64.b64encode(open('static/img2.jpg', "rb").read()).decode(),
        base64.b64encode(open('static/photo_act.jpg', "rb").read()).decode()
    ), unsafe_allow_html=True)

def graphiques():
    add_bg_from_local(os.path.join('static', 'wt.webp'))
    st.markdown('<h1 class="white-text">Tennis : Data Storytelling</h1>', unsafe_allow_html=True)
    
    # Intro
    st.header("Introduction")
    st.subheader("1. Histoire")
    st.markdown("""
    Le tennis, descendant du jeu de paume français du 11e siècle, impliquait de frapper une balle avec la paume de main pour la faire rebondir contre les murs et les pans inclinés. Au 19e siècle, en Angleterre, le tennis moderne a pris son essor grâce au All England Croquet Club, qui a ouvert ses terrains de croquet à ce nouveau sport. Cette décision a marqué le début de la popularité du sport. Depuis, de nombreuses fédérations nationales ont été créées dans le monde entier afin de régir ce sport en pleine expansion.
    """, unsafe_allow_html=True)

    st.subheader("2. Jeux Olympiques 2024")
    st.markdown("""
    Aux JO, le tennis présente des épreuves masculines et féminines de simple et de double, ainsi qu'une épreuve de double mixte. Les matchs individuels pour hommes et femmes se jouent au meilleur des trois sets, avec l'introduction d'un tie-break dans le set décisif de chaque discipline. Cependant, dans le double mixte, en cas d'égalité à un set partout, un super tie-break est disputé pour départager les joueurs.
    """, unsafe_allow_html=True)
    
    st.subheader("3. Mots clés")
    st.markdown("""
    - épreuve simple/double/double mixte : Les joueurs se s’affrontent en tête-à-tête/deux équipes de deux s’affrontent/deux équipes composées d’un homme et d’une femme.  
    - Hard/Clay/Grass/Carpet court : Terrain dur, en terre battue, de gazon, en moquette.
    - GOAT : Greatest of All Time, soit le plus grand de tous les temps.
    - Set : Série de jeux disputés, le premier qui atteint un certain nombre de jeux remporte le set.
    - Rank, Seed : Classement.
    - Runner-up : Finaliste.
    - Major : Les quatres tournoi du Grand Chelem: L’Open Australie, France, Wimbledon(London) et les US.
    - Aces : Des services qui ne sont pas retournés par l'adversaire et qui permettent au serveur de marquer directement un point.
    """, unsafe_allow_html=True)
    
    # Problématique
    st.header("Problématiques")
    st.markdown("""
    1. Les facteurs influençant les performances des joueurs (physiques,...)
    2. Les facteurs causant des blessures aux joueurs
    """, unsafe_allow_html=True)
    
    # Objectifs
    st.header("Objectifs")
    st.markdown("""
    - Optimisation des performances des joueurs aux Jeux Olympiques 2024.
    - Prédiction des blessures.
    """, unsafe_allow_html=True)
    
    # Plan 
    st.header("Plan suivi")
    st.subheader("Collecte des données")
    st.markdown("""
    **1.1 Données collectées :**
    - Tournois : Année, Champions, Finalistes, Scores, Points, Classements, Surface.
    - Joueurs : Nom, Âge, Pays, Taille, Poids, Main Utilisée.
    - Terrains : Nom, Adresse, Ville, Surface, Latitude, Longitude, Lumière, Couvert.
    - Équipements : Nom Complexe, Type, Utilisation, Utilisateurs, Année de mise en service, Type d’énergie utilisée.
    - Blessures : Nom, Type, Endroit du corps, Cause, Surface, Traitement.
    
    **1.2 Moyens utilisés :**
    - Open data, Scrapping, OpenStreetMap (données cartographiques)
    """, unsafe_allow_html=True)
    
    st.image('static/eq.png', use_column_width=True)
    
    # Analyse des données
    st.header("3. Analyse des données")
    
    
    st.markdown("""
    1. Les evolutions :
    """)
    st.image('static/tournois_temps.png', use_column_width=True)
    st.image('static/Tournois_surfaces.png', use_column_width=True)
    st.image('static/classement_HFF.png', use_column_width=True)
    
    st.markdown("""
    2. Terrains / Equipements :
    """)
    st.image('static/etr.png', use_column_width=True)
    
    
    df_fr = pd.read_excel('fr-en-dataes-types-d-equipement_nettoye.xlsx')
    equipements_uniques = df_fr['EquipementTypeLib'].unique()
    non_tennis_equipements = [equipement for equipement in equipements_uniques if 'tennis' not in str(equipement).lower()]
    df_tennis_cleaned = df_fr[~df_fr['EquipementTypeLib'].isin(non_tennis_equipements)]
    
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    installations_par_niveau_type = df_tennis_cleaned.groupby(['EquipementTypeLib', 'Niveau pratiqué'])['InsNom'].count().unstack()
    installations_par_niveau_type.plot(kind='bar', stacked=True, ax=axes[0])
    axes[0].set_xlabel('Type d\'équipement')
    axes[0].set_ylabel('Nombre d\'installations')
    axes[0].set_title('Niveau pratiqué par type d\'équipement')
    axes[0].legend(title='Niveau pratiqué')
    axes[0].tick_params(axis='x', rotation=90)
    axes[0].grid(True)
    nature_par_type = df_tennis_cleaned.groupby(['EquipementTypeLib', 'NatureLibelle']).size().unstack()
    nature_par_type.plot(kind='bar', stacked=True, ax=axes[1])
    axes[1].set_xlabel('Type d\'équipement')
    axes[1].set_ylabel('Nombre d\'installations')
    axes[1].set_title('Répartition des installations par nature et type d\'équipement')
    axes[1].legend(title='Nature')
    axes[1].tick_params(axis='x', rotation=90)
    axes[1].grid(True)
    plt.tight_layout()
    
    # Affichage du graphe
    st.pyplot(fig)
    
    st.image('static/instsport.png', use_column_width=True)
    st.image('static/util_terr.png', use_column_width=True)
    st.image('static/balles.png', use_column_width=True)
    
    
    st.markdown("""
    3. Joueurs :
    """)
    st.image('static/pays.png', use_column_width=True)
    st.image('static/clssatp.png', use_column_width=True)
    st.image('static/clss_fm.png', use_column_width=True)
    st.image('static/Joueurs.png', use_column_width=True)
    st.image('static/aces.png', use_column_width=True)
    st.image('static/main.png', use_column_width=True)
    
    st.markdown("""
    3. Blessures :
    """)
    st.image('static/bl1.png', use_column_width=True)
    st.image('static/bl3.png', use_column_width=True)
    st.image('static/bl8.png', use_column_width=True)
    st.image('static/bl6.png', use_column_width=True)
    st.image('static/bl7.png', use_column_width=True)
    st.image('static/bl5.png', use_column_width=True)
    st.image('static/bl4.png', use_column_width=True)
    
    st.header("Répondre aux probématiques")
    st.markdown("""
    1. Performances :
    """)
    
    st.markdown("""
    2. Blessures :
    """)
    
    st.header("Conclusion")
    
    
def modeles_ml():
    add_bg_from_local(os.path.join('static', 'img.jpg'))
    st.markdown('<h1 class="white-text">Page des modèles de ML</h1>', unsafe_allow_html=True)
    st.markdown('<p class="white-text">Ici, vous verrez les modèles réalisés et leurs résultats.</p>', unsafe_allow_html=True)
    
    st.markdown("""
    1. Régression mutiple : Prédiction du classement d'un joueur  :
    """)
    
    df_kg = pd.read_csv('GOATList_nettoye.csv')
    df_kg['dob'] = pd.to_datetime(df_kg['dob'])
    df_kg['age'] = 2024 - df_kg['dob'].dt.year
    df_kg['wonPct'] = df_kg['wonPct'].str.rstrip('%').astype('float') / 100.0
    
    X = df_kg[['totalPoints', 'tournamentPoints', 'rankingPoints', 'achievementsPoints', 'bestEloRating', 'wonPct', 'age', 'bestRankPoints']]
    y = df_kg['rank']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    st.write("Mean Squared Error:", mse)
    st.write("R^2 Score:", r2)
    fig, ax = plt.subplots()
    ax.scatter(X_test['totalPoints'], y_test, color='blue', label='Valeurs réelles')
    ax.scatter(X_test['totalPoints'], y_pred, color='red', label='Prédictions')
    ax.set_xlabel('Total Points')
    ax.set_ylabel('Rank')
    ax.set_title('Modèle de Régression Linéaire')
    ax.legend()
    st.pyplot(fig)
    
    #widgets pour tester le modèle
    st.markdown('### Testez le modèle avec vos propres valeurs')
    
    totalPoints = st.number_input('Total Points', min_value=0)
    tournamentPoints = st.number_input('Tournament Points', min_value=0)
    rankingPoints = st.number_input('Ranking Points', min_value=0)
    achievementsPoints = st.number_input('Achievements Points', min_value=0)
    bestEloRating = st.number_input('Best Elo Rating', min_value=0)
    wonPct = st.number_input('Won Percentage', min_value=0.0, max_value=1.0)
    age = st.number_input('Age', min_value=0)
    bestRankPoints = st.number_input('Best Rank Points', min_value=0)
    
    if st.button('Prédire le Rang'):
        input_data = pd.DataFrame({
            'totalPoints': [totalPoints],
            'tournamentPoints': [tournamentPoints],
            'rankingPoints': [rankingPoints],
            'achievementsPoints': [achievementsPoints],
            'bestEloRating': [bestEloRating],
            'wonPct': [wonPct],
            'age': [age],
            'bestRankPoints': [bestRankPoints]
        })
        
        #prédiction et arrondir 
        prediction = model.predict(input_data)
        prediction_rounded = round(prediction[0])
        
        st.write(f'Le rang prédit pour les valeurs saisies est : {prediction_rounded}')

        
        st.write(f'Le rang prédit pour les valeurs saisies est : {prediction[0]:.2f}')

    
    st.markdown("""
    1. Classification : Blessures :
    """)
    
    
    
    

def main():
    st.sidebar.title('Menu')
    page = st.sidebar.selectbox('Sélectionnez une page', ['Accueil', 'Graphiques', 'Modèles'])

    if page == 'Accueil':
        accueil()
    elif page =='Graphiques':
        graphiques()
    elif page == 'Modèles':
        modeles_ml()

if __name__ == '__main__':
    main()