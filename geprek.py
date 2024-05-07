import pandas as pd
import plotly.express as px
import streamlit as st

# Load the CSV file from GitHub
df = pd.read_csv('netflix_titles.csv')

# Convert release_year to datetime
df['release_year'] = pd.to_datetime(df['release_year'], format='%Y')

# Visualize release year distribution for both movies and TV shows
fig_release_year = px.histogram(df, x='release_year', color='type', title='Release Year Distribution by Type')
st.plotly_chart(fig_release_year)

# Visualize ratings distribution for both movies and TV shows
fig_rating = px.bar(df['rating'].value_counts(), x=df['rating'].value_counts().index, y=df['rating'].value_counts().values, title='Ratings Distribution')
st.plotly_chart(fig_rating)

# Visualize duration distribution for TV shows
tv_shows_df = df[df['type'] == 'TV Show']
tv_shows_df['duration'] = tv_shows_df['duration'].str.extract('(\d+)').astype(int)  # Extract numerical duration
fig_duration_tv = px.histogram(tv_shows_df, x='duration', title='TV Show Duration Distribution')
st.plotly_chart(fig_duration_tv)

# Visualize country distribution for movies and TV shows
fig_country = px.bar(df['country'].value_counts(), x=df['country'].value_counts().index, y=df['country'].value_counts().values, title='Country Distribution')
st.plotly_chart(fig_country)
