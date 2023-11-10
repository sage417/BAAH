from typing import override

from assets.PageName import PageName
from assets.ButtonName import ButtonName
from assets.PopupName import PopupName

from AllPage.Page import Page
from AllTask.Task import Task

from utils import click, swipe, match, page_pic, button_pic, popup_pic, sleep

class InContest(Task):
    def __init__(self, name="InContest") -> None:
        super().__init__(name)

    @override
    def pre_condition(self) -> bool:
        return super().pre_condition()
    
    @override
    def on_run(self) -> None:
        super().on_run()

    @override
    def post_condition(self) -> bool:
        return super().post_condition()