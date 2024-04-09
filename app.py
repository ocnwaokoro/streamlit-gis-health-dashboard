import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")

from apps import facilities, districts, regions  # import your app modules here

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": regions.app, "title": "Regions", "icon": "globe-europe-africa"},
    {"func": districts.app, "title": "Districts", "icon": "pin-map"},
    {"func": facilities.app, "title": "Facilities", "icon": "hospital"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.query_params

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
        orientation='horizontal'
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web app is maintained by Obinna Nwaokoro. You can follow me on social media:
            [GitHub](https://github.com/ocnwaokoro) | [LinkedIn](https://www.linkedin.com/in/obinna-nwaokoro).

        The goal of this web app is to facilitate the easy access and retrieval of data pertaining to health access in Ghana.
        """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
