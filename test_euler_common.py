import unittest
from euler_common import *

class TestEulerCommon(unittest.TestCase):
    
    def test_eratosthenes(self):
        self.assertEqual(eratosthenes(10), [2, 3, 5, 7])
        self.assertEqual(eratosthenes(2), [2])
        self.assertEqual(eratosthenes(1), [])
        self.assertEqual(eratosthenes(30), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    
    def test_is_prime(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(7))
        self.assertTrue(is_prime(11))
        self.assertTrue(is_prime(97))
        
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(6))
        self.assertFalse(is_prime(8))
        self.assertFalse(is_prime(9))
        self.assertFalse(is_prime(100))
    
    def test_prime_factors(self):
        self.assertEqual(prime_factors(12), {2, 3})
        self.assertEqual(prime_factors(15), {3, 5})
        self.assertEqual(prime_factors(17), {17})
        self.assertEqual(prime_factors(30), {2, 3, 5})
        self.assertEqual(prime_factors(1), set())
    
    def test_gcd(self):
        self.assertEqual(gcd(12, 8), 4)
        self.assertEqual(gcd(15, 25), 5)
        self.assertEqual(gcd(17, 13), 1)
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(7, 7), 7)
    
    def test_hcf(self):
        self.assertEqual(hcf(12, 8), 4)
        self.assertEqual(hcf(15, 25), 5)
        self.assertEqual(hcf(17, 13), 1)
        self.assertEqual(hcf(48, 18), 6)
        self.assertEqual(hcf(7, 7), 7)
    
    def test_lcm(self):
        self.assertEqual(lcm(4, 6), 12)
        self.assertEqual(lcm(15, 25), 75)
        self.assertEqual(lcm(7, 11), 77)
        self.assertEqual(lcm(12, 18), 36)
        self.assertEqual(lcm(5, 5), 5)
    
    def test_phi(self):
        self.assertEqual(phi(1), 1)
        self.assertEqual(phi(2), 1)
        self.assertEqual(phi(3), 2)
        self.assertEqual(phi(4), 2)
        self.assertEqual(phi(5), 4)
        self.assertEqual(phi(6), 2)
        self.assertEqual(phi(9), 6)
        self.assertEqual(phi(10), 4)
    
    def test_factors(self):
        self.assertEqual(factors(12), {1, 2, 3, 4, 6, 12})
        self.assertEqual(factors(15), {1, 3, 5, 15})
        self.assertEqual(factors(17), {1, 17})
        self.assertEqual(factors(1), {1})
        self.assertEqual(factors(6), {1, 2, 3, 6})
    
    def test_triangle(self):
        self.assertEqual(triangle(1), 1)
        self.assertEqual(triangle(2), 3)
        self.assertEqual(triangle(3), 6)
        self.assertEqual(triangle(4), 10)
        self.assertEqual(triangle(5), 15)
        self.assertEqual(triangle(10), 55)
    
    def test_get_digit(self):
        self.assertEqual(get_digit(12345, 0), 5)
        self.assertEqual(get_digit(12345, 1), 4)
        self.assertEqual(get_digit(12345, 2), 3)
        self.assertEqual(get_digit(12345, 3), 2)
        self.assertEqual(get_digit(12345, 4), 1)
        self.assertEqual(get_digit(12345, 5), 0)
        self.assertEqual(get_digit(7, 0), 7)
        self.assertEqual(get_digit(7, 1), 0)
    
    def test_phi_sieve(self):
        result = phi_sieve(10)
        expected = [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4]
        self.assertEqual(result, expected)
        
        small_result = phi_sieve(5)
        expected_small = [0, 1, 1, 2, 2, 4]
        self.assertEqual(small_result, expected_small)
    
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome(121))
        self.assertTrue(is_palindrome(1221))
        self.assertTrue(is_palindrome(1))
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("12321"))
        
        self.assertFalse(is_palindrome(123))
        self.assertFalse(is_palindrome(1234))
        self.assertFalse(is_palindrome("hello"))
    
    def test_is_permutation(self):
        self.assertTrue(is_permutation(123, 321))
        self.assertTrue(is_permutation(1234, 4321))
        self.assertTrue(is_permutation(125874, 874521))
        self.assertTrue(is_permutation(11, 11))
        
        self.assertFalse(is_permutation(123, 124))
        self.assertFalse(is_permutation(123, 1234))
        self.assertFalse(is_permutation(111, 112))
    
    def test_is_perfect_square(self):
        self.assertTrue(is_perfect_square(1))
        self.assertTrue(is_perfect_square(4))
        self.assertTrue(is_perfect_square(9))
        self.assertTrue(is_perfect_square(16))
        self.assertTrue(is_perfect_square(25))
        self.assertTrue(is_perfect_square(100))
        
        self.assertFalse(is_perfect_square(2))
        self.assertFalse(is_perfect_square(3))
        self.assertFalse(is_perfect_square(5))
        self.assertFalse(is_perfect_square(15))
        self.assertFalse(is_perfect_square(99))
    
    def test_digit_sum(self):
        self.assertEqual(digit_sum(123), 6)
        self.assertEqual(digit_sum(1234), 10)
        self.assertEqual(digit_sum(999), 27)
        self.assertEqual(digit_sum(1), 1)
        self.assertEqual(digit_sum(0), 0)
        self.assertEqual(digit_sum(505), 10)

if __name__ == '__main__':
    unittest.main()