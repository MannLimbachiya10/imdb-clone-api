# IMDB API Clone With DRF

<h3>🔗 Final Project Links (Arranged According To Usage)</h3>

# Install Dependencies

pip install -r requirements.txt

# Create a Superuser

python manage.py createsuperuser

# Migrate the Models

python manage.py makemigrations
python manage.py migrate

# Start the Project

python manage.py runserver

# Usage

<h3>Accessing the Admin Interface</h3>
Navigate to http://127.0.0.1:8000/admin in your web browser and log in using the superuser credentials you created earlier.

<h3>API Documentation</h3>
Access the Swagger documentation at http://127.0.0.1:8000/api/docs/ to explore and test the API endpoints.

<h3>Additional Notes</h3>
Remember, we are using the default SQLite database provided by Django, so no additional database configuration is required.
Make sure to import the Thunder Client collections for easier testing of all API endpoints.

<br>
<b>1. Admin Access</b>

<ul>
    <li>Admin Section: http://127.0.0.1:8000/admin/</li>
</ul>
<br>

<b>2. Accounts</b>

<ul>
    <li>Registration: http://127.0.0.1:8000/account/register/</li>
    <li>Login: http://127.0.0.1:8000/account/login/</li>
    <li>Logout: http://127.0.0.1:8000/account/logout/</li>
</ul>
<br>

<b>3. Stream Platforms</b>

<ul>
    <li>Create Element & Access List: http://127.0.0.1:8000/streamplatforms/</li>
    <li>Access, Update & Destroy Individual Element: http://127.0.0.1:8000/streamplatforms/&lt;int:streamplatform_id&gt;/</li>

</ul>
<br>

<b>4. Watch List</b>

<ul>
    <li>Create & Access List: http://127.0.0.1:8000/watchlist/</li>
    <li>Access, Update & Destroy Individual Element: http://127.0.0.1:8000/watchlist/&lt;int:movie_id&gt;/</li>
</ul>
<br>

<b>5. Reviews</b>

<ul>
    <li>Create Review For Specific Movie: http://127.0.0.1:8000/&lt;int:movie_id&gt;/review-create/</li>
    <li>List Of All Reviews For Specific Movie: http://127.0.0.1:8000/&lt;int:movie_id&gt;/review/</li>
    <li>Access, Update & Destroy Individual Review: http://127.0.0.1:8000/review/&lt;int:review_id&gt;/</li>
</ul>
<br>

<b>6. User Review</b>

<ul>
    <li>Access All Reviews For Specific User: http://127.0.0.1:8000/review/&lt;str:review_user&gt;/</li>
</ul>
<br>
