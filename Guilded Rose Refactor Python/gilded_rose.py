# -*- coding: utf-8 -*-
class check():    
    def updateQuality(item, by):
        if item.sell_in >=0:
            item.quality = item.quality + by;
        else:
            item.quality = item.quality + 2*by;
        if item.quality < 0:
            item.quality=0
        return item

    def updateSellin(item, by):
        if not check.is_sulfuras(item):
            item.sell_in = item.sell_in + by;
        return item

    def is_sulfuras(item):
        if item.name == "Sulfuras, Hand of Ragnaros":
           return True
        return False

    def is_backstage(item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return True

    def is_normal(item):
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name.lower().find("conjured") == -1:#1
                if item.quality > 0:
                    if not check.is_sulfuras(item):
                        return True
                    return False

    def is_aged_brie(item):
        if item.name == "Aged Brie":
               return True
        return False

    def is_backstage_sellin_less_11(item):
        if item.sell_in < 11:
           if item.quality < 50:
              return True

    def is_backstage_sellin_less_6(item):
        if item.sell_in < 6:
            if item.quality < 50:
               return True

    def add_backstage(item):
        if check.is_backstage(item):
            if check.is_backstage_sellin_less_6(item):
                check.updateQuality(item, 3)
            elif check.is_backstage_sellin_less_11(item):
                check.updateQuality(item, 2)
            if item.sell_in < 0:
                item.quality = 0

    def sub_conjured(item, subber, quality):
        if item.quality > quality and item.name.lower().find("conjured") != -1:#2
            check.updateQuality(item, subber)

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            check.updateSellin(item, -1)
            if check.is_aged_brie(item):
                check.updateQuality(item, 1)
            elif check.is_backstage(item):
                check.add_backstage(item)
            elif check.is_sulfuras(item):
                item.quality = 80
            else:
                if check.is_normal(item):
                    check.updateQuality(item, -1)
                else:
                    check.updateQuality(item, -2)
            if item.quality >= 50 and not check.is_sulfuras(item):
                item.quality = 50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
