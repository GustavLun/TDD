# # # 2.
# def sum_list(list):
#     total = 0
#     for i in list:
#         total+= i
#     return total
#
#
# def test_empty_list():
#     expected = 0
#     actual = sum_list([])
#     assert actual == expected
#
#
# def test_number_list():
#     assert sum_list([5]) == 5
#     assert sum_list([5, 5]) == 10
#     assert sum_list([1, 2, 2, 1, 2, 2]) == 10
#     # testet failade alltid när return = None
#     # Vi måste därmed definera en loop funktion som går igenom list steg för steg och plussar på värdet i varje i

    #. 3A & 3B
    # Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)
    # just nu finns inget i funktionen som faktiskt identifierar vokaler.
# def count_vowels(word):
#     total = 0
#     for vowel in word:
#         if vowel in "AEIOUYÅÄÖaeiouyåäö":
#             total += 1
#     return total
#
# def detect_vowels(word):
#     expected = 0
#     for vowel in "AEIOUYÅÄÖaeiouyåäö":
#         if vowel == "AEIOUYÅÄÖaeiouyåäö":
#             expected += 1
#     actual = count_vowels(word)
#     assert actual == expected # Denna verkar inte funka alls, tester kommer ut som pass men ah jag vet inte.
#
# def test_no_vowels():
#     assert count_vowels("qwrt") == 0
#     assert count_vowels("Tt") == 0
#     assert count_vowels("123 123") == 0
#     assert count_vowels("") == 0

def max_number(lista):
    max = 0
    if len(lista) == 0:
        return None
    for i in lista:
        if i > max:
            max = i
    return max

def find_max_number(lista):
    max = 0
    for i in max_number([]):
        if i > max:
            max = i

def test_max_number():
    assert max_number([])
    assert max_number([1,2,3])