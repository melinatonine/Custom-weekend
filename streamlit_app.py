import streamlit as st

st.set_page_config(page_title="Week-end")


options_total = ['en Auvergne', 'dans les Cévennes', 'dans les Gorges du Verdon', 'au Cap Fréhel', 
         "à Rennes", "à La Rochelle", "à Annecy", "à Strasbourg", 'à Bruges', 'à Vienne', 
         'à Turin', 'à Prague', 'au Mont Saint Michel']

questions = [
  {"id": "style",
   "question": "T'as plutôt quelle envie ?",
   "options": {
     "Risquer ma vie en pleine nature": ['en Auvergne', 'dans les Cévennes', 'dans les Gorges du Verdon', 'au Cap Fréhel'],
     "Un truc tranquille": ["à Rennes", "à La Rochelle", "à Annecy", "à Strasbourg"],
     "Visiter, découvrir": ['à Bruges', 'à Vienne', 'à Turin', 'à Prague', 'au Mont Saint Michel']
   }},

  {"id": "meteo",
   "question": "Quelle météo veux-tu ?",
   "options": {
     "Du soleil stp": ['dans les Cévennes', 'dans les Gorges du Verdon', 'à Turin'],
     "Peu importe": options_total,
     "Restons au frais": ['au Cap Fréhel', "à Rennes", "à La Rochelle", "à Annecy", 'au Mont Saint Michel']
   }},

  {"id": "transport",
   "question": "Tu veux voyager combien de temps ?",
   "options": {
     "Moins de 2h, c'est juste un we": ["à Rennes", "à La Rochelle", "à Strasbourg"],
     "3-5h, allez soyons fous": ["à Annecy", 'à Bruges', 'au Mont Saint Michel', 'en Auvergne', 'dans les Cévennes', 
            'dans les Gorges du Verdon', 'au Cap Fréhel'],
     "Je suis un kiffeur": ['à Vienne', 'à Turin', 'à Prague']
   }},

  {"id": "paysage",
   "question": "OK ferme les yeux, imagine toi en we, tu vois quoi ?",
   "options": {
     "Des montagnes": ['à Annecy', 'en Auvergne'],
     "De l'H2O, évidemment": ['au Cap Fréhel', "à La Rochelle", 'au Mont Saint Michel'],
     "Des immeubles, j'ai pas d'imagination": ['à Prague', 'à Vienne', 'à Strasbourg', 'à Bruges', "à Rennes", 'à Turin']
   }},

  {"id": "foule",
   "question": "A quel point tu détestes les touristes ?",
   "options": {
     "Qu'ils brûlent en enfer": ['dans les Cévennes', 'en Auvergne', 'au Cap Fréhel'],
     "Je les touche avec un baton à la limite": ["à Rennes", "à Strasbourg", 'à Turin', 'à La Rochelle', 'à Bruges'],
     "Je veux lécher leur sueur" : ['à Prague', 'au Mont Saint Michel', 'à Vienne']
   }},

  {"id": "food",
   "question": "Tu veux vivre une expérience gastronomique ?",
   "options": {
     "Oui, c'est bon les chips j'en ai marre": ['à Turin', 'à Strasbourg', 'à Prague'],
     "J'aime manger comme tout humain": ["à La Rochelle", 'à Vienne'],
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

  st.success(f"C'est décidé on part... {max(scores, key=scores.get)}")


  # with st.expander("Voir les scores (debug)"):
  #   st.write(scores)


