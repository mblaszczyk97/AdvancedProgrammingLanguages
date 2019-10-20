Advanced Programming Languages

Projects:  
1 - Gilded Rose - only add to code:  
	Adding new functionality to badly coded eshop 
   
**Krok 1:**  
  
Wyciągnięcie linii zmieniającej wartość **quality** przedmiotu w sklepie:  
zamiana liniach:  
```python
       	item.quality = item.quality - 1
        item.quality = item.quality + 1
	item.quality = item.quality - 3
	item.quality = item.quality - item.quality
  
	item.sell_in = item.sell_in - 1
```
na  
```python
	check.updateQuality(item, -1)  
	check.updateQuality(item, 1)
	check.updateQuality(item, -3)  
	check.updateQuality(item, -item.quality)
  
	check.updateSellin(item, -1)
```
za pomocą dodanych metod:  
```python
class check():    
	def updateQuality(item, by):
        	item.quality = item.quality + by;
        	return item

	def updateSellin(item, by):
        	item.sell_in = item.sell_in + by;
        	return item
```
oraz dodanie testu - **test_items_quality_decreases_as_name_suggest** sprawdzającego czy wartość **quality** jest w odpowiedni sposób zmieniana w czasie  

**Krok 2:**  
  
Stworzenie metod **boolowskich** sprawdzających warunki w "if-ach":  
zmiana w liniach:  
```python
       	if item.name == "Sulfuras, Hand of Ragnaros":
	if item.name == "Aged Brie":
	if item.name == "Backstage passes to a TAFKAL80ETC concert":
```
na  
```python
	check.is_sulfuras(item) 
	check.is_aged_brie(item)
	check.is_backstage(item)
```
za pomocą dodanych metod:  
```python
class check():    
	def is_sulfuras(item):
        	if item.name == "Sulfuras, Hand of Ragnaros":
           		return True
        	return False

	def is_aged_brie(item):
        	if item.name == "Aged Brie":
               		return True
        	return False

	def is_backstage(item):
        	if item.name == "Backstage passes to a TAFKAL80ETC concert":
           		return True
```
oraz dodanie testu - **test_items_sellin_decreases_as_name_suggest** sprawdzającego czy wartość **sell_in** jest w odpowiedni sposób zmieniana w czasie  

**Krok 3:**  
  
Stworzenie metod które będą sprawdzać o ile zwiększać **quality** przedmiotu o nazwie **concert**:  
zmiana w liniach:  
```python
       	if item.name == "Backstage passes to a TAFKAL80ETC concert":
        	if item.sell_in < 11:
        		if item.quality < 50:
                                item.quality = item.quality + 1
        	if item.sell_in < 6:
                	if item.quality < 50:
                                item.quality = item.quality + 1
```
na  
```python
	check.add_backstage(item)
```
za pomocą dodanych metod:  
```python
class check():    
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
            if check.is_backstage_sellin_less_11(item):
                item.quality = item.quality + 1
            if check.is_backstage_sellin_less_6(item):
                item.quality = item.quality + 1
```
oraz dodanie testu - **test_add_backstage** sprawdzającego czy wartość zmiany w "concercie"  
**Krok 4:**  
  
Sprawdzanie czy przedmiot jest "normalny":  
zmiana w liniach:  
```python
	if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name.lower().find("conjured") == -1:
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
```
na  
```python
	if check.is_normal(item):
```
za pomocą dodanej metody:  
```python
class check():    
    def is_normal(item):
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name.lower().find("conjured") == -1:
                if item.quality > 0:
                    if not check.is_sulfuras(item):
                        return True
                    return False
```
oraz dodanie testu - **test_add_normal** sprawdzającego czy wartość zmiany w "normalnym" przedmiocie  
**Krok 5:**  
  
Zmiana warunku, który obsługuje przedmioty, które nie są "normalne":  
zmiana w liniach:  
```python
	else:
                if item.quality < 50:
                    check.updateQuality(item, 1)
                    if item.quality > 2 and item.name.lower().find("conjured") != -1:
                            check.updateQuality(item, -3)
                    check.add_backstage(item)
```
na  
```python
	if not check.is_normal(item) and item.quality < 50:
                    check.updateQuality(item, 1)
                    check.sub_conjured(item, -3, 2)
                    check.add_backstage(item)
```
za pomocą dodanej metody:  
```python
class check():    
	def sub_conjured(item, subber, quality):
        	if item.quality > quality and item.name.lower().find("conjured") != -1:
            		check.updateQuality(item, subber)
```
oraz dodanie testu - **test_add_not_normal** sprawdzającego czy wartość zmiany w "nienormalnym" przedmiocie  

**Krok 6:**  
  
Zmiana spsobu odejmowania wartości **sell_in** tak aby była ona odejmowana dla wszystkich po obrocie pętli oraz  
zamienienie podwojenia zmian wartości **quality* gdy *sell_in* jest mniejsza od 0 tak aby działo to się od razu w 
metodzie **updateQuality(item, by)**. W tym celu usuwam wszystkie warunki po **if item.sell_in < 0:** oraz
dla przedmiotu, który jest "conjured" muszę dodać warunek sprawdzający jak zmniejszać jego quality czyli -
**if item.name.lower().find("conjured") == -1 or item.name.lower().find("conjured") != -1 and item.quality > 0:**  
zmiana w liniach:  
```python
    def update_quality(self):
        for item in self.items:
            if check.is_normal(item):
                check.updateQuality(item, -1)
            if not check.is_normal(item) and item.quality < 50:
                    check.updateQuality(item, 1)
                    check.sub_conjured(item, -3, 2)
                    check.add_backstage(item)
            if not check.is_sulfuras(item):
                check.updateSellin(item, -1)
            if item.sell_in < 0:
                if not check.is_aged_brie(item):
                    if not check.is_backstage(item):
                        if item.name.lower().find("conjured") != -1 and item.quality > 1:
                                check.updateQuality(item, -1)
                        if item.quality > 0:
                            if not check.is_sulfuras(item):
                                check.updateQuality(item, -1)
                    else:
                        check.updateQuality(item, -item.quality)
                else:
                    if item.quality < 50:
                        check.updateQuality(item, 1)
```
na  
```python
    def update_quality(self):
        for item in self.items:
            if check.is_normal(item):
                check.updateQuality(item, -1)
            if not check.is_normal(item) and item.quality < 50:
                if item.name.lower().find("conjured") == -1 or item.name.lower().find("conjured") != -1 and item.quality > 0:
                    check.updateQuality(item, 1)
                check.sub_conjured(item, -3, 2)
                check.add_backstage(item)
            if not check.is_sulfuras(item):
                check.updateSellin(item, -1)

class check():    
    def updateQuality(item, by):
        if item.sell_in >0:
            item.quality = item.quality + by;
        else:
            item.quality = item.quality + 2*by;
        if item.quality <= 0:
            item.quality=0
        return item
```
oraz dodanie testu - **test_quality_check_conjured** sprawdzającego czy wartość przedmiotu "conjured" jest odpowiednio zmniejszana po  
osiągnięciu stanu **sell_in** mniejszego od 0

