import pyperclip


class Transactions:
    def __init__(self, text):
        self._transactions = list()
        for line in text.splitlines():
            trans = list()
            initial_split = line.split("\t")
            if(len(initial_split) == 5):
                for idx in range(5):
                    thing_to_add = initial_split[idx]
                    if idx == 2 and len(thing_to_add) == 0:
                        continue
                    if idx == 3:
                        if len(thing_to_add) == 0:
                            continue
                        else:
                            # TODO: Make it negative
                            thing_to_add = thing_to_add.replace("£", "£-")

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

# Chat
#
# We want to make adding transactions an undo-able, journalled, action.
# A bunch of transactions should be in an event that can be rolled back,
# along with any associated events. Do we have a graph for the associated
# actions? So we can understand result of undo-ing an action, e.g. removing
# a transaction means any labelling/balancing of the trans should also go,
# which could also be a bunch of time-ordered actions. A diagram would probably
# help
#
# ...first things first
# allow us to accumulate transactions, persist them and undo them.
#
# Stories (what offline planning tool can I use? Wunderlist? FreeMind?)
#
# * As a user I would like transactions to be remembered between sessions so I
#   can build up my history
#   * I want offline storage
#   * I want to be able to secure it myself.
#   * I want it to sync across machines
#     * This is interesting, do I want to me able to resolve/merge conflicts?
#       If just faced with a binary nothing can help me.
#     * Is there an existing format out there I could use, with supporting tools?
#     * Or will it all be bundled up in an encrypted volume anyway?
#     * How can we support simultaneous use?
#     * Right now it's not a big issue, it's more about merging two logs that
#       diverged at some point.
#   * We need to mind data corruption, we need to be sure it's solid.
#   * We need to store the log and the data. The log is a double-linked list.
#     It points to our graph of actions. Our actions are executable against
#     data. That data must be taken from output of a previous action, in order to
#     get the correct ordering.
#
# 1. "Import" (addTrans(A), addTrans(B), addTrans(C))
# 2. "Label B" (label(addTrans(B)), "Something")
# 3. "Label C" (label(addTrans(C)), "Something")
# 4. "Undo import" (interesting, we know that we only need to delete the trans,
#     we don't ahve to unlabel. How to deal with this?)
