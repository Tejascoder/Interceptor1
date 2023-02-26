import unittest
class Pressure:
    def __init__(self, pressure):
        self.pressure = pressure
        #print('hi',self.pressure)

    def get_pressure(self):
        if self.pressure > 80:
            return "High pressure alert!"

class TestHighPressure(unittest.TestCase):
    def test_positiveornegative(self):
        #Change argument to anything lesser than 80 becomes negative test or else greater becomes positive
        #taking postive for example
        pressure= Pressure(89)
        pressure_string = pressure.get_pressure()
        firstValue= pressure_string
        secondValue= "High pressure alert!"
        message= "Assert Equal- PASSED!"
        self.assertEqual(firstValue, secondValue, message)

unittest.main()