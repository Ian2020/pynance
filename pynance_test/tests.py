from nose.tools import assert_equals
import pynance
import pyperclip


# For some reason using a pound sign here means nose can't read the file!
# Even if I change the encoding to utf-8. Bizarre.

def copy_one_trans_to_clipboard():
    pyperclip.copy("17/11/2016\tCARD PAYMENT TO Amazon UK Marketplace,54.96"
                   " GBP, RATE 1.00/GBP ON 15-11-2016 \t\t$54.96 \t$1,490.99")


def test_importing_nothing_gives_nothing():
    pyperclip.copy("")
    trans = pynance.import_sant()
    assert_equals(trans, None)


def test_importing_gives_transactions():
    copy_one_trans_to_clipboard()
    trans = pynance.import_sant()
    # Is there an assert_notequals ?
    assert trans is not None


def test_importing_gives_one_transaction():
    copy_one_trans_to_clipboard()
    trans = pynance.import_sant()
    printed_trans = trans.to_list()
    assert_equals(len(printed_trans), 1)
    assert_equals(len(printed_trans[0]), 4)
