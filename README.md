                                                          # Hematology NLP Simplifier  

 Hematology NLP Simplifier
A Streamlit + HuggingFace application for simplifying complex hematology lab reports into clear, patient‑friendly language.

 Introduction
        Hematology lab reports are often filled with dense medical terminology that can be difficult for patients, students, and even non‑specialist clinicians to interpret. This project leverages Natural Language Processing (NLP) to transform complex hematology text into simplified, accessible explanations. The goal is to support patient education, clinical communication, and healthcare literacy using modern, open‑source AI tools.

Problem Statement

         Patients frequently receive hematology reports that contain technical jargon, abbreviations, and clinical markers that are not intuitive. This creates barriers to understanding their own health information, leading to confusion, anxiety, and misinterpretation.
Healthcare providers also face challenges when explaining results quickly and clearly.

There is a need for an automated, reliable, and user‑friendly tool that can simplify hematology text without losing clinical meaning.

   Objectives of the Study
This project aims to:

          Develop an NLP‑powered tool that simplifies hematology lab reports into plain language.

          Provide a Streamlit interface for real‑time text simplification.

          Support batch processing for CSV datasets.

          Demonstrate the use of lightweight, open‑source HuggingFace models for clinical NLP tasks.

          Improve accessibility and understanding of medical information for non‑experts.

   Methodology & Technologies Used
Methodology

          Collect sample hematology report text.

          Preprocess and clean input text.

          Use transformer‑based NLP models to generate simplified summaries.

          Evaluate clarity, readability, and preservation of meaning.

          Deploy the application using Streamlit and HuggingFace Spaces.

Technologies  
          Python 3.10+

          Streamlit for the interactive UI

          HuggingFace Transformers for NLP inference

          Lightweight LLMs (Phi‑3 Mini, DistilGPT‑2, or similar)

          Pandas for CSV handling

          Docker / HuggingFace Spaces for deployment

          GitHub for version control and project management

 Models That May Be Applied
 This project is designed to work with small, efficient, open‑source models such as:

         Phi‑3 Mini (HuggingFace version)
 
         Flan‑T5 Small / Base

         LLaMA‑based small variants (if supported)

These models are chosen for:

         Fast inference

         Low compute requirements

         Compatibility with free hosting environments

         Strong performance on summarization and simplification tasks

  Results
  
         The application successfully:

          Simplifies hematology text into clear, readable summaries.

          Preserves clinical meaning while reducing complexity.

          Handles both single‑text input and batch CSV uploads.

          Runs efficiently on CPU‑only environments.

          Provides a clean, intuitive interface for users.

          Users can instantly see the difference between the original and simplified text, improving comprehension and accessibility.

   Lessons Learned

          Lightweight models can perform surprisingly well for clinical text simplification.

          Streamlit provides a fast, flexible way to build interactive NLP apps.

          HuggingFace Spaces is an excellent platform for free deployment, though it requires careful packaging of dependencies.

          Clean repo structure and .gitignore rules are essential for smooth deployment.

           Simplification must balance readability with clinical accuracy — too much simplification can distort meaning.
           
   Conclusion
   
         The Hematology NLP Simplifier demonstrates how modern NLP can make medical information more accessible. By combining open‑source models, a simple UI, and cloud deployment, this project provides a practical tool for patients, students, and healthcare teams. It also serves as a strong portfolio example of applied NLP, model integration, and full‑stack deployment.

This project contains a Streamlit app that simplifies hematology lab reports using an AI model.

#  Structure
- app.py: Main Streamlit application
- requirements.txt: Dependencies for deployment
- sample_data/: Example datasets
