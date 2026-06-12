# # # 2.
from main import *


def test_empty_list():
    expected = 0
    actual = sum_list([])
    assert actual == expected
# Vår expectetion i är summan på listan skall vara 0, actual är vår current lista "sum_list" sen assertar vi actual list som expected värde.

def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([5, 5]) == 10
    assert sum_list([1, 2, 2, 1, 2, 2]) == 10
   # Test cases som just nu testar att elementen plussas ihop och blir adderade.





def test_no_vowels():
    assert count_vowels("qwrt") == 0
    assert count_vowels("Tt") == 0
    assert count_vowels("123 123") == 0
    assert count_vowels("") == 0
# Testen just nu är fokuserar på att ej innehålla några vokaler


def test_max_number():
    assert max_number([]) == None
    assert max_number([1,2,9,3]) == 9
    # Test som kollar att vi får ut none om listan är tom och att vi får det största värde ur en osorterad lista.

def test_find_2nd_max():
    assert find_2nd_max([2,9,8,9,3,10,6]) == 9
    assert find_2nd_max([]) == None
    assert find_2nd_max([1]) == None
    #i detta test testar värdet som är näst störst i en lista kommer ut som = värdet
    # Vi testar även om listan endast innehåller ett element eller inget element då returnar None.

def test_c_to_f():
    assert c_to_f(50) == 122
    assert c_to_f(-1) == 30.2
    assert c_to_f(90) == 194
    assert c_to_f(-273) == -459.4
    assert c_to_f(-273.15) == -459.67
    assert c_to_f(-273.16) == None
# I dessa testfall testar vi olika grader, vi testar även det exakta värdet som tillåts. Vi testar även de om värdet går lägre än de tillåtna.
# Det finns totalt 2 ekvivalens klasser.

def test_Count_Words():
    assert count_words("Hello Worlds") == 2
    assert count_words("hello world, im gustav") == 4
    assert count_words("hello world , im gustav") == 5
    assert count_words("hell") == 1
    assert count_words("") == None

def test_find_median():
    assert find_median([10,2,9,3,7]) == 7
    assert find_median([]) == None
    assert find_median([1]) == 1
    assert find_median([1,2]) == 1.5
    assert find_median([8,2,7,3]) == 5

def test_is_sorted_ascending():
    assert is_sorted_ascending([1,2,3,4,5]) == True
    assert is_sorted_ascending([1,2,3,5,4]) == False
    assert is_sorted_ascending([]) == None

