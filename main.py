from fastapi import FastAPI, File, UploadFile
from transformers import pipeline
import logging
from transformers import pipeline, AutoTokenizer, AutoModelForQuestionAnswering

app = FastAPI()
# qa_pipeline = pipeline("question-answering")
model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)

model = AutoModelForQuestionAnswering.from_pretrained(model_name)
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
@app.post("/query/")
async def create_item(query: str, document: UploadFile = File(...)):
    try:
        print(1)
        document_text = document.file.read().decode("ISO-8859-1")
        logger.info("Processing query: %s", query)
        result = qa_pipeline(question=query, context=document_text)
        logger.info("Answer retrieved: %s", result["answer"])
        print(1)
        return {"answer": result["answer"]}
    except Exception as e:
        logger.error("Error processing query: %s", e)
        return {"error": "Failed to retrieve answer."}

# from fastapi import FastAPI, File, UploadFile
# from transformers import pipeline

# app = FastAPI()

# qa_pipeline = pipeline("question-answering")

# @app.post("/query/")
# async def process_query(query: str, document: UploadFile = File(...)):
#     try:
#         document_text = document.file.read().decode("utf-8")
#         result = qa_pipeline(question=query, context=document_text)
#         return {"answer": result["answer"]}
#     except Exception as e:
#         print("Error:", e)
#         return {"error": "Failed to retrieve answer."}


