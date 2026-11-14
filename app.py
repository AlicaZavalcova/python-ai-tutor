import ast
import streamlit as st

st.set_page_config(
    page_title="Python Tutor",
    page_icon="🐍",
    layout="wide"
)

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

# These notes are prepared in the app. No external AI service or API key is used.
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

def get_lesson(topic):
    if topic in LESSONS:
        return LESSONS[topic]
    explanation = (
        f"Téma **{topic}** rozširuje tvoje znalosti Pythonu. "
        "Všímaj si nové pojmy, porovnaj ich s tým, čo už poznáš, "
        "a skús si každý príklad upraviť podľa seba."
    )
    example = (
        "# Skús si pripraviť vlastný príklad k téme:\n"
        "message = 'I am practising Python'\n"
        "print(message)"
    )
    exercise = (
        f"Vytvor krátky program, v ktorom prakticky použiješ tému "
        f"'{topic}'. Pridaj komentár, ktorý vysvetlí, čo robí každý dôležitý riadok."
    )
    return explanation, example, exercise

if "completed" not in st.session_state:
    st.session_state.completed = []
if "show_lesson" not in st.session_state:
    st.session_state.show_lesson = False

st.title("🐍 Python Tutor")
st.write(
    "Learn Python step by step. Vyber si kapitolu, prečítaj si vysvetlenie "
    "a precvič si programovanie."
)
st.info(
    "Bezplatná offline verzia: lekcie a kontrola syntaxe sú pripravené priamo "
    "v aplikácii. Nie je potrebný OpenAI API kľúč."
)

with st.sidebar:
    st.header("📚 Learning plan")
    selected_topic = st.selectbox("Choose a chapter:", TOPICS)
    st.divider()
    st.subheader("Your progress")
    completed_count = len(st.session_state.completed)
    st.progress(completed_count / len(TOPICS))
    st.write(f"{completed_count} of {len(TOPICS)} chapters completed")
    if st.button("Reset progress"):
        st.session_state.completed = []
        st.rerun()

chapter_number = TOPICS.index(selected_topic) + 1
st.subheader(f"Chapter {chapter_number}: {selected_topic}")

explanation, example, exercise = get_lesson(selected_topic)

if st.button("📖 Prepare my lesson"):
    st.session_state.show_lesson = True

if st.session_state.show_lesson:
    st.markdown("### Explanation")
    st.write(explanation)
    st.markdown("### Example")
    st.code(example, language="python")
    st.markdown("### Your exercise")
    st.write(exercise)

st.divider()
st.subheader("💻 Try your Python code")
st.caption(
    "Kontrola overí, či má kód správnu Python syntax. Kód sa v tejto verzii "
    "nespúšťa a kontrola neposudzuje, či riešenie správne plní zadanie."
)
student_code = st.text_area(
    "Write your code here:",
    height=220,
    placeholder='print("Hello, Python!")'
)

if st.button("Check my code"):
    if not student_code.strip():
        st.warning("Najskôr napíš svoj Python kód.")
    else:
        try:
            ast.parse(student_code)
            st.success("Syntax looks correct! Výborne, kód je syntakticky správny.")
        except SyntaxError as error:
            st.error(
                f"Našiel sa problém v syntaxi na riadku {error.lineno}: "
                f"{error.msg}"
            )
            if error.text:
                st.code(error.text, language="python")

st.divider()
st.subheader("✅ Chapter progress")
is_completed = selected_topic in st.session_state.completed
new_status = st.checkbox(
    "I have completed this chapter",
    value=is_completed,
    key=f"completed_{chapter_number}"
)
if new_status and not is_completed:
    st.session_state.completed.append(selected_topic)
    st.rerun()
elif not new_status and is_completed:
    st.session_state.completed.remove(selected_topic)
    st.rerun()

st.caption(
    "Poznámka: Pokrok sa v tejto jednoduchej verzii ukladá počas aktuálnej "
    "relácie aplikácie. Po reštarte alebo novej relácii sa môže vynulovať."
)
