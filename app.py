import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# 1. Cache the model so it loads only once
@st.cache_resource
def load_model():
    model_name = "microsoft/Phi-3-mini-4k-instruct"
    pipe = pipeline(
        "text-generation",
        model=model_name,
        tokenizer=model_name,
        torch_dtype="auto",
        device_map="auto",
        max_new_tokens=120
    )
    return pipe

# 2. Load the model ONCE
pipe = load_model()

# 3. Your Streamlit UI starts here
st.title("Hematology NLP Simplifier")

user_input = st.text_area("Enter hematology text")

if st.button("Simplify"):
    output = pipe(user_input)[0]["generated_text"]
    st.write(output)





import streamlit as st

st.title("Hematology NLP Simplifier")
st.write("Streamlit app placeholder. Add your model and UI here.")
