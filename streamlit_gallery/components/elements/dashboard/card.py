from streamlit_elements import mui, html
import streamlit as st
from .dashboard import Dashboard


class Card(Dashboard.Item):

    DEFAULT_CONTENT = """
        尾数：1053 尾
        予測給餌量： 500 kg
        種類： 生餌（サバ）
    """

    def __call__(self, content):
        with mui.Card(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            mui.CardHeader(
                title="生簀番号：１",
                # subheader="September 14, 2016",
                # avatar=mui.Avatar("R", sx={"bgcolor": "red"}),
                # action=mui.IconButton(mui.icon.MoreVert),
                className=self._draggable_class)
            
            # mui.CardMedia(
            #     component="img",
            #     height=194,
            #     alt="ikesu",
            # )

            with mui.CardContent(sx={"flex": 1}):
                with mui.Typography:
                    # 文字列を改行で分割
                    lines = content.strip().split('\n')
                    # 各行に対して処理を実行
                    for line in lines:
                        html.div(line)
                        # html.br()
                        
            # with mui.CardContent(sx={"flex": 1}):
            # # Here, we exit the mui context and use Streamlit's markdown function to render HTML
            #     st.markdown(content, unsafe_allow_html=True)
            # with mui.CardActions(disableSpacing=True):
            #     mui.IconButton(mui.icon.Favorite)
            #     mui.IconButton(mui.icon.Share)
