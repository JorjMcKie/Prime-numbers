# -*- coding: latin-1 -*-
import os
import array
import zipfile
import bisect

class Primes():
    _appdata = os.path.expanduser("~")
    _primedata = "primenumbers.data"
    _primezip  = os.path.join(_appdata, "primenumbers.zip")
    primes = array.array("L")
    store_limit = 5*10**6           # largest prime we want to store
    if str is bytes:
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
        """Change maximum prime that can be stored to disk."""
        if max_primes > 0:
            self.store_limit = max_primes

#==============================================================================
# Use Miller-Rabin-Test for primality checks
#==============================================================================
    def _enlarge(self, zahl):
        """Extend the primes array up to provided parameter."""
        def mrtest(n):
            # the actual Miller-Rabin logic ----------------------------------
            def mrt(n, a):
                n1 = n - 1
                d = n1 >> 1
                j = 1
                while (d & 1) == 0:
                    d >>= 1
                    j += 1
                t = a
                p = a
                while d:  # square and multiply: a^d mod n
                    d >>= 1
                    p = p*p % n
                    if d & 1:
                        t = t*p % n
                if t == 1 or t == n1:
                    return True   # n ist wahrscheinlich prim
                for k in range(1, j):
                    t = t*t % n
                    if t == n1: return True
                    if t <= 1: break
                return False      # n ist nicht prim
            #-----------------------------------------------------------------
        
            # testing the following a-values suffices for a determninistic test,
            # if checked number n <= 2**32
            # see https://de.wikipedia.org/wiki/Miller-Rabin-Test
            # n <     1.373.653 => alist = {2, 3}
            # n <     9.080.191 => alist = {31, 73}
            # n < 4.759.123.141 => alist = {2, 7, 61}
            if n < 1373653:
                alist = (2, 3)
            elif n < 9080191:
                alist = (31, 73)
            else:
                alist = (2, 7, 61)
        
            for a in alist:
                if not mrt(n, a):
                    return False
            return True

        check = self.primes[-1]        # last stored prime
        while check <= zahl:
            check += 2                 # stick with odd numbers
            if mrtest(check):
                self.primes.append(check)
        return

#==============================================================================
# Save to disk (eventually) when object gets deleted
#==============================================================================
    def __del__(self):
        if self.oldlen >= len(self.primes):      # did not go beyond old limit
            return
        if self.primes[-1] > self.store_limit:   # exceeds size limit
            return
        self.save()
        
    def save(self):
        with zipfile.ZipFile(self._primezip, "w", self._ziplevel) as mzip:
            mzip.writestr(self._primedata, self.primes.tostring(), self._ziplevel)
        mzip.close()

#==============================================================================
# Binary search for index of next prime
#==============================================================================
    def _nxt_prime_idx(self, zahl):
        """Binary search for the smallest index i with zahl <= primes[i]
        """
        p = zahl
        while zahl >= self.primes[-1]: # larger than what we have so far?
            p += 1000                  # big enough for max. one loop
            self._enlarge(p)
        return bisect.bisect_left(self.primes, zahl)
        
#==============================================================================
# Calculate prime factors
#==============================================================================
    def factors(self, zahl):
        """Return the prime factors of an integer as a list of lists. Each list consists of a prime factor and its exponent.
        """
        if (type(zahl) is not int) or (zahl < 1):
            raise ValueError("arg must be integer > 0")
        if zahl == self.nextprime(zahl):
            return [[zahl, 1]]
        x = []
        for n in self.primes:
            if n > zahl: break
            if zahl % n != 0: continue
            i = 0
            nz = zahl
            while nz % n == 0:
                nz = nz // n
                i += 1
            x.append([n, i])
        return x
        
#==============================================================================
# Deliver next prime
#==============================================================================
    def nextprime(self, zahl):
        """Return the next prime following a provided number."""
        return self.primes[self._nxt_prime_idx(zahl)]
        
#==============================================================================
# Deliver next prime twin
#==============================================================================
    def nexttwin(self, zahl):
        """Return the first prime twin following a provided number."""
        start_here = max(self._nxt_prime_idx(zahl), 1)   # prime twin must be GE ...
        p = zahl
        while 1:   # look several times if next twin not within know primes
            for i in range(start_here, len(self.primes)):
                p1 = self.primes[i - 1]
                p2 = self.primes[i]
                if zahl <= p1 and p1 + 2 == p2:
                    return (p1, p2)
            start_here = len(self.primes) - 1
            p += 1000        # big enough for max. one loop
            self._enlarge(p)

    def prev_twins(self, zahl):
        """Return the number of prime twins less or equal a given number."""
        p = zahl
        while zahl > self.primes[-1]:      # larger than what we have so far?
            p += 1000                      # big enough for max. one loop
            self._enlarge(p)
        j = 0
        for i in range(len(self.primes)-1):
            if self.primes[i + 1] > zahl:
                break
            if self.primes[i] == self.primes[i + 1] - 2:
                j += 1
        return j

    def prev_primes(self, zahl):
        """Return the number of primes less or equal a given number."""
        p = zahl
        while zahl > self.primes[-1]:      # larger than what we have so far?
            p += 1000                      # big enough for max. one loop
            self._enlarge(p)
        return bisect.bisect_right(self.primes, zahl)
