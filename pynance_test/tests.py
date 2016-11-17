from nose.tools import eq_
from nose.tools import ok_
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

    eq_(trans, None)


def test_importing_gives_transactions():
    copy_one_trans_to_clipboard()

    trans = pynance.import_sant()

    # Is there an assert_notequals ?
    ok_(trans is not None)


def test_importing_gives_one_transaction():
    copy_one_trans_to_clipboard()

    trans = pynance.import_sant()
    printed_trans = trans.to_list()

    eq_(len(printed_trans), 1)
    eq_(len(printed_trans[0]), 4)
    # eq_(printed_trans[0][1], ???)