# theatre_service

## Overview
Theatre Service is a Django project designed to manage various aspects of a theatre, including actors, genres, theatre halls, plays, performances, and reservations.

## Contents
1. [Pages](#pages)
    - [Home Page](#home-page)
    - [Theatre API](#theatre-api)
    - [User API](#user-api)
    - [Swagger Documentation](#swagger-documentation)
    - [Redoc Documentation](#redoc-documentation)

2. [Instructions for Local Setup](#instructions-for-local-setup)
3. [Environment Configuration](#environment-configuration)

## Pages

### Home Page
- URL: `/`
- Description: Main page of the project.

### Theatre API
- URL: `/api/theatre/`
- Description: Endpoint for managing theatre-related data.

### User API
- URL: `/api/user/`
- Description: Endpoint for user-related functionalities like registration and token management.

### Swagger Documentation
- URL: `/api/doc/swagger/`
- Description: Swagger documentation for the API.

### Redoc Documentation
- URL: `/api/doc/redoc/`
- Description: Redoc documentation for the API.

## Instructions for Local Setup
1. Clone the repository: `git clone https://github.com/yourusername/theatre-service.git`
2. Install necessary dependencies: `pip install -r requirements.txt`
3. Start the server: `python manage.py runserver`

## Environment Configuration
- Create a `.env` file based on `env.sample` and enter your secret keys and other settings.