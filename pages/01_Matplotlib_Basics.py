# 01 Matplotlib Basics
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Matplotlib Basics",
    page_icon="1️⃣",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("# Matplotlib Basics")

# Tab menu
tab_project, tab_solution,= st.tabs( 
    ["🛠️ Project", "✅ Solution"]
)

with tab_project:
    st.markdown("""
    ## Project 
    In this first module, you gained a solid understanding of what Matplotlib is, how its syntax works, and **how to create almost any basic chart with it**. 

    Now, let's apply this knowledge to real-life datasets before we bring your skills to the next level! 🚀

    ### 📍 Goal
    The aim of this first mini project is to make you work on finding the right chart for a given dataset, and then translate this idea into actual code.

    To do this, you'll choose from multiple datasets and create charts to visualize them.

    ### 💾 Datasets

    """)

    # Tab menu
    tab1, tab2, tab3 = st.tabs(
        ["Storms", "Footprint", "Mario Kart"] 
    )

    with tab1:
        st.markdown("""

    #### 💨 Frequency of Different Kinds of Storms

    **Description:** 

    This dataset comes from the National Oceanic and Atmospheric Administration (NOAA), [an agency that enriches life through science](https://www.noaa.gov/about-our-agency).

    It contains information on the frequency of different types of storms between 2010 and 2022.

    - `year`: The year of the storm occurrence.
    - `status`: The type of storm (e.g., hurricane, tropical depression).
    - `n`: The number of storms that occurred.

    **Import**::


    ```python
    import pandas as pd
    from pyodide.http import open_url

    url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/storms.csv"
    df_storms = pd.read_csv(open_url(url))
    ```


    **Preview**:

    | year | status              | n     |
    |------|---------------------|-------|
    | 2010 | hurricane           | 163.0 |
    | 2010 | tropical depression | 72.0  |
    | 2010 | tropical storm      | 212.0 |
    | 2010 | tropical wave       | 0.0   |
    | 2011 | hurricane           | 106.0 |
    | 2011 | tropical depression | 47.0  |




    """)

    with tab2:

        st.markdown("""

    #### 🦶 Footprint and Biocapacity

    **Description:**  

    This dataset comes from the Global Footprint Network, [an international nonprofit organization](https://www.footprintnetwork.org/about-us/).  

    It contains the footprint and other measures of biocapacity for different countries around the world.

    - `country`: The name of the country.  
    - `region`: The geographical region to which the country belongs (e.g., EU-27, Asia-Pacific, Africa).  
    - `populationMillions`: The total population of the country, expressed in millions.  
    - `footprint`: The ecological footprint of the country, representing global hectares per person.  
    - `biocapacity`: The biocapacity of the country, representing global hectares per person.  
    - `earthsRequired`: The number of Earths required to sustain the current consumption levels if everyone lived like the average resident of the country.

    **Import**:

    ```python
    import pandas as pd
    from pyodide.http import open_url

    url = "https://raw.githubusercontent.com/holtzy/the-python-graph-gallery/master/static/data/footprint.csv"
    df_footprint = pd.read_csv(open_url(url))
    ```

    **Preview**:

    | country   | region          | populationMillions | footprint | biocapacity | earthsRequired |
    |-----------|-----------------|---------------------|-----------|-------------|----------------|
    | Albania   | Other Europe    | 2.9                 | 2.1       | 1.18        | 1.37           |
    | Angola    | Africa          | 35.0                | 0.9       | 1.59        | 0.57           |
    | Argentina | South America   | 46.0                | 3.2       | 5.23        | 2.13           |
    | Australia | Asia-Pacific    | 26.1                | 5.8       | 11.02       | 3.83           |
    | Austria   | EU-27           | 9.1                 | 5.6       | 2.89        | 3.73           |

        """)


    with tab3: 
        st.markdown("""

    #### 🏎️ Mario Kart World Records per Track

    **Description:**  

    The data originates from the [Mario Kart World Records site](https://mkwrs.com/) and was highlighted as part of the Tidytuesday challenge in 2021.

    It includes various world records for different tracks in the Nintendo 64 Mario Kart game. There are 16 tracks, with records available for both the fastest single lap and the fastest complete race.

    Records are provided for runs both with and without the use of shortcuts.

    Additionally, the dataset includes records for both NTSC and PAL systems, as the game runs slightly slower on PAL systems.

    - `track`: Name of the track (e.g., Toad's Turnpike, Luigi Raceway).  
    - `type`: Whether the record is for a single lap or a complete race.  
    - `shortcut`: Yes/No variable that identifies records where a shortcut was used.  
    - `date`: Date when the record was achieved.  
    - `time`: How many seconds it took to complete the track.  
    - `player`: Name of the player.  
    - `record_duration`: Duration of the record in days.  

    **Import**:

    ```python
    import pandas as pd
    from pyodide.http import open_url

    url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/records.csv"
    df_mario = pd.read_csv(open_url(url))
    ```

    **Preview**:

    | track           | type          | shortcut | player      | system | date       | time   | record_duration |
    |------------------|---------------|----------|-------------|--------|------------|--------|-----------------|
    | Luigi Raceway    | Three Lap     | No       | Salam       | NTSC   | 1997-02-15 | 132.99 | 1               |
    | Luigi Raceway    | Three Lap     | No       | Booth       | NTSC   | 1997-02-16 | 129.99 | 0               |
    | Luigi Raceway    | Three Lap     | No       | Salam       | NTSC   | 1997-02-16 | 128.99 | 12              |
    | Luigi Raceway    | Three Lap     | No       | Gregg G     | NTSC   | 1997-03-07 | 124.51 | 54              |
    | Luigi Raceway    | Three Lap     | No       | Rocky G     | NTSC   | 1997-04-30 | 122.89 | 0               |

        """)



    st.markdown("""

    ### 🚀 Let's go!

    Your main objective is to **create 10 unique** charts using the provided datasets. Feel free to focus on one dataset or experiment with all of them.

    Once you've crafted your 10 charts (the more, the better!), share them in the **share-your-viz** channel on [Discord](https://discord.gg/XKmpbv4VWY).

    If you end up with fewer than 10 charts, no problem! Post what you have, explore others' work, and don’t hesitate to ask for help.




    """            
    )


