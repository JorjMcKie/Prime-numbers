# Prime-numbers
Some demo prime number methods using elementary pure Python.
## Contains              
* **primzahl.py:** A cli demo script to invoke prime number methods and display their results. These function are prime factorization and calculating a number's subsequent prime or prime twin. Whenever possible, just hitting ENTER uses last function's output as input. So ENTER will continue to show primes (prime twins) in ascending order.

* **primes.py:** Contains class definition for prime number calculations. Can be used independently from the rest of the other files. Loading stored, previously calculated prime numbers is done during import of the file. So the primes array is available on a class basis, i.e. across all created objects. Updating and saving this array will be done by all objects independently thus making results available to all objects. There is a built-in limit on the largest prime array size saved to disk (currently prime numbers cannot exceed 5 million). This limit can be overwritten during object creation. When new primes must be claculated, the **deterministic** version of the **Miller-Rabin-Test** is used.

* **primzahl.json:** Ddefines message translations from English to another language (optional) for the cli script **primzahl.py**. If missing, English will be used.

* **primenumbers.zip:** contains prime numbers until about one million (optional). To be placed in the user's home directory. The actual prime number data in this file is LZMA-compressed (Python 3, or DEFLATEd in Python 2) and only occupies 58 KB. Will be extended automatically based on highest prime number used in a session. Will be created automatically if missing. During a session, these data serve as a cache to keep calculations of new prime number to a minimum. User-available methods therefore only use standard Python array lookup functions to perform their tasks.

## Features
* Perform prime factorization of an integer. Returns a list of pairs `[p, e]`, where `p` is a prime and `e` its exponent.
* return the smallest **prime** greater than a given integer.
* return the smallest **prime twin** greater than a given number. 
* return **count of primes** less or equal a given number (Pi function). 
* return **count of prime twins** less or equal a given number. 
* automatically stores new calculated prime numbers in an `array.array` of format "L" (unsigned long).
* automatically saves the prime number array in a zip file, if new primes have been created in the
  current session.

## Dependencies
Runs with Python 2 or 3.

When **switching back from Python 3** to Python 2 an eventually existing primenumbers.zip file must be deleted first, because Python 2 does not support compression LZMA (which is automatically used if Python 3).

When switching from Python 2 to Python 3, the next save of prime numbers will automatically use LZMA compression.

## Changes
* Use the deterministic version of the **Miller-Rabin-Test** for primality. This is about **33% more efficient** than Eratosthenes in our context.

## Example Session


    $ python primzahl.py
    primzahl.json translation does not exist
    ====== Prime number functions ======
    Last stored prime: 1000999 (78573)
    1 = prime factors, 2 = next prime, 3 = next prime twin, q = quit: 1
    === Find prime factors ===
    Enter a number or 'q': 478523
    Factors: [[478523, 1]]
    
    Enter a number or 'q': 397397
    Factors: [[7, 1], [11, 1], [13, 1], [397, 1]]
    
    Enter a number or 'q': q
    1 = prime factors, 2 = next prime, 3 = next prime twin, q = quit: 2
    === Find the next prime ===
    ENTER, a number or 'q':
    Next prime: 397427
    
    ENTER, a number or 'q':
    Next prime: 397429
    
    ENTER, a number or 'q': q
    1 = prime factors, 2 = next prime, 3 = next prime twin, q = quit: 3
    === Find the next prime twin ===
    ENTER, a number or 'q': 999999
    Next prime twin: (1000037, 1000039)
    
    ENTER, a number or 'q': q
    1 = prime factors, 2 = next prime, 3 = next prime twin, q = quit: q
    
    $


