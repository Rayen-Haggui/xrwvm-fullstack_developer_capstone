# Best Cars Dealership - Full Stack Web Application

## Repository
**Repository Name:** xrwvm-fullstack_developer_capstone

## Project Name
**Best Cars Dealership**

## Project Overview
Best Cars Dealership is a full-stack web application that allows users to browse car dealerships across the United States, read customer reviews, and submit their own reviews with AI-powered sentiment analysis.

## Tech Stack
- **Backend:** Django (Python)
- **Frontend:** React.js with static HTML pages
- **Database Microservice:** Node.js / Express with MongoDB
- **Sentiment Analysis Microservice:** Python Flask deployed on IBM Code Engine
- **CI/CD:** GitHub Actions

## Features
- Browse and filter car dealerships by state
- User registration and authentication
- View dealer reviews with sentiment indicators
- Submit reviews with purchase and vehicle details
- Admin panel for managing car makes, models, and data
- Automated linting via GitHub Actions

## Setup
```bash
cd server
pip install virtualenv
virtualenv djangoenv
source djangoenv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
