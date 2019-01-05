#!/usr/bin/env python
# codding: UTF-8
#
## @package Ranking Class
#
#  @brief This class generate a ranking from inputs
#  @note calculate footrule and kemeny distance
#  @author Carlos Thadeu Santos - ID: 17113050228
#  @date 04-Nov-2018
#  @version 0.0.2 alpha
#
from ranking import *
import unittest

class TestRanking(unittest.TestCase):
    """
    Testa entrada de rankings
    """
    def testInput(self):
        """
        Testa se um ranking para entradas em tuplas
        :return:
        """
        a = (0.75, 0.36, 0.65, -1.5, 0.85)
        b = [0.75, 0.36, 0.65, -1.5, 0.85]
        result = Ranking(a)
        expect = [2, 4, 3, 5, 1]
        self.assertEqual(result.ranking, expect)
        result = Ranking(b)
        expect = [2, 4, 3, 5, 1]
        self.assertEqual(result.ranking, expect)

    def testFootrule(self):
        a = [4,3,1,5,2]
        b = (5,4,1,3,2)
        x = Ranking(a)
        y = Ranking(b)
        expect = 4
        self.assertEqual(x.footrule(x,y), expect)

    def testKemeny(self):
        a = Ranking([4,3,1,5,2])
        b = Ranking((5,4,1,3,2))
        expect = 2
        self.assertEqual(a.kemeny(a,b), expect)

    def testInversion(self):
        a = Ranking((1,5,3,8,4,2,7,6))
        expect = 10
        self.assertEqual(a.invCount(), expect)
        b = Ranking((1, 2, 4, 5, 3))
        expect = 2
        self.assertEqual(b.invCount(), expect)

    def testNoneExceptionsTuple(self):
        a = (1,5,3,8,4,2,7,None)
        result = Ranking(a)
        self.assertRaises(TypeError, result)

    def testNoneExceptionsList(self):
        a = [1,5,3,8,4,2,7,None]
        result = Ranking(a)
        self.assertRaises(TypeError, result)

    def testNoneExceptionsInstance(self):
        a = None
        result = Ranking(a)
        self.assertRaises(TypeError, result)

    def testDistinctElementsList(self):
        a = [1,2,3,4,4,5,6,7]
        result = Ranking(a)
        self.assertRaises(TypeError, result)    

    def testDistinctElementsTuple(self):
        a = (1,5,3,8,4,2,7,7)
        result = Ranking(a)
        self.assertRaises(TypeError, result)

    def testGetRank(self):
        expect = 5
        result = Ranking((0.75, 0.36, 0.65, -1.5, 0.85))
        self.assertEqual(result.getRank(4), expect)
        
    def testGetNumItens(self):
        expect = 5
        result = Ranking((0.75, 0.36, 0.65, -1.5, 0.85))
        self.assertEqual(result.getNumItems, expect)

    # Testa Footrule - valores da AD1
    def testFdist1(self):
        instancia1 = Ranking(tuple("43152"))
        instancia2 = Ranking(list("541326"))
        self.assertEqual(instancia1.fDist(instancia2), None)
    def testFdist2(self):
        instancia1 = Ranking(list("43152"))
        instancia2 = Ranking(tuple("54132"))
        self.assertEqual(instancia1.fDist(instancia2),4)

    # Testa distâncias Kemeny - valores da AD1
    def testKdist1(self):
        instancia1 = Ranking(tuple("43152"))
        instancia2 = Ranking(tuple("541326"))
        self.assertEqual(instancia1.kDist(instancia2), None)
    def testKdist2(self):
        instancia1 = Ranking(tuple("43152"))
        instancia2 = Ranking(tuple("54132"))
        self.assertEqual(instancia1.kDist(instancia2),2)
    
    ## Testa inversões
    def testInvcount1(self):
        instancia1 = Ranking((2,1,3,4,5))
        self.assertEqual(instancia1.invCount(),1)
    def testInvcount2(self):
        instancia1 = Ranking([1,2,3,4,5,6,7,8,9,10])
        self.assertEqual(instancia1.invCount(),0)

    
    #def test
    #def testDistances(self):
     #   a = [4,3,1,5,2]
      #  b = [5,4,1,3,2]
       # c = (1,2,4,5,3)
        #x = Ranking(a)
        #y = Ranking(b)
        #z = Ranking(c)
        #self.assertEqual(x.footrule(x,y),4)
        #self.assertEqual(x.kemeny(x, y), 2)

if __name__ == '__main__':
    unittest.main()
