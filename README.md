# Prime-numbers
Some demo prime number methods using elementary pure Python.
## Contains              
* **primzahl.py**   cli script to invoke prime number methods and display results.

* **primes.py**     class definition for prime number calculations. Can be used independently from the rest of the other files. Loading prime numbers is done during import of the file. So the primes array is available on a class basis, i.e. across all created objects. Saving the primes however occurs during deletion of any object. There is a built-in limit of how many primes will be saved to disk. This limit can be modified during object creation.

* **primzahl.json** defines message translations from English to another language (optional). If missing, English will be used.

* **primzahl.zip**  file containing prime numbers until about one million (optional). To be placed in the user's home directory. Will be extended automatically based on highest prime number used in the session. Will be created automatically if missing.

## Features
* Perform prime factorizations of any integer. Feedback is a list of pairs [p, e] where p is a prime factor and e its exponent.
* return the smallest prime greater than a provided integer.
* return the smallest prime twin grater than a provided number. 
* automatically stores new calculated prime numbers in an array.array of format "L" (unsigned long)
* automatically save the prime number array in a zip file, if new primes have been created in the
  current session.

## Dependencies
Runs with Python 2 or 3. When switching back from Python 3 to Python 2 an existing primzahl.zip file must be deleted first, because Python 2 does not support zipfile compression LZMA (which is automatically used if Python 3).

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


