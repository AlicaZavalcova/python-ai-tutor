import ast
import streamlit as st

st.set_page_config(page_title="Python Tutor", page_icon="🐍", layout="wide")

TOPICS = [
    "Your First Python Program",
    "Main Concepts",
    "Numbers",
    "Strings",
    "Boolean",
    "Lists",
    "Conditional Statements",
    "Loops",
    "Functions",
    "Summary",
    "Introduction",
    "Code Style",
    "Working With Numbers",
    "Working With Strings",
    "Lists In Details",
    "Dict Basics",
    "Type Conversion",
    "Loops In Details",
    "Functions Revisited",
    "Summary",
    "How to Solve GitHub Tasks",
    "Mutable Immutable Types",
    "List and Dict Comprehensions",
    "Functions in Details",
    "Decorators",
    "Classes",
    "Classes in Details",
    "Iterators and Generators",
    "Modules and Imports",
    "OOP: Single Inheritance",
    "OOP: Multiple Inheritance",
    "OOP: Encapsulation, Polymorphism, Abstraction",
    "Properties and Descriptors",
    "Exception Handling",
    "Exceptions in Details",
    "File Handling",
    "Memory Management",
    "Testing",
    "Testing in Details",
    "Basic Modules Overview",
    "Dict Advanced",
    "Extra",
    "Python Practice"
]

LESSONS = {
    "Your First Python Program": (
        "Python program je postupnosť príkazov, ktoré počítač vykoná. "
        "Na vypísanie textu na obrazovku používame funkciu print().",
        'print("Hello, world!")',
        "Napíš program, ktorý vypíše tvoje meno a vetu I am learning Python."
    ),
    "Numbers": (
        "Python pracuje s celými číslami (int) aj desatinnými číslami (float). "
        "Čísla môžeš sčítavať, odčítavať, násobiť a deliť.",
        "a = 12\nb = 5\nprint(a + b)\nprint(a / b)",
        "Vytvor dve číselné premenné a vypíš ich súčet, rozdiel a súčin."
    ),
    "Strings": (
        "String je textový reťazec. V Pythone ho zapisujeme do úvodzoviek. "
        "Texty môžeme spájať a zisťovať ich dĺžku pomocou len().",
        'name = "Anna"\nprint("Hello " + name)\nprint(len(name))',
        "Ulož svoje meno do premennej a vypíš jeho dĺžku."
    ),
    "Boolean": (
        "Typ bool má iba dve hodnoty: True a False. Používa sa pri "
        "rozhodovaní a porovnávaní hodnôt.",
        "age = 15\nprint(age >= 18)",
        "Vytvor dve čísla a vypíš, či je prvé väčšie ako druhé."
    ),
    "Lists": (
        "List (zoznam) uchováva viac hodnôt v jednom poradí. "
        "Prvky vyberáme pomocou indexov, pričom prvý index je 0.",
        'colors = ["red", "green", "blue"]\nprint(colors[0])\ncolors.append("yellow")',
        "Vytvor zoznam troch obľúbených jedál a vypíš druhé jedlo."
    ),
    "Conditional Statements": (
        "Podmienky if, elif a else umožňujú vykonať rôzne príkazy "
        "podľa toho, či je podmienka pravdivá.",
        "temperature = 25\nif temperature > 20:\n    print('It is warm')\nelse:\n    print('It is cold')",
        "Napíš podmienku, ktorá zistí, či je číslo kladné, záporné alebo nula."
    ),
    "Loops": (
        "Cyklus opakuje skupinu príkazov. for sa často používa na "
        "prechádzanie prvkov a while opakuje príkazy, kým platí podmienka.",
        "for number in range(1, 4):\n    print(number)",
        "Pomocou cyklu vypíš čísla od 1 do 10."
    ),
    "Functions": (
        "Funkcia je pomenovaný blok kódu, ktorý môžeme opakovane použiť. "
        "Definujeme ju pomocou def a výsledok môže vrátiť príkazom return.",
        "def greet(name):\n    return 'Hello ' + name\n\nprint(greet('Eva'))",
        "Vytvor funkciu square(number), ktorá vráti druhú mocninu čísla."
    ),
    "Dict Basics": (
        "Dictionary (slovník) ukladá dvojice key-value. Ku každej hodnote "
        "pristupujeme cez jej kľúč.",
        'student = {"name": "Peter", "age": 14}\nprint(student["name"])',
        "Vytvor slovník s kľúčmi name, age a city. Potom vypíš hodnotu age."
    ),
    "Type Conversion": (
        "Type conversion znamená zmenu dátového typu. Napríklad int() "
        "mení hodnotu na celé číslo a str() na text.",
        'age_text = "15"\nage = int(age_text)\nprint(age + 1)',
        'Premeň text "123" na celé číslo a pripočítaj k nemu 7.'
    ),
    "Exception Handling": (
        "Výnimky (exceptions) sú chyby, ktoré vzniknú počas behu programu. "
        "Blok try/except umožňuje chybu zachytiť a vhodne na ňu reagovať.",
        "try:\n    number = int(input('Enter a number: '))\n    print(number * 2)\nexcept ValueError:\n    print('Please enter a whole number.')",
        "Použi try/except pri prevode textu na číslo."
    ),
    "Classes": (
        "Class je predloha na vytváranie objektov. Objekt má údaje (attributes) "
        "a správanie (methods). Metóda __init__ nastavuje počiatočné údaje.",
        "class Dog:\n    def __init__(self, name):\n        self.name = name\n\nmy_dog = Dog('Benny')\nprint(my_dog.name)",
        "Vytvor triedu Book s atribútom title a vytvor jednu jej inštanciu."
    ),
    "Modules and Imports": (
        "Module je súbor s Python kódom, ktorý môžeme použiť v inom programe. "
        "Príkaz import sprístupní jeho funkcie a objekty.",
        "import math\nprint(math.sqrt(25))",
        "Importuj modul random a pomocou neho vypíš náhodné celé číslo od 1 do 6."
    ),
    "Testing": (
        "Testovanie overuje, či program funguje podľa očakávania. "
        "Pri jednoduchých testoch môžeme použiť assert.",
        "def add(a, b):\n    return a + b\n\nassert add(2, 3) == 5",
        "Napíš funkciu is_even(number) a otestuj ju pomocou assert."
    )
}

