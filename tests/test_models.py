import unittest
import HTMLTestRunner
import xmlrunner
from polymer.models import Day
from django.contrib.auth.models import User

class TestModels(unittest.TestCase):

     def setUp(self):
        a = User(id=1, username='amol')
        b = User(id=2, username='amy')
        self.day1 = Day.objects.create(id=1, account=a, date='2014-12-10')
        self.day2 = Day.objects.create(id=2, account=b, date='2014-12-11')
                        
     def test_something(self):
        a = User(id=1, username='amol')
        b = User(id=2, username='amy')
        self.assertEquals(self.day1.date, '2014-12-10')
        self.assertEquals(self.day2.date, '2014-12-11')
  
        self.assertNotEquals(self.day1.account, b)
        self.assertEquals(self.day1.account, a)

suite = unittest.TestLoader().loadTestsFromTestCase(TestModels) #replace htmlreportsdemo with your class name
#unittest.TextTestRunner(verbosity=2).run(suite)
unittest.TextTestRunner(verbosity=2)
output = open("reports/results1.html","w")
runner = HTMLTestRunner.HTMLTestRunner(stream=output,title='Test Report',description='This is for demonstrating HTMLTestResults')
runner.run(suite)


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)

