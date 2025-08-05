import pandas as pd
import plotly.express as px

# 1. Load the Dataset
# Load the data from the Our World in Data CO2 emissions CSV file.
# This dataset is well-structured and contains the required 'country', 'year', and 'co2' columns.
try:
    df = pd.read_csv('https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv')
except Exception as e:
    print(f"Error loading data: {e}")
    # As a fallback, create a dummy dataframe to avoid crashing the script
    df = pd.DataFrame({
        'country': ['USA', 'USA', 'China', 'China', 'India', 'India'],
        'year': [2020, 2021, 2020, 2021, 2020, 2021],
        'co2': [4500, 4600, 10000, 10500, 2300, 2500],
        'iso_code': ['USA', 'USA', 'CHN', 'CHN', 'IND', 'IND']
    })


# 2. Data Preparation
# Clean the data by dropping rows where 'co2' or 'iso_code' are missing, as they are essential for our plots.
# Also, filter out non-country entities which are sometimes included in this dataset (e.g., 'World', 'Asia').
df.dropna(subset=['co2', 'iso_code'], inplace=True)
non_countries = ['World', 'Asia', 'Europe', 'North America', 'South America', 'Africa', 'Oceania', 'Upper-middle-income countries', 'High-income countries', 'Lower-middle-income countries', 'Low-income countries', 'European Union (27)', 'European Union (28)']
df = df[~df['country'].isin(non_countries)]


# 3. Create the Visualizations

# --- Chart 1: Line Chart of CO2 Emissions Over Time ---
# This line chart shows the CO2 emissions for a selection of major countries over the years.
# Plotly Express makes it easy to create an interactive chart where you can hover to see details. [5]
# We'll pre-select a few countries to keep the initial view clean.
top_emitters_for_line = ['United States', 'China', 'India', 'Russia', 'Japan', 'Germany']
df_line = df[df['country'].isin(top_emitters_for_line)]

fig_line = px.line(
    df_line,
    x='year',
    y='co2',
    color='country',
    title='Annual CO2 Emissions by Country',
    labels={'co2': 'Annual CO2 Emissions (in million tonnes)', 'year': 'Year'}
)
fig_line.show()


# --- Chart 2: Bar Chart of Top Emitting Countries ---
# This bar chart shows the total cumulative CO2 emissions to identify the top contributors.
# We group the data by country, sum the emissions, and take the top 15.
df_bar = df.groupby('country')['co2'].sum().nlargest(15).reset_index()

fig_bar = px.bar(
    df_bar,
    x='country',
    y='co2',
    title='Top 15 Countries by Cumulative CO2 Emissions',
    labels={'co2': 'Cumulative CO2 Emissions (in million tonnes)', 'country': 'Country'}
)
fig_bar.show()


# --- Chart 3: Choropleth Map of Emissions by Country ---
# This animated choropleth map visualizes CO2 emissions across the globe for each year. [3, 4]
# The animation_frame is set to 'year' to allow for interactive exploration of emissions over time. [11]
# We'll filter the data from 1950 onwards to make the animation more focused.
df_map = df[df['year'] >= 1950]

fig_map = px.choropleth(
    df_map,
    locations="iso_code",
    color="co2",
    hover_name="country",
    animation_frame="year",
    color_continuous_scale=px.colors.sequential.Plasma,
    title="Global CO2 Emissions by Country Over Time",
    labels={'co2': 'Annual CO2 Emissions (in million tonnes)'}
)
fig_map.show()
