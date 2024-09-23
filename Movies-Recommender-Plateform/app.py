import streamlit as st 
import pickle
import pandas as pd

def recommend(movie) : 
    

movie_dict = pickle.load(open('movies.dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

st.title('Movie Recommender System')

Selected_movie_name = st.selectbox(
    'How woult you like to be contacted?',
    movies['title'].values
)

if st.button('Recommend'): 
    recommend(Selected_movie_name)
    st.write(Selected_movie_name)