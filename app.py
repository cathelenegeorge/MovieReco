import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Set Streamlit page configuration
st.set_page_config(page_title="Movie Recommendation System", layout="wide")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("imdb_top_1000.csv")
    df['Genre'] = df['Genre'].str.replace(',', ' ')  # Preprocess genre
    return df

df = load_data()

# Convert genres into vectors and compute similarity
vectorizer = CountVectorizer()
genre_matrix = vectorizer.fit_transform(df['Genre'])
cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

# Function to fetch movie details from the dataset
def fetch_movie_details(title):
    movie = df[df['Series_Title'].str.lower() == title.lower()]
    
    if not movie.empty:
        movie_data = movie.iloc[0]
        
        # Fetch poster from dataset
        poster_url = movie_data["Poster_Link"] if pd.notna(movie_data["Poster_Link"]) else "https://via.placeholder.com/150"
        
        return {
            "Title": movie_data["Series_Title"],
            "Runtime": movie_data["Runtime"],
            "IMDb Rating": movie_data["IMDB_Rating"],
            "Certificate": movie_data["Certificate"],
            "Director": movie_data["Director"],
            "Cast": f"{movie_data['Star1']}, {movie_data['Star2']}, {movie_data['Star3']}, {movie_data['Star4']}",
            "Summary": movie_data["Overview"],
            "Poster": poster_url
        }
    
    return None

# Function to recommend movies based on genre
def recommend_movies_by_genre(selected_genre, num_recommendations=5):
    filtered_movies = df[df['Genre'].str.contains(selected_genre, case=False, na=False)]
    return filtered_movies[['Series_Title']].head(num_recommendations)

# Streamlit UI
st.title("🎬 Movie Recommendation System")
st.write("Find movies based on your favorite genre!")

# Extract unique genres from the dataset
all_genres = sorted(set(df['Genre'].str.split().sum()))
selected_genre = st.selectbox("Select a Genre:", all_genres)

if st.button("Recommend Movies"):
    recommendations = recommend_movies_by_genre(selected_genre)
    
    if recommendations.empty:
        st.warning("No recommendations found for this genre.")
    else:
        st.subheader(f"Recommended Movies for {selected_genre}:")
        for _, row in recommendations.iterrows():
            movie_details = fetch_movie_details(row['Series_Title'])
            
            if movie_details:
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.image(movie_details["Poster"], width=150)
                with col2:
                    st.markdown(f"### {movie_details['Title']}")
                    st.write(f"📀 **Runtime:** {movie_details['Runtime']}")
                    st.write(f"⭐ **IMDb Rating:** {movie_details['IMDb Rating']}")
                    st.write(f"🎭 **Certificate:** {movie_details['Certificate']}")
                    st.write(f"🎬 **Director:** {movie_details['Director']}")
                    st.write(f"🎭 **Cast:** {movie_details['Cast']}")
                    st.write(f"📖 **Summary:** {movie_details['Summary']}")
            else:
                st.write(f"⚠️ Could not fetch details for **{row['Series_Title']}**.")
