from playwright.sync_api import Page, expect

from components.base_componet import BaseComponent
from elements.text import Text


class DashboardToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page) -> None:
        self.title = Text(page, "dashboard-toolbar-title-text", 'Title')

    def check_visible(self):
        self.title.check_visible()
        self.title.check_have_text('Dashboard')
