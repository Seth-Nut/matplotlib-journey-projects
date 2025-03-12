# 02 Beyond The Defaults
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from pypalettes import load_cmap


st.set_page_config(
    page_title="Beyond the defaults",
    page_icon="2️⃣",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("# Beyond the defaults")

# Tab menu
tab_project, tab_solution,= st.tabs( 
    ["🛠️ Project", "✅ Solution"]
)

with tab_project:
    st.markdown("""
    ## Project
    Congratulations on completing the **second module** of your Matplotlib journey! 🎉

    You're now equipped to go **beyond the default** Matplotlib charts! To reinforce this knowledge, let's dive into some real-world datasets to use your **creativity** and **coding** skills.

    ### 💾 Datasets
    This project introduces **three new datasets**. All datasets can be found on the Matplotlib Journey [dataset repository](https://github.com/JosephBARBIERDARNAL/data-matplotlib-journey).

                
    """)

    # Tab menu
    tab1, tab2, tab3 = st.tabs(
        ["Natural disasters", "Wine quality", "New York Airbnb"] 
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

    st.markdown("### 🎮 Your Turn!")

    # 1. Reproduce a chart 
    with st.expander("Reproduce a Chart"):
        st.markdown("""
        **Dataset:** Natural Disasters  
        **Instructions:**
        - Use the [Antique palette](https://python-graph-gallery.com/color-palette-finder/?palette=antique) from `pypalettes`.
        - Shift the y-axis from the left to the right using `ax.yaxis.tick_right()`.
        - For the legend, add `labels=columns` in the plotting function and call `ax.legend(reverse=True, loc=\"center left\")`.
        """)

    # 2. Reproduce another chart 
    with st.expander("Reproduce Another Chart"):
        st.markdown("""
        **Dataset:** New York Airbnb  
        - No special instructions are needed for this chart.  
        - The challenge is to add labels with the correct formatting.
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
    with st.expander("Reproduce Natural Disasters Chart"):
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/natural-disasters/natural-disasters.csv"
        df = pd.read_csv(url)

        columns = df.drop(columns="Year").sum().sort_values().index.to_list()
        x = df["Year"]
        y = np.stack(df[columns].values, axis=-1)

        fig, ax = plt.subplots(figsize=(10, 5))

        # Manually defined antique-like palette
        antique_palette = ["#8B7E66", "#B29F7E", "#D2B48C", "#F5DEB3", "#FFE4C4"]

        ax.stackplot(x, y, colors=antique_palette, labels=columns)
        ax.set_xlim(1960, 2023)
        ax.spines[["top", "left"]].set_visible(False)
        ax.yaxis.tick_right()
        ax.text(
            x=1960,
            y=380,
            s="Evolution of natural disasters between 1960 and 2023",
            size=12,
        )
        ax.text(x=1960, y=355, s="Data source: EM-DAT")
        ax.legend(reverse=True, loc="center left")
        ax.set_xticks([1960, 1980, 2000, 2020])
        ax.set_yticks([100, 200, 300, 400])
        ax.tick_params(length=0, pad=5)

        st.pyplot(fig)
             
    # 2. Reproduce another chart 
    with st.expander("Reproduce New York Airbnb Chart"):
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/newyork-airbnb/newyork-airbnb.csv"
        df = pd.read_csv(url)

        df_agg = (
            df["neighbourhood"]
            .value_counts()
            .head(10)
            .to_frame(name="count")
            .reset_index()
            .rename(columns={"index": "neighbourhood"})
            .sort_values("count")
        )
        labels = df_agg["neighbourhood"]
        values = df_agg["count"]

        fig, ax = plt.subplots(layout="tight")

        color_mapping = {True: "#2d8653", False: "#d6d6d6"}
        colors = labels == "Williamsburg"
        colors = colors.map(color_mapping)

        ax.barh(labels, values, color=colors)
        ax.set_xticks([])
        ax.spines[["top", "right", "left", "bottom"]].set_visible(False)
        ax.tick_params(length=0)

        ax.text(
            x=3920 / 2,
            y=10.5,
            s="New York neighbourhood with the most Airbnbs",
            ha="center",
            va="top",
            size=14,
        )

        for i in range(len(values)):
            value = values[i]
            color = "white" if i == 0 else "black"
            format_value = f"{value / 1000:.1f}k"
            ax.text(
                x=value - 350, y=len(values) - 1 - i, s=format_value, va="center", color=color
            )

        st.pyplot(fig)

    # 3. Improve a chart
    with st.expander("Improve a Chart"):
        # Load the dataset
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/wine/wine.csv"
        df = pd.read_csv(url)

        # Select only numeric columns
        df_numeric = df.select_dtypes(include=[np.number])

        # Compute the correlation matrix
        corr = df_numeric.corr()

        # Create a mask for the upper triangle
        mask = np.triu(np.ones_like(corr, dtype=bool))


        # Create a custom diverging color palette
        cmap = sns.diverging_palette(240, 10, as_cmap=True)

        # Plot the heatmap
        fig, ax = plt.subplots(figsize=(12, 10))
        sns.heatmap(
            corr,
            mask=mask,
            cmap=cmap,
            vmax=1,
            vmin=-1,
            center=0,
            annot=True,
            fmt=".2f",
            square=True,
            linewidths=.5,
            cbar_kws={"shrink": .75, "label": "Correlation"},
            annot_kws={"size": 12, "weight": "bold", "color": "black"},
            ax=ax
        )

        # Set title and layout
        ax.set_title("Wine Correlation Heatmap", fontsize=18, weight='bold', pad=20)
        plt.xticks(rotation=45, ha='right', fontsize=12)
        plt.yticks(fontsize=12)
        plt.tight_layout()

        # Display the heatmap in Streamlit
        st.pyplot(fig)

    # 4. Improve another chart
    with st.expander("Improve Another Chart"):

        # Load data
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/wine/wine.csv"
        df = pd.read_csv(url)

        # Compute correlations and select the top correlated feature with 'quality'
        corr = df.corr(numeric_only=True)
        sorted_corr = corr['quality'].sort_values(ascending=False)
        best_feature = sorted_corr.index[1]

        # Define a custom palette with enough colors
        unique_qualities = df['quality'].nunique()
        custom_palette = sns.color_palette("coolwarm", n_colors=unique_qualities)

        # Create the figure
        fig, ax = plt.subplots(figsize=(14, 8))

        # Create the violin plot with 'hue'
        sns.violinplot(
            x='quality',
            y=best_feature,
            data=df,
            hue='quality',
            palette=custom_palette,
            inner=None,
            linewidth=2,
            saturation=0.9,
            ax=ax,
            legend=False  # Disable the redundant hue legend
        )

        # Add custom annotations for median values
        medians = df.groupby('quality')[best_feature].median()
        for i, median in enumerate(medians):
            ax.text(i, median + 0.02, f'{median:.2f}', ha='center', va='center', 
                    fontweight='bold', fontsize=12, color='black', 
                    bbox=dict(facecolor='white', alpha=0.6, boxstyle='round,pad=0.3'))

        # Highlight max and min points for each quality score
        grouped = df.groupby('quality')[best_feature]
        max_points = grouped.max()
        min_points = grouped.min()

        ax.scatter(max_points.index - 1, max_points.values, color='green', label='Max', s=100, marker='^', edgecolor='k')
        ax.scatter(min_points.index - 1, min_points.values, color='red', label='Min', s=100, marker='v', edgecolor='k')

        # Customize grid and borders
        ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
        for spine in ax.spines.values():
            spine.set_visible(True)
            spine.set_linewidth(1.2)
            spine.set_edgecolor('gray')

        # Titles and axis labels
        ax.set_title(f"Enhanced Distribution of '{best_feature}' Across Wine Quality Scores", fontsize=18, weight='bold', pad=20)
        ax.set_xlabel("Wine Quality (Score)", fontsize=14, weight='bold')
        ax.set_ylabel(f"{best_feature.capitalize()} Value", fontsize=14, weight='bold')

        # Add legend
        ax.legend(title="Highlights", fontsize=12)

        # Final layout adjustment
        plt.tight_layout()

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