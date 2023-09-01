from streamlit_elements import mui, html
import streamlit as st
from .dashboard import Dashboard


class Card(Dashboard.Item):

    DEFAULT_CONTENT = """
        最大風速： 4 m/s
        潮：大潮
        水温（5m）： 20℃
        溶存酸素：6 mg/L
        天気：晴れ
        赤潮予測：あり
        活性予測：よい
    """

    def __call__(self, content):
        with mui.Card(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            mui.CardHeader(
                title="本日（2023/9/1）の給餌環境",
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
                        
