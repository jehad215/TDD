import unittest
import tests

class TSpeed (unittest.TestCase):
    def test_speed1(self):
        self.assertEqual('Invalid', tests.car_speed(-1))
    def test_speed2(self):
        self.assertEqual('Low', tests.car_speed(39))
    def test_speed3(self):
        self.assertEqual('Normal', tests.car_speed(119))
    def test_speed4(self):
        self.assertEqual('High', tests.car_speed(199))
    def test_speed5(self):
        self.assertEqual('V.High', tests.car_speed(219))
    def test_speed6(self):
        self.assertEqual('Invalid', tests.car_speed(221))

mysuitspeed = unittest.TestSuite()
mysuitspeed.addTest(TSpeed())


class TScore (unittest.TestCase):
    def test_score1(self):
        self.assertEqual('Invalid', tests.student_score(-1))
    def test_score2(self):
        self.assertEqual('Failed', tests.student_score(49))
    def test_score3(self):
        self.assertEqual('Passed', tests.student_score(64))
    def test_score4(self):
        self.assertEqual('Good', tests.student_score(74))
    def test_score5(self):
        self.assertEqual('V.Good', tests.student_score(84))
    def test_score6(self):
        self.assertEqual('Excellent', tests.student_score(90))
    def test_score7(self):
        self.assertEqual('Invalid', tests.student_score(110))

mysuitscore = unittest.TestSuite()
mysuitscore.addTest(TScore())



if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(mysuitspeed)
    runner.run(mysuitscore)

