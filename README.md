Advanced Programming Languages

Projects:  
1 - Gilded Rose - only add to code:  
	Adding new functionality to badly coded eshop 
   
2 -  
Krok 1:  
  
Wyciągnięcie linii zmieniającej wartoś **quality** przedmiotu w sklepie:  
zamiana linii:  
```python
def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name.lower().find("conjured") == -1:#1
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1
```
na  
```python
    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name.lower().find("conjured") == -1:  #1
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        check.updateQuality(item, -1)
            else:
                if item.quality < 50:
                    check.updateQuality(item, 1)
                    if item.quality > 2 and item.name.lower().find("conjured") != -1:                                                               #2
                            check.updateQuality(item, -3)                                                                                           #3
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                check.updateQuality(item, 1)
                        if item.sell_in < 6:
                            if item.quality < 50:
                                check.updateQuality(item, 1)
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.name.lower().find("conjured") != -1 and item.quality > 1:                                                           #4
                                check.updateQuality(item, -1)                                                                                       #5
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                check.updateQuality(item, -1)
                    else:
                        check.updateQuality(item, -item.quality)
                else:
                    if item.quality < 50:
                        check.updateQuality(item, 1)
```
za pomocą dodanej metody:  
```python
class check():    
    def updateQuality(item, by):
        item.quality = item.quality + by;
        return item
```