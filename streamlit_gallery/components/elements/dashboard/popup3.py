from streamlit_elements import mui, html
import streamlit as st
from .dashboard import Dashboard


class Popup3(Dashboard.Item):

    DEFAULT_CONTENT = """
        今月の給餌費用目標： 115,924,000 円
        今月の給餌費用実績：   3,984,000 円
        今月の給餌費用予測： 110,345,000 円
    """

    def __call__(self, content):
        with mui.Card(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            mui.CardHeader(
                title="給餌目標・実績",
                # subheader="September 14, 2016",
                # avatar=mui.Avatar("R", sx={"bgcolor": "red"}),
                # action=mui.IconButton(mui.icon.MoreVert),
                className=self._draggable_class)
            

            with mui.CardContent(sx={"flex": 1}):
                with mui.Typography:
                    # 文字列を改行で分割
                    lines = content.strip().split('\n')
                    # 各行に対して処理を実行
                    for line in lines:
                        html.div(line)
                        # html.br()
