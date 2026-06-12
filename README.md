# 2A Count_Words

## Krav
Systemet ska kunna ta emot en textsträng och räkna antalet ord i strängen. Ord definieras som en serie tecken separerade av ett eller flera mellanslag. Om inga ord matas in ska systemet returnera `None`.

---

## Acceptanskriterier (AK)

### AK1
Om användaren skriver in ett ord ska funktionen returnera 1.  
- Input: `"Hej"`  
- Resultat: `1`

---

### AK2
Om användaren skriver in flera ord ska funktionen returnera rätt antal ord.  
- Input: `"Hej svejs Arne"`  
- Resultat: `3`

---

### AK3
Om användaren inte skriver in några ord ska funktionen returnera `None`.  
- Input: `""`  
- Resultat: `None`

---

# 3A Find_Median(numbers)

## Krav:
Systemet skall kunna ta nummer från en lista jämn som ojämn och därefter returnera medianen. Om listan är tom skall systemet returnera `None`

### AK1:
Om användaren skriver in ett jämnt antal nummer i en lista ska funktionen först sortera listan för att sedan ta de två talen, addera dem och dela dem på två, resultatet skall returneras.
- input `[4,6,1,9,6,2]`
- Resultat `5`

### AK2:
Om användaren skriver in ett ojämnt antal nummber i en listan ska funktion sortera listan och returnera de mellersta siffran 
- input `[4,6,1,9,6]`
- Resultat `6`

### AK3:
Om användaren väljer att inte skriva in något tal alls i listan skall funktionen returnera `None`
- input `[]`
- Resultat `None

---

# 4 A B & C

### A Består av 2 ekvivalnensklasser, den kan bli true eller False. 
### B
## Krav:
Systemet skall kunna identifiera om en lista är sorterad i såpass att den stiger i värde och därav returnera True. Om listan ej stiger i värde skall den returnera False. Skulle listan vara tom så returneras ``None``

### AK1
Om använder väljer att skriva in tal så att varje tal stiger efter varandra returneras `True`
- Input: `[1,2,3,4,5,]`
- Resultat: `"True"`

### AK2
Om använder väljer att skriva in tal i en lista så att de inte stiger efter varandra returneras `False`
- Input: ``[1,3,2,5]``
- Resultat: `"False"`

### AK3 
om användaren väljer att inte skriva in något värde i listan så returneras ``None``
- input: ``[]``
- Resultat ``"None"``

# Söka efter användare
