from subwindows.subWindow import SubWindow
from journalScreenObject import JournalScreenObject

class JournalSubWindow(SubWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        journal = JournalScreenObject(pos=self.ids["content"].pos, size=self.ids["content"].size)
        self.ids["content"].add_widget(journal)
