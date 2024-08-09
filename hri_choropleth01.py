import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
data = pd.read_csv('aggregate_HRI_data.csv')

# Filter the necessary columns
data_filtered = data[['country', 'year', 'human_rights_score']]

# Streamlit app
st.subheader("Human Rights Score by Country Over Time")

# Create the choropleth map
fig = px.choropleth(
    data_filtered,
    locations="country",
    locationmode="country names",
    color="human_rights_score",
    hover_name="country",
    animation_frame="year",
    color_continuous_scale="ylorrd",
    range_color=(data_filtered['human_rights_score'].min(), data_filtered['human_rights_score'].max()),
    labels={'human_rights_score': 'Human Rights Score'},
    title="Human Rights Score by Country Over Time"
)

fig.update_geos(projection_type="natural earth")

# Show the figure in the Streamlit app
st.plotly_chart(fig)
