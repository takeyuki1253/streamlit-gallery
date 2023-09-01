from streamlit_elements import mui, html
import streamlit as st
from .dashboard import Dashboard


class Card(Dashboard.Item):

    DEFAULT_CONTENT = """
        マグロの給餌量と給餌判断について\n
        日付：2023/8/29\n
        本日の給餌可否： Yes\n
        本日の給餌量： 100kg\n
    """

    def __call__(self, content):
        with mui.Card(key=self._key, sx={"display": "flex", "flexDirection": "column", "borderRadius": 3, "overflow": "hidden"}, elevation=1):
            mui.CardHeader(
                title="生簀ごとのツナ給餌量",
                subheader="September 14, 2016",
                avatar=mui.Avatar("R", sx={"bgcolor": "red"}),
                action=mui.IconButton(mui.icon.MoreVert),
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
                        html.h2(line)
                        
            # with mui.CardContent(sx={"flex": 1}):
            # # Here, we exit the mui context and use Streamlit's markdown function to render HTML
            #     st.markdown(content, unsafe_allow_html=True)
            # with mui.CardActions(disableSpacing=True):
            #     mui.IconButton(mui.icon.Favorite)
            #     mui.IconButton(mui.icon.Share)
