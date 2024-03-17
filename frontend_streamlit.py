import streamlit as st
import requests
from io import BytesIO


BACKEND_URL = "http://localhost:8000"


def main():
    st.title("Question Answering System")

 
    query = st.text_input("Enter your question:")
    document = st.file_uploader("Upload document (txt file):")


    if st.button("Submit"):
        if query and document:
            try:
                # Send query and document to backend
                response = send_query(query, document)
                if "answer" in response:
                    st.success(f"Answer: {response['answer']}")
                elif "error" in response:
                    st.error(response["error"])
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

def send_query(query, document):
    files = {"document": document.getvalue()}
    response = requests.post(f"{BACKEND_URL}/query/?query={query}", files=files)
    return response.json()

# if _name_ == "_main_":
main()
# import streamlit as st
# import requests

# # Corrected backend URL
# # BACKEND_URL = "http://127.0.0.1:8000/docs/quer/"
# BACKEND_URL = "http://127.0.0.1:8000/query/"

# def main():
#     st.title("Document Chatbot System")
    
#     query = st.text_input("Enter your query:")
#     uploaded_file = st.file_uploader("Upload a document", type=['txt', 'pdf'])
    
#     if st.button("Search"):
#         if query and uploaded_file:
#             st.write(f"Searching for: {query}")
#             response = process_query(query, uploaded_file)
#             if response:
#                 st.write("Answer:", response["answer"])
#             else:
#                 st.error("Failed to retrieve answer.")
#         else:
#             st.warning("Please enter a query and upload a document.")

# def process_query(query, document):
#     try:
#         # Print the contents of the uploaded file
#         st.write("Uploaded File Content:", document.getvalue())

#         files = {"document": document.getvalue()}
#         data = {"query": query}

#         # Print the payload being sent to the backend
#         st.write("Sending Payload:", files, data)
#         st.write(files)
#         response = requests.post(f"{BACKEND_URL}", files=files, data={"query":query})
        
#         # Print the response from the backend
#         st.write("Response from Backend:", response.text)

#         if response.status_code == 200:
#             return response.json()
#         else:
#             return None
#     except Exception as e:
#         print("Error:", e)
#         return None

# if __name__ == "__main__":
#     main()
