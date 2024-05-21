FROM python:3.9

# Set the environment variable PYTHONUNBUFFERED to 1
ENV PYTHONUNBUFFERED 1

# Create a /code directory and make it the working directory
RUN mkdir /code
WORKDIR /code

# Copy the requirements.txt file and install the dependencies
COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . /code/

# Expose the port 8000
EXPOSE 8000

# Run the command python manage.py runserver
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]