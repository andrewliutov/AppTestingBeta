import unittest
from task_1_docs_app_test import app


class TestDocsApp(unittest.TestCase):

    def test_find_people(self):
        self.assertEqual(app.find_people('11-2'), "Геннадий Покемонов")

    def test_add_doc(self):
        self.assertEqual(
            app.add_doc('паспорт', '101101', 'Джейсон Стетхем', '1'),
                         'паспорт с номером 101101 с именем Джейсон Стетхем '
                         'добавлен в каталог и перечень полок')

    def test_delete_doc(self):
        self.assertEqual(app.delete_doc('101101'), 'Документ с номером 101101 '
                                                   'удален с полки 1')


if __name__ == '__main__':
    unittest.main()
