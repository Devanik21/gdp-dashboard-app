import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("C:\\Users\\debna\\Downloads\\GDP.csv")
    return data

data = load_data()

# Sidebar for user inputs
st.sidebar.header('User Input Features')

def user_input_features():
    countries = data['country'].unique()
    country = st.sidebar.selectbox('Country', countries)
    return country

selected_country = user_input_features()

# Filter data based on the selected country
filtered_data = data[data['country'] == selected_country]

# Display data
st.write(f"**GDP Data for {selected_country}**")
st.write(filtered_data)

# Plotting
fig, ax = plt.subplots()
ax.plot(filtered_data['year'], filtered_data['gdp'])
ax.set_xlabel('Year')
ax.set_ylabel('GDP')
ax.set_title(f'GDP Trend for {selected_country}')
st.pyplot(fig)

# Show additional statistics
st.write(f"**Total GDP from 1960 to 2020 for {selected_country}:**")
total_gdp = filtered_data['gdp'].sum()
st.write(f"${total_gdp:,.2f}")
