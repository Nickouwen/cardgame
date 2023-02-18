from unittest import TestCase

from src.cardgame_service.deck.card import Card


class TestCard(TestCase):
    def setUp(self) -> None:
        self.card = Card()


class TestInit(TestCard):
    def test_initial_number(self):
        self.assertEqual(self.card.get_number(), 1)

    def test_number_too_high(self):
        with self.assertRaises(ValueError):
            Card(105)

    def test_number_too_low(self):
        with self.assertRaises(ValueError):
            Card(0)


class TestSetNumber(TestCard):
    def test_set_card_number(self):
        self.card.set_number(5)
        self.assertEqual(self.card.get_number(), 5)

    def test_set_out_of_bounds(self):
        with self.assertRaises(ValueError):
            self.card.set_number(105)

        with self.assertRaises(ValueError):
            self.card.set_number(0)
