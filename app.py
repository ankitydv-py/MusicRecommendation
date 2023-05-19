import streamlit as st
import pandas as pd
import pickle

# loading data to fit the model

data = pd.read_csv('./usr/src/app/data.csv')
data_fit = data[['acousticness','energy','danceability','instrumentalness','liveness','speechiness','tempo']]

# load the model
pickle_in = open("./usr/src/app/model.pickle","rb")
model = pickle.load(pickle_in)
song_clusters = model.predict(data_fit)
data['cluster'] = song_clusters

     
# recommendation function
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
        top_songs = cluster_songs.sort_values(by='popularity', ascending=False).head(15)['name'].tolist()
        
        # Generating output
        success_text = 'The recommended songs are:\n'
        for i, song in enumerate(top_songs):
            success_text += (f"\n{i+1}.{song}\n")
    return success_text

def first():
       #data_fit = data[['acousticness','energy','danceability','instrumentalness','liveness','speechiness','tempo']]
    #get songs cluster
       
       st.write(f"Enter your music preferences below to get personalized recommendations and Year range")  
       song_name = st.selectbox("Select a song:", [""] + list(data["name"].unique()))
       if song_name:
            year = st.selectbox("Select Year:", [""] + list(data[data['name'] == song_name]['year'].unique()))
            if year:
                if st.button("Click Here to see Recommendation"):
                    results = recommend_songs(song_name, year)
                    st.write(results) 

def second():
    st.write("Upload a CSV file to get recommendations:")
    file = st.file_uploader("Choose a CSV file", type="csv")
    if file is not None:
            uploaded_data = pd.read_csv(file)
            data = pd.read_csv('./usr/src/app/data.csv')
            data = pd.concat([uploaded_data, data])
            
            
# load the model
    
            data_fit = data[['acousticness','energy','danceability','instrumentalness','liveness','speechiness','tempo']]
            pickle_in = open("./usr/src/app/model.pickle","rb")
            model = pickle.load(pickle_in)

# get songs cluster
            song_clusters = model.predict(data_fit)
            data['cluster'] = song_clusters
            #data = pd.concat([uploaded_data, data])
            # Use the uploaded data to generate recommendations
            st.write(data)
            #min_year = data["year"].min()
            #max_year = data["year"].max()
            #st.write(uploaded_data)
            st.write(f"Enter your music preferences below to get personalized recommendations and Year range")
            #data = pd.concat([uploaded_data, data])  
            song_name = st.selectbox("Select a music:", [""] + list(data["name"].unique()))
            if song_name:
               year = st.selectbox("Select which Year:", [""] + list(data[data['name'] == song_name]['year'].unique()))
               if year:
                    if st.button("Click Here to see Recommendation List"):
                          song = data[(data['name'] == song_name) & (data['year'] == year)]
                          if song.empty:
                               failure_text ='Song not Found'
                               st.write(failure_text)

                          else:
        # selecting song cluster
                               cluster = song_clusters[song.index[0]]

        # top songs from each cluster (TOP 5)
                               cluster_songs = data[data['cluster'] == cluster]
                               top_songs = cluster_songs.sort_values(by='popularity', ascending=False).head(15)['name'].tolist()
        
        # Generating output
                               success_text = 'The recommended songs are:\n'
                               for i, song in enumerate(top_songs):
                                      success_text += (f"\n{i+1}.{song}\n")
                          st.write(success_text)

                          #results = recommend_songs(song_name, year)
                          #st.write(results)



def main():
   
    

    # Set page title and subtitle
    st.set_page_config(page_title="Music Recommendation System", page_icon=":musical_note:")
    st.title("Music Recommendation System")

    # Add custom CSS styles
    


    # Create two tabs
    tabs = st.tabs(["Recommendation", "Upload CSV File"])


    # Add elements to the first tab
    with tabs[0]:
        first()
        #min_year = data["year"].min()
        #max_year = data["year"].max()
           
    # Add elements to the second tab
    with tabs[1]:
         second()
        
         
   
if __name__ == '__main__':
    main()



    