# Each task has an independently defined output/structure check.
# The first lessons have carefully specified checks. Later chapters use
# structured practice tasks; they are clearly labeled as limited checks.
TASKS = {
 "Your First Python Program": [
  {"title":"Print a message", "prompt":"Vypíš presne text Hello, Python!", "example":'print("Hello, world!")', "hint":"Použi print(), text vlož do úvodzoviek a nezabudni na zátvorky.", "expected":"Hello, Python!\n", "mode":"output"},
  {"title":"Two lines", "prompt":"Vypíš na dva samostatné riadky texty Hello a I am learning Python.", "example":'print("Hello")\nprint("Python")', "hint":"Dva príkazy print() na dvoch riadkoch.", "expected":"Hello\nI am learning Python.\n", "mode":"output"},
  {"title":"Variable and output", "prompt":"Vytvor premennú name s textom Anna a vypíš jej hodnotu pomocou print(name).", "example":'name = "Eva"\nprint(name)', "hint":"Použi name = \"Anna\" a potom print(name).", "expected":"Anna\n", "mode":"output", "required":["assign_name", "print_name"]},
  {'title': 'Exclamation', 'prompt': 'Vypíš text I can code!', 'example': 'print("I can learn!")', 'hint': 'Pozor na výkričník.', 'expected': 'I can code!\n', 'mode': 'output'},
  {'title': 'Number', 'prompt': 'Vypíš číslo 2026 bez úvodzoviek.', 'example': 'print(42)', 'hint': 'Číslo patrí do print() bez úvodzoviek.', 'expected': '2026\n', 'mode': 'output'},
  {'title': 'Three lines', 'prompt': 'Vypíš na tri riadky A, B a C.', 'example': 'print("X")\nprint("Y")', 'hint': 'Každý print() začína nový riadok.', 'expected': 'A\nB\nC\n', 'mode': 'output'},
  {'title': 'Greeting', 'prompt': 'Vytvor premennú name s hodnotou Eva a vypíš Hello Eva pomocou dvoch argumentov print().', 'example': 'name = "Tom"\nprint("Hi", name)', 'hint': 'Použi print("Hello", name).', 'expected': 'Hello Eva\n', 'mode': 'output', 'required': ['assign_name', 'print_name']},
  {'title': 'My first calculation', 'prompt': 'Vypíš výsledok 2 + 3 pomocou operátora +.', 'example': 'print(1 + 1)', 'hint': 'Použi print(2 + 3).', 'expected': '5\n', 'mode': 'output', 'required': ['addition']},
 ],
 "Main Concepts": [
  {"title":"Variable", "prompt":"Vytvor premennú age s hodnotou 12 a vypíš ju.", "example":"age = 10\nprint(age)", "hint":"Číslo 12 nepíš do úvodzoviek; použij age = 12.", "expected":"12\n", "mode":"output", "required":["assign_age"]},
  {"title":"Addition", "prompt":"Vypíš výsledok 8 + 5 pomocou operátora +.", "example":"print(2 + 3)", "hint":"Vnútri print() použi 8 + 5.", "expected":"13\n", "mode":"output", "required":["addition"]},
  {"title":"Comment", "prompt":"Napíš komentár začínajúci # a príkaz, ktorý vypíše Python.", "example":"# A comment\nprint('Hello')", "hint":"Komentár začína znakom #.", "expected":"Python\n", "mode":"output", "required":["comment"]},
  {'title': 'Text variable', 'prompt': 'Ulož do premennej name text Lea a vypíš ho.', 'example': 'name = "Eva"\nprint(name)', 'hint': 'Text musí byť v úvodzovkách.', 'expected': 'Lea\n', 'mode': 'output', 'required': ['assign_name', 'print_name']},
  {'title': 'Two values', 'prompt': 'Vytvor x = 4 a y = 6, vypíš ich súčet.', 'example': 'x = 2\ny = 3\nprint(x + y)', 'hint': 'Použi + medzi premennými.', 'expected': '10\n', 'mode': 'output', 'required': ['addition']},
  {'title': 'Change variable', 'prompt': 'Nastav x = 3, potom x = 9 a vypíš x.', 'example': 'x = 1\nx = 2\nprint(x)', 'hint': 'Druhé priradenie prepíše prvé.', 'expected': '9\n', 'mode': 'output'},
  {'title': 'Math in print', 'prompt': 'Vypíš 20 - 8.', 'example': 'print(9 - 2)', 'hint': 'Použi znak mínus.', 'expected': '12\n', 'mode': 'output'},
  {'title': 'Comment and value', 'prompt': 'Napíš komentár a vypíš číslo 7.', 'example': ' # môj komentár\nprint(3)', 'hint': 'Komentár začína #.', 'expected': '7\n', 'mode': 'output', 'required': ['comment']},
 ],
 "Numbers": [
  {"title":"Sum", "prompt":"Vypíš súčet čísel 7 a 4 pomocou +.", "example":"print(2 + 3)", "hint":"Napíš print(7 + 4).", "expected":"11\n", "mode":"output", "required":["addition"]},
  {"title":"Multiplication", "prompt":"Vypíš súčin 6 a 3 pomocou *.", "example":"print(2 * 4)", "hint":"Násobenie zapisujeme hviezdičkou *.", "expected":"18\n", "mode":"output", "required":["multiplication"]},
  {"title":"Division", "prompt":"Vypíš výsledok 10 / 2 pomocou /.", "example":"print(8 / 2)", "hint":"Delenie používa /, nie dvojbodku.", "expected":"5.0\n", "mode":"output", "required":["division"]},
  {'title': 'Subtract', 'prompt': 'Vypíš výsledok 15 - 7.', 'example': 'print(9 - 2)', 'hint': 'Odčítanie zapisujeme -.', 'expected': '8\n', 'mode': 'output'},
  {'title': 'Negative number', 'prompt': 'Vypíš záporné číslo -5.', 'example': 'print(-2)', 'hint': 'Mínus je pred číslom.', 'expected': '-5\n', 'mode': 'output'},
  {'title': 'Float', 'prompt': 'Vypíš desatinné číslo 2.5.', 'example': 'print(1.5)', 'hint': 'Použi bodku, nie čiarku.', 'expected': '2.5\n', 'mode': 'output'},
  {'title': 'Variables and sum', 'prompt': 'Vytvor a = 9 a b = 6, vypíš a + b.', 'example': 'a = 2\nb = 4\nprint(a+b)', 'hint': 'Premenné môžeš sčítať.', 'expected': '15\n', 'mode': 'output', 'required': ['addition']},
  {'title': 'Multiply variables', 'prompt': 'Vytvor a = 4 a b = 5, vypíš ich súčin.', 'example': 'a = 2\nb = 3\nprint(a*b)', 'hint': 'Použi *.', 'expected': '20\n', 'mode': 'output', 'required': ['multiplication']},
 ],
 "Strings": [
  {"title":"Text", "prompt":"Vypíš presne Hello, Anna!", "example":'print("Hello!")', "hint":"Text musí byť v úvodzovkách.", "expected":"Hello, Anna!\n", "mode":"output"},
  {"title":"Join strings", "prompt":"Spoj dva texty 'Py' a 'thon' pomocou + a vypíš Python.", "example":'print("Hi" + "!")', "hint":"Použi + medzi dvoma reťazcami.", "expected":"Python\n", "mode":"output", "required":["string_add"]},
  {"title":"Length", "prompt":"Vypíš dĺžku textu Python pomocou len().", "example":'print(len("cat"))', "hint":"len() spočíta znaky textu.", "expected":"6\n", "mode":"output", "required":["len"]},
  {'title': 'Your name', 'prompt': 'Vypíš text My name is Eva.', 'example': 'print("My name is Tom.")', 'hint': 'Skontroluj medzery a bodku.', 'expected': 'My name is Eva.\n', 'mode': 'output'},
  {'title': 'Text variable', 'prompt': 'Ulož name = "Mia" a vypíš Mia.', 'example': 'name = "Eva"\nprint(name)', 'hint': 'Použi premennú name.', 'expected': 'Mia\n', 'mode': 'output', 'required': ['assign_name', 'print_name']},
  {'title': 'Join greeting', 'prompt': 'Spoj "Good " a "morning" pomocou + a vypíš Good morning.', 'example': 'print("Hi " + "Eva")', 'hint': 'Medzera je na konci prvého textu.', 'expected': 'Good morning\n', 'mode': 'output', 'required': ['string_add']},
  {'title': 'Length of word', 'prompt': 'Vypíš dĺžku slova school pomocou len().', 'example': 'print(len("dog"))', 'hint': 'Slovo school má šesť písmen.', 'expected': '6\n', 'mode': 'output', 'required': ['len']},
  {'title': 'Two texts', 'prompt': 'Vypíš na samostatné riadky cat a dog.', 'example': 'print("sun")\nprint("moon")', 'hint': 'Použi dva print().', 'expected': 'cat\ndog\n', 'mode': 'output'},
 ],
 "Boolean": [
  {"title":"Compare", "prompt":"Vypíš výsledok porovnania 8 > 3.", "example":"print(5 > 2)", "hint":"Použi znak >.", "expected":"True\n", "mode":"output", "required":["compare"]},
  {"title":"Equality", "prompt":"Vypíš výsledok porovnania 5 == 5.", "example":"print(2 == 2)", "hint":"== porovnáva, = priraďuje.", "expected":"True\n", "mode":"output", "required":["equality"]},
  {"title":"False", "prompt":"Vypíš výsledok porovnania 3 > 9.", "example":"print(1 > 5)", "hint":"Výsledok bude False.", "expected":"False\n", "mode":"output", "required":["compare"]},
  {'title': 'Less than', 'prompt': 'Vypíš výsledok 2 < 5.', 'example': 'print(1 < 3)', 'hint': 'Znak < znamená menšie ako.', 'expected': 'True\n', 'mode': 'output', 'required': ['compare']},
  {'title': 'Not equal', 'prompt': 'Vypíš výsledok porovnania 3 != 4.', 'example': 'print(1 != 2)', 'hint': '!= znamená nerovná sa.', 'expected': 'True\n', 'mode': 'output', 'required': ['compare']},
  {'title': 'Equal false', 'prompt': 'Vypíš výsledok 2 == 3.', 'example': 'print(1 == 2)', 'hint': 'Výsledok je False.', 'expected': 'False\n', 'mode': 'output', 'required': ['equality']},
  {'title': 'Greater or equal', 'prompt': 'Vypíš výsledok 5 >= 5.', 'example': 'print(3 >= 2)', 'hint': '>= znamená väčšie alebo rovné.', 'expected': 'True\n', 'mode': 'output', 'required': ['compare']},
  {'title': 'Compare variables', 'prompt': 'Nastav x = 8, y = 10 a vypíš x > y.', 'example': 'x = 2\ny = 3\nprint(x > y)', 'hint': 'Výsledok bude False.', 'expected': 'False\n', 'mode': 'output', 'required': ['compare']},
 ],
 "Lists": [
  {"title":"First item", "prompt":"Vytvor zoznam [10, 20, 30] a vypíš prvý prvok pomocou indexu 0.", "example":"items = [1, 2]\nprint(items[0])", "hint":"Prvý prvok má index [0].", "expected":"10\n", "mode":"output", "required":["list", "subscript"]},
  {"title":"Length of list", "prompt":"Vypíš počet prvkov zoznamu [1, 2, 3] pomocou len().", "example":"print(len([4, 5]))", "hint":"len([1, 2, 3])", "expected":"3\n", "mode":"output", "required":["list", "len"]},
  {"title":"Append", "prompt":"Vytvor zoznam [1, 2], pridaj 3 pomocou append() a vypíš celý zoznam.", "example":"a = [5]\na.append(6)\nprint(a)", "hint":"Metóda append(3) pridá prvok na koniec.", "expected":"[1, 2, 3]\n", "mode":"output", "required":["append"]},
  {'title': 'Second item', 'prompt': 'Vytvor zoznam [4, 8, 12] a vypíš druhý prvok cez index 1.', 'example': 'a = [1, 2]\nprint(a[1])', 'hint': 'Indexy začínajú nulou.', 'expected': '8\n', 'mode': 'output', 'required': ['list', 'subscript']},
  {'title': 'Last item', 'prompt': 'Vytvor zoznam ["red", "blue"] a vypíš posledný prvok cez index 1.', 'example': 'a = ["a", "b"]\nprint(a[1])', 'hint': 'Druhý prvok má index 1.', 'expected': 'blue\n', 'mode': 'output', 'required': ['list', 'subscript']},
  {'title': 'List of names', 'prompt': 'Vytvor zoznam ["Eva", "Tom"] a vypíš celý zoznam.', 'example': 'print(["A", "B"])', 'hint': 'Použi hranaté zátvorky.', 'expected': "['Eva', 'Tom']\n", 'mode': 'output', 'required': ['list']},
  {'title': 'Append number', 'prompt': 'Vytvor zoznam [5], pridaj 6 pomocou append() a vypíš zoznam.', 'example': 'a = [1]\na.append(2)\nprint(a)', 'hint': 'append() pridáva na koniec.', 'expected': '[5, 6]\n', 'mode': 'output', 'required': ['append']},
  {'title': 'Length four', 'prompt': 'Vypíš dĺžku zoznamu [1, 2, 3, 4] pomocou len().', 'example': 'print(len([2, 3]))', 'hint': 'len() vráti počet prvkov.', 'expected': '4\n', 'mode': 'output', 'required': ['list', 'len']},
 ],
 "Conditional Statements": [
  {"title":"If", "prompt":"Nastav x = 10 a pomocou if x > 5: vypíš Big.", "example":"x = 8\nif x > 2:\n    print('Yes')", "hint":"Za if je dvojbodka : a nasledujúci riadok musí byť odsadený.", "expected":"Big\n", "mode":"output", "required":["if"]},
  {"title":"Else", "prompt":"Nastav x = 2. Použi if/else: ak x > 5 vypíš Big, inak Small.", "example":"x = 1\nif x > 3:\n    print('Yes')\nelse:\n    print('No')", "hint":"else: sa píše bez podmienky.", "expected":"Small\n", "mode":"output", "required":["if", "else"]},
  {"title":"Equality condition", "prompt":"Nastav x = 4 a cez if x == 4: vypíš Equal.", "example":"x = 3\nif x == 3:\n    print('OK')", "hint":"V podmienke porovnávaj pomocou ==.", "expected":"Equal\n", "mode":"output", "required":["if", "equality"]},
  {'title': 'Positive', 'prompt': 'Nastav x = 7 a ak x > 0, vypíš Positive.', 'example': 'x = 1\nif x > 0:\n    print("Yes")', 'hint': 'Nezabudni na odsadenie.', 'expected': 'Positive\n', 'mode': 'output', 'required': ['if']},
  {'title': 'Small', 'prompt': 'Nastav x = 3. Ak x > 10 vypíš Big, inak Small.', 'example': 'x = 1\nif x > 5:\n    print("Big")\nelse:\n    print("Tiny")', 'hint': 'Použi else:.', 'expected': 'Small\n', 'mode': 'output', 'required': ['if', 'else']},
  {'title': 'Equal', 'prompt': 'Nastav x = 5 a ak x == 5, vypíš Five.', 'example': 'x = 2\nif x == 2:\n    print("Two")', 'hint': '== je porovnanie.', 'expected': 'Five\n', 'mode': 'output', 'required': ['if', 'equality']},
  {'title': 'Not equal', 'prompt': 'Nastav x = 4 a ak x != 5, vypíš Different.', 'example': 'x = 2\nif x != 3:\n    print("Other")', 'hint': '!= znamená nie je rovné.', 'expected': 'Different\n', 'mode': 'output', 'required': ['if']},
  {'title': 'Else branch', 'prompt': 'Nastav x = 0. Ak x > 0 vypíš Plus, inak Zero.', 'example': 'x = 1\nif x > 0:\n    print("Yes")\nelse:\n    print("No")', 'hint': 'Pri nule sa vykoná else.', 'expected': 'Zero\n', 'mode': 'output', 'required': ['if', 'else']},
 ],
 "Loops": [
  {"title":"Count", "prompt":"Pomocou for a range() vypíš 1, 2, 3 na samostatné riadky.", "example":"for i in range(1, 3):\n    print(i)", "hint":"range(1, 4) vytvorí čísla 1, 2, 3.", "expected":"1\n2\n3\n", "mode":"output", "required":["for", "range"]},
  {"title":"Repeat", "prompt":"Pomocou for vypíš Hi presne trikrát.", "example":"for i in range(2):\n    print('Go')", "hint":"range(3) zopakuje cyklus trikrát.", "expected":"Hi\nHi\nHi\n", "mode":"output", "required":["for"]},
  {"title":"Sum loop", "prompt":"Pomocou for a range() spočítaj čísla od 1 do 4 a vypíš 10.", "example":"total = 0\nfor i in range(1, 3):\n    total += i\nprint(total)", "hint":"Použi total = 0 a v cykle total += i.", "expected":"10\n", "mode":"output", "required":["for", "range"]},
  {'title': 'Count zero', 'prompt': 'Pomocou for a range(3) vypíš 0, 1, 2 na samostatné riadky.', 'example': 'for i in range(2):\n    print(i)', 'hint': 'range(3) začína nulou.', 'expected': '0\n1\n2\n', 'mode': 'output', 'required': ['for', 'range']},
  {'title': 'Count to five', 'prompt': 'Pomocou for a range() vypíš čísla 1 až 5.', 'example': 'for i in range(1, 3):\n    print(i)', 'hint': 'Použi range(1, 6).', 'expected': '1\n2\n3\n4\n5\n', 'mode': 'output', 'required': ['for', 'range']},
  {'title': 'Repeat Python', 'prompt': 'Pomocou for vypíš Python štyrikrát.', 'example': 'for i in range(2):\n    print("Hi")', 'hint': 'range(4) zopakuje cyklus štyrikrát.', 'expected': 'Python\nPython\nPython\nPython\n', 'mode': 'output', 'required': ['for']},
  {'title': 'Sum three', 'prompt': 'Pomocou for a range() spočítaj 1 + 2 + 3 a vypíš 6.', 'example': 'total = 0\nfor i in range(1, 3):\n    total += i\nprint(total)', 'hint': 'Použi range(1, 4).', 'expected': '6\n', 'mode': 'output', 'required': ['for', 'range']},
  {'title': 'Repeat star', 'prompt': 'Pomocou for vypíš znak * na tri samostatné riadky.', 'example': 'for i in range(2):\n    print("#")', 'hint': 'Znak * daj do úvodzoviek.', 'expected': '*\n*\n*\n', 'mode': 'output', 'required': ['for']},
 ],
 "Functions": [
  {"title":"Define function", "prompt":"Definuj funkciu greet(), ktorá vypíše Hello, a zavolaj ju.", "example":"def hello():\n    print('Hi')\nhello()", "hint":"def greet(): ... potom greet().", "expected":"Hello\n", "mode":"output", "required":["function"]},
  {"title":"Return", "prompt":"Definuj funkciu double(n), ktorá vráti n * 2. Vypíš double(4).", "example":"def triple(n):\n    return n * 3\nprint(triple(2))", "hint":"Použi return, nie iba print vo funkcii.", "expected":"8\n", "mode":"output", "required":["function", "return"]},
  {"title":"Parameters", "prompt":"Definuj add(a, b), ktorá vráti súčet. Vypíš add(3, 5).", "example":"def add(a, b):\n    return a + b\nprint(add(1, 2))", "hint":"Funkcia prijíma dva parametre.", "expected":"8\n", "mode":"output", "required":["function", "return", "addition"]},
 ],
}

