#1.
#1a. x<100: har bara 2 över och under

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
def sum_list(list):
    return None

def test_empty_list():
    expected = 0
    actual   = sum_list([])
    assert actual == expected

def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([5,5]) == 10
    assert sum_list([1,2,2,1,2,2]) == 10


