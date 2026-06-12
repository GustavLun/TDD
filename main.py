#1.
#1a. x<100: har bara 2 över och under
from os import remove
from unittest import result


#1b. y == 42: har 2, antingen är y exakt 42 eller inte.

#1c len(text) >= 5:  3 gånger, den kollar om texten är 5 eller högre, är den lägre skippas den.

#1d z == true: Denna har nog 2, den sätter bara att z är lika med true om de inte är z så är den False.

#1e 8 < v < 16: 4 tror jag, är 8 lägre eller högre än v, är v lägre eller högre än 16.
# Detta var fel så jag tänkte fel, man få inte räkna dem separat.
# 8 ska vara lägre än v och v ska var lägre än 16 så om v är högre än 8 failar de, är v högre än 16 failar de och andra möjligeten är att de funkar.
# Rätt svar 3

#1f  w == 32 or w == 64 or w == 128 # Här tror jag det är 4, de kollar 3 godkända och den misslyckade är om ingen uppfyller.
# igen fel, så alla tre godkända räknas som en, och en fail är om ingen är uppfylld.

#1g if x < 5: … elif x < 10: … elif x < 15: … else …
#min tanke är totalt 4, om den är mindre än 5 så körs först, mindre än 10 den andra, mindre än 15 den tredje och 15 eller större körs fjärde
# Rätt

#2 # Returnerar summan av alla tal i listan

# # # 2.
def sum_list(list): # Funktion som plussar varje element i listan, för varje i (element) blir det totalen som sedan plussas med nästa i (element
    total = 0
    for i in list:
        total+= i
    return total

   #-----------------------------------------------------------------------------------------------------------#

# 3A & 3B
def count_vowels(word):
    total = 0
    for vowel in word:
        if vowel in "AEIOUYÅÄÖaeiouyåäö":
            total += 1
    return total
#Total är noll, för varje vowel i listan list, om vovel är någon av små eller stora vokaler plussas totalen med 1.

    #-----------------------------------------------------------------------------------------------------------#

def max_number(lista):
    if len(lista) == 0:
        return None
    biggest = max(lista)
    return biggest
# för kollar funktionen om listan är tom ==0 då returnar None, annars blir variablen biggest största värdet i listan vilket representerar max(lista) gör.
   #-----------------------------------------------------------------------------------------------------------#
#5
def find_2nd_max(list):
    lista = list
    if len(lista) > 1:
        lista.sort()
        andra_plats = lista[-2]
        return andra_plats
    elif len(list) <=1 :
        return None
    # först kollar vi om listan innehåller mer än 0 element, om de gör de så tillverkas en variabel lista som är list.
    # Efter detta sorterar vi listan från minst till störst
    # sen tar vi en variabel andra_plats som då skall vara andra elementet från höger alltså -2 vilket är de nästa största talet i en sorterad lista.
    #Finns inget tall returnas None

#-----------------------------------------------------------------------------------------------------------------------------------------------------#

# 2. Öva på TDD

#1A
def c_to_f(degree):

    if degree < -273.15:
        return None
    else:
        return (round(degree * 9 / 5 + 32 , 2))



#-----------------------------------------------------------------------------------------------------------------------------------------------------#

#2.A

def count_words(sentence):
    words = sentence.split() #
    if len(words) == 0:
        return None
    else:
        return len(words)



#-----------------------------------------------------------------------------------------------------------------------------------------------------#
# 3.A
def find_median(numbers):
    numbers.sort()
    if len(numbers) <1:
        return None
    elif len(numbers) > 0 and len(numbers) % 2 == 0:
        mid1 = numbers[len(numbers)//2 - 1]
        mid2 = numbers[len(numbers)//2]
        median = (mid1 + mid2) / 2
        return median
    else:
        median = numbers[len(numbers)//2]
        return median

#-----------------------------------------------------------------------------------------------------------------------------------------------------#
# 4

def is_sorted_ascending(numbers):

    if len(numbers) < 1:
        return None
    for num in range(len(numbers)-1):
       if numbers[num] > numbers[num+1]:
        return False

    else:
        return True

master_list=("Xbox", "Ps5", "Nintendo", "PC", "Sega")
x = input("Please enter a sentence: ")

# Söka efter användare
def autocomplete_list(input, master_list):
    result=[]
    for game in master_list:
        if game.startswith(input.upper()):
            result.append(game)
            return result
    print(x)

print(autocomplete_list(x, master_list))