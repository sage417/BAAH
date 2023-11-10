from typing import override

from assets.PageName import PageName
from assets.ButtonName import ButtonName
from assets.PopupName import PopupName

from AllPage.Page import Page
from AllTask.Task import Task

from utils import click, swipe, match, page_pic, button_pic, popup_pic, sleep

# =====

from .CollectPower import CollectPower
from .TouchHead import TouchHead

class InCafe(Task):
    def __init__(self, name="InCafe", pre_times = 3, post_times = 3) -> None:
        super().__init__(name, pre_times, post_times)

    @override
    def pre_condition(self) -> bool:
        return Page.is_page(PageName.PAGE_HOME)
    
    @override
    def on_run(self) -> None:
        # 进入咖啡厅
        click((92, 670))
        CollectPower().run()
        TouchHead().run()
        # 返回主页
        Task.back_to_home()

    @override
    def post_condition(self) -> bool:
        return Page.is_page(PageName.PAGE_HOME)