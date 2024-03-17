# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the frontend and backend files into the container
COPY frontend_streamlit.py /app/
COPY backend_api.py /app/

# Install any needed dependencies specified in requirements.txt for both frontend and backend
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8501 available to the world outside this container (Streamlit default port)
EXPOSE 8501

# Run the Streamlit frontend app when the container launches
CMD ["streamlit", "run", "frontend_streamlit.py"]
