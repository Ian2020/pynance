# pynance

Pynance is a Python package to help you manage your finances. At the moment it
is limited to just helping you import transactions from banking websites into
your own spreadsheet(s):

1. You login to your bank in your browser and copy a transaction listing to the
   clipboard
1. Run an expression in the Python interpreter and the transactions will be printed
   in a format that's easy to import into a spreadsheet

It only works with following bank sites:

* Santander

## Requirements

* Python3

## Installation

Install the requirements (in a virtual env):

```shell
git clone https://github.com/Ian2020/pynance.git
[CREATE AND ACTIVATE A VIRTUAL ENV]
pip install -r requirements.txt
```

## Usage

Login to your bank's site. Copy some transactions to your clipboard then in a Python
interpreter (running under your virtual env) enter:

```python
import pynance
print(pynance.import_sant())
```

...and they will be printed in a format ready to be copied into a spreadsheet:

>DATE|DESCRIPTION|AMOUNT|BALANCE

For example:

>19/11/2016 |CARD PAYMENT TO BP,10.00 GBP, RATE 1.00/GBP ON 17-11-2016 |£10.00 |£50.00

## Troubleshooting

Pyperclip may have mechanism problems: see [Not Implemented Error (pyperclip.readthedocs.io)](https://pyperclip.readthedocs.io/en/latest/introduction.html)

...note we use pipe (|) as the separator.
