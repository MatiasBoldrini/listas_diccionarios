import unittest

from listas import *


class Test_Palindromo(unittest.TestCase):
    def test_NumerosRepetidos_1(self):
        diccionario = encontrar_Numeros_Repetidos([1, 2, 2, 3, 4, 4, 4])
        self.assertEqual(diccionario, {1: 1, 2: 2, 3: 1, 4: 3})

    def test_NumerosRepetidos_2(self):
        diccionario = encontrar_Numeros_Repetidos([1, 2, 2, 3, 4, 4, 4])
        self.assertEqual(diccionario, {1: 1, 2: 2, 3: 1, 4: 3})


if __name__ == "__main__": # pragma: no cover
    unittest.main()
