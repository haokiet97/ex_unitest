import unittest
from hopnt.ex_9.services import BanhMiService
from hopnt.ex_9.models import BanhMi


class BadmintonYardTest(unittest.TestCase):
    service = BanhMiService()

    def test_has_magic_wand_key_sword(self):
        user = BanhMi(has_magic_wand=True, has_key=True, has_sword=True)
        result = self.service.let_go_banh_mi(user)
        self.assertEqual(result, 'WINNER')

    def test_has_magic_wand_key_no_sword(self):
        user = BanhMi(has_magic_wand=True, has_key=True, has_sword=False)
        result = self.service.let_go_banh_mi(user)
        self.assertEqual(result, 'IN ROOM')

    def test_has_magic_wand_no_key(self):
        user = BanhMi(has_magic_wand=True, has_key=False, has_sword=False)
        result = self.service.let_go_banh_mi(user)
        self.assertEqual(result, 'FIND ROOM')

    def test_has_helper_key_sword(self):
        user = BanhMi(has_helper=True, has_key=True, has_sword=True)
        result = self.service.let_go_banh_mi(user)
        self.assertEqual(result, "WINNER")

    def test_has_helper_wand_key_no_sword(self):
        user = BanhMi(has_helper=True, has_key=True, has_sword=False)
        result = self.service.let_go_banh_mi(user)
        self.assertEqual(result, 'IN ROOM')

    def test_has_helper_wand_no_key(self):
        user = BanhMi(has_helper=True, has_key=False, has_sword=False)
        result = self.service.let_go_banh_mi(user)
        self.assertEqual(result, 'FIND ROOM')

    def test_no_helper_no_magic_wand(self):
        user = BanhMi(has_helper=False, has_key=False, has_sword=False)
        result = self.service.let_go_banh_mi(user)
        self.assertEqual(result, "CAN'T FIND ROOM")

