import runner as runn
import unittest

is_frozen = False

class RunnerTest(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.TestCase.main