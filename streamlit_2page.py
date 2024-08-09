import pandas as pd
import plotly.express as px
import streamlit as st

# Load the dataset
data = pd.read_csv('aggregate_HRI_data.csv')

# Filter the necessary columns
data_filtered = data[['country', 'year', 'human_rights_score']]

# Create a sidebar for navigation
st.sidebar.title("Global Human Rights")
page = st.sidebar.radio("Data Visual:", ["Choropleth Map", "Country Time-Series"])

# Page 1: Choropleth Map
if page == "Choropleth Map":

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

    fig.update_layout(
        width=1200,
        height=800,
    )
    # Show the figure in the Streamlit app
    st.plotly_chart(fig)

# Page 2: Country Time-Series
elif page == "Country Time-Series":
    st.subheader("Human Rights Score Over Time by Country")

    # Select multiple countries
    countries = st.multiselect("Select countries", sorted(data_filtered['country'].unique()))

    if countries:
        # Filter data for the selected countries
        selected_data = data_filtered[data_filtered['country'].isin(countries)]

        # Sort data to ensure proper plotting
        selected_data = selected_data.sort_values(by=['country', 'year'])

        # Create the line chart
        fig = px.line(
            selected_data,
            x="year",
            y="human_rights_score",
            color="country",
            title="Human Rights Score Over Time",
            labels={'human_rights_score': 'Human Rights Score', 'year': 'Year'},
            line_group="country"  # Ensure that each country is treated as a separate line
        )

        # Show the figure in the Streamlit app
        st.plotly_chart(fig)
    else:
        st.write("Please select at least one country to display the chart.")
