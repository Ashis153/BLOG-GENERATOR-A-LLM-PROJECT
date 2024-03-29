import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers


def getLLamaresponse(input_text, no_words, blog_style, language, tone_style):
    # LLama2 model
    llm = CTransformers(model='Models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                        model_type='llama',
                        config={'max_new_tokens': 256, 'temperature': 0.01})

    # Prompt Template
    template = """
        Write a {tone_style} blog in {language} language for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    prompt = PromptTemplate(input_variables=["tone_style", "language", "blog_style", "input_text", 'no_words'],
                            template=template)

    # Generate the response from the LLama 2 model
    response = llm(prompt.format(tone_style=tone_style, language=language, blog_style=blog_style, input_text=input_text,
                                 no_words=no_words))
    print(response)
    return response


st.set_page_config(
    page_title="Blog Generator",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.sidebar.header("Blog Generator 🚀")

input_text = st.sidebar.text_input("Enter the Blog Topic")

no_words = st.sidebar.text_input('Number of Words')

blog_style = st.sidebar.selectbox('Writing the blog for',
                                  ('Academic Researchers', 'Tech Enthusiasts', 'Everyday Readers'))

language = st.sidebar.selectbox('Language',
                                ('English', 'Spanish', 'French'))

tone_style = st.sidebar.selectbox('Tone/Style',
                                  ('Formal', 'Informal', 'Technical', 'Conversational'))

submit = st.sidebar.button("Generate Your Blog", help="Click to generate the blog")

st.header("Blog Generator 🚀")
col1, col2 = st.columns([3, 7])

with col1:
    st.write("")  # Placeholder to maintain alignment
with col2:
    st.subheader("Blog Topic:")
    st.write(input_text)

st.write("")  # Spacer

## Final response
if submit:
    if input_text.strip() == "" or no_words.strip() == "":
        st.warning("Please fill in all required fields.")
    else:
        response = getLLamaresponse(input_text, no_words, blog_style, language, tone_style)
        st.subheader("Generated Blog:")
        st.write(response)
