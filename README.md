# Persona Support Agent

## Overview

Persona Support Agent is an AI-powered customer support assistant that combines Persona Detection and Retrieval-Augmented Generation (RAG) to provide context-aware responses.

## Features

* Persona Classification

  * Technical Expert
  * Frustrated User
  * Business Executive
  * General User

* Knowledge Base Retrieval

  * Searches support documents
  * Retrieves relevant information

* AI Response Generation

  * Uses Groq LLM
  * Generates contextual responses

## Project Structure

persona-support-agent/

* data/ (support documents)
* src/

  * config.py
  * classifier.py
  * rag_pipeline.py
  * llm.py
* app.py
* requirements.txt
* README.md

## Installation

1. Create virtual environment

python -m venv venv

2. Activate environment

Windows:

venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

## Run Application

python app.py

## Example Queries

* How do I reset my password?
* What is the refund policy?
* My API token is not working.
* I am frustrated with this service.

## Technologies Used

* Python
* Groq
* RAG
* Sentence Transformers
* VS Code

## Author

Sunil
