
import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="Python AI Tutor",
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

SYSTEM_PROMPT = """
You are Python AI Tutor, a friendly and patient Python programming teacher.

Teaching language: English and Slovak.
Explain concepts mainly in Slovak, but keep Python terminology,
programming keywords and topic names in English.

Your teaching style:
- Explain concepts step by step.
- Use simple examples.
- Show Python code in code blocks.
- Ask the student questions.
- Give practical exercises.
- Do not immediately reveal every solution.
- Offer hints when the student is struggling.
- Check code carefully and explain mistakes.
- Adapt explanations to the student's level.
- Encourage the student and be patient.

The student is following a course of 43 chapters.
Stay focused on the selected chapter unless the student asks otherwise.
"""

def get_client():
    try:
        api_key = st.secrets["OPENAI_API_KEY"]
        return OpenAI(api_key=api_key)
    except Exception:
        return None


if "messages" not in st.session_state:
    st.session_state.messages = []

if "completed" not in st.session_state:
    st.session_state.completed = []

st.title("🐍 Python AI Tutor")
st.write("Learn Python step by step with your personal AI teacher.")

with st.sidebar:
    st.header("📚 Learning plan")

    selected_topic = st.selectbox(
        "Choose a chapter:",
        TOPICS,
        index=0
    )

    st.divider()
    st.subheader("Your progress")

    completed_count = len(st.session_state.completed)
    progress = completed_count / len(TOPICS)

    st.progress(progress)
    st.write(f"{completed_count} of {len(TOPICS)} chapters completed")

    st.divider()
    st.subheader("Mark chapter as completed")

    is_completed = st.checkbox(
        "I have completed this chapter",
        value=selected_topic in st.session_state.completed
    )

    if is_completed and selected_topic not in st.session_state.completed:
        st.session_state.completed.append(selected_topic)
        st.rerun()

    if not is_completed and selected_topic in st.session_state.completed:
        st.session_state.completed.remove(selected_topic)
        st.rerun()

    if st.button("Start a new conversation"):
        st.session_state.messages = []
        st.rerun()


chapter_number = TOPICS.index(selected_topic) + 1

st.subheader(f"Chapter {chapter_number}: {selected_topic}")

st.write(
    "Ask your AI teacher to explain the topic, give you an exercise "
    "or check your Python code."
)

client = get_client()

if client is None:
    st.warning(
        "The AI teacher is not connected yet. "
        "The application administrator needs to configure the "
        "OpenAI API key before the AI lessons can work."
    )

if st.button("📖 Prepare my lesson", disabled=client is None):
    with st.spinner("Your teacher is preparing the lesson..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": (
                            f"Prepare a structured beginner-friendly lesson "
                            f"for Chapter {chapter_number}: {selected_topic}. "
                            "Include an explanation in Slovak, English "
                            "programming terminology, Python examples, "
                            "and three exercises of increasing difficulty. "
                            "Do not show the solutions immediately."
                        )
                    }
                ]
            )

            lesson = response.choices[0].message.content

            st.session_state.messages = [
                {"role": "assistant", "content": lesson}
            ]
            st.rerun()

        except Exception as error:
            st.error(f"Could not prepare the lesson: {error}")


st.divider()
st.subheader("💬 Talk to your AI teacher")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_question = st.chat_input(
    "Ask a question or paste your Python code...",
    disabled=client is None
)

if user_question and client is not None:
    st.session_state.messages.append(
        {"role": "user", "content": user_question}
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    with st.chat_message("assistant"):
        with st.spinner("Your teacher is thinking..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {
                            "role": "system",
                            "content": (
                                f"The current chapter is: "
                                f"{selected_topic}."
                            )
                        },
                        *st.session_state.messages
                    ]
                )

                answer = response.choices[0].message.content
                st.markdown(answer)

                st.session_state.messages.append(
                    {"role": "assistant", "content": answer}
                )

            except Exception as error:
                st.error(f"An error occurred: {error}")
