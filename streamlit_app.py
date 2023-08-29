import streamlit as st

from streamlit_gallery import apps, components
from streamlit_gallery.utils.page import page_group
from streamlit_elements import dashboard

def main():
    page = page_group("p")

    with st.sidebar:
        st.title("tsuna-test")

        # with st.expander("✨ APPS", True):
        #     page.item("Streamlit gallery", apps.gallery, default=True)

        with st.expander("🧩 COMPONENTS", True):
            # page.item("Ace editor", components.ace_editor)
            # page.item("Disqus", components.disqus)
            page.item("Elements⭐", components.elements)
            # page.item("Pandas profiling", components.pandas_profiling)
            # page.item("Quill editor", components.quill_editor)
            # page.item("React player", components.react_player)
            with elements("dashboard"):

            # You can create a draggable and resizable dashboard using
            # any element available in Streamlit Elements.
        
        
            # First, build a default layout for every element you want to include in your dashboard
        
            layout = [
                # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
                dashboard.Item("first_item", 0, 0, 2, 2),
                dashboard.Item("second_item", 2, 0, 2, 2, isDraggable=False, moved=False),
                dashboard.Item("third_item", 0, 2, 1, 1, isResizable=False),
            ]
        
            # Next, create a dashboard layout using the 'with' syntax. It takes the layout
            # as first parameter, plus additional properties you can find in the GitHub links below.
        
            with dashboard.Grid(layout):
                mui.Paper("First item", key="first_item")
                mui.Paper("Second item (cannot drag)", key="second_item")
                mui.Paper("Third item (cannot resize)", key="third_item")
        
            # If you want to retrieve updated layout values as the user move or resize dashboard items,
            # you can pass a callback to the onLayoutChange event parameter.
        
            def handle_layout_change(updated_layout):
                # You can save the layout in a file, or do anything you want with it.
                # You can pass it back to dashboard.Grid() if you want to restore a saved layout.
                print(updated_layout)
    
        with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
            mui.Paper("First item", key="first_item")
            mui.Paper("Second item (cannot drag)", key="second_item")
            mui.Paper("Third item (cannot resize)", key="third_item")

    page.show()

if __name__ == "__main__":
    st.set_page_config(page_title="Tsuna-test", page_icon="🎈", layout="wide")
    main()
