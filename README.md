Advanced Programming Languages

Projects:  
1 - Gilded Rose - only add to code:  
	Adding new functionality to badly coded eshop 
   
2 -  
Krok 1:  
  
Wyciągnięcie linii zmieniającej wartość **quality** przedmiotu w sklepie:  
zamiana linii:  
```python
       	item.quality = item.quality - 1
        item.quality = item.quality + 1
	item.quality = item.quality - 3
	item.quality = item.quality - item.quality
```
na  
```python
	check.updateQuality(item, -1)  
	check.updateQuality(item, 1)
	check.updateQuality(item, -3)  
	check.updateQuality(item, -item.quality)
```
za pomocą dodanej metody:  
```python
class check():    
    def updateQuality(item, by):
        item.quality = item.quality + by;
        return item
```
oraz dodanie testu - **test_items_qulity_decreases_as_name_suggest** sprawdzającego czy wartość **quality** jest w odpowiedni sposób zmieniana w czasie:  
