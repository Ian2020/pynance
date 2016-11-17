import pynance
import pyperclip


def test_import():
    # For some reason using a pound sign here means nose can't read the file!
    # Even if I change the encoding to utf-8. Bizarre.

    pyperclip.copy("17/11/2016\tCARD PAYMENT TO Amazon UK Marketplace,54.96"
                   " GBP, RATE 1.00/GBP ON 15-11-2016 \t\t$54.96 \t$1,490.99")
    trans = pynance.import_sant()
    assert len(trans) > 0
