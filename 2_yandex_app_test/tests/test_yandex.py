import unittest
from task_2_yandex_test import yandex


class MyTestCase(unittest.TestCase):
    def test_upload_folder(self):
        self.assertEqual(yandex.backup_ul.upload_folder(), 201)

    def test_upload_folder_ifexists(self):
        self.assertEqual(yandex.backup_ul.upload_folder(), 409)


if __name__ == '__main__':
    unittest.main()
