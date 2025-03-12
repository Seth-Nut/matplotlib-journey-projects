# 03 Annotations
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from highlight_text import ax_text
from drawarrow import ax_arrow

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
            
    st.markdown("### 🎮 Your Turn!")

    # 1. Reproduce a chart 
    with st.expander("Reproduce a Chart"):
        st.markdown("""
        **Dataset:** Economic Measures 
                    
        **Instructions:**      
        - The color for the USA is **#ae2f2f** and for Japan it's **#44487e**. Background color is **#fffaf4** and other colors are either black or nuances of this lightgrey: **#b9b9b9**
        - Outside of this, there's nothing magic to do here. Always keep in mind that there are multiple ways to do the same thing with matplotlib.
        - As long as your solution looks like the goal, you're good to go!
        """)

    # 2. Reproduce another chart 
    with st.expander("Reproduce Another Chart"):
        st.markdown("""
        **Dataset:** Economic Measures 
                    
        **Instructions:** 
                    
        - Background color is **#3f3f3f** and the dots are in **#a2a2bf**. Other colors are either white or gray/lightgray.
        """)

    # 3. Improve a chart
    with st.expander("Improve a Chart"):
        st.markdown("""
        *(Complete details here)*
        """)

    # 4. Improve another chart
    with st.expander("Improve Another Chart"):
        st.markdown("""
        *(Complete details here)*
        """)


with tab_solution:
    st.markdown("""## Solution""")

    # 1. Reproduce a chart 
    with st.expander("Reproduce a Chart"):
        # Load the data
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/economic/economic.csv"
        df = pd.read_csv(url)

        # Calculate max unemployment rate for the USA
        max_usa = df.loc[df["country"] == "united states", "unemployment rate"].max()

        # Define colors
        us_color = "#ae2f2f"
        japan_color = "#44487e"

        # Create the figure and axis
        fig, ax = plt.subplots()
        fig.subplots_adjust(hspace=1)
        ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
        ax.set_facecolor("#fffaf4")
        fig.set_facecolor("#fffaf4")
        ax.tick_params(size=0)
        ax.set_xticks([])
        ax.set_ylim(0, 15.5)
        ax.grid(axis="y", color="#dfdfdf", linewidth=0.4, zorder=2)

        # Plot the data for each country
        for country in df["country"].unique():
            subset = df[df["country"] == country]
            x = subset["date"]
            y = subset["unemployment rate"]

            if country == "united states":
                style = dict(color=us_color, zorder=10, lw=2.2)
            elif country == "japan":
                style = dict(color=japan_color, zorder=10, lw=2.2)
            else:
                style = dict(color="#b6b5b5", zorder=4, lw=0.8)
            ax.plot(x, y, **style)

        # Add custom text annotations
        text_style = dict(y=-0.8, ha="center", size=7, color="#b4b4b4")
        ax.text(x="2020-01-01", s="Jan 2020", **text_style)
        ax.text(x="2023-12-01", s="Dec 2023", **text_style)

        # Highlighted annotations using highlight_text
        ax_text(
            x="2020-07-01",
            y=13.7,
            s=f"The <USA> had a peak unemployment\nrate of <{max_usa}%> in April 2020.",
            highlight_textprops=[{"color": us_color, "weight": "bold"}, {"weight": "bold"}],
            size=9,
        )

        ax_text(
            x="2021-04-01",
            y=1.5,
            s="<Japan> has maintained a very low unemployment\nrate during the entire period.",
            highlight_textprops=[{"color": japan_color, "weight": "bold"}],
            size=9,
        )

        # Add titles and subtitles
        fig.text(x=0.5, y=0.94, s="Unemployment rates during COVID-19", ha="center", size=18)
        fig.text(
            x=0.5,
            y=0.9,
            s="From January 2020 to December 2023",
            color="#b9b9b9",
            weight="light",
            ha="center",
            size=10,
        )

        # Display the plot in Streamlit
        st.pyplot(fig)

    # 2. Reproduce another chart
    with st.expander("Reproduce Another Chart"):

        # Load the data
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/economic/economic.csv"
        df = pd.read_csv(url)

        # Filter data for the chosen date
        chosen_date = "2020-04-01"
        df = df[df["date"] == chosen_date]
        df = df.sort_values("date")

        # Create the figure and axis
        fig, ax = plt.subplots()
        fig.set_facecolor("#3f3f3f")
        ax.set_facecolor("#3f3f3f")

        # Scatter plot for consumer confidence vs unemployment rate
        ax.scatter(
            df["consumer confidence"],
            df["unemployment rate"],
            s=300,
            edgecolor="white",
            color="#a2a2bf",
        )

        # Add country labels to the plot
        for country in df["country"].unique():
            x = df.loc[df["country"] == country, "consumer confidence"].values[0]
            y = df.loc[df["country"] == country, "unemployment rate"].values[0]
            ax.text(x=x + 6, y=y - 0.5, s=country.title(), va="center", color="white")

        # Add arrows using drawarrow
        ax_arrow([-61, 1.5], [130, 1.5], color="white", fill_head=False)
        ax_arrow([-60, 1.4], [-60, 15], color="white", fill_head=False)

        # Hide axis spines and customize ticks
        ax.spines[["bottom", "left", "top", "right"]].set_visible(False)
        ax.tick_params(size=0, pad=-8, labelsize=9, labelcolor="white")

        # Add axis labels
        ax.text(x=100, y=2, s="Consumer confidence", color="#d9d9d9", size=6, style="italic")
        ax.text(x=-55, y=14, s="Unemployment rates", color="#d9d9d9", size=6, style="italic")

        # Add title
        ax.text(
            x=35,
            y=16,
            s="Unemployment rates and Consumer confidence\nduring peak COVID (April 2020)",
            ha="center",
            weight="bold",
            size=12,
            color="white",
        )

        # Display the plot in Streamlit
        st.pyplot(fig)

    # 3. Improve a chart
    with st.expander("Improve a Chart"):
        # Load the dataset
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/game-sales/game-sales.csv"
        df = pd.read_csv(url)

        # Filter top 10 best-selling games globally
        top_10 = df.sort_values(by='Global_Sales', ascending=False).head(10)

        # Define colors
        highlight_color = "#ff6347"
        default_color = "#b6b6b6"

        # Create the figure and axis
        fig, ax = plt.subplots(figsize=(12, 8))
        ax.set_facecolor("#f0f0f0")
        fig.set_facecolor("#f0f0f0")

        # Plot the bar chart
        ax.barh(top_10['Name'], top_10['Global_Sales'], color=default_color, edgecolor='black')

        # Highlight the top-selling game
        ax.barh(top_10.iloc[0]['Name'], top_10.iloc[0]['Global_Sales'], color=highlight_color, edgecolor='black')

        # Add annotation for the top-selling game
        ax_text(
            x=top_10.iloc[0]['Global_Sales'] - 5,
            y=0,
            s=f"The top-selling game is <{top_10.iloc[0]['Name']}> with <{top_10.iloc[0]['Global_Sales']}M> copies sold globally.",
            highlight_textprops=[{"color": highlight_color, "weight": "bold"}, {"weight": "bold"}],
            size=10,
        )

        # Add custom arrows
        ax_arrow([50, 0.5], [82, 0.5], color=highlight_color, fill_head=True)

        # Titles and axis customization
        ax.set_title("Top 10 Best-Selling Video Games Globally", fontsize=16, weight='bold')
        ax.set_xlabel("Global Sales (in millions)", fontsize=12)
        ax.tick_params(axis='y', labelsize=10)
        ax.spines[['top', 'right']].set_visible(False)

        plt.tight_layout()

        # Display the plot in Streamlit
        st.pyplot(fig)

    # 4. Improve another chart
    with st.expander("Improve Another Chart"):
        # Load the dataset
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/netflix/netflix.csv"
        df = pd.read_csv(url)

        # Extract release years and count movies per year
        year_counts = df['release_year'].value_counts().sort_index()

        # Filter for the last 20+ years
        recent_years = year_counts[year_counts.index >= 2000]

        # Define colors
        colors = sns.color_palette("coolwarm", len(recent_years))

        # Create the radial bar chart
        fig, ax = plt.subplots(figsize=(10, 10), subplot_kw={'projection': 'polar'})
        ax.set_facecolor("#1f1f1f")
        fig.set_facecolor("#1f1f1f")

        # Define theta (angles) and radii (bar lengths)
        theta = [i / float(len(recent_years)) * 2 * 3.1415 for i in range(len(recent_years))]
        radii = recent_years.values

        # Plot the bars
        bars = ax.bar(theta, radii, width=0.3, color=colors, edgecolor='black', alpha=0.8)

        # Highlight the year with the maximum number of movies
        max_idx = radii.argmax()
        ax_arrow([theta[max_idx], radii[max_idx] + 5], [theta[max_idx], radii[max_idx]], color='white', fill_head=True)

        # Add annotation
        ax.text(
            theta[max_idx], radii[max_idx] + 8,
            f"Peak in {recent_years.index[max_idx]} with {radii[max_idx]} movies",
            ha='center', color='white', weight='bold'
        )

        # Customize grid and labels
        ax.set_xticks(theta)
        ax.set_xticklabels(recent_years.index, color='white', fontsize=12)
        ax.set_yticklabels([])
        ax.spines['polar'].set_visible(False)

        # Add title
        ax.set_title("Netflix Movies Released Per Year (2000-2023)", fontsize=16, color='white', weight='bold')

        # Display the plot in Streamlit
        st.pyplot(fig)


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