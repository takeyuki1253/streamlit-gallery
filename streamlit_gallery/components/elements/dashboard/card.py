from streamlit_elements import mui, html
from .dashboard import Dashboard


class Card(Dashboard.Item):

    DEFAULT_CONTENT = (
        "マグロの給餌量と給餌判断について "
        "日付：023/8/29"
        "本日の給餌可否： Yes"
        "本日の給餌量： 100kg"
    )

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
                mui.Typography:
                    html.h1(content)
            # with mui.CardActions(disableSpacing=True):
            #     mui.IconButton(mui.icon.Favorite)
            #     mui.IconButton(mui.icon.Share)