DETAILED_EXPLANATIONS = {'Your First Python Program': ('`print()` znamená „vypíš“. Zátvorky `()` obsahujú to, čo sa má vypísať. '
                               'Úvodzovky označujú text. `print("A")` vypíše A, ale `print(A)` hľadá '
                               'premennú A.',
                               '`print("Hello")`',
                               '1. Python nájde funkciu `print`. 2. Prečíta text medzi úvodzovkami. 3. '
                               'Zobrazí ho a prejde na nový riadok.',
                               'Nezabudni na koncovú úvodzovku, uzatváraciu zátvorku a medzery vo '
                               'výstupe.'),
 'Main Concepts': ('Premenná je pomenované miesto pre hodnotu. V `age = 12` je `age` názov, `=` '
                   'priradenie a `12` číslo. `=` neznamená porovnanie.',
                   '`age = 12` potom `print(age)`',
                   '1. Hodnota 12 sa uloží pod názvom age. 2. `print(age)` načíta hodnotu. 3. Vypíše '
                   '12.',
                   'Text patrí do úvodzoviek, číslo spravidla nie. Názvy premenných rozlišujú veľké a '
                   'malé písmená.'),
 'Numbers': ('Python používa `+` sčítanie, `-` odčítanie, `*` násobenie a `/` delenie. Desatinné čísla '
             'píš s bodkou, napríklad `2.5`.',
             '`print(6 * 3)`',
             '1. Python vypočíta 6 krát 3. 2. Výsledok 18 odovzdá funkcii print. 3. Zobrazí 18.',
             'Pri násobení používaj `*`, nie x. Delenie nulou spôsobí chybu.'),
 'Strings': ('String je text v jednoduchých alebo dvojitých úvodzovkách. `+` môže spájať dva texty. '
             '`len()` spočíta znaky vrátane medzier.',
             '`print("Good " + "morning")`',
             '1. Vytvoria sa dva texty. 2. `+` ich spojí vrátane medzery. 3. print vypíše Good morning.',
             'Bez medzery v texte vznikne Goodmorning. Číslo a text sa nedajú jednoducho sčítať pomocou '
             '+.'),
 'Boolean': ('Boolean má hodnotu `True` alebo `False`. `>` znamená väčšie, `<` menšie, `==` rovná sa, '
             '`!=` nerovná sa, `>=` väčšie alebo rovné.',
             '`print(8 > 3)`',
             '1. Python porovná 8 a 3. 2. Podmienka platí. 3. Vypíše True.',
             'Na porovnávanie použi `==`; samostatné `=` hodnotu priraďuje.'),
 'Lists': ('Zoznam zapisujeme do `[]`. Prvý prvok má index `0`, druhý `1`. `len()` počíta prvky a '
           '`.append()` pridá nový prvok na koniec.',
           '`a = [10, 20]` potom `print(a[0])`',
           '1. Vznikne zoznam dvoch čísel. 2. `a[0]` vyberie prvý prvok. 3. Vypíše 10.',
           'Index 2 v dvojprvkovom zozname neexistuje. Nezamieňaj index s poradovým číslom.'),
 'Conditional Statements': ('`if` overí podmienku. Za podmienkou nasleduje `:`. Odsadené riadky patria '
                            'do bloku. `else` sa vykoná, keď podmienka neplatí.',
                            '`x = 2` potom `if x > 5: ... else: ...`',
                            '1. Python vyhodnotí `2 > 5`. 2. Výsledok je False. 3. Vykoná odsadený blok '
                            'pod else.',
                            'Nezabudni na dvojbodku a štyri medzery odsadenia. `else:` nemá vlastnú '
                            'podmienku.'),
 'Loops': ('`for` opakuje odsadené príkazy. `range(3)` dá hodnoty 0, 1, 2. `range(1, 4)` dá 1, 2, 3; '
           'koncová hodnota 4 sa nezahrnie.',
           '`for i in range(1, 4):` potom odsadené `print(i)`',
           '1. i = 1, vypíše 1. 2. i = 2, vypíše 2. 3. i = 3, vypíše 3. 4. Cyklus skončí.',
           'Nezabudni na `:` a odsadenie. Posledné číslo v range() nie je zahrnuté.')}

