# -*- coding: utf-8 -*-
import unittest
import sys

from gilded_rose import Item, GildedRose, Check


class GildedRoseTest(unittest.TestCase):

    def setUp(self):
        self.items = [Item(name="item1", sell_in=10, quality=20),
                      Item(name="Aged Brie", sell_in=2, quality=0),
                      Item(name="item3", sell_in=5, quality=9),
                      Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                      Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
                      Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
                      Item(name="Conjured item3", sell_in=3, quality=12)]

    def test_items_quality_decreases_as_name_suggest(self): 

        itemsValues = [[20, 0,	9, 80, 80, 49, 12],
                       [19, 1,	8, 80, 80, 50, 10],
                       [18, 2,	7, 80, 80, 50, 8],
                       [17, 4,	6, 80, 80, 50, 6],
                       [16, 6,	5, 80, 80, 50, 2],
                       [15, 8,	4, 80, 80, 50, 0],
                       [14, 10, 2,	80, 80,	50,	0],
                       [13, 12, 0,	80,	80,	50,	0],
                       [12, 14, 0,	80,	80,	50,	0],
                       [11, 16, 0,	80,	80,	50,	0],
                       [10, 18, 0,	80,	80,	50,	0],
                       [8,	20,	0, 80, 80, 0, 0]]

        itemsSellins = [[10, 2,	5, 0, -1, 10, 3],
                        [9, 1, 4, 0, -1, 9, 2],
                        [8, 0, 3, 0, -1, 8, 1],
                        [7, -1, 2, 0, -1, 7, 0],
                        [6, -2, 1, 0, -1, 6, -1],
                        [5, -3, 0, 0, -1, 5, -2],
                        [4, -4, -1, 0, -1, 4, -3],
                        [3, -5, -2, 0, -1, 3, -4],
                        [2, -6, -3, 0, -1, 2, -5],
                        [1, -7, -4, 0, -1, 1, -6],
                        [0, -8, -5, 0, -1, 0, -7],
                        [-1, -9, -6, 0, -1, -1, -8]]
        gilded_rose = GildedRose(self.items)
        days = 11
        iter = 0
        if len(sys.argv) > 1:
            days = int(sys.argv[1]) + 1
        for day in range(days):
            gilded_rose.update_quality()
            arrayOfItemsValues = []
            arrayOfItemsSellins = []
            iter = iter + 1
            for item in self.items:
                arrayOfItemsValues.append(item.quality)
                arrayOfItemsSellins.append(item.sell_in)
            self.assertEqual([itemsValues[iter], itemsSellins[iter]], [arrayOfItemsValues, arrayOfItemsSellins])

    def test_add_backstage(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=10),
                 Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([12, 13], [items[0].quality, items[1].quality])

    def test_add_aged_brie(self):
        items = [Item(name="Aged Brie", sell_in=2, quality=0),
                 Item(name="Aged Brie", sell_in=-1, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([1, 2], [items[0].quality, items[1].quality])

    def test_add_sulfuras(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
                 Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([80, 80], [items[0].quality, items[1].quality])

    def test_add_conjured(self):
        items = [Item(name="Conjured item3", sell_in=1, quality=10),
                 Item(name="Conjured item4", sell_in=-1, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([8, 6], [items[0].quality, items[1].quality])

    def test_add_normal(self):
        items = [Item(name="item1", sell_in=9, quality=10),
                 Item(name="item1", sell_in=-2, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([9, 8], [items[0].quality, items[1].quality])

    def test_updateQuality(self):
        item = Item(name="item1", sell_in=9, quality=10)
        self.assertEqual(9, Check(item).updateQuality(-1).quality)

    def test_updateSellIn(self):
        item = Item(name="item1", sell_in=9, quality=10)
        self.assertEqual(8, Check(item).updateSellin(-1).sell_in)

    def test_items_quality_not_less_zero(self):
        items = [Item(name="item1", sell_in=9, quality=0),
                 Item(name="item1", sell_in=-2, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertNotEqual([-1, -2], [items[0].quality, items[1].quality])

    def test_items_checker_normal(self):
        items = [Item(name="item1", sell_in=1, quality=23)]
        self.assertTrue(Check(items[0]).is_normal())

    def test_items_checker_aged(self):
        items = [Item(name="Aged Brie", sell_in=1, quality=1)]
        self.assertTrue(Check(items[0]).is_aged_brie())

    def test_items_checker_backstage(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=1, quality=1)]
        self.assertTrue(Check(items[0]).is_backstage())

    def test_items_checker_sulfuras(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=1)]
        self.assertTrue(Check(items[0]).is_sulfuras())

    def test_items_checker_conjured(self):
        items = [Item(name="Conjured item3", sell_in=1, quality=22)]
        self.assertFalse(Check(items[0]).is_normal())

if __name__ == '__main__':
    unittest.main()
