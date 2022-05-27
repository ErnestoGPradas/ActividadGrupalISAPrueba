import unittest
import ActividadGrupalISA


class TestUnitarios(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(ActividadGrupalISA.suma(-8, 4), -4)

    def test_resta(self):
        self.assertEqual(ActividadGrupalISA.resta(5, 12), -7)

    def test_raiz_cuadrada(self):
        self.assertEqual(ActividadGrupalISA.raiz_cuadrada(9), 3)


if __name__ == "__main__":
    unittest.main()