SYMBOLS = [
 ("`\"text\"` alebo `'text'`", "Úvodzovky označujú text. Bez nich Python hľadá premennú s daným názvom."),
 ("`=`", "Priradenie: uloží hodnotu do premennej, napríklad `age = 12`."),
 ("`==`", "Porovnanie: zisťuje, či sú dve hodnoty rovnaké. Výsledok je `True` alebo `False`."),
 ("`()`", "Zátvorky sa používajú pri volaní funkcie, napríklad `print('Hi')`."),
 ("`:`", "Dvojbodka uvádza blok pri `if`, `for`, `while`, `def` a ďalších príkazoch."),
 ("**Odsadenie**", "Štyri medzery na začiatku riadku označujú, že riadok patrí do bloku."),
 ("`#`", "Za znakom # nasleduje komentár, ktorý Python nevykoná."),
 ("`[]`", "Hranaté zátvorky tvoria zoznam alebo vyberajú jeho prvok podľa indexu."),
 ("`+`, `-`, `*`, `/`", "Operátory pre sčítanie, odčítanie, násobenie a delenie."),
]

def fallback_tasks(topic):
    # These are practice activities, not semantic correctness tests for the topic.
    return [
      {"title":f"Explore {topic}", "prompt":f"Vyskúšaj si príklad z kapitoly {topic}. Pridaj komentár, čo sa podľa teba stane.", "example":get_lesson(topic)[1], "hint":"Začni od vzorového príkladu a zmeň jednu hodnotu.", "mode":"syntax"},
      {"title":"Modify the example", "prompt":f"Uprav príklad k téme {topic} tak, aby sa zmenil výsledok programu.", "example":get_lesson(topic)[1], "hint":"Zmeň číslo alebo text a vysvetli očakávaný výsledok.", "mode":"syntax"},
      {"title":"Your own example", "prompt":f"Napíš vlastný krátky príklad k téme {topic} a pridaj komentár vysvetľujúci, čo robí.", "example":get_lesson(topic)[1], "hint":"Napíš najskôr komentár s # a potom svoj kód.", "mode":"syntax"},
    ]

