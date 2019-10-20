# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_items_quality_decreases_as_name_suggest(self):
        items = [
             Item(name="item1", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="item3", sell_in=5, quality=9),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Conjured item3", sell_in=3, quality=12)
             ]

        itemsValues = [
            [20, 0,	9, 80, 80, 49, 12],
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
            [8,	20,	0, 80, 80, 0, 0],
        ]

        gilded_rose = GildedRose(items)
        days = 11
        iter = 0
        import sys
        if len(sys.argv) > 1:
            days = int(sys.argv[1]) + 1
        for day in range(days):
            gilded_rose.update_quality()
            arrayOfItems = []
            iter = iter + 1
            for item in items:
                arrayOfItems.append(item.quality)
            self.assertEqual(itemsValues[iter], arrayOfItems)

    def test_items_sellin_decreases_as_name_suggest(self):
        items = [
             Item(name="item1", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="item3", sell_in=5, quality=9),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Conjured item3", sell_in=3, quality=12)
             ]

        itemsSellins = [
            [10, 2,	5, 0, -1, 10, 3],
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
            [-1, -9, -6, 0, -1, -1, -8],
        ]

        gilded_rose = GildedRose(items)
        days = 11
        iter = 0
        import sys
        if len(sys.argv) > 1:
            days = int(sys.argv[1]) + 1
        for day in range(days):
            gilded_rose.update_quality()
            arrayOfItems = []
            iter = iter + 1
            for item in items:
                arrayOfItems.append(item.sell_in)
            self.assertEqual(itemsSellins[iter], arrayOfItems)

    def test_add_backstage(self):
        items = [
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=9, quality=10),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=4, quality=10)
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual([12,13], [items[0].quality,items[1].quality])

if __name__ == '__main__':
    unittest.main()
