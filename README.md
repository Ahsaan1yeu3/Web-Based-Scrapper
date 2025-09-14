# Website-Based-Scrapper

Website-Based-Scrapper
🔗 Link Collector - Django Website Scraper
A simple Django project to scrape all links (<a> tags) from any website and store them in a database.
It also provides a clean Bootstrap UI for viewing and managing the collected links.

🚀 Features
Enter any website URL and scrape all links.
Save scraped links (text + address) into a database.
Display saved links in a responsive Bootstrap table.
Option to delete all saved links with a single click.
Built with Django, BeautifulSoup4, and Bootstrap 4.


🛠️ Tech Stack
Backend: Django 5.x
Frontend: HTML, Bootstrap 4
Scraping: BeautifulSoup4, Requests
Database: SQLite

#📂 Project Structure
#mysite/ │ ├── myapp/ │ ├── migrations/ │ ├── templates/ │ │ └── myapp/ │ │ └── result.html # UI for displaying links
│ ├── models.py # Link model (id, name, address) │ ├── views.py # Scraping + rendering logic │ ├── urls.py # App routes 
│ ├── mysite/ │ ├── settings.py │ ├── urls.py │ └── manage.py


