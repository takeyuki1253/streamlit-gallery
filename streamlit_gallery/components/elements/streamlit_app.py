import json
import streamlit as st

from pathlib import Path
from streamlit import session_state as state
from streamlit_elements import elements, sync, event, mui, html, dashboard
from types import SimpleNamespace

from .dashboard import Dashboard, Editor, Card, DataGrid, Radar, Pie, Player, Popup1, Popup2, Popup3


def main():
    st.write(
        """
        Tsuna Test 
        =====================

        ツナの給餌量・給仕判断の可視化
        
        """
    )

    # with st.expander("GETTING STARTED"):
    #     st.write((Path(__file__).parent/"README.md").read_text())

    st.title("")

    if "w" not in state:
        board = Dashboard()
        w = SimpleNamespace(
            dashboard=board,
            editor=Editor(board, 0, 7, 6, 7, minW=3, minH=3),
            # player=Player(board, 0, 12, 6, 10, minH=5),
            # pie=Pie(board, 6, 0, 6, 7, minW=3, minH=4),
            # radar=Radar(board, 12, 7, 3, 7, minW=2, minH=4),
            header=Popup1(board, 0, 0, 12, 3, minW=2, minH=4),
            header2=Popup2(board, 0, 3, 12, 3, minW=2, minH=4),
            header3=Popup3(board, 0, 3, 12, 3, minW=2, minH=4),
            card=Card(board, 0, 4, 3, 6, minW=2, minH=4),
            card2=Card(board, 3, 4, 3, 6, minW=2, minH=4),
            card3=Card(board, 6, 4, 3, 6, minW=2, minH=4),
            card4=Card(board, 9, 4, 3, 6, minW=2, minH=4),
            # data_grid=DataGrid(board, 7, 7, 6, 7, minH=4),
        )
        state.w = w
        
        w.editor.add_tab("header content", Popup1.DEFAULT_CONTENT, "plaintext")
        w.editor.add_tab("header content2", Popup2.DEFAULT_CONTENT, "plaintext")
        w.editor.add_tab("header content3", Popup3.DEFAULT_CONTENT, "plaintext")
        w.editor.add_tab("Card content", Card.DEFAULT_CONTENT, "plaintext")
        w.editor.add_tab("Card content2", Card.DEFAULT_CONTENT, "plaintext")
        w.editor.add_tab("Card content3", Card.DEFAULT_CONTENT, "plaintext")
        w.editor.add_tab("Card content4", Card.DEFAULT_CONTENT, "plaintext")
        # w.editor.add_tab("Data grid", json.dumps(DataGrid.DEFAULT_ROWS, indent=2), "json")
        # w.editor.add_tab("Radar chart", json.dumps(Radar.DEFAULT_DATA, indent=2), "json")
        # w.editor.add_tab("Pie chart", json.dumps(Pie.DEFAULT_DATA, indent=2), "json")
    else:
        w = state.w

    with elements("demo"):
        event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)

        with w.dashboard(rowHeight=57):
            w.editor()
            # w.player()
            # w.pie(w.editor.get_content("Pie chart"))
            # w.radar(w.editor.get_content("Radar chart"))
            w.header(w.editor.get_content("header content"))
            w.header(w.editor.get_content("header content2"))
            w.header(w.editor.get_content("header content3"))
            w.card(w.editor.get_content("Card content"))
            w.card2(w.editor.get_content("Card content2"))
            w.card3(w.editor.get_content("Card content3"))
            w.card4(w.editor.get_content("Card content4"))
            # w.data_grid(w.editor.get_content("Data grid"))

if __name__ == "__main__":
    st.set_page_config(layout="wide")
    main()