def get_lesson(topic):
    if topic in LESSONS:
        return LESSONS[topic]
    return (f"Kapitola {topic}: pozri si príklad a porovnaj jednotlivé príkazy. "
            "Všímaj si zátvorky, operátory a odsadenie.",
            "message = 'I am learning Python'\nprint(message)",
            "Vyskúšaj príklad a uprav ho.")

def features(tree, code):
    nodes=list(ast.walk(tree))
    calls=[n.func for n in nodes if isinstance(n, ast.Call)]
    named=lambda s:any(isinstance(f,ast.Name) and f.id==s for f in calls)
    return {
      "assign_name":any(isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='name' for t in n.targets) for n in nodes),
      "assign_age":any(isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='age' for t in n.targets) for n in nodes),
      "print_name":any(isinstance(n,ast.Call) and isinstance(n.func,ast.Name) and n.func.id=='print' and any(isinstance(a,ast.Name) and a.id=='name' for a in n.args) for n in nodes),
      "addition":any(isinstance(n,ast.BinOp) and isinstance(n.op,ast.Add) for n in nodes),
      "string_add":any(isinstance(n,ast.BinOp) and isinstance(n.op,ast.Add) for n in nodes),
      "multiplication":any(isinstance(n,ast.BinOp) and isinstance(n.op,ast.Mult) for n in nodes),
      "division":any(isinstance(n,ast.BinOp) and isinstance(n.op,ast.Div) for n in nodes),
      "comment":"#" in code,
      "len":named('len'), "range":named('range'),
      "compare":any(isinstance(n,ast.Compare) for n in nodes),
      "equality":any(isinstance(n,ast.Compare) and any(isinstance(o,ast.Eq) for o in n.ops) for n in nodes),
      "list":any(isinstance(n,ast.List) for n in nodes),
      "subscript":any(isinstance(n,ast.Subscript) for n in nodes),
      "append":any(isinstance(f,ast.Attribute) and f.attr=='append' for f in calls),
      "if":any(isinstance(n,ast.If) for n in nodes),
      "else":any(isinstance(n,ast.If) and bool(n.orelse) for n in nodes),
      "for":any(isinstance(n,ast.For) for n in nodes),
      "function":any(isinstance(n,ast.FunctionDef) for n in nodes),
      "return":any(isinstance(n,ast.Return) for n in nodes),
    }

