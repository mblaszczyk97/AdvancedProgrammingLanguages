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
       	if item.name != "Sulfuras, Hand of Ragnaros":
	if item.name != "Aged Brie":
```
na  
```python
	check.is_sulfuras(item) 
	check.is_aged_brie(item)
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
```
oraz dodanie testu - **test_items_sellin_decreases_as_name_suggest** sprawdzającego czy wartość **sell_in** jest w odpowiedni sposób zmieniana w czasie  