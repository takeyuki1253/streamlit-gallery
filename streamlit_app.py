import streamlit as st

from streamlit_gallery import apps, components
from streamlit_gallery.utils.page import page_group
from streamlit_elements import elements, mui, html, dashboard

def main():
    page = page_group("p")

    with st.sidebar:
        st.title("tsuna-test")

        # with st.expander("✨ APPS", True):
        #     page.item("Streamlit gallery", apps.gallery, default=True)

        with st.expander("🧩 Tsuna-ikesu", True):
            # page.item("Ace editor", components.ace_editor)
            # page.item("Disqus", components.disqus)
            page.item("Ikesu-1⭐", components.elements)
            page.item("Ikesu-2⭐", components.elements)
            page.item("Ikesu-3⭐", components.elements)
            # page.item("Pandas profiling", components.pandas_profiling)
            # page.item("Quill editor", components.quill_editor)
            # page.item("React player", components.react_player)

    page.show()

if __name__ == "__main__":
    st.set_page_config(page_title="Tsuna-test", page_icon="🎈", layout="wide")
    main()