# Interpret a small subset of Python syntax without executing student code.
class CannotEvaluate(Exception):
    pass


def evaluate_program(tree):
    remaining = 1200
    output = []
    output_size = 0

    def tick():
        nonlocal remaining
        remaining -= 1
        if remaining < 0:
            raise CannotEvaluate()

    def bounded(value):
        # Count nested items even when a list refers to the same item twice.
        budget = 2000

        def visit(item, depth):
            nonlocal budget
            budget -= 1 + (len(item) if type(item) is str else 0)
            if budget < 0 or depth > 12:
                raise CannotEvaluate()
            if type(item) is int and item.bit_length() > 512:
                raise CannotEvaluate()
            if type(item) in (list, tuple):
                for child in item:
                    visit(child, depth + 1)
            elif type(item) not in (int, float, str, bool, range, type(None)):
                raise CannotEvaluate()

        visit(value, 0)
        return value

    def expr(node, env, functions, depth):
        tick()
        if depth > 24:
            raise CannotEvaluate()
        read = lambda child: expr(child, env, functions, depth + 1)
        if isinstance(node, ast.Constant):
            return bounded(node.value)
        if isinstance(node, ast.Name):
            if node.id not in env:
                raise NameError(node.id)
            return bounded(env[node.id])
        if isinstance(node, (ast.List, ast.Tuple)):
            items = [read(child) for child in node.elts]
            return bounded(items if isinstance(node, ast.List) else tuple(items))
        if isinstance(node, ast.Subscript):
            return bounded(read(node.value)[read(node.slice)])
        if isinstance(node, ast.UnaryOp):
            value = read(node.operand)
            if isinstance(node.op, ast.USub):
                return bounded(-value)
            if isinstance(node.op, ast.UAdd):
                return bounded(+value)
            if isinstance(node.op, ast.Not):
                return not value
        if isinstance(node, ast.BinOp):
            a, b = read(node.left), read(node.right)
            if isinstance(node.op, ast.Add):
                return bounded(a + b)
            if isinstance(node.op, ast.Sub):
                return bounded(a - b)
            if isinstance(node.op, ast.Mult):
                for seq, count in ((a, b), (b, a)):
                    if type(seq) in (str, list, tuple) and type(count) in (int, bool):
                        if count > 2000 or len(seq) * max(count, 0) > 2000:
                            raise CannotEvaluate()
                return bounded(a * b)
            if isinstance(node.op, ast.Div):
                return bounded(a / b)
        if isinstance(node, ast.Compare) and len(node.ops) == 1:
            a, b = read(node.left), read(node.comparators[0])
            op = node.ops[0]
            if isinstance(op, ast.Gt):
                return a > b
            if isinstance(op, ast.Lt):
                return a < b
            if isinstance(op, ast.Eq):
                return a == b
            if isinstance(op, ast.GtE):
                return a >= b
            if isinstance(op, ast.LtE):
                return a <= b
            if isinstance(op, ast.NotEq):
                return a != b
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and not node.keywords:
            name = node.func.id
            args = [read(arg) for arg in node.args]
            if name in functions and name not in env:
                fn = functions[name]
                if len(args) != len(fn.args.args):
                    raise TypeError()
                local = dict(env)
                local.update(zip((arg.arg for arg in fn.args.args), args))
                return block(fn.body, local, dict(functions), depth + 1, True)[1]
            if name not in env and name == "len" and len(args) == 1:
                return bounded(len(args[0]))
            if name not in env and name == "range" and 1 <= len(args) <= 3:
                return range(*args)
        raise CannotEvaluate()

    def block(statements, env, functions, depth=0, in_function=False):
        nonlocal output_size
        if depth > 24:
            raise CannotEvaluate()
        read = lambda node: expr(node, env, functions, depth + 1)
        for node in statements:
            tick()
            if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
                env[node.targets[0].id] = read(node.value)
            elif isinstance(node, ast.AugAssign) and isinstance(node.target, ast.Name) and isinstance(node.op, ast.Add):
                current = read(node.target)
                extra = read(node.value)
                updated = bounded(current + extra)
                if type(current) is list:
                    current[:] = updated
                    bounded(current)
                else:
                    env[node.target.id] = updated
            elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                call = node.value
                if call.keywords:
                    raise CannotEvaluate()
                if isinstance(call.func, ast.Name) and call.func.id == "print" and "print" not in env and "print" not in functions:
                    line = " ".join(str(read(arg)) for arg in call.args) + "\n"
                    output_size += len(line)
                    if output_size > 5000:
                        raise CannotEvaluate()
                    output.append(line)
                elif isinstance(call.func, ast.Attribute) and call.func.attr == "append" and len(call.args) == 1:
                    target = read(call.func.value)
                    if type(target) is not list:
                        raise CannotEvaluate()
                    target.append(read(call.args[0]))
                    bounded(target)
                else:
                    read(call)
            elif isinstance(node, ast.If):
                returned, value = block(node.body if read(node.test) else node.orelse, env, functions, depth + 1, in_function)
                if returned:
                    return True, value
            elif isinstance(node, ast.For) and isinstance(node.target, ast.Name) and not node.orelse:
                iterable = read(node.iter)
                if len(iterable) > 100:
                    raise CannotEvaluate()
                for item in iterable:
                    tick()
                    env[node.target.id] = bounded(item)
                    returned, value = block(node.body, env, functions, depth + 1, in_function)
                    if returned:
                        return True, value
            elif isinstance(node, ast.FunctionDef):
                args = node.args
                if (node.decorator_list or node.returns or args.posonlyargs or args.kwonlyargs
                        or args.vararg or args.kwarg or args.defaults or any(arg.annotation for arg in args.args)):
                    raise CannotEvaluate()
                functions[node.name] = node
                env.pop(node.name, None)
            elif isinstance(node, ast.Return) and in_function:
                return True, read(node.value) if node.value is not None else None
            elif isinstance(node, ast.Expr):
                read(node.value)
            elif not isinstance(node, ast.Pass):
                raise CannotEvaluate()
        return False, None

    block(tree.body, {}, {})
    return "".join(output)


