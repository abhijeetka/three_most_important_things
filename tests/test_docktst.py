import unittest
import HTMLTestRunner
import xmlrunner



from django.test import Client

# Create your tests here.
class TestView(unittest.TestCase):
    
    def setUp(self):
        self.client = Client()


    def test_register(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    
    #    self.assertContains(response, 'Register Your Account')

    #    response = self.client.post('/register/', {'username': 'amol', 'password': 'password','email': 'amolsh@cybage.com'})
     #   self.assertEqual(response.status_code, 200)







suite = unittest.TestLoader().loadTestsFromTestCase(TestView) #replace htmlreportsdemo with your class name
#unittest.TextTestRunner(verbosity=2).run(suite)
unittest.TextTestRunner(verbosity=2)
output = open("reports/results.html","w")
runner = HTMLTestRunner.HTMLTestRunner(stream=output,title='Test Report',description='This is for demonstrating HTMLTestResults')
runner.run(suite)


if __name__ == '__main__':
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='test-reports'),
        # these make sure that some options that are not applicable
        # remain hidden from the help menu.
        failfast=False, buffer=False, catchbreak=False)

