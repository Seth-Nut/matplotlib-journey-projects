# 05 Maps
import streamlit as st
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd
import cartopy.crs as ccrs

st.set_page_config(
    page_title="Maps",
    page_icon="5️⃣",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("# Maps")

# Tab menu
tab_project, tab_solution,= st.tabs( 
    ["🛠️ Project", "✅ Solution"]
)

with tab_project:
    st.markdown("""
    ## Project
                
    In previous lessons, you learned to create various maps using `GeoPandas` and `Matplotlib`.

    Now, in this module’s project, you'll work with a real-world dataset to **apply your skills** and create insightful maps.
    
    ### 💾 Datasets           
    For this project, we'll use a dataset about CO2 per capita dataset. You can find and download the datasets [here](https://github.com/JosephBARBIERDARNAL/data-matplotlib-journey).

                  
                """)
    
    st.markdown("""

### CO2 per Capita 

**Description:**  
This dataset provides the CO2 emissions per capita for each country in the world as of 2021, along with a breakdown of these emissions.

**Importing the Dataset:**

```python
import pandas as pd
from pyodide.http import open_url

url = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/CO2/CO2.csv"
df = pd.read_csv(open_url(url))
```

---

### Dataset Preview

| Country     | ISO | Total   | Coal    | Oil     | Gas     | Cement  | Flaring | Other |
|-------------|-----|---------|---------|---------|---------|---------|---------|-------|
| Afghanistan | AFG | 0.29612 | 0.10483 | 0.18503 | 0.00596 | 0.00031 | 0.0     |       |
| Albania     | ALB | 1.61807 | 0.06110 | 1.13716 | 0.05263 | 0.36718 | 0.0     |       |
| Algeria     | DZA | 3.98998 | 0.02480 | 1.26807 | 2.10041 | 0.24963 | 0.34707 |       |
| Andorra     | AND | 5.73029 | 0.0     | 5.73029 | 0.0     | 0.0     | 0.0     |       |
| Angola      | AGO | 0.61914 | 0.0     | 0.40290 | 0.08554 | 0.03257 | 0.09813 |       |
| Anguilla    | AIA | 9.18835 | 0.0     | 9.18835 | 0.0     | 0.0     | 0.0     |       |

---

## 🎮 Your turn!

Let's use this dataset to create 2 maps from scratch:


    """)

    with st.expander("Choropleth Map"):
        st.markdown("""
        Your job is to make a **choropleth map** with the provided dataset.
    
        We provide this [starter sandbox](https://your-sandbox-link) with a very basic version, but there are many aspects to improve:
    
        - 🔍 Zooming in on a specific region.  
        - 🎨 Enhancing the color scheme.  
        - 📝 Refining annotations.  
        - ❌ Removing unnecessary elements.  
        - 💡 Implementing other creative ideas (changing the projection, adding a legend, etc.).
        """)

    # Bubble Map Expander
    with st.expander("Bubble Map"):
        st.markdown("""
        Your job is to make a **Bubble Map** with the provided dataset. 

        We provide this [starter sandbox](https://your-sandbox-link) with a very basic version, but there are many aspects to improve:  

        - 🔍 Zooming in on a specific region.  
        - 🔵 Adjusting bubble sizes to highlight differences between countries.  
        - 🎨 Enhancing the color scheme.  
        - 📝 Refining annotations.  
        - ❌ Removing unnecessary elements.  
        - 💡 Implementing other creative ideas (changing the projection, adding a legend, etc.).
        """)

    st.markdown("""

You can work in the provided sandboxes, but you can also work locally if you prefer!

Once you've crafted a chart, click the `publish` button and share the graph's URL in the **#share-your-viz** channel on [Discord](https://discord.gg/XKmpbv4VWY).

> 💡 **Note:** There is a [gallery](/gallery) with every student's work to get inspiration! 🙂
""")
with tab_solution:
    st.markdown("""## Solution""")

    # Load the world map
    url_world = "https://naciscdn.org/naturalearth/110m/cultural/ne_110m_admin_0_countries.zip"
    world = gpd.read_file(url_world)
    
    # Load the CO2 dataset
    url_co2 = "https://raw.githubusercontent.com/JosephBARBIERDARNAL/data-matplotlib-journey/refs/heads/main/CO2/CO2.csv"
    df = pd.read_csv(url_co2)
    
    # Merge datasets
    merged = world.merge(df, how="left", left_on="ADM0_A3", right_on="ISO")
    
    # Choropleth Map
    with st.expander("Choropleth Map"):
        fig, ax = plt.subplots(1, 1, figsize=(15, 10))
        merged.plot(
            column='Total',
            cmap='Blues',
            linewidth=0.8,
            ax=ax,
            edgecolor='0.8',
            legend=True
        )
        ax.set_title('CO2 Emissions Per Capita (2021)', fontdict={'fontsize': 20})
        ax.set_axis_off()
        cax = plt.gcf().axes[-1]
        cax.set_position([0.85, 0.3, 0.03, 0.4])
        st.pyplot(fig)
    
    # Bubble Map
    with st.expander("Bubble Map"):
        merged = merged[~merged['Total'].isnull()]
        merged["Longitude"] = merged.geometry.centroid.x
        merged["Latitude"] = merged.geometry.centroid.y
    
        projection = ccrs.Mercator()
        previous_proj = ccrs.PlateCarree()
    
        new_coords = projection.transform_points(
            previous_proj,
            merged["Longitude"],
            merged["Latitude"]
        )
    
        x = new_coords[:, 0]  # Transformed longitudes
        y = new_coords[:, 1]  # Transformed latitudes
    
        min_s = 10
        max_s = 1000
        s = merged["Total"]
        s = min_s + (s - s.min()) * (max_s - min_s) / (s.max() - s.min())
    
        fig, ax = plt.subplots(
            subplot_kw={"projection": projection},
            figsize=(15, 10),
            layout="tight"
        )
    
        world.boundary.plot(ax=ax, linewidth=0.5, color="black", transform=previous_proj)
        ax.scatter(x, y, s=s, alpha=0.6, color='dodgerblue', edgecolor='k', linewidth=0.5)
        ax.set_title('CO2 Emissions Bubble Map (2021)', fontdict={'fontsize': 20})
        ax.axis("off")
    
        for size in [10, 50, 100]:
            plt.scatter([], [], c='dodgerblue', alpha=0.6, s=size, label=str(size // 100) + ' CO2 Units')
        plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title="Bubble Size")
    
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