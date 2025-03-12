# 04 Custom Layouts
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from pypalettes import load_cmap
from highlight_text import ax_text, fig_text


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

    st.markdown("### 🎮 Your Turn!")

    # 1. Reproduce a chart 
    with st.expander("Reproduce a Chart"):
        st.markdown("""
        **Dataset:** Video Games  
                    
        **Instructions:**      
        - Sometimes, you may need to create charts with **extreme aspect ratios**, as shown here.
        - Notice that both charts share the **same X-axis limits**, enabling a quick comparison between the two datasets. You can achieve this using the `set_xlim` function.
        """)

    # 2. Small multiple with title in the middle
    with st.expander("Small multiple with title in the middle"):
        st.markdown("""
        **Dataset:** Natural Disasters
                    
        **Instructions:** 
        - Mastering small multiples is essential for effective data visualization. This technique enhances clarity by organizing data into separate, easily comparable panels.
        - Use the `subplots_adjust` function to add space between rows, making room for titles and improving readability.
        """)

    # 3. Partial small multiple
    with st.expander("Partial small multiple"):
        st.markdown("""
        **Dataset:** Economic Measures
                    
        **Instructions:** 
        - Small multiples are a powerful dataviz technique.
        - Instead of overcrowding a single chart with all groups, splitting them into separate panels makes comparisons clearer and more insightful.
        """)



with tab_solution:
    st.markdown("""## Solution""")
    # 1. Reproduce a chart 
    with st.expander("Reproduce a Chart"):
        # Load the dataset
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/game-sales/game-sales.csv"
        df = pd.read_csv(url)

        # Data Cleaning and Grouping
        df = df.replace({
            "Konami Digital Entertainment": "Konami",
            "Take-Two Interactive": "Take-Two",
            "Sony Computer Entertainment": "Sony",
            "Microsoft Game Studios": "Microsoft",
            "Virgin Interactive": "Virgin",
            "Eidos Interactive": "Eidos",
            "Acclaim Entertainment": "Acclaim",
            "Namco Bandai Games": "Namco",
        })

        # Group data for 1990s
        df1990 = df[(df["Year"] >= 1990) & (df["Year"] < 2000)]
        df1990 = (
            df1990.groupby("Publisher", as_index=False)["Global_Sales"]
            .sum()
            .sort_values("Global_Sales", ascending=False)[:10]
            .reset_index()
            .drop("index", axis=1)
        )

        # Group data for 2000s
        df2000 = df[(df["Year"] >= 2000) & (df["Year"] < 2010)]
        df2000 = (
            df2000.groupby("Publisher", as_index=False)["Global_Sales"]
            .sum()
            .sort_values("Global_Sales", ascending=False)[:10]
            .reset_index()
            .drop("index", axis=1)
        )

        # Load color palette
        colors = load_cmap("Antique").colors
        col1, col2 = colors[0], colors[1]

        # Create the figure
        fig, axs = plt.subplots(nrows=2, figsize=(5, 9))
        fig.subplots_adjust(hspace=0.07, top=0.85)

        # Plot for 1990s
        axs[0].barh(df1990["Publisher"], df1990["Global_Sales"], color=col1)
        axs[0].set_xticks([0, 200, 400, 600, 800], labels=["", "", "", "", ""])
        ax_text(
            x=200,
            y=8,
            s="Overall sales during the <90s>",
            ax=axs[0],
            highlight_textprops=[{"color": col1, "weight": "bold"}],
        )

        # Plot for 2000s
        axs[1].barh(df2000["Publisher"], df2000["Global_Sales"], color=col2)
        axs[1].set_xticks([200, 400, 600, 800], labels=["200M", "400M", "600M", "800M"], size=8)
        ax_text(
            x=200,
            y=8,
            s="Overall sales during the <2000s>",
            ax=axs[1],
            highlight_textprops=[{"color": col2, "weight": "bold"}],
        )

        # Customizing the subplots
        for ax in axs:
            ax.set_xlim(0, 890)
            ax.spines[["top", "right", "left"]].set_visible(False)
            ax.grid(axis="x", color="grey", lw=0.5, alpha=0.3, zorder=-1)
            ax.tick_params(length=0)
            ax.set_yticks([])

        # Adding text labels
        for i, row in df1990.iterrows():
            company = row["Publisher"]
            value = row["Global_Sales"]
            axs[0].text(x=value + 10, y=i, s=company, va="center", size=7)

        for i, row in df2000.iterrows():
            company = row["Publisher"]
            axs[1].text(x=7, y=i, s=company, va="center", size=7)

        # Adding a global title
        fig.text(x=0.5, y=0.88, s="Video games Sales by major publishers", ha="center", size=14)

        # Display the plot in Streamlit
        st.pyplot(fig)

    # 2. Small multiple with title in the middle
    with st.expander("Small multiple with title in the middle"):


        # Load the dataset
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/natural-disasters/natural-disasters.csv"
        df = pd.read_csv(url)

        # Drop less relevant columns
        df = df.drop(columns=["Volcanic activity", "Wildfire"])

        # Load color palette
        colors = load_cmap("Antique").colors

        # Define events for visualization
        events = [
            "Flood",
            "Extreme weather",
            "Earthquake",
            "Extreme temperature",
            "Drought",
            "Wet mass movement",
        ]

        # Create subplots
        fig, axs = plt.subplots(ncols=3, nrows=2, figsize=(10, 6))
        fig.subplots_adjust(hspace=0.5)

        # Plot data for each event
        for ax, event, color in zip(axs.flat, events, colors):
            for sub_event in events:
                ax.plot(
                    df["Year"], df[sub_event], color="grey", alpha=0.2, zorder=1, linewidth=0.7
                )

            # Highlight the main event in each subplot
            ax.plot(df["Year"], df[event], color=color, zorder=5, linewidth=0.9)
            ax.spines[["top", "right"]].set_visible(False)
            ax.tick_params(length=0, labelsize=6)
            ax.set_ylim(0, 235)
            ax.set_xlim(1960, 2023)
            ax.text(x=1962, y=150, s=event.title(), size=9, color=color, weight="bold")

            # Customize y-axis
            if event not in ["Flood", "Extreme temperature"]:
                ax.spines["left"].set_visible(False)
                ax.set_yticks([])
            else:
                ax.set_yticks([50, 100, 150, 200])

            # Customize x-axis
            if event not in ["Extreme temperature", "Drought", "Wet mass movement"]:
                ax.set_xticks([])

        # Add overall annotation using fig_text
        fig_text(
            x=0.5,
            y=0.53,
            s="<Flood> and <Extreme Weather> are the most\nfrequent natural disasters since the 60s.",
            size=13,
            weight="bold",
            ha="center",
            highlight_textprops=[
                {"color": colors[0]},
                {"color": colors[1]},
            ],
        )

        # Display the plot in Streamlit
        st.pyplot(fig)


    # 3. Partial small multiple
    with st.expander("Partial small multiple"):
        # Load the dataset
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/economic/economic.csv"
        df = pd.read_csv(url)

        # Data Cleaning and Transformation
        df = df[~df["country"].isin(["europe", "new zealand"])]
        df["country"] = df["country"].replace({"united states": "US", "united kingdom": "UK"})
        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")

        # Define colors and styles
        grey_lines_color = "#7c7c7c"
        background_color = "#191c3b"
        color_mapping = {
            "china": "#e84f4f",
            "switzerland": "#4bcf82",
            "japan": "#de5fee",
            "australia": "#786cf3",
        }

        # Create the figure and subplots
        fig, axs = plt.subplots(ncols=2, nrows=2, figsize=(10, 10))
        fig.set_facecolor(background_color)

        # Loop through each subplot and country
        for ax in axs.flat:
            for country in df["country"].unique():
                subset = df[df["country"] == country]
                x = subset["date"]
                y = subset["interest rates"]

                last_date = x.values[-1] + pd.Timedelta(days=25)
                last_value = y.values[-1]

                # Define styles based on country and subplot
                if country == "china" and ax == axs[0, 0]:
                    text_style = dict(color=color_mapping[country])
                    plot_style = dict(zorder=5, linewidth=2, color=color_mapping[country])

                elif country == "switzerland" and ax == axs[0, 1]:
                    text_style = dict(color=color_mapping[country])
                    plot_style = dict(zorder=5, linewidth=2, color=color_mapping[country])

                elif country == "japan" and ax == axs[1, 0]:
                    text_style = dict(color=color_mapping[country])
                    plot_style = dict(zorder=5, linewidth=2, color=color_mapping[country])

                elif country == "australia" and ax == axs[1, 1]:
                    text_style = dict(color=color_mapping[country])
                    plot_style = dict(zorder=5, linewidth=2, color=color_mapping[country])

                else:
                    text_style = dict(color=grey_lines_color)
                    plot_style = dict(color=grey_lines_color)

                # Plotting
                ax.plot(x, y, **plot_style)
                ax.text(x=last_date, y=last_value, s=country.upper(), va="center", **text_style)

                # Customize the x-axis
                ax.set_xticks(["2020-01-01", "2022-01-01", "2024-01-01"], labels=[2020, 2022, 2024])
                ax.tick_params(length=3, labelcolor="#c3c3c3", labelsize=8, color="white")

                # Customize spines and background
                ax.spines[["top", "right"]].set_visible(False)
                ax.spines[["top", "right", "left", "bottom"]].set_color("white")
                ax.set_facecolor(background_color)

        # Hide left spine and y-ticks for certain subplots
        axs[0, 1].spines["left"].set_visible(False)
        axs[1, 1].spines["left"].set_visible(False)
        axs[0, 1].set_yticks([])
        axs[1, 1].set_yticks([])

        # Add main title
        fig.text(
            x=0.13, y=0.92, s="Interest Rates, from 2020 to 2024",
            size=18, color="#e2e2e2"
        )

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