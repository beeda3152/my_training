import unittest
import module_12_1
import module_12_2

uni_testST = unittest.TestSuite()
uni_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
uni_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runn = unittest.TextTestRunner(verbosity=2)
runn.run(uni_testST)