EVALUATION_ERRORS = (CannotEvaluate, TypeError, ValueError, ArithmeticError,
                     NameError, LookupError, RecursionError)


def run_student_code(code):
    if not code.strip():
        return "warning", "Najskôr napíš kód."
    if len(code) > 4000:
        return "warning", "Kód je príliš dlhý. Skús kratší program."
    try:
        # Compile only to validate syntax (e.g. return outside a function).
        # The compiled code is never executed.
        compile(code, "<žiacky kód>", "exec", dont_inherit=True)
        return "success", evaluate_program(ast.parse(code))
    except SyntaxError as error:
        return "error", f"Syntaktická chyba na riadku {error.lineno}: {error.msg}"
    except NameError as error:
        return "error", f"Názov {str(error)!r} nie je definovaný. Ak chceš vypísať text, vlož ho do úvodzoviek."
    except ZeroDivisionError:
        return "error", "Nulou sa nedá deliť."
    except IndexError:
        return "error", "Takýto index v zozname alebo texte neexistuje."
    except EVALUATION_ERRORS:
        return "info", "Tento zápis alebo rozsah programu náhľad nepodporuje. Skús krátky príklad s print(), premennými, výpočtami, if alebo for."


def check_answer(code, task):
    if not code.strip(): return "warning", "Najskôr napíš svoj kód."
    if len(code)>4000: return "error", "Kód je príliš dlhý. Skús kratšie riešenie."
    try: tree=ast.parse(code)
    except SyntaxError as e: return "error", f"Syntax error – riadok {e.lineno}: {e.msg}. Skontroluj úvodzovky, zátvorky, dvojbodku a odsadenie."
    if task['mode']=='syntax':
        return "info", "Syntax je správna. Táto pokročilá úloha zatiaľ nemá automatický test správnosti; porovnaj svoje riešenie so zadaním."
    found=features(tree,code)
    missing=[f for f in task.get('required',[]) if not found.get(f)]
    if missing: return "warning", "Kód má správnu syntax, ale chýba požadovaný spôsob riešenia. Nápoveda: "+task['hint']
    try: result=evaluate_program(tree)
    except EVALUATION_ERRORS:
        return "info", "Syntax je správna, ale tento spôsob zápisu automatická kontrola ešte nepodporuje. Skús jednoduchší zápis podľa príkladu."
    if result==task['expected']: return "success", "Správne! Program spĺňa požadovaný výstup aj kontrolované pravidlá zadania. Môžeš kliknúť na Next Task."
    return "warning", "Syntax je správna, ale výsledok nezodpovedá zadaniu. Očakávaný výstup: " + repr(task['expected'].rstrip('\n')) + ". Tvoj výstup: " + repr(result.rstrip('\n')) + "."

if 'chapter_index' not in st.session_state: st.session_state.chapter_index=0
if 'task_positions' not in st.session_state: st.session_state.task_positions={}
if 'completed' not in st.session_state: st.session_state.completed=[]
if 'result' not in st.session_state: st.session_state.result=None

