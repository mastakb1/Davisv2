import pandas as pd
import plotly.express as px
import streamlit as st

# Sample dataset
data = {
    'show_id': ['s1'],
    'type': ['Movie'],
    'title': ['Dick Johnson Is Dead'],
    'director': ['Kirsten Johnson'],
    'cast': [''],
    'country': ['United States'],
    'date_added': ['September 25, 2021'],
    'release_year': [2020],
    'rating': ['PG-13'],
    'duration': ['90 min'],
    'listed_in': ['Documentaries'],
    'description': ['As her father nears the end of his life, filmmaker Kirsten Johnson stages his death in inventive and comical ways to help them both face the inevitable.']
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert release_year to datetime
df['release_year'] = pd.to_datetime(df['release_year'], format='%Y')

# Visualize release year distribution
fig_release_year = px.histogram(df, x='release_year', title='Release Year Distribution')
st.plotly_chart(fig_release_year)

# Visualize ratings distribution
fig_rating = px.bar(df['rating'].value_counts(), x=df['rating'].value_counts().index, y=df['rating'].value_counts().values, title='Ratings Distribution')
st.plotly_chart(fig_rating)

# Visualize movie duration distribution
df['duration'] = df['duration'].str.replace(' min', '').astype(int)  # Convert duration to integer
fig_duration = px.histogram(df, x='duration', title='Movie Duration Distribution')
st.plotly_chart(fig_duration)

# Visualize country distribution
fig_country = px.bar(df['country'].value_counts(), x=df['country'].value_counts().index, y=df['country'].value_counts().values, title='Country Distribution')
st.plotly_chart(fig_country)
