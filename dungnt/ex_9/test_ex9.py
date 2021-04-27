import unittest
from .models import HanoiQuest, RESULT


class TestEx9(unittest.TestCase):
    def test_can_not_find_big_boss_room(self):
        hanoi_quest = HanoiQuest(False)
        self.assertEqual(hanoi_quest.check_can_defeat_big_boss(), RESULT[0])

    def test_can_find_big_boss_room(self):
        hanoi_quest = HanoiQuest(True)
        self.assertEqual(hanoi_quest.check_can_defeat_big_boss(), RESULT[1])

    def test_can_find_big_boss_room_1(self):
        hanoi_quest = HanoiQuest(False, True)
        self.assertEqual(hanoi_quest.check_can_defeat_big_boss(), RESULT[1])

    def test_can_get_into_big_boss_room(self):
        hanoi_quest = HanoiQuest(False, True, True)
        self.assertEqual(hanoi_quest.check_can_defeat_big_boss(), RESULT[2])

    def test_can_get_into_big_boss_room_2(self):
        hanoi_quest = HanoiQuest(True, False, True)
        self.assertEqual(hanoi_quest.check_can_defeat_big_boss(), RESULT[2])

    def test_can_defeat_big_boss(self):
        hanoi_quest = HanoiQuest(True, False, True, True)
        self.assertEqual(hanoi_quest.check_can_defeat_big_boss(), RESULT[3])

    def test_can_defeat_big_boss_2(self):
        hanoi_quest = HanoiQuest(False, True, True, True)
        self.assertEqual(hanoi_quest.check_can_defeat_big_boss(), RESULT[3])
