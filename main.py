# Project Python 

from pyscript import display, document

def show_nickname(e):
    nickname = document.getElementById("country_name").value
    document.getElementById("result").innerHTML = f"Nickname: {nickname}"

def add2_list (e): 
    document.getElementById('result').innerHTML = ' '

    # Sets 
    given_name = document.getElementById('first_name').value.title().strip()
    surname = document.getElementById('last_name').value.title().strip()
    new_member = {given_name + " " + surname} 

    grade_seven_members = {'Maria Julia Cortes', 'Alekos Canares', 'Shiloh Jolie'}
    grade_eight_members = {'Charles Villar', 'Victoria Pascual', 'Henry Tolentino'}
    grade_nine_members = {'Sheldon Cooper', 'Missy Cooper', 'George Cooper'}
    grade_ten_members = {'Aisha Padua', 'Tori Vega', 'Ray Ben'}

    # Union 
    all_members = grade_seven_members | grade_eight_members |  grade_nine_members |grade_ten_members | new_member 

    # Display
    display(f'The people in Math Club are {all_members}.', target='result')
    display(f'The total number of people in Math Club is {len(all_members)}.', target='result')

non_metals = {
    "H": "Symbol: H, Element: Hydrogen, Atomic Number: 1, Molar Mass: 1.008 g/mol", 
    "He": "Symbol: He, Element: Helium, Atomic Number: 2, Molar Mass: 4.0026 g/mol", 
    "C": "Symbol: C,Element: Carbon, Atomic Number: 6, Molar Mass: 12.011 g/mol", 
    "N": "Symbol: N, Element: Nitrogen, Atomic Number: 7, Molar Mass: 14.007 g/mol", 
    "O": "Symbol: O, Element: Oxygen, Atomic Number: 8, Molar Mass: 15.999 g/mol", 
    "F": "Symbol: F, Element: Fluorine, Atomic Number: 9, Molar Mass: 18.998 g/mol", 
    "Ne": "Symbol: Ne, Element: Neon, Atomic Number: 10, Molar Mass: 20.180 g/mol", 
    "P": "Symbol: P, Element: Phosphorus, Atomic Number: 15, Molar Mass: 30.974 g/mol", 
    "S": "Symbol: S, Element: Sulfur, Atomic Number: 16, Molar Mass: 32.06 g/mol", 
    "Cl": "Symbol: Cl, Element: Chlorine, Atomic Number: 17, Molar Mass: 35.45 g/mol", 
    "Ar": "Symbol: Ar, Element: Argon, Atomic Number: 18, Molar Mass: 39.948 g/mol", 
    "Se": "Symbol: Se, Element: Selenium, Atomic Number: 34, Molar Mass: 78.971 g/mol", 
    "Br": "Symbol: Br, Element: Bromine, Atomic Number: 35, Molar Mass: 79.904 g/mol",
    "Kr": "Symbol: Kr, Element: Krypton, Atomic Number: 36, Molar Mass: 83.798 g/mol", 
    "I": "Symbol: I, Element: Iodine, Atomic Number: 53, Molar Mass: 126.90 g/mol", 
    "Xe": "Symbol: Xe, Element: Xenon, Atomic Number: 54, Molar Mass: 131.29 g/mol",
    "Rn": "Symbol: Rn, Element: Radon, Atomic Number: 86, Molar Mass: (222) g/mol"
}

def check_element(e):
    document.getElementById('result').innerHTML = ''
    symbol = document.getElementById('element').value.title().strip()
                     
    info = non_metals.get(symbol, f'Sorry, symbol {symbol} was not found in the list.') 
    display(info, target='result', append=False)
