class Check():
    """Class which helps us to check different cases in Item object"""
    def __init__(self, item):
        self.item = item

    def updateQuality(self, by):
        """Updating Quality of one item"""
        if self.item.sell_in >= 0:
            self.item.quality = self.item.quality + by
        else:
            self.item.quality = self.item.quality + 2*by
        if self.item.quality < 0:
            self.item.quality = 0
        return self.item

    def updateSellin(self, by):
        """Updating Sellin of one item"""
        if not Check(self.item).is_sulfuras():
            self.item.sell_in = self.item.sell_in + by
        return self.item

    def is_sulfuras(self):
        """Bool check for Sulfuras"""
        if self.item.name == "Sulfuras, Hand of Ragnaros":
            return True
        return False

    def is_backstage(self):
        """Bool check for Backstage"""
        if self.item.name == "Backstage passes to a TAFKAL80ETC concert":
            return True
        return False

    def is_normal(self):
        """Bool check for Normal"""
        if self.item.name != "Aged Brie" and self.item.name != "Backstage passes to a TAFKAL80ETC concert" and self.item.name.lower().find("conjured") == -1:#1
            if self.item.quality > 0:
                if not Check(self.item).is_sulfuras():
                    return True
        return False

    def is_aged_brie(self):
        """Bool check for Aged Brie"""
        if self.item.name == "Aged Brie":
            return True
        return False

    def is_backstage_sellin_less_11(self):
        """Bool check for Concert less than 11 sellin"""
        if self.item.sell_in < 11:
            if self.item.quality < 50:
                return True
        return False

    def is_backstage_sellin_less_6(self):
        """Bool check for Concert less than 6 sellin"""
        if self.item.sell_in < 6:
            if self.item.quality < 50:
                return True
        return False

    def add_backstage(self):
        """Changing backstage according to instructions"""
        if Check(self.item).is_backstage():
            if Check(self.item).is_backstage_sellin_less_6():
                Check(self.item).updateQuality(3)
            elif Check(self.item).is_backstage_sellin_less_11():
                Check(self.item).updateQuality(2)
            if self.item.sell_in < 0:
                self.item.quality = 0

    def sub_conjured(self, subber, quality):
        """Method for subbing conjured items"""
        if self.item.quality > quality and self.item.name.lower().find("conjured") != -1:#2
            Check(self.item).updateQuality(subber)

class GildedRose():
    """Main Gilded Rose class"""
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """Method to update every item"""
        for item in self.items:
            Check(item).updateSellin(-1)
            if Check(item).is_aged_brie():
                Check(item).updateQuality(1)
            elif Check(item).is_backstage():
                Check(item).add_backstage()
            elif Check(item).is_sulfuras():
                item.quality = 80
            else:
                if Check(item).is_normal():
                    Check(item).updateQuality(-1)
                else:
                    Check(item).updateQuality(-2)
            if item.quality >= 50 and not Check(item).is_sulfuras():
                item.quality = 50


class Item:
    """Item object class"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
