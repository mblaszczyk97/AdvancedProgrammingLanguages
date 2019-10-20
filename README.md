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
	if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name.lower().find("conjured") == -1:#1
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
        if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name.lower().find("conjured") == -1:#1
                if item.quality > 0:
                    if not check.is_sulfuras(item):
                        return True
                    return False
```
oraz dodanie testu - **test_add_normal** sprawdzającego czy wartość zmiany w "normalnym" przedmiocie  