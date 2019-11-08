from __future__ import print_function
from gilded_rose import Item, GildedRose

if __name__ == "__main__":
    print("OMGHAI!")
    Items = [Item(name="item1", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="item3", sell_in=5, quality=9),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Conjured item3", sell_in=3, quality=12)]

    Days = 30
    import sys
    if len(sys.argv) > 1:
        Days = int(sys.argv[1]) + 1
    for day in range(Days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in Items:
            print(item)
        print("")
        GildedRose(Items).update_quality()