st.title('🐍 Python Tutor')
st.write('Learn Python step by step | Uč sa Python krok za krokom')
st.info('Bezplatná verzia bez API kľúča. Automatické testy sú pripravené pre úvodné kapitoly; pokročilé kapitoly zatiaľ kontrolujú len syntax.')
with st.sidebar:
    st.header('📚 Learning plan')
    chapter=st.selectbox('Choose a chapter:',range(len(TOPICS)),index=st.session_state.chapter_index,format_func=lambda i:f'{i+1}. {TOPICS[i]}')
    if chapter!=st.session_state.chapter_index:
        st.session_state.chapter_index=chapter
        st.session_state.result=None
        st.session_state.pop('run_result',None)
    st.subheader('Your progress')
    st.progress(len(st.session_state.completed)/len(TOPICS))
    st.write(f'{len(st.session_state.completed)} of {len(TOPICS)} chapters completed')
    if st.button('Reset progress'):
        st.session_state.completed=[]
        st.session_state.task_positions={}
        st.session_state.result=None
        st.session_state.pop('run_result',None)
        st.rerun()

topic=TOPICS[chapter]
tasks=TASKS.get(topic) or fallback_tasks(topic)
pos=st.session_state.task_positions.get(chapter,0)
task=tasks[pos]
explanation,original_example,_=get_lesson(topic)
st.subheader(f'Chapter {chapter+1}: {topic}')
st.markdown('### 📖 Explanation / Vysvetlenie')
st.write(explanation)
if topic in DETAILED_EXPLANATIONS:
    details = DETAILED_EXPLANATIONS[topic]
    st.markdown('#### 🧩 Podrobné vysvetlenie')
    st.markdown(details[0])
    st.markdown('**Ukážka zápisu:**')
    st.markdown(details[1])
    st.markdown('**Čo Python urobí krok za krokom:**')
    st.markdown(details[2])
    st.markdown('**Pozor na časté chyby:**')
    st.warning(details[3])
st.markdown('### 🔎 What do the symbols mean? / Čo znamenajú znaky?')
with st.expander('Úvodzovky, =, ==, (), :, odsadenie a ďalšie znaky',expanded=True):
    for symbol,meaning in SYMBOLS:
        st.markdown(f'**{symbol}** – {meaning}')
st.markdown('### 💡 Example / Príklad')
st.code(task['example'],language='python')
st.write('**Čo sa stane po zadaní príkazu?**')
for line in task['example'].splitlines():
    clean=line.strip()
    if not clean: continue
    if clean.startswith('#'): meaning='Komentár: Python tento riadok nevykoná.'
    elif clean.startswith('print('): meaning='Funkcia print() zobrazí hodnotu alebo text na obrazovke.'
    elif clean.startswith('if '): meaning='Podmienka sa vyhodnotí; odsadený blok sa vykoná, len ak platí.'
    elif clean.startswith('else:'): meaning='Tento blok sa vykoná, ak predchádzajúca podmienka neplatí.'
    elif clean.startswith('for '): meaning='Cyklus postupne prechádza hodnoty a opakuje odsadený blok.'
    elif clean.startswith('def '): meaning='Týmto sa definuje funkcia; jej telo sa vykoná až pri zavolaní.'
    elif clean.startswith('return '): meaning='Funkcia vráti vypočítanú hodnotu.'
    elif '.append(' in clean: meaning='Do zoznamu sa pridá nový prvok.'
    elif '=' in clean and '==' not in clean: meaning='Priradenie: vypočítaná hodnota sa uloží do premennej.'
    else: meaning='Python vykoná tento príkaz podľa jeho významu.'
    st.markdown(f'`{clean}` – {meaning}')
try:
    sample_result=evaluate_program(ast.parse(task['example']))
    if sample_result:
        st.write('**Výstup príkladu:**')
        st.code(sample_result,language='text')
except EVALUATION_ERRORS:
    st.caption('Výstup tohto príkladu sa v bezpečnom náhľade nedá automaticky vypočítať.')
st.divider()
st.markdown(f'### 📝 Task {pos+1} of {len(tasks)}: {task["title"]}')
st.write(task['prompt'])
with st.expander('💡 Hint / Nápoveda'):
    st.write(task['hint'])
code_key=f'code_{chapter}_{pos}'
student_code=st.text_area('Write your Python code:',key=code_key,height=180,placeholder='print("Hello, Python!")')
st.caption("Run Code ukáže výstup podporovaných príkazov aj bez kontroly zadania.")
left,middle,right=st.columns(3)
with left:
    if st.button('▶ Run Code',use_container_width=True):
        st.session_state.run_result=(chapter,pos,student_code,*run_student_code(student_code))
with middle:
    if st.button('✅ Check my solution',use_container_width=True):
        st.session_state.result=(chapter,pos,*check_answer(student_code,task))
with right:
    if st.button('➡️ Next Task',use_container_width=True,disabled=(pos>=len(tasks)-1)):
        st.session_state.task_positions[chapter]=pos+1
        st.session_state.result=None
        st.session_state.pop('run_result',None)
        st.rerun()
run_result=st.session_state.get('run_result')
if run_result and run_result[:3]==(chapter,pos,student_code):
    _,_,_,run_status,run_message=run_result
    st.markdown('#### Program Output / Výstup programu')
    if run_status=='success':
        if run_message:
            st.code(run_message,language='text')
        else:
            st.info('Program nič nevypísal. Na zobrazenie výsledku použi print().')
    else:
        getattr(st,run_status)(run_message)
if st.session_state.result and st.session_state.result[:2]==(chapter,pos):
    _,_,status,message=st.session_state.result
    getattr(st,status)(message)
if pos==len(tasks)-1:
    st.caption('Toto je posledná úloha v kapitole. Ďalšiu kapitolu vyber v ľavom menu.')
if st.button('↩️ First Task in this chapter'):
    st.session_state.task_positions[chapter]=0
    st.session_state.result=None
    st.session_state.pop('run_result',None)
    st.rerun()
st.divider()
completed=chapter in st.session_state.completed
if st.checkbox('I have completed this chapter',value=completed,key=f'done_{chapter}')!=completed:
    if completed: st.session_state.completed.remove(chapter)
    else: st.session_state.completed.append(chapter)
    st.rerun()
st.caption('Pokrok sa uchováva iba v aktuálnej relácii. Kontrola je obmedzená na podporované vzory kódu; nejde o úplné spúšťanie Pythonu ani AI hodnotenie.')
