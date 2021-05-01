
import unittest
import calc 

class Testcalc(unittest.TestCase):
    def test_addition_works(self):
        summ = calc.sum(3,5)
        self.assertEqual(summ, 8)

    def test_addition_no(self):
        summ = calc.sum(4,10)
        self.assertEqual(summ, 14)
    
    def test_add(self):
        summ = calc.sum(4,10)
        self.assertEqual(summ, 10)
    
    def test_subtract(self):
        subb = calc.sub(4,12)
        self.assertEqual(subb,8)
    
    def test_subt(self):
        s = calc.sub(10,5)
        self.assertEqual(s,5)

    def test_su(self):
        su = calc.sub(10,5)
        self.assertEqual(su,-5)
    
    def test_m(self):
        m = calc.mul(10,5)
        self.assertEqual(m,50)

    def test_mu(self):
        m = calc.mul(1,5)
        self.assertEqual(m,5)

    def test_mul(self):
        m = calc.mul(5, .2)
        self.assertEqual(m,2)

    def test_d(self):
        m = calc.div(10,5)
        self.assertEqual(m,.5)
    def test_div(self):
        d = calc.div(10,50)
        self.assertEqual(d,5)
    def test_divide(self):
        d = calc.div(10,500)
        self.assertEqual(d,5)



if __name__ == '__main__':
    unittest.main()
