import pyperclip


class Transactions:
    def __init__(self, text):
        self._transactions = list()
        for line in text.splitlines():
            trans = list()
            initial_split = line.split("\t")
            for idx in range(5):
                thing_to_add = initial_split[idx]
                if idx == 2 and len(thing_to_add) == 0:
                    continue
                if idx == 3:
                    if len(thing_to_add) == 0:
                        continue
                    else:
                        # TODO: Make it negative
                        # thing_to_add = ???
                        pass

                trans.append(thing_to_add)
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
