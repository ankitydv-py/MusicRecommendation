import streamlit as st
import pandas as pd
import pickle

# loading data to fit the model
data = pd.read_csv('data.csv')
data_fit = data[['acousticness','energy','danceability','instrumentalness','liveness','speechiness','tempo']]

# load the model
pickle_in = open("model.pickle","rb")
model = pickle.load(pickle_in)

# Set page title and icon
st.set_page_config(page_title="Music Recommendation System", page_icon=":musical_note:")

# get songs cluster
song_clusters = model.predict(data_fit)
data['cluster'] = song_clusters

# recommendation funstion
def recommend_songs(song_name, year):
    song = data[(data['name'] == song_name) & (data['year'] == year)]

    if song.empty:
        failure_text ='Song not Found'
        return failure_text

    else:
        # selecting song cluster
        cluster = song_clusters[song.index[0]]

        # top songs from each cluster (TOP 5)
        cluster_songs = data[data['cluster'] == cluster]
        top_songs = cluster_songs.sort_values(by='popularity', ascending=False).head(5)['name'].tolist()
        
        # Generating output
        success_text = 'The recommended songs are:\n'
        for i, song in enumerate(top_songs):
            success_text += (f"\n{i+1}.{song}\n")
    return success_text

def main():
    min_year = data["year"].min()
    max_year = data["year"].max()

    # Set page title and subtitle
    st.title("Music Recommendation System")

    # Create select dropdown box for Song Name
    st.write(f"Enter your music preferences below to get personalized recommendations and Year range {min_year} - {max_year}")  
    song_name = st.selectbox("Select a song:", [""] + list(data["name"].unique()))

    # Create select dropdown box for Song creation year
    if song_name:
        year = st.selectbox("Select Year:", [""] + list(data[data['name'] == song_name]['year'].unique()))

        if year:
            # Create button for show recommended results
            if st.button("Click Here to see Recommendation"):
                results = recommend_songs(song_name, year)
                st.write(results)
        

if __name__ == '__main__':
    main()