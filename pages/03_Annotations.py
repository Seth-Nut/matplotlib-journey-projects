# 03 Annotations


import streamlit as st

st.set_page_config(
    page_title="Annotations",
    page_icon="3️⃣",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("# Annotations")

# Tab menu
tab_project, tab_solution,= st.tabs( 
    ["🛠️ Project", "✅ Solution"]
)

with tab_project:
    st.markdown("""## Project""")

    with tab_project:
        st.markdown("""
        ## Project

        Congratulations on completing the **third module** of your Matplotlib Journey! You now have all the tools you need to create **truly inspiring charts**.

        As always, let's put those skills to work with real-life datasets, reinforcing your knowledge and preparing you to create impactful visualizations.

        ### 💾 Datasets
        This project introduces **three new datasets**. All datasets can be found on the Matplotlib Journey [dataset repository](https://github.com/JosephBARBIERDARNAL/data-matplotlib-journey).


        """)

        # Tab menu
        tab1, tab2, tab3 = st.tabs(
            ["Video games", "Economic Measures", "Netflix Movies"] 
        )

        with tab1:
            st.markdown("""

#### 🎮 Video Games Sales


##### Description
This dataset provides the ranking and regional sales of video games that have sold over 100,000 copies as of 2016. All sales figures are in millions.

##### Columns:
- `Rank`: The ranking of the video game (e.g., 10 indicates the 10th best-selling game worldwide)
- `Name`: The title of the video game
- `Platform`: The platform on which the game was released
- `Year`: Release date of the game
- `Genre`: The genre of the game
- `Publisher`: The original publisher of the game
- `NA_Sales`: Sales in North America
- `EU_Sales`: Sales in Europe
- `JP_Sales`: Sales in Japan
- `Other_Sales`: Sales in the rest of the world
- `Global_Sales`: Total worldwide sales

##### Importing the dataset

```python
import pandas as pd
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/game-sales/game-sales.csv"
df = pd.read_csv(open_url(url))
```

##### Example Preview

| Rank | Name                  | Platform | Year | Genre       | Publisher | NA_Sales | EU_Sales | JP_Sales | Other_Sales | Global_Sales |
|------|-----------------------|----------|------|------------|-----------|----------|----------|----------|-------------|--------------|
| 1    | Wii Sports            | Wii      | 2006 | Sports     | Nintendo  | 41.49    | 29.02    | 3.77     | 8.46        | 82.74        |
| 2    | Super Mario Bros. (NES) | NES      | 1985 | Platform   | Nintendo  | 29.08    | 3.58     | 6.81     | 0.77        | 40.24        |
| 3    | Mario Kart Wii        | Wii      | 2008 | Racing     | Nintendo  | 15.85    | 12.88    | 3.79     | 3.31        | 35.82        |
| 4    | Wii Sports Resort     | Wii      | 2009 | Sports     | Nintendo  | 15.75    | 11.01    | 3.28     | 2.96        | 33.00        |
| 5    | Pokemon Red/Blue      | GB       | 1996 | Role-Playing | Nintendo | 11.27    | 8.89     | 10.22    | 1.00        | 31.37        |



        """)
        with tab2:
            st.markdown("""

#### 🌐 Evolution of Economic Measures

##### Description
This dataset includes various economic measurements for countries around the world at specific dates. Each row represents data for a single country at a given month along with the corresponding measurement values.

##### Columns:
- `country`: The name of the country or region.
- `date`: The date (always the first day of the month).
- `consumer confidence`: A standardized confidence indicator reflecting expectations for future household consumption and saving. Learn more [here](https://www.oecd.org/en/data/indicators/consumer-confidence-index-cci.html).
- `interest rates`: The interest rate set by the country's monetary authority (e.g., central bank).
- `unemployment rates`: The proportion of the labor force that is unemployed.

##### Importing the dataset

```python
import pandas as pd
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/economic/economic.csv"
df = pd.read_csv(open_url(url))
```

##### Example Preview

| Country   | Date       | Consumer Confidence | Interest Rates | Unemployment Rate |
|-----------|-----------|---------------------|---------------|-------------------|
| Australia | 2020-01-01 | 93.4                | 0.75          | 5.2               |
| Australia | 2020-02-01 | 95.5                | 0.75          | 5.1               |
| Australia | 2020-03-01 | 91.9                | 0.50          | 5.2               |
| Australia | 2020-04-01 | 75.6                | 0.25          | 6.3               |
| Australia | 2020-05-01 | 88.1                | 0.25          | 7.0               |
| Australia | 2020-06-01 | 93.7                | 0.25          | 7.4               |

        """)
        with tab3:
            st.markdown("""

#### 🎬🍿 Netflix Movies


##### Description
Each row in this dataset represents a movie on Netflix, providing extensive details such as its release date, duration, description, and more.

While working with the qualitative columns may require some data wrangling, a bit of effort (and perhaps a cup of coffee) should make it an achievable task! ☕  

##### Columns:
- `show_id`: A unique identifier for the movie, distinct for every row.
- `title`: The title of the movie.
- `director`: The director of the movie.
- `cast`: The actors featured in the movie.
- `country`: The country where the movie was produced.
- `date_added`: The date when the movie was added to Netflix.
- `release_year`: The actual year the movie was released.
- `rating`: The TV rating of the movie.
- `duration`: The duration of the movie (in minutes).
- `listed_in`: The categories or genres of the movie.
- `description`: A brief description of the movie.

##### Importing the dataset

```python
import pandas as pd
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/netflix/netflix.csv"
df = pd.read_csv(open_url(url))
```

##### Example Preview

| Show ID | Title        | Director        | Country             | Release Year | Rating | Duration | Genre                          |
|---------|-------------|-----------------|----------------------|--------------|--------|----------|--------------------------------|
| s8      | Sankofa     | Haile Gerima    | USA, Ghana, UK, etc. | 1993         | TV-MA  | 125 min  | Dramas, Independent, International |
| s10     | The Starling | Theodore Melfi | United States        | 2021         | PG-13  | 104 min  | Comedies, Dramas              |
| s13     | Je Suis Karl | Christian Schwochow | Germany, Czech Republic | 2021 | TV-MA  | 127 min  | Dramas, International Movies |
| s25     | Jeans       | S. Shankar      | India                | 1998         | TV-14  | 166 min  | Comedies, Romantic Movies     |
| s28     | Grown Ups   | Dennis Dugan    | United States        | 2010         | PG-13  | 103 min  | Comedies                      |
| s29     | Dark Skies  | Scott Stewart   | United States        | 2013         | PG-13  | 97 min   | Horror, Sci-Fi & Fantasy      |



        """)


with tab_solution:
    st.markdown("""## Solution""")
    # Tab menu
    tab1, tab2, tab3 = st.tabs(
        ["Video games", "Economic Measures", "Netflix Movies"] 
    )
    with tab1:
        st.markdown("""
        """)
    with tab2:
        st.markdown("""
        """)
    with tab3:
        st.markdown("""
        """)

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