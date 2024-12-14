import runner as runn
import unittest
import runner_and_tournament as ru_tour



class RunnerTest(unittest.TestCase):
    is_frozen = False
    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        wal = runn.Runner('walk')
        for _ in range(10):
            wal.walk()
        self.assertEqual(wal.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        ru = runn.Runner('run')
        for _ in range(10):
            ru.run()
        self.assertEqual(ru.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        ru = runn.Runner('run')
        wal = runn.Runner('walk')
        for _ in range(10):
            ru.run()
            wal.walk()
        self.assertNotEqual(wal.distance, ru.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.i = 1  # № теста

    #@unittest.skipIf(not is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.run1 = ru_tour.Runner('Усэйн', 10)
        self.run2 = ru_tour.Runner('Андрей', 9)
        self.run3 = ru_tour.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour1(self):
        tour = ru_tour.Tournament(90, self.run1, self.run3)
        rez = tour.start()
        TournamentTest.all_results[TournamentTest.i] = rez
        self.assertTrue(rez[2] == self.run3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour2(self):
        tour = ru_tour.Tournament(90, self.run2, self.run3)
        rez = tour.start()
        TournamentTest.all_results[TournamentTest.i] = rez
        self.assertTrue(rez[2] == self.run3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour3(self):
        tour = ru_tour.Tournament(90, self.run1, self.run2, self.run3)
        rez = tour.start()
        TournamentTest.all_results[TournamentTest.i] = rez
        self.assertTrue(rez[3] == self.run3.name)

    def tearDown(self):
        TournamentTest.i += 1

    @classmethod
    def tearDownClass(cls):
        b = {}
        for k in cls.all_results:
            for i1, j1 in cls.all_results[k].items():
                b[i1] = str(j1)
            print(b)

if __name__ == '__main__':
    unittest.TestCase.main