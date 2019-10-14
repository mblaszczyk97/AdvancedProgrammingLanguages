# -*- coding: utf-8 -*-
class check():
    def is_sulfuras(item):
        if item.name == "Sulfuras, Hand of Ragnaros":
           return True
        return False

    def is_normal(item):
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name.lower().find("conjured") == -1:#1
                if item.quality > 0:
                    if not check.is_sulfuras(item):
                        return True

    def is_backstage(item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            return True
    
    def is_backstage_sellin_less_11(item):
        if item.sell_in < 11:
           if item.quality < 50:
              return True

    def is_backstage_sellin_less_6(item):
        if item.sell_in < 6:
            if item.quality < 50:
               return True

    def is_aged_brie(item):
        if item.name == "Aged Brie":
               return True
        return False

    def quality_not_zero(item):
        if item.quality > 0:
               return True
        return False


class quality():
    def add_quality_in_less_50(item):
        if item.quality < 50:
           item.quality = item.quality + 1

    def add_bakcstage(item):
        if check.is_backstage(item):
            if check.is_backstage_sellin_less_11(item):
                item.quality = item.quality + 1
            if check.is_backstage_sellin_less_6(item):
                item.quality = item.quality + 1

    def sub_conjured(item, subber, quality):
        if item.quality > quality and item.name.lower().find("conjured") != -1:#2
           item.quality = item.quality - subber#2

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if check.is_normal(item):#1
               item.quality = item.quality - 1

            if not check.is_normal(item) and item.quality < 50:
                    item.quality = item.quality + 1
                    quality.sub_conjured(item, 3, 2)
                    quality.add_bakcstage(item)

            if not check.is_sulfuras(item):
                item.sell_in = item.sell_in - 1

            if item.sell_in < 0 and not check.is_aged_brie(item):
                    quality.sub_conjured(item, 1, 1)#3
                    if not check.is_backstage(item) and check.quality_not_zero(item) and not check.is_sulfuras(item):
                        item.quality = item.quality - 1
                    else:
                        if not check.is_sulfuras(item):
                            item.quality = item.quality - item.quality

            if item.sell_in < 0 and check.is_aged_brie(item):
                    quality.add_quality_in_less_50


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
