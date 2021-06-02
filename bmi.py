max=24
min=18.5
owner='Pai'
def bmi(w,h):
    return w/h**2

def calculate(w,h):
    return round(w/h**2,2)
def cmToM(cm):
    return cm/100



class Profile:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def showProfile(self):
        print('My name is %s, I am %s years old.' % (self.name, self.age))

#print(__name__)#shou __main__
if __name__ == '__main__':
    import unittest
    #1. define test case
    class BmiTestCase(unittest.TestCase):

        def test_calculate(self):
            result=calculate(65,1.75)
            self.assertEqual(21.22,result)
        def test_cmToM(self):
            result=cmToM(175)
            self.assertEqual(1.75,result)
        def test_profile(self):
            pro=Profile("Pai",16)    
            self.a
    #2 define test suite
    tests=[#put into list
        BmiTestCase('test_calculate'),
        BmiTestCase('test_cmToM'),            
    ]      
   
    suite = unittest.TestSuite()
    suite.addTests(tests)
    #define test runner
    runner = unittest.TextTestRunner()
    pass
  