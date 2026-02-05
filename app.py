import streamlit as st
from transformers import TFT5ForConditionalGeneration, AutoTokenizer

# Set page config for a modern look
st.set_page_config(page_title="English to Spanish Translator", page_icon=":speech_balloon:", layout="centered")

# --- Load Model and Tokenizer ---
@st.cache_resource
def load_model():
    model_path = "./my_t5_model"
    model = TFT5ForConditionalGeneration.from_pretrained(model_path)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    return model, tokenizer

model, tokenizer = load_model()

# --- Translation Function ---
def translate_text(text):
    inputs = 'translate English to Spanish: ' + text
    input_ids = tokenizer(inputs, return_tensors='tf').input_ids

    outputs = model.generate(
        input_ids,
        max_length=128,
        num_beams=5,
        early_stopping=True
    )

    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translation

# --- Streamlit UI ---
st.title(" English ➡️ Spanish Translator")
st.markdown("### Powered by a fine-tuned T5 model")

st.write("Enter an English sentence below to get its Spanish translation.")

# Input text area
english_input = st.text_area("Enter English Text Here:", "Hello, how are you today?", height=100)

if st.button("Translate"):
    if english_input:
        with st.spinner('Translating...'):
            spanish_output = translate_text(english_input)
        st.success("Translation Complete!")
        st.markdown("**Spanish Translation:**")
        st.write(f"```\n{spanish_output}\n```")
    else:
        st.warning("Please enter some English text to translate.")

st.markdown("---")
st.info("This translator is based on a T5-base model fine-tuned on an English-Spanish dataset.")
