import streamlit as st

st.set_page_config(page_title="Week-end")
options_total = ['Parc Volcans d Auvergne', 'Cévennes', 'Gorges du Verdon', 'Cap Fréhel', 
                 "Rennes", "La Rochelle", "Annecy", "Strasbourg", 'Bruges', 'Vienne', 
                 'Turin', 'Prague', 'Mont Saint Michel']

questions = [
    {"id": "style",
     "question": "T'as plutôt quelle envie ?",
     "options": {
         "Risquer ma vie en pleine nature": ['Parc Volcans d Auvergne', 'Cévennes', 'Gorges du Verdon', 'Cap Fréhel'],
         "Un truc tranquille": ["Rennes", "La Rochelle", "Annecy", "Strasbourg"],
         "Visiter, découvrir": ['Bruges', 'Vienne', 'Turin', 'Prague', 'Mont Saint Michel']
     }},

    {"id": "meteo",
     "question": "Quelle météo veux-tu ?",
     "options": {
         "Du soleil stp": ['Cévennes', 'Gorges du Verdon', 'Turin'],
         "Peu importe": options_total,
         "Restons au frais": ['Cap Fréhel', "Rennes", "La Rochelle", "Annecy", 'Mont Saint Michel']
     }},

    {"id": "transport",
     "question": "Tu veux voyager combien de temps ?",
     "options": {
         "Moins de 2h, c'est juste un we": ["Rennes", "La Rochelle", "Strasbourg"],
         "3-5h, allez soyons fous": ["Annecy", 'Bruges', 'Mont Saint Michel', 'Parc Volcans d Auvergne', 'Cévennes', 
                       'Gorges du Verdon', 'Cap Fréhel'],
         "Je suis un kiffeur": ['Vienne', 'Turin', 'Prague']
     }},

    {"id": "paysage",
     "question": "OK ferme les yeux, imagine toi en we, tu vois quoi ?",
     "options": {
         "Des montagnes": ['Annecy', 'Parc Volcans d Auvergne'],
         "De l'H2O, évidemment": ['Cap Fréhel', "La Rochelle", 'Mont Saint Michel'],
         "Des immeubles, j'ai pas d'imagination": ['Prague', 'Vienne', 'Strasbourg', 'Bruges', "Rennes", 'Turin']
     }},

    {"id": "foule",
     "question": "A quel point tu détestes les touristes ?",
     "options": {
         "Qu'ils brûlent en enfer": ['Cévennes', 'Parc Volcans d Auvergne', 'Cap Fréhel'],
         "Je les touche avec un baton à la limite": ["Rennes", "Strasbourg", 'Turin', 'La Rochelle', 'Bruges'],
         "Je veux lécher leur sueur" : ['Prague', 'Mont Saint Michel', 'Vienne']
     }},

    {"id": "food",
     "question": "Tu veux vivre une expérience gastronomique ?",
     "options": {
         "Oui, c'est bon les chips j'en ai marre": ['Turin', 'Strasbourg', 'Prague'],
         "J'aime manger comme tout humain": ["La Rochelle", 'Vienne'],
         "On organise un we, la bouffe c'est pas un critère": options_total
     }},
]



st.header("Réponds à ces questions")

st.write("**Hervé va deviner ta destination de week-end rêvée**")

answers = {}

for q in questions:
    choice = st.radio(q["question"], list(q["options"].keys()), key=q["id"])
    answers[q["id"]] = choice

if st.button("Bon alors Hervé?"):
    
    # Reset scores
    scores = {}
    for destination in options_total:
        scores[destination] = 0

    # Calcul
    for q in questions:
        selected = answers[q["id"]]
        impacts = q["options"][selected]
        for lieu in impacts :
            scores[lieu] += 1 

    st.success(f"C'est décidé on part à... {max(scores, key=scores.get)}")


    # with st.expander("Voir les scores (debug)"):
    #     st.write(scores)


