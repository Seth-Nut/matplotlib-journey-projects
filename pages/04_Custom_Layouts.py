# 04 Custom Layouts

import streamlit as st

st.set_page_config(
    page_title="Custom Layouts",
    page_icon="4️⃣",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("# Custom Layouts")

# Tab menu
tab_project, tab_solution,= st.tabs( 
    ["🛠️ Project", "✅ Solution"]
)

with tab_project:
    st.markdown("""
    ## Project
    Congrats on completing this module on **complex layouts**! You've moved beyond basic single-chart designs and unlocked powerful techniques like **small multiples**. 

    Now, let's put your skills to the test with real-world datasets, ensuring you're ready to apply them in practice!
    
    ### 💾 Datasets
    For this project, we'll use datasets from module 2 and 3. Remember that you can find and download the datasets [here](https://github.com/JosephBARBIERDARNAL/data-matplotlib-journey).

                
    """)

    # Tab menu
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Natural disasters", "Wine", "Airbnb",
         "Video games", "Economic", "Netflix"] 
    )

    with tab1:
        st.markdown("""
#### 🌪️ Frequency of Natural Disasters

##### Description

This dataset is sourced from [EM-DAT](https://www.emdat.be/), the international disaster database and a leading center for research on the epidemiology of disasters. It contains information about various natural disasters that occurred between 1960 and 2023.

- The `Year` column indicates the year of each event.
- Other columns represent different types of natural disasters.

##### Importing the Dataset

To work with the dataset, you can use the following Python code:

```python
import pandas as pd
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/natural-disasters/natural-disasters.csv"
df = pd.read_csv(open_url(url))
```

##### Preview of the Dataset

| Year | Drought | Earthquake | Extreme temperature | Extreme weather | Flood | Volcanic activity | Wet mass movement | Wildfire |
|------|---------|------------|----------------------|-----------------|-------|-------------------|-------------------|----------|
| 1960 | 1.0     | 8.0        | 14.0                | 20.0           | 8.0   | 1.0               | 2.0               | 2.0      |
| 1961 | 1.0     | 3.0        | 1.0                 | 14.0           | 9.0   | 5.5               | 2.0               | 2.0      |
| 1962 | 1.0     | 4.0        | 1.0                 | 13.0           | 8.0   | 5.0               | 2.0               | 2.0      |
| 1963 | 1.0     | 3.0        | 2.0                 | 21.0           | 8.0   | 3.0               | 2.0               | 2.0      |
| 1964 | 8.0     | 7.0        | 14.5                | 22.0           | 22.0  | 1.0               | 1.0               | 1.0      |
| 1965 | 7.0     | 8.0        | 1.0                 | 19.0           | 19.0  | 1.0               | 6.0               | 1.0      |

                   

##### Interesting Questions to Explore

To spark your curiosity, here are some questions you might explore:

- Which years saw the highest number of reported storms?
- What type of storm occurs most frequently, and does this change over time?
- Are there years that display notable patterns?
- Is there a discernible trend?
- Which decade stands out as the worst in terms of natural disasters?

                    
        """)

    with tab2:
        st.markdown("""

#### 🍷 Wine Quality



##### Description
This dataset originates from [a 2009 research paper](https://archive.ics.uci.edu/dataset/186/wine+quality) focused on wine quality.

It contains data on various wines, detailing their characteristics and quality.  
Each row represents a single wine, listing the values of its features along with its quality score, which ranges from 3 to 9.

##### Import the dataset
```python
import pandas as pd
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/wine/wine.csv"
df = pd.read_csv(open_url(url))
```

##### Preview
| Fixed Acidity | Volatile Acidity | Citric Acid | Residual Sugar | Chlorides | Free Sulfur Dioxide | Total Sulfur Dioxide | Density | pH  | Sulphates | Alcohol | Quality |
|---------------|------------------|-------------|----------------|-----------|---------------------|----------------------|---------|------|-----------|---------|---------|
| 11.6          | 0.58            | 0.66        | 2.2            | 0.074     | 10.0                | 47.0                 | 1.0008  | 3.25 | 0.57      | 9.0     | 3       |
| 10.4          | 0.61            | 0.49        | 2.1            | 0.200     | 5.0                 | 16.0                 | 0.9994  | 3.16 | 0.63      | 8.4     | 3       |

##### Interesting Questions
- Which characteristic most strongly influences wine quality?
- What distinguishes a "good" wine from a "bad" one?
- Which characteristic has the least effect on wine quality?
- Are there any features that exhibit a high degree of correlation?


        """)

    with tab3:
        st.markdown("""

#### 🗽 New York Airbnb



##### Description
The data comes from [Inside Airbnb](https://insideairbnb.com/), a website that aggregates Airbnb data.  
Each row represents an Airbnb listing in New York, including details such as name, price, location, and more.

##### Import the dataset
```python
import pandas as pd
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/newyork-airbnb/newyork-airbnb.csv"
df = pd.read_csv(open_url(url))
```

##### Preview
| id   | name                                     | neighbourhood_group | neighbourhood | room_type        | price | minimum_nights | number_of_reviews | availability_365 |
|------|------------------------------------------|---------------------|---------------|------------------|-------|----------------|--------------------|------------------|
| 2539 | Clean & quiet apt home by the park       | Brooklyn            | Kensington    | Private room     | 149   | 1              | 9                  | 365              |
| 2595 | Skylit Midtown Castle                   | Manhattan           | Midtown       | Entire home/apt  | 225   | 1              | 45                 | 355              |
| 3647 | THE VILLAGE OF HARLEM....NEW YORK !     | Manhattan           | Harlem        | Private room     | 150   | 3              | 0                  | 365              |

##### Interesting Questions
To spark your curiosity, here is a non-exhaustive list of compelling questions you might explore:
- Which neighborhoods are the most and least expensive?
- What factors most significantly determine the price of an Airbnb?
- What are the most common names among guests or hosts?
- Do certain names correlate with better or worse reviews?
- Is price a reliable indicator of quality, such as good reviews?


        """)
        with tab4:
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
        with tab5:
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
        with tab6:
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