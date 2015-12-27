Helper Files for Project Euler Problems
***********************************************

These moduduls/packages will mostly deal with common processes these problems
call for such as finding factors and primes.

Primes
================================================
Class for manipulating primes. Mostly used to make prime genrators. Works by 
loading a list of the first 10,000 primes instead of calculating them on the 
spot.

..  autoclass::  prime.Prime
	:members:

Factorial
=================================================
Contains various functions for finding factors. Uses Prime method initially 
with a list of the first 10,000 primes. If the number is larger than that
defaults to brute force method primes have been exhausted
..  automodule::  factorials
	:members:



