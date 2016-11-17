import pyperclip


class Transactions:
    def to_list(self):
        return [[0,0,0,0]]


def import_sant():
    clipboard = pyperclip.paste()

    if (clipboard == ""):
        return

    return Transactions()
