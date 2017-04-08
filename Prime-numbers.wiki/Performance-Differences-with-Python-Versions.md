Just a few notes on differences I observed using this program with different Python versions.

With an empty `primenumbers.zip` store I invoked method `nextprime` for parameter number 5 million. This forces the `primes` array to be built from scratch up to a prime number exceeding 5 million (5'001'001). Performance differences between Python versions and their bitness, as well as different primality test algorithms are quite remarkable.

Test machine was Windows 10 64bit, AMD 4 GHz, 8 GB memory.

Interestingly, about the same profile came out, when using an Intel-based (i7-6700) Win 10 laptop with only 2.6 GHz, but 16 GB memory and a Win system SSD. The (Intel) laptop even showed a slightly better performance, which probably goes back to the Python versions being installed on the SSD system disk.

Py Version | Eratosthenes | Miller-Rabin
--------|--------------|--------------
2.7 x86 | 71 sec | 40 sec |
3.5 x64 | 45 sec | 24 sec |
3.6 x64 | 29 sec | 21 sec |

## Conclusion
Python 3.x 64bit is about twice as fast as Python 2.7, especially when using the Miller-Rabin-Test. 
Some minor but noticable differences do exist between Python 3.5 and 3.6 - as was to be expected according to remarks accompanying the 3.6 release.

I also did performance tests after porting the `primes.py` module to Cython (v 0.25.2) and then using the `primes.pyd` version. The above Miller-Rabin-Tests showed very significant speed improvements by a factor of more than 20 (both, for Python 2 and 3). This means that prime numbers up to about **5 million** can be calculated and stored in an array in **just 1 second** using Python 3!

Improvement factors for other methods of the module range from 1.8 to 6.

## Remark on PYX / Cython Versions
I have tested most of the above figures using a C-compiled version of `primes.py`. The source for this is contained in `primes.pyx`, and the resulting C sources are contained in `primes.c27` (for Python 2) and `primes.c3x`, respectively.

The performance improvements are remarkable: calculating the table of primes until just above 5 million is 20 times faster in C than in pure Python. So, e.g. with Python 3.6 x64 you can do that in just about 1 second.