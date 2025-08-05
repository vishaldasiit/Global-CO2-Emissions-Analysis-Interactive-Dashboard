# Global CO₂ Emissions Analysis & Visualization

This project uses a Python script to analyze and visualize global CO₂ emissions data from the Our World in Data dataset. The script generates three key interactive plots using the Pandas and Plotly libraries to explore historical emissions trends.

## Features

The script generates the following three visualizations:

1.  **Line Chart:** Shows the annual CO₂ emissions for a selection of major emitting countries over time, highlighting their different emission trajectories.
2.  **Bar Chart:** Displays the top 15 countries based on their *cumulative* CO₂ emissions, identifying the largest historical contributors.
3.  **Animated Choropleth Map:** Provides a year-by-year animated map of global CO₂ emissions from 1950 onwards, showing how the global landscape of emissions has evolved.

## Data Source

The data is sourced from the "Our World in Data" CO₂ and Greenhouse Gas Emissions dataset. This is a comprehensive, publicly available dataset that is regularly updated.

*   **Dataset URL:** [https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv](https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv)

## Project Setup and Requirements

To run this project locally, you will need Python and the following libraries:

*   pandas
*   plotly
*   nbformat (often a required dependency for showing figures in some environments)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/vishaldasiit/Global-CO2-Emissions-Analysis-Interactive-Dashboard
    cd co2-emissions-visualization
    ```

2.  **Install the required libraries:**
    For best practice, use a virtual environment.
    ```bash
    # Create and activate a virtual environment
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

    # Install from requirements.txt
    pip install -r requirements.txt
    ```
    The `requirements.txt` file should contain:
    ```
    pandas
    plotly
    nbformat
    ```

### How to Run the Project

Once you have installed the dependencies, you can run the script directly from your terminal:

```bash
python co2_visualization_script.py
