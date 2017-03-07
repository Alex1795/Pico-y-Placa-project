
import unittest
from pyp import Consulta
from pyp import check



class Test(unittest.TestCase):

    #Checks if the program gives a correct output when the car is allowed to be on the road all day
    def testotherday(self):
        a = Consulta('XYZ-1234','jueves','12:35')
        self.assertEqual(a.predictor(),'Puede circular todo el día de hoy')

    #Checks if the program give the correct output when the car is allowed to be on the read only on certain hours
    #and when it is out of the allowed time

    def testsameday(self):

        a = Consulta('XYZ-0000','viernes','06:55')
        self.assertEqual(a.predictor(), 'Puede circular hoy antes de las 7:00, despues de las 19:30  y entre las 9:30 y 16:30')

        a.hour = '07:01'
        self.assertEqual(a.predictor(),'No puede circular hoy en este horario')


    #Tests the output when an acceptable and a wrong plate number is given
    def testcheckplate(self):

        with self.assertRaises(SyntaxError) as error:
            check('pio-1234')

        self.assertTrue('Por favor ingrese una placa valida en la forma: AAA-0000' in str(error.exception))

        self.assertEqual(check('PIO-1234'),0)

    # Tests the output when an acceptable and a wrong day name is given
    def testcheckday(self):

        with self.assertRaises(SyntaxError) as error:
            check(0,'marte')

        self.assertTrue('Por favor ingrese un día válido' in str(error.exception))

        self.assertEqual(check(0,'martes'),0)

    # Tests the output when an acceptable and a wrong date is given
    def testcheckdate(self):

        with self.assertRaises(SyntaxError) as error:
            check(0,'2017/01/01',0)

        self.assertTrue('Por favor ingrese un día válido' in str(error.exception))

        self.assertEqual(check(0,'01/01/2017'),0)

    # Tests the output when an acceptable and a wrong time format is given
    def testchecktime(self):

        with self.assertRaises(SyntaxError) as error:
            check(0,0, '7:')

        self.assertTrue('Por favor ingrese una hora separada por ":" ' in str(error.exception))

        with self.assertRaises(SyntaxError) as error:
            check(0,0, '7:65')

        self.assertTrue('La hora no puede tener mas de 59 minutos' in str(error.exception))

        self.assertEqual(check(0,0,'7:35'),0)








if __name__ == '__main__':
    unittest.main()


