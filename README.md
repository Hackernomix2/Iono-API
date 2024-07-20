# Iono-API

Welcome to the Iono-API repository! Iono is a centralized, AI-powered platform designed to guide researchers through their research journey. This repository contains the source code, development history, and supporting materials for the API of the Iono platform.

## Structure

This repository is structured as follows:

- **iono_api/**: Contains the main Django code for the Iono API application.
- **migrations/**: Includes database migration files.
- **settings/**: Contains the Django settings for different environments (development, production).
- **models/**: Contains the Django models representing the database schema.
- **views/**: Includes the views for handling HTTP requests.
- **serializers/**: Contains the serializers for transforming data between models and JSON.
- **urls/**: Defines the URL routing for the API endpoints.
- **tests/**: Includes unit tests for the application.

## Technologies Used

- **Django**: For building the web framework.
- **Django REST framework**: For building the API endpoints.
- **PostgreSQL**: For the database.

## Getting Started

To get started with the Iono-API, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Hackernomix/Iono-API.git
   ```
2. **Navigate to the API Directory**:
   ```bash
   cd Iono-API/iono_api
   ```
3. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Set Up the Database**:
- Configure the PostgreSQL database settings in `settings.py`.
- Apply migrations:
   ```bash
   python manage.py migrate
   ```
7. **Run the Application**:
   ```bash
   python manage.py runserver
   ```
   
## Purpose

The purpose of this repository is to provide a collaborative space for the development and improvement of the Iono platform. By making the repository publicly accessible, we aim to foster community engagement, allowing developers, contributors, and users to explore the codebase, report issues, and suggest enhancements.

## How AI Powers Iono

Iono leverages multiple AI models and technologies to offer a comprehensive research assistance platform. Key features include:

- **Data Collection and Visualization**: Integration with Google Forms to collect and visualize research data.
- **Document Digitization**: OCR technology to digitize physical documents.
- **AI-Driven Conversations**: An interactive AI assistant for meaningful interactions based on research datasets and related academic papers.
- **Real-Time Project Tracking**: Tools to monitor research project progress and milestones in real time.

