import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# 1. Cache the model so it loads only once
@st.cache_resource
def load_model():
    model_name = "microsoft/Phi-3-mini-4k-instruct"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    pipe = pipeline(
        "text-generation",
        model=model_name,
        tokenizer=tokenizer,
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

