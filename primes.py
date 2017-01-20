# -*- coding: latin-1 -*-
import os, sys
import array
from math import sqrt
import zipfile

class Primes():
    _appdata = os.path.expanduser("~")
    _primedata = "primenumbers.data"
    _primezip  = os.path.join(_appdata, "primenumbers.zip")
    primes = array.array("L")
    store_limit = 5*10**6           # size of largest prime we want to store
    if sys.version_info[0] < 3:
        _ziplevel = zipfile.ZIP_DEFLATED
    else:
        _ziplevel = zipfile.ZIP_LZMA

    if os.path.exists(_primezip):
        mzip = zipfile.ZipFile(_primezip, "r")
        pzin = mzip.read(_primedata)
        primes.fromstring(pzin)
        mzip.close()
        del mzip, pzin
    else:
        primes.fromlist([2, 3, 5, 7, 11])
    oldlen = len(primes)

    def __init__(self, max_primes = 0):
        """Change maximum prime to be stored to disk."""
        if max_primes > 0:
            self.store_limit = max_primes
            
    def _enlarge(self, zahl):
        """Extend the primes array up to provided parameter."""
        check = self.primes[-1]        # last stored prime
        while check <= zahl:
            check += 2                 # stick with odd numbers
            i = 1                      # forget the 2
            checksq = sqrt(check)
            newprime = True
            while self.primes[i] <= checksq:
                if check % self.primes[i] == 0:
                    newprime = False
                    break
                i += 1
            if newprime:
                self.primes.append(check)
        return

    def __del__(self):
        if self.oldlen >= len(self.primes):
            return
        if len(self.primes) > self.store_limit:
            return
        with zipfile.ZipFile(self._primezip, "w", self._ziplevel) as mzip:
            mzip.writestr(self._primedata, self.primes.tostring(), self._ziplevel)
        mzip.close()
        
    def factors(self, zahl):
        """Return the prime factors of an integer as a list of lists. Each list consists of a prime factor and its exponent.
        """
        if (type(zahl) is not int) or (zahl < 1):
            raise ValueError("arg must be integer > 0")
        if zahl > self.primes[-1]:
            self._enlarge(zahl)
        x = []
        for n in [p for p in self.primes if zahl % p == 0]:
            i = 0
            nz = zahl
            while nz % n == 0:
                nz = nz // n
                i += 1
            x.append([n, i])
        return x
        
    def nextprime(self, zahl):
        if type(zahl) is not int:
            raise ValueError("arg must be integer")
        p = zahl
        while zahl > self.primes[-1]:      # larger than what we have so far?
            p += 1000                      # should be enough to have just 1 loop
            self._enlarge(p)
            
        for p in self.primes:
            if p > zahl:
                return p
        
    def nexttwin(self, zahl):
        if type(zahl) is not int:
            raise ValueError("arg must be integer")
        start_here = 1
        p = zahl
        while 1:   # look several times if next twin not within know primes
            for i in range(start_here, len(self.primes)):
                p1 = self.primes[i - 1]
                p2 = self.primes[i]
                if zahl <= p1 and p1 + 2 == p2:
                    return (p1, p2)
            start_here = len(self.primes) - 1
            p += 1000        # one more loop should be sufficient with this ...
            self._enlarge(p)
