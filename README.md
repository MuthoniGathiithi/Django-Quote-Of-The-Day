#  Random Quote Django Web App

This is a simple Django web application that displays a random quote from a database each time the page is loaded. It's designed to be a beginner-friendly project that demonstrates how to work with Django models, views, templates, and URL routing.

##  Features
- Stores quotes (text + author) in a database
- Displays a random quote on each page refresh
- Uses Django's ORM to fetch data
- Clean and minimalist HTML template

##  Tech Stack
- Python
- Django
- SQLite (default Django DB)
- HTML/CSS (basic)

## 📂 Project Structure
```
randomquote_project/
├── manage.py
├── randomquote_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── quotes/
│   ├── migrations/
│   ├── templates/
│   │   └── quote.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
```

##  How It Works
1. **Model Setup:** A `Quote` model is created with `text` and `author` fields.
2. **Admin Panel:** Quotes are added using Django's admin dashboard.
3. **Random Logic:** The view uses `Quote.objects.order_by('?').first()` to fetch a random quote.
4. **Template Rendering:** The quote is passed to `quote.html` and rendered dynamically.
5. **URL Routing:** A path is defined so that `/quote/` loads the random quote view.

##  Getting Started

1. **Clone the repo**  
   ```bash
   git clone https://github.com/yourusername/random-quote-django.git
   cd random-quote-django
   ```

2. **Create virtual environment**  
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install django
   ```

4. **Apply migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**  
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the server**  
   ```bash
   python manage.py runserver
   ```

7. **Add Quotes**  
   Go to `http://127.0.0.1:8000/admin`, log in, and add a few quotes.

8. **View Random Quote**  
   Visit `http://127.0.0.1:8000/quote/` to see a random quote displayed.

##  Example Quote Output
> “The best way to get started is to quit talking and begin doing.”  
> — Walt Disney

##  Optional Ideas
- Add a button to refresh the quote via AJAX
- Schedule daily quote emails
- Create a desktop widget for quotes (future upgrade)

##  License
This project is licensed under the MIT License.

---

Made with ❤️ using Django by MuthoniGathiithi.
