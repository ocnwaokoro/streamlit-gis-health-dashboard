import streamlit as st

st.set_page_config(
    page_title='Ghana Health Access Dashboard', 
    layout='wide',
    page_icon='🗺️')

from apps import facilities, districts, regions  # import your app modules here

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": regions.app, "title": "Regions", "icon": "🌍"},
    {"func": districts.app, "title": "Districts", "icon": "📍"},
    {"func": facilities.app, "title": "Facilities", "icon": "🏥"},
]

titles = [app["title"] for app in apps]
icons = [app["icon"] for app in apps]

params = st.query_params

if "page" in params:
    default_index = titles.index(params["page"][0])
else:
    default_index = 2

selected = st.sidebar.radio("Navigate", titles, index=default_index)

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
