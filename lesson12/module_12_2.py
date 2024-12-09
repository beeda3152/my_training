import runner_and_tournament as ru_tour
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
        cls.i = 1  # № теста

    @unittest.skipIf(is_frozen , 'Тесты в этом кейсе заморожены')
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
        """b = {}
        for key in TournamentTest.all_results[TournamentTest.i]:
            b[key] = str(TournamentTest.all_results[TournamentTest.i][key])
        print(b)"""
        TournamentTest.i += 1

    @classmethod
    def tearDownClass(cls):
        b = {}
        for k in cls.all_results:
            for i1, j1 in cls.all_results[k].items():
                b[i1] = str(j1)
            print(b)

    """
    При удалении элемента из списка все остальные сдвигаются и следующий 
    элемент пропускает итерацию цикла. Если следующий успеет закончить, 
    то ответ будет не верным. На пример: на дистанции меньше 18.
    Исправление: можно обнулять скорость и дистанцию финишеров;
    можно дистанцию финишера загнать в минус participant.distance = -10 000

    def start(self):
        finishers = {}
        place = 1
        l = len(self.participants)
        while l >= place:
            for participant in self.participants:
                participant.run()
                #print(participant.distance)
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    participant.distance = 0
                    participant.speed = 0     """


if __name__ == '__main__':
    unittest.TestCase.main()