from nose.tools import eq_
from nose.tools import ok_
import pynance
import pyperclip


def copy_one_trans_to_clipboard():
    pyperclip.copy("17/11/2016\tCARD PAYMENT TO Amazon UK Marketplace,54.96"
                   " GBP, RATE 1.00/GBP ON 15-11-2016 \t\t£54.96 \t£1,490.99")


def copy_one_positive_trans_to_clipboard():
    pyperclip.copy("17/11/2016\tCARD PAYMENT TO Amazon UK Marketplace,54.96"
                   " GBP, RATE 1.00/GBP ON 15-11-2016 \t£40.00 \t\t£1,490.99")


def copy_two_trans_to_clipboard():
    pyperclip.copy("17/11/2016\tCARD PAYMENT TO Amazon UK Marketplace,54.96"
                   " GBP, RATE 1.00/GBP ON 15-11-2016 \t\t£54.96 \t£1,490.99\n"
                   "17/11/2016\tCARD PAYMENT TO Amazon UK Marketplace,54.96"
                   " GBP, RATE 1.00/GBP ON 15-11-2016 \t\t£54.96 \t£1,490.99")


def copy_two_trans_with_ad_to_clipboard():
    pyperclip.copy("17/11/2016\tCARD PAYMENT TO Amazon UK Marketplace,54.96"
                   " GBP, RATE 1.00/GBP ON 15-11-2016 \t\t£54.96 \t£1,490.99\n"
                   "NEW! Earn 15% Cash Back when you next dine with Gourmet Burger Kitchen\n"
                   "Choose Offer\n"
                   "17/11/2016\tCARD PAYMENT TO Amazon UK Marketplace,54.96"
                   " GBP, RATE 1.00/GBP ON 15-11-2016 \t\t£54.96 \t£1,490.99")


def copy_one_trans_to_clipboard_trailing_newline():
    pyperclip.copy("17/11/2016\tCARD PAYMENT TO Amazon UK Marketplace,54.96"
                   " GBP, RATE 1.00/GBP ON 15-11-2016 \t\t£54.96 \t£1,490.99"
                   "\n")


# ## Actual tests


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
    eq_(printed_trans[0][0], "17/11/2016")
    eq_(printed_trans[0][1], "CARD PAYMENT TO Amazon UK Marketplace,54.96 GBP,"
                             " RATE 1.00/GBP ON 15-11-2016 ")
    eq_(printed_trans[0][2], "£-54.96 ")
    eq_(printed_trans[0][3], "£1,490.99")


def test_importing_gives_one_positive_transaction():
    copy_one_positive_trans_to_clipboard()

    trans = pynance.import_sant()
    printed_trans = trans.to_list()

    eq_(len(printed_trans), 1)
    eq_(len(printed_trans[0]), 4, "Expected 4 items in trans, found this: %s"
                                  % trans)
    eq_(printed_trans[0][0], "17/11/2016")
    eq_(printed_trans[0][1], "CARD PAYMENT TO Amazon UK Marketplace,54.96 GBP,"
                             " RATE 1.00/GBP ON 15-11-2016 ")
    eq_(printed_trans[0][2], "£40.00 ")
    eq_(printed_trans[0][3], "£1,490.99")


def test_importing_trailing_newline_gives_one_transaction():
    copy_one_trans_to_clipboard_trailing_newline()

    trans = pynance.import_sant()
    printed_trans = trans.to_list()

    eq_(len(printed_trans), 1)


def test_importing_gives_two_transaction():
    copy_two_trans_to_clipboard()

    trans = pynance.import_sant()
    printed_trans = trans.to_list()

    eq_(len(printed_trans), 2)
    eq_(len(printed_trans[0]), 4)
    eq_(printed_trans[1][0], "17/11/2016")
    eq_(printed_trans[1][1], "CARD PAYMENT TO Amazon UK Marketplace,54.96 GBP,"
                             " RATE 1.00/GBP ON 15-11-2016 ")
    eq_(printed_trans[1][2], "£-54.96 ")
    eq_(printed_trans[1][3], "£1,490.99")


def test_importing_with_ad_transaction():
    copy_two_trans_with_ad_to_clipboard()

    trans = pynance.import_sant()
    printed_trans = trans.to_list()

    eq_(len(printed_trans), 2)
