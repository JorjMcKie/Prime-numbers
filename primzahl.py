# -*- coding: latin-1 -*-
"""
Created on Thu Jan 19 07:00:00 2017

@author: Jorj McKie
Copyright (c) 2017 Jorj X. McKie

The license of this program is governed by the MIT LICENSE.

Demo program for some prime number functions.

Consists of
------------
primzahl.py       (this program), primes.py (class definition), primzahl.json for translating
                  program messagges to another language (German contained as an example), primzahlen.zip.
primes.py         class definition for prime number calculations
primzahl.json     defines translation from English to another language (optional)
primenumbers.zip  file containing prime numbers until about one million (optional). To be placed in the
                  user's hme directory. Will be crated / maintained automatically if absent.

Features
---------
* Perform prime factorizations of any integer. Feedback is a list of pairs [p, e] where p is a       prime factor and e its exponent.abs
* return the smallest prime not smaller than a given number.
* return the smallest prime twin not smaller than a given number.
* return the count of primes up to a given number.
* return the count of prime twins up to a given number. 
* automatically stores new calculated prime numbers in an array.array of format "L" (unsigned long)
* automatically save the prime number array in a zip file, if new primes have been created in the
  current session.

Dependencies:
-------------
Runs with Python 2 or 3. When switching back from Python 3 to Python 2 an existing primzahl.zip file must be deleted first, because Python 2 does not support zipfile compression LZMA (which is automatically used if Python 3).

"""
from __future__ import print_function
import sys, os
from primes import Primes
import json
if len(sys.argv) == 2:
    suffix = sys.argv[1]
    xlatefn = __file__[:-2] + suffix
    if os.path.exists(xlatefn):
        xlate = json.loads(open(xlatefn).read())
        def _(s):
            if s in xlate.keys():
                return xlate[s]
            else:
                return s
else:
    def _(s):
        return s

if sys.version_info[0] < 3:
    lies = raw_input
else:
    lies = input

pz = Primes()

def factors(zahl):
    """Return the prime factors of a given positive integer."""
    print(_("=== Find prime factors ==="))
    answer = ""
    while answer != "q":
        print(_("Enter a number or 'q'"), end = ": ")
        answer = lies()
        if answer == "q": break
        try:
            zahl = int(answer)
            print(_("Factors:"), pz.factors(zahl), "\n")
        except ValueError:
            pass
        answer = ""
    return zahl

def nextprime(zahl):
    """Return the smallest prime following a given number."""
    print(_("=== Find the next prime ==="))
    answer = ""
    while answer != 'q':
        print(_("ENTER, a number or 'q'"), end = ": ")
        answer = lies()
        if answer == "q": break
        try:
            zahl = pz.nextprime(float(answer))
        except ValueError:
            zahl = pz.nextprime(zahl + 1)
        print(_("Next prime:"), zahl, "\n")
        answer = ""
    return zahl

def nexttwin(zahl):
    """Return the smallest prime twin following a given number."""
    print(_("=== Find the next prime twin ==="))
    answer = ""
    while answer != 'q':
        print(_("ENTER, a number or 'q'"), end = ": ")
        answer = lies()
        if answer == "q": break
        try:
            p1, p2 = pz.nexttwin(float(answer))
        except ValueError:
            p1, p2 = pz.nexttwin(zahl)
        print(_("Next prime twin:"), (p1, p2), "\n")
        zahl = p2
        answer = ""
    return zahl
    
def prevprimes():
    """Return number of primes less or equal a number."""
    print(_("=== Count previous primes ==="))
    answer = ""
    while answer != 'q':
        print(_("Enter a number or 'q'"), end = ": ")
        answer = lies()
        if answer == "q": break
        try:
            print(pz.prev_primes(float(answer)))
        except ValueError:
            pass
        answer = ""
    return
    
def prevtwins():
    """Return the smallest prime twin following a given number."""
    print(_("=== Count previous prime twins ==="))
    answer = ""
    while answer != 'q':
        print(_("Enter a number or 'q'"), end = ": ")
        answer = lies()
        if answer == "q": break
        try:
            print(pz.prev_twins(float(answer)))
        except ValueError:
            pass
        answer = ""
    return
    
#-------------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    textlines = (_("1: prime factors"),
                 _("2: next prime number"),
                 _("3: next prime twin"),
                 _("4: count prime numbers"),
                 _("5: count prime number twins"),
                 _("q: quit"))
    print(_("Last prime number in store: %s (%s entries)") % (pz.primes[-1], pz.oldlen))
    answer = ""
    zahl = 0
    while answer != "q":
        print(_("====== Prime number functions ======"))
        for t in textlines:
            print("\t", t)
        print("> ", end = "")
        answer = lies()
        if answer == "q": break
        if answer == "1":
            zahl = factors(zahl)
        elif answer == "2":
            zahl = nextprime(zahl)
        elif answer == "3":
            zahl = nexttwin(zahl)
        elif answer == "4":
            prevprimes()
        elif answer == "5":
            prevtwins()
        answer = ""