with tab_solution:
    st.markdown("""
    ## Solution      
    """)

    
    # Tab menu
    tab1, tab2, tab3 = st.tabs(
        ["Storms", "Footprint", "Mario Kart"] 
    )

    with tab1:

        # Load the dataset
        url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/storms.csv"
        df_storms = pd.read_csv(url)
        
        # Streamlit layout
        st.markdown("### 💨 Frequency of Different Kinds of Storms")
        
        # Botones para seleccionar gráficos
        selected_chart = st.radio(
            "Select a chart to display:",
            ("Total Storms Per Year", "Proportion of Storm Types", "Trends of Storm Frequency", "Top Storm Types", "Heatmap of Storm Occurrences"),
        )
        
        # 1. Bar Chart: Total storms per year
        if selected_chart == "Total Storms Per Year":
            total_storms_year = df_storms.groupby("year")["n"].sum()
            fig1, ax1 = plt.subplots(figsize=(5, 3))  # Tamaño reducido
            ax1.bar(total_storms_year.index, total_storms_year.values, color="skyblue", edgecolor="black")
            ax1.set_title("Total Storms Per Year")
            ax1.set_xlabel("Year")
            ax1.set_ylabel("Number of Storms")
            st.pyplot(fig1,use_container_width=False)
        
        # 2. Pie Chart: Proportion of storm types
        elif selected_chart == "Proportion of Storm Types":
            storm_types = df_storms.groupby("status")["n"].sum()
            fig2, ax2 = plt.subplots(figsize=(5, 3))  # Tamaño reducido
            ax2.pie(
                storm_types,
                labels=storm_types.index,
                autopct="%1.1f%%",
                startangle=90,
                colors=["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"],
            )
            ax2.set_title("Proportion of Storm Types")
            st.pyplot(fig2,use_container_width=False)
        
        # 3. Line Chart: Trends of storm frequency over the years
        elif selected_chart == "Trends of Storm Frequency":
            fig3, ax3 = plt.subplots(figsize=(7, 3))  # Tamaño reducido
            for status in df_storms["status"].unique():
                status_data = df_storms[df_storms["status"] == status].groupby("year")["n"].sum()
                ax3.plot(status_data.index, status_data.values, label=status)
            ax3.set_title("Trends of Storm Frequency")
            ax3.set_xlabel("Year")
            ax3.set_ylabel("Number of Storms")
            ax3.legend()
            st.pyplot(fig3,use_container_width=False)
        
        # 4. Horizontal Bar Chart: Top storm types by total occurrences
        elif selected_chart == "Top Storm Types":
            # Group by storm types to calculate totals
            storm_types = df_storms.groupby("status")["n"].sum()
            storm_types_sorted = storm_types.sort_values(ascending=False)
            fig4, ax4 = plt.subplots(figsize=(5, 3))  # Tamaño reducido
            ax4.barh(storm_types_sorted.index, storm_types_sorted.values, color="orange", edgecolor="black")
            ax4.set_title("Top Storm Types")
            ax4.set_xlabel("Number of Storms")
            ax4.set_ylabel("Storm Type")
            st.pyplot(fig4,use_container_width=False)
        
        # 5. Heatmap: Storm occurrences by year and type
        elif selected_chart == "Heatmap of Storm Occurrences":
            storm_pivot = df_storms.pivot_table(values="n", index="status", columns="year", aggfunc="sum", fill_value=0)
            fig5, ax5 = plt.subplots(figsize=(5, 3))  # Tamaño reducido
            cax = ax5.matshow(storm_pivot, cmap="YlGnBu")
            fig5.colorbar(cax)
            ax5.set_title("Heatmap of Storm Occurrences")
            ax5.set_xticks(np.arange(len(storm_pivot.columns)))
            ax5.set_yticks(np.arange(len(storm_pivot.index)))
            ax5.set_xticklabels(storm_pivot.columns)
            ax5.set_yticklabels(storm_pivot.index)
            plt.xticks(rotation=90)
            st.pyplot(fig5,use_container_width=False)


    with tab2:

        st.markdown("""### 🦶 Footprint and Biocapacity""")

        # Load the dataset
        url = "https://raw.githubusercontent.com/holtzy/The-Python-Graph-Gallery/master/static/data/footprint.csv"
        df_footprint = pd.read_csv(url)

        # Buttons to select charts
        selected_chart = st.radio(
            "Select a chart to display:",
            (
                "Population by Region",
                "Average Footprint by Region",
                "Footprint vs Biocapacity",
                "Top Countries by Earths Required",
                "Bubble Chart: Footprint vs Biocapacity with Population",
            ),
        )

        # 1. Bar Chart: Population by Region
        if selected_chart == "Population by Region":
            population_by_region = df_footprint.groupby("region")["populationMillions"].sum()
            fig1, ax1 = plt.subplots(figsize=(5, 3))
            ax1.bar(population_by_region.index, population_by_region.values, color="skyblue", edgecolor="black")
            ax1.set_title("Population by Region")
            ax1.set_xlabel("Region")
            ax1.set_ylabel("Population (Millions)")
            ax1.tick_params(axis="x", rotation=45)
            st.pyplot(fig1, use_container_width=False)

        # 2. Pie Chart: Average Footprint by Region
        elif selected_chart == "Average Footprint by Region":
            avg_footprint = df_footprint.groupby("region")["footprint"].mean()
            fig2, ax2 = plt.subplots(figsize=(5, 3))
            ax2.pie(
                avg_footprint,
                labels=avg_footprint.index,
                autopct="%1.1f%%",
                startangle=90,
                colors=plt.cm.Paired(np.linspace(0, 1, len(avg_footprint))),
            )
            ax2.set_title("Average Footprint by Region")
            st.pyplot(fig2, use_container_width=False)

        # 3. Scatter Plot: Footprint vs Biocapacity
        elif selected_chart == "Footprint vs Biocapacity":
            fig3, ax3 = plt.subplots(figsize=(5, 3))
            ax3.scatter(df_footprint["footprint"], df_footprint["biocapacity"], alpha=0.7, c="orange", edgecolor="black")
            ax3.set_title("Footprint vs Biocapacity")
            ax3.set_xlabel("Footprint (Global Hectares per Person)")
            ax3.set_ylabel("Biocapacity (Global Hectares per Person)")
            st.pyplot(fig3, use_container_width=False)

        # 4. Horizontal Bar Chart: Top Countries by Earths Required
        elif selected_chart == "Top Countries by Earths Required":
            top_countries = df_footprint.sort_values("earthsRequired", ascending=False).head(10)
            fig4, ax4 = plt.subplots(figsize=(5, 3))
            ax4.barh(top_countries["country"], top_countries["earthsRequired"], color="green", edgecolor="black")
            ax4.set_title("Top Countries by Earths Required")
            ax4.set_xlabel("Earths Required")
            ax4.set_ylabel("Country")
            st.pyplot(fig4, use_container_width=False)

        # 5. Bubble Chart: Footprint vs Biocapacity with Population
        elif selected_chart == "Bubble Chart: Footprint vs Biocapacity with Population":
            fig5, ax5 = plt.subplots(figsize=(7, 5))
            scatter = ax5.scatter(
                df_footprint["footprint"],
                df_footprint["biocapacity"],
                s=df_footprint["populationMillions"] * 10,  # Bubble size proportional to population
                alpha=0.6,
                c=np.random.rand(len(df_footprint)),  # Random colors for fun
                cmap="viridis",
                edgecolors="black"
            )
            ax5.set_title("Bubble Chart: Footprint vs Biocapacity")
            ax5.set_xlabel("Footprint (Global Hectares per Person)")
            ax5.set_ylabel("Biocapacity (Global Hectares per Person)")
            ax5.grid(True, linestyle="--", alpha=0.5)

            # Annotating the top 5 countries by population
            top_countries = df_footprint.sort_values("populationMillions", ascending=False).head(5)
            for _, row in top_countries.iterrows():
                ax5.text(
                    row["footprint"],
                    row["biocapacity"],
                    row["country"],
                    fontsize=8,
                    ha="center",
                    va="center",
                    bbox=dict(facecolor="white", alpha=0.6, edgecolor="black", boxstyle="round"),
                )

            st.pyplot(fig5, use_container_width=False)


    with tab3: 
        # Load the dataset
        url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2021/2021-05-25/records.csv"
        df_mario = pd.read_csv(url)

        # Page Layout
        st.markdown("### 🏎️ Mario Kart World Records per Track")

        # Chart selection
        selected_chart = st.radio(
            "Select a chart to display:",
            (
                "Fastest Tracks",
                "Records by Track Type",
                "Top Players",
                "Shortcut vs Non-Shortcut Times",
                "Lap vs Full Race Distribution",
            ),
        )

        # 1. Fastest Tracks: Horizontal Bar Chart
        if selected_chart == "Fastest Tracks":
            fastest_tracks = df_mario.groupby("track")["time"].min().sort_values()
            fig1, ax1 = plt.subplots(figsize=(7, 5))
            ax1.barh(fastest_tracks.index, fastest_tracks.values, color="limegreen", edgecolor="black")
            ax1.set_title("Fastest Tracks in Mario Kart")
            ax1.set_xlabel("Time (seconds)")
            ax1.set_ylabel("Track")
            st.pyplot(fig1, use_container_width=False)

        # 2. Records by Track Type: Pie Chart
        elif selected_chart == "Records by Track Type":
            type_counts = df_mario["type"].value_counts()
            fig2, ax2 = plt.subplots(figsize=(5, 3))
            ax2.pie(
                type_counts,
                labels=type_counts.index,
                autopct="%1.1f%%",
                startangle=140,
                colors=["#FFD700", "#1E90FF"],
            )
            ax2.set_title("Records by Track Type")
            st.pyplot(fig2, use_container_width=False)

        # 3. Top Players: Bar Chart
        elif selected_chart == "Top Players":
            top_players = df_mario["player"].value_counts().head(10)
            fig3, ax3 = plt.subplots(figsize=(7, 4))
            ax3.bar(top_players.index, top_players.values, color="orange", edgecolor="black")
            ax3.set_title("Top Players by Record Count")
            ax3.set_xlabel("Player")
            ax3.set_ylabel("Number of Records")
            ax3.tick_params(axis="x", rotation=45)
            st.pyplot(fig3, use_container_width=False)

        # 4. Shortcut vs Non-Shortcut Times: Box Plot
        elif selected_chart == "Shortcut vs Non-Shortcut Times":
            fig4, ax4 = plt.subplots(figsize=(6, 4))
            df_mario["shortcut"] = df_mario["shortcut"].map({"Yes": "Shortcut", "No": "No Shortcut"})
            df_mario.boxplot(column="time", by="shortcut", ax=ax4, grid=False, notch=True, patch_artist=True)
            ax4.set_title("Shortcut vs Non-Shortcut Times")
            ax4.set_xlabel("Type")
            ax4.set_ylabel("Time (seconds)")
            ax4.grid(axis="y")
            fig4.suptitle("")  # Removes default title
            st.pyplot(fig4, use_container_width=False)

        # 5. Lap vs Full Race Distribution: Histogram
        elif selected_chart == "Lap vs Full Race Distribution":
            fig5, ax5 = plt.subplots(figsize=(7, 4))
            df_mario["type"].replace({"Three Lap": "Full Race", "One Lap": "Single Lap"}, inplace=True)
            for t in df_mario["type"].unique():
                subset = df_mario[df_mario["type"] == t]
                ax5.hist(subset["time"], bins=20, alpha=0.7, label=t)
            ax5.set_title("Lap vs Full Race Distribution")
            ax5.set_xlabel("Time (seconds)")
            ax5.set_ylabel("Frequency")
            ax5.legend()
            st.pyplot(fig5, use_container_width=False)


css = '''
    <style>
        /* Ajusta el tamaño del texto en las pestañas (Tabs) */
        .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
            font-size: 1.5rem; /* Tamaño del texto en las pestañas */
        }

        /* Opción adicional: Ajusta el tamaño de los encabezados dentro de los expanders */
        .st-expander h1, .st-expander h2, .st-expander h3 {
            font-size: 4rem; /* Tamaño de los encabezados dentro de los expanders */
        }

        /* Ajustar el tamaño del texto del selectbox en el sidebar */
        .sidebar .stSelectbox label {
            font-size: 1.5rem; /* Ajusta este valor para cambiar el tamaño del texto */
        }

    </style>
    '''

st.markdown(css, unsafe_allow_html=True)