# URL--Shortner
Flask-Based URL Shortener – Detailed Explanation
Overview
This project is a simple URL shortener built using Flask for the backend and HTML/CSS/JavaScript for the frontend. It allows users to enter a long URL, which gets shortened using an MD5 hash and stored in a dictionary. The user can then copy, share, or open the shortened URL. When someone accesses the shortened URL, Flask redirects them to the original URL.

How It Works
1. User Input & Shortening Process
The user enters a long URL into the input field on the webpage.
When the user submits the URL, JavaScript sends it to the Flask backend using an HTTP request.
Flask generates a unique short URL by creating an MD5 hash of the original URL.
A dictionary (or a database) stores the mapping of the short URL → original URL.
2. Displaying the Shortened URL
Once the URL is shortened, Flask sends it back to the frontend.
The shortened URL is displayed on the webpage for the user to copy, share, or open.
3. Redirecting to the Original URL
When a user accesses the shortened URL, Flask retrieves the original URL from the dictionary and redirects the user to it.
4. JavaScript Functionality
JavaScript enables actions like:
Copying the shortened URL to the clipboard.
Sharing the shortened URL.
Handling form submission and updating the UI dynamically.
Technologies Used
Flask (Python) – Handles backend logic, hashing, and redirections.
MD5 Hashing – Used to generate unique short URLs.
Dictionary (or Database) – Stores the URL mappings.
HTML/CSS – Builds the frontend interface.
JavaScript – Manages user interactions (copy, share, etc.).
Potential Enhancements
Store shortened URLs in a database (SQLite, PostgreSQL, etc.) instead of a dictionary.
Use a shorter hash function (e.g., Base62 encoding) instead of MD5.
Implement custom short URLs (user-defined).
Add expiration times for shortened links.
Track click analytics for shortened URLs.
