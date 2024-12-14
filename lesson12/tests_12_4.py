import rt_with_exceptions as ru_tour
from unittest import TestCase
import logging
import traceback


logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')

class RunnerTest(TestCase):

    def test_walk(self):
        try:
            wal = ru_tour.Runner('walk', -5)
            for _ in range(10):
                wal.walk()
            self.assertEqual(wal.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning("Неверная скорость для Runner")
            logging.warning(traceback.format_exc())

    def test_run(self):
        try:
            runn = ru_tour.Runner(12, 10)
            for _ in range(10):
                runn.run()
            self.assertEqual(runn.distance, 100)
            logging.info('"Test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner')
            logging.warning(traceback.format_exc())

if __name__ == '__main__':
    TestCase.main()