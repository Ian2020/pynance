import pyperclip


class Transactions:
    def __init__(self, text):
        self._transactions = list()
        for line in text.split("\r\n"):
            if(len(line) > 0):
                trans = list()
                initial_split = line.split("\t")
                for idx in (0, 1, 3, 4):
                    trans.append(initial_split[idx])
                self._transactions.append(trans)

    def __str__(self):
        printed = ""
        for line in self._transactions:
            for item in line:
                printed += "%s|" % item
            printed += "\n"
        return printed

    def to_list(self):
        return self._transactions


def import_sant():
    clipboard = pyperclip.paste()

    if (clipboard == ""):
        return

    return Transactions(clipboard)
