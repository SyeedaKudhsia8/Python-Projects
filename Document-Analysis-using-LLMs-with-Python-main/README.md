
# Document Analysis using LLMs with Python

## Description
This project leverages **Large Language Models (LLMs)** to analyze PDF documents retrieved from Google. It integrates **summarization, question generation, and question answering** using state-of-the-art models from the Hugging Face transformers library. 

### Key Features:
- **Summarization**: Condenses long text documents into concise summaries using `t5-small`.
- **Question Generation**: Automatically generates questions from text passages using `valhalla/t5-base-qg-hl`.
- **Question Answering**: Extracts answers from documents using `deepset/roberta-base-squad2`.

This project is ideal for **automated document analysis, knowledge extraction, and educational applications** where understanding and querying large documents is necessary.

---

## Installation

Clone the repository and install dependencies:
```bash
git clone https://github.com/mauzumshamil/Document-Analysis-LLMs.git
cd Document-Analysis-LLMs
pip install -r requirements.txt
```

Ensure you have Python 3.8+ installed.

---

## Usage

### 1. Load and Analyze a PDF
```python
from pipeline import analyze_document

pdf_path = "path_to_your_pdf.pdf"
summary, questions, answers = analyze_document(pdf_path)
```

### 2. Summarization
```python
from transformers import pipeline
summarizer = pipeline("summarization", model="t5-small")
summary = summarizer(text, max_length=150, min_length=50, do_sample=False)
```

### 3. Question Generation
```python
from transformers import pipeline
qg_pipeline = pipeline("text2text-generation", model="valhalla/t5-base-qg-hl")
questions = qg_pipeline(text)
```

### 4. Question Answering
```python
from transformers import pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")
result = qa_pipeline({"context": text, "question": "What is the main topic?"})
```

---

## Project Structure
```
Document-Analysis-LLMs/
│── data/                   # Sample PDFs
│── models/                 # Pretrained models
│── pipeline.py             # Main processing pipeline
│── requirements.txt        # Dependencies
│── README.md               # Documentation
```

---

## Dependencies
- `transformers`
- `PyMuPDF` (for PDF processing)
- `torch`
- `numpy`
- `pandas`

Install with:
```bash
pip install transformers torch numpy pandas pymupdf
```

---

## About the Author
This project was developed by **Mauzum Shamil**, a Data Scientist passionate about AI, NLP, and automation. Connect with me:

- **GitHub**: [github.com/mauzumshamil](https://github.com/mauzumshamil)
- **LinkedIn**: [linkedin.com/in/mauzum-shamil](http://linkedin.com/in/mauzum-shamil)
- **Portfolio**: [linktr.ee/mauzum_shamil](https://linktr.ee/mauzum_shamil)

For inquiries or collaboration, feel free to reach out!

---

## License
This project is open-source under the MIT License. Contributions are welcome!

