import unittest
import tests_12_3


uni_testST = unittest.TestSuite()
uni_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
uni_testST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runn = unittest.TextTestRunner(verbosity=2)
runn.run(uni_testST)
