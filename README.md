# Prime-numbers
Some demo prime number methods using elementary Python only.
## Contains

primzahl.py   (this program), primes.py (class definition), primzahl.json for translating
              program messagges to another language (German contained as an example), primzahlen.zip.
primzahl.py   cli script to invoke prime number methods and display results
primes.py     class definition for prime number calculations
primzahl.json defines translation from English to another language (optional)
primzahl.zip  file containing prime numbers until about one million (optional). To be placed in the
              user's hme directory. Will be crated / maintained automatically if absent.

## Features
* Perform prime factorizations of any integer. Feedback is a list of pairs [p, e] where p is a       prime factor and e its exponent.abs
* return the smallest prime greater than a provided integer.
* return the smallest prime twin grater than a provided number. 
* automatically stores new calculated prime numbers in an array.array of format "L" (unsigned long)
* automatically save the prime number array in a zip file, if new primes have been created in the
  current session.

## Dependencies
Runs with Python 2 or 3. When switching back from Python 3 to Python 2 an existing primzahl.zip file must be deleted first, because Python 2 does not support zipfile compression LZMA (which is automatically used if Python 3).

