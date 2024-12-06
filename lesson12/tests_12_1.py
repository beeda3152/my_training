from unittest import TestCase
import runner as runn

class RunnerTest(TestCase):
    def test_walk(self):
        wal = runn.Runner('walk')
        for _ in range(10):
            wal.walk()
        self.assertEqual(wal.distance, 50)

    def test_run(self):
        ru = runn.Runner('run')
        for _ in range(10):
            ru.run()
        self.assertEqual(ru.distance, 100)

    def test_challenge(self):
        ru = runn.Runner('run')
        wal = runn.Runner('walk')
        for _ in range(10):
            ru.run()
            wal.walk()
        self.assertNotEqual(wal.distance, ru.distance)

if __name__ == '__main__':
    TestCase.main
