# Library Management System

This is a Django web application for managing an online library system. Admins can manage books, authors, and borrow records. The application allows admins to add books, authors, and assign books to authors. Additionally, admins can export the library data to an Excel sheet.

## Features

- Add, edit, and delete authors
- Add, edit, and delete books
- Add, edit, and delete borrow records
- Paginated lists of authors, books, and borrow records
- Export data to an Excel file

## Setup Instructions

### Prerequisites

- Python 3.8 or later
- Django 3.2 or later
- pandas and openpyxl libraries for exporting data to Excel

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd library_system

python `venv\Scripts\activate`

install dependencies:
pip install django pandas openpyxl

python manage.py makemigrations
python manage.py migrate


Run server

python manage.py runserver
