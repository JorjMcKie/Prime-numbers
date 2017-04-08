# Prime-numbers
Some demo prime number methods using elementary pure Python.
## Contains              
* **primzahl.py:** A CLI demo script to serve as a frontend for invoking prime number methods and displaying their results. These functions are prime factorization,looking up the next prime (twin) and counting primes and prime twins below a certain number. Whenever possible, just hitting ENTER uses last function's output as input. So for example, ENTER will continue to show primes (or prime twins respectively) in ascending order.

* **primes.py:** Contains the class definition for all prime number calculations. Can be used independently from the other files. Loading stored, previously calculated prime numbers is done during import - not during object creation. The `__del__` method of this class automatically performs a save to disk, if new prime numbers have been calculated. There is a built-in limit on the largest prime saved to disk, currently 5 million. This limit can be overwritten during object creation, and of course the definition can be updated, too. Prime numbers are stored as 32 bit integers ("unsigned long", using the `array` standard Python module, not a simple list), so there is an absolute upper limit of about 4.3 billion for the largest usable prime number. When new primes must be claculated, a **deterministic** version of the **Miller-Rabin-Test** is used.

* **primzahl.de, primzahl.es:** optional files defining message translations from English to German and Spanish, respectively. The CLI script **primzahl.py** will check its first invocation parameter for an appropriate file extension - "de"and "es" in these cases.  In order to support your favorite language, create a **primzahl.xx** file and invoke the script with the parameter **xx**. If missing, English will be used.

* **primenumbers.zip:** an optional file containing prime numbers until about one million. To be placed in the user's home directory. The actual prime number data in this file is LZMA-compressed (Python 3, or DEFLATEd in Python 2) and only occupies 58 KB. Will be extended automatically, based on highest prime number used in a session. Will be created automatically in the user's home directory if missing. During a session, these data serve as a cache to keep calculations of new prime number to a minimum.

## Features
* Perform prime factorization of an integer. Returns a list of pairs `[p, e]`, where `p` is a prime and `e` its exponent. Primes obviously only contain one such pair.
* Return the smallest **prime** following a given number.
* Return the smallest **prime twin** following a given number. 
* Return **count of primes** less or equal a given number (so-called Pi function). 
* Return **count of prime twins** less or equal a given number. 
* Automatically append new calculated prime numbers to an `array.array` of format "L" (unsigned long).
* Automatically save the prime number array in a zip file, if new primes have been created in the current session.

## Dependency Notes
Runs with Python 2 or 3.

When **switching back** from Python 3 to Python 2 an eventually existing `primenumbers.zip` file must be deleted first, because Python 2 does not support compression LZMA (which is automatically used if Python 3).

No issues exist, when switching from Python 2 to Python 3. The next prime number save under Python 3 will automatically use LZMA compression.

## Changes
* Use the deterministic version of the **Miller-Rabin-Test** for primality. This is about **30 - 50% more efficient** than Eratosthenes in our context.
* Use of binary search module `bisect` when looking up the index of a prime.
* Parameterize message translations in the CLI script.

## Example Session

    Last prime number in store: 1001003 (78574 entries)
    ====== Prime number functions ======
         1: prime factors
         2: next prime number
         3: next prime twin
         4: count prime numbers
         5: count prime number twins
         q: quit
    > 1
    === Find prime factors ===
    Enter a number or 'q': 478523
    Factors: [[478523, 1]]

    Enter a number or 'q': 397397
    Factors: [[7, 1], [11, 1], [13, 1], [397, 1]]

    Enter a number or 'q': q
    ====== Prime number functions ======
         1: prime factors
         2: next prime number
         3: next prime twin
         4: count prime numbers
         5: count prime number twins
         q: quit
    > 2
    === Find the next prime ===
    ENTER, a number or 'q':
    Next prime: 397427                    # ENTER was hit, so show prime >= 397397

    ENTER, a number or 'q':
    Next prime: 397429

    ENTER, a number or 'q': q
    ====== Prime number functions ======
         1: prime factors
         2: next prime number
         3: next prime twin
         4: count prime numbers
         5: count prime number twins
         q: quit
    > 3
    === Find the next prime twin ===
    ENTER, a number or 'q': 999999
    Next prime twin: (1000037, 1000039)

    ENTER, a number or 'q': q
    ====== Prime number functions ======
         1: prime factors
         2: next prime number
         3: next prime twin
         4: count prime numbers
         5: count prime number twins
         q: quit
    > 4
    === Count previous primes ===
    Enter a number or 'q': 999999
    78498
    Enter a number or 'q': q
    ====== Prime number functions ======
         1: prime factors
         2: next prime number
         3: next prime twin
         4: count prime numbers
         5: count prime number twins
         q: quit
    > 5
    === Count previous prime twins ===
    Enter a number or 'q': 999999
    8169
    Enter a number or 'q': q
    ====== Prime number functions ======
         1: prime factors
         2: next prime number
         3: next prime twin
         4: count prime numbers
         5: count prime number twins
         q: quit
    > q
    $
