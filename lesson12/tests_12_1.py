from runner import Runner as r
from unittest import TestCase

class RunnerTest(TestCase):
    def test_walk(self):
        wal = r('walk')
        for _ in range(10):
            wal.walk()
        self.assertEqual(wal.distance, 50)

    def test_run(self):
        ru = r('run')
        for _ in range(10):
            ru.run()
        self.assertEqual(ru.distance, 100)

    def test_challenge(self):
        ru = r('run')
        wal = r('walk')
        for _ in range(10):
            ru.run()
            wal.walk()
        self.assertNotEqual(wal.distance, ru.distance)

if __name__ == '__main__':
    TestCase.main
