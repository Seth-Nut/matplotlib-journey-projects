# 02 Beyond The Defaults

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

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


with tab_solution:
    st.markdown("""## Solution""")

        
    # Tab menu
    tab1, tab2, tab3 = st.tabs(
        ["Natural disasters", "Wine quality", "New York Airbnb"] 
    )

    with tab1:

        # Load the dataset
        url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/natural-disasters/natural-disasters.csv"
        df_disasters = pd.read_csv(url)

        # Streamlit layout
        st.markdown("### 🌪️ Frequency of Natural Disasters")
        st.markdown(
            "This dataset is sourced from [EM-DAT](https://www.emdat.be/), the international disaster database."
        )

        # Dropdown menu for selecting the question
        selected_question = st.radio(
            "Select a question to explore the data:",
            (
                "Which years saw the highest number of reported storms?",
                "What type of storm occurs most frequently, and does this change over time?",
                "Are there years that display notable patterns?",
                "Is there a discernible trend?",
                "Which decade stands out as the worst in terms of natural disasters?",
            ),
        )

        # 1. Which years saw the highest number of reported storms?
        if selected_question == "Which years saw the highest number of reported storms?":
            total_disasters_year = df_disasters.iloc[:, 1:].sum(axis=1)
            top_years = total_disasters_year.nlargest(10).sort_values(ascending=False)
            fig1, ax1 = plt.subplots(figsize=(5, 3))  # Smaller size
            ax1.bar(top_years.index, top_years.values, color="blue", edgecolor="black")
            ax1.set_title("Top Years with Highest Number of Reported Storms")
            ax1.set_xlabel("Year")
            ax1.set_ylabel("Total Disasters")
            st.pyplot(fig1, use_container_width=True)

        # 2. What type of storm occurs most frequently, and does this change over time?
        elif selected_question == "What type of storm occurs most frequently, and does this change over time?":
            total_by_type = df_disasters.iloc[:, 1:].sum()
            fig2, ax2 = plt.subplots(figsize=(5, 3))  # Smaller size
            ax2.bar(total_by_type.index, total_by_type.values, color="green", edgecolor="black")
            ax2.set_title("Most Frequent Storm Types")
            ax2.set_xlabel("Storm Type")
            ax2.set_ylabel("Total Occurrences")
            st.pyplot(fig2, use_container_width=True)
            st.write("The chart above shows the most frequent storm types overall.")

            # Trends over time for each storm type
            fig3, ax3 = plt.subplots(figsize=(6, 3))  # Smaller size
            for disaster_type in df_disasters.columns[1:]:
                ax3.plot(
                    df_disasters["Year"],
                    df_disasters[disaster_type],
                    label=disaster_type,
                    marker="o",
                    markersize=4,
                    linewidth=1.5,
                )
            ax3.set_title("Trends of Storm Types Over Time")
            ax3.set_xlabel("Year")
            ax3.set_ylabel("Number of Occurrences")
            ax3.legend(fontsize="small")
            st.pyplot(fig3, use_container_width=True)

        # 3. Are there years that display notable patterns?
        elif selected_question == "Are there years that display notable patterns?":
            fig4, ax4 = plt.subplots(figsize=(6, 3))  # Smaller size
            disaster_pivot = df_disasters.set_index("Year").T
            sns.heatmap(
                disaster_pivot,
                cmap="coolwarm",
                annot=False,
                ax=ax4,
                cbar_kws={"label": "Occurrences"},
            )
            ax4.set_title("Heatmap of Disaster Occurrences by Year and Type")
            st.pyplot(fig4, use_container_width=True)

        # 4. Is there a discernible trend?
        elif selected_question == "Is there a discernible trend?":
            total_disasters_year = df_disasters.iloc[:, 1:].sum(axis=1)
            fig5, ax5 = plt.subplots(figsize=(5, 3))  # Smaller size
            ax5.plot(
                df_disasters["Year"],
                total_disasters_year,
                marker="o",
                color="purple",
                linewidth=1.5,
            )
            ax5.set_title("Trend of Total Natural Disasters Over Time")
            ax5.set_xlabel("Year")
            ax5.set_ylabel("Total Disasters")
            st.pyplot(fig5, use_container_width=True)

        # 5. Which decade stands out as the worst in terms of natural disasters?
        elif selected_question == "Which decade stands out as the worst in terms of natural disasters?":
            df_disasters["Decade"] = (df_disasters["Year"] // 10) * 10
            total_by_decade = df_disasters.groupby("Decade").sum().iloc[:, :-1].sum(axis=1)
            fig6, ax6 = plt.subplots(figsize=(5, 3))  # Smaller size
            ax6.bar(total_by_decade.index, total_by_decade.values, color="red", edgecolor="black")
            ax6.set_title("Total Disasters Per Decade")
            ax6.set_xlabel("Decade")
            ax6.set_ylabel("Total Disasters")
            st.pyplot(fig6, use_container_width=True)


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