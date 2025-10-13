# 🎬 moviebucket

A personal movie tracker and review platform. Discover, track, and review your favorite films with a clean, responsive interface powered by real-time movie data.

---

## 🚀 Features

| Feature | Description | Screenshot |
|---------|-------------|------------|
| **Profile Management (CRUD)** | Create, read, update, and delete user profiles with customizable avatars, privacy settings, and public contribution tracking | ![Profile CRUD](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/profilecrud.png) |
| **Review System (CRUD)** | Write, edit, and delete movie reviews with duplicate prevention. View community reviews on movie pages and user profiles | ![Review CRUD](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/reviews.png) |
| **TMDB API Integration** | Real-time movie data from The Movie Database including high-quality posters (w500), comprehensive details (title, synopsis, release date, ratings), and fast accurate search | - |
| **Toast Notifications** | Real-time feedback for user actions with success, error, and info messages in a clean, non-intrusive design | ![Toast 1](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/toasts.png) ![Toast 2](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/toasts2.png) ![Toast 3](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/toasts3.png) |

---

## 📸 Application Screenshots

| Page | Description |
|------|-------------|
| **Homepage** | Browse popular movies with pagination and search functionality |
| **Movie Details** | View comprehensive movie information with user reviews |
| **User Profile** | Manage personal information and view review history |
| **Review Management** | Create, edit, and delete movie reviews |

---

## 🧑‍💻 User Experience

| Aspect | Description |
|--------|-------------|
| **Navigation** | Simple, intuitive interface for easy browsing |
| **Search** | Fast search and filtering powered by TMDB API |
| **Authentication** | Seamless login/logout and profile management |
| **Design** | Clean, modern UI with responsive layout |
| **Integration** | Real-time movie data for up-to-date information |

---

## 📝 User Stories

| Category | User Story | Expected Outcome | Status |
|----------|------------|------------------|--------|
| **Authentication & Profiles** | As a user, I want to register for an account so that I can manage my profile and reviews | Signup flow creates a user account; console email backend used when DEBUG=True | ✅ Pass |
| | As a user, I want to log in and log out so that I can securely access my account | Login/logout works and toasts show on both actions | ✅ Pass |
| | As a user, I want a profile page so that I can share information about myself | Profile page exists; avatar shows placeholder when Cloudinary is not configured | ✅ Pass |
| | As a user, I want to manage my profile privacy settings | Basic profile settings page present; privacy toggles implemented | ✅ Pass |
| **Search & Movie Details** | As a user, I want to search for movies so that I can quickly find ones I'm interested in | Search bar returns results from TMDB API and supports pagination | ✅ Pass |
| | As a user, I want to click on a movie from the search results so that I can view its details | Movie detail pages render with poster, title, synopsis, and reviews | ✅ Pass |
| | As a user, I want to see posters, titles, and descriptions so that I can recognize the movie | Posters use TMDB w500 images and are sized consistently | ✅ Pass |
| **Reviews** | As a user, I want to leave a review on a movie so that I can share my opinion | Users can create reviews; duplicate prevention in place | ✅ Pass |
| | As a user, I want to see other users' reviews so that I can discover what people think before watching | Reviews listed on movie detail pages and user profiles | ✅ Pass |
| | As a user, I want to delete my own reviews so that I can manage my contributions | Users can delete their own reviews; toasts appear on delete | ✅ Pass |
| **Profiles & Community** | As a user, I want to click on a reviewer's username so that I can view their profile | Reviewer username links to profile pages | ✅ Pass |
| | As a user, I want to see another user's public contributions so that I can get recommendations | Public reviews and profile info shown with privacy settings respected | ✅ Pass |
| **Deployment & Reliability** | As a user, I want the site to be live on the web so that I can access it without installing anything | App deploys to Heroku; Tailwind is built and collectstatic runs during build | ✅ Pass |
| | As a developer, I want the app to run with DEBUG=False so that it's production-ready | Settings support DEBUG=False; console email backend switched off in production; SECRET_KEY secured | ✅ Pass |

---

## 🎯 Goals

| Goal | Description |
|------|-------------|
| **Personalized Experience** | Deliver a customized movie tracking platform for each user |
| **User Reviews** | Enable authenticated users to create and manage movie reviews |
| **Data Integrity** | Prevent duplicate reviews per user per movie |
| **Real-time Data** | Integrate live movie information via TMDB API |
| **Responsive Design** | Maintain clean, accessible design across all devices |

### Browser Compatibility

| Browser | Supported |
|---------|-----------|
| Chrome | ✅ Latest |
| Firefox | ✅ Latest |
| Safari | ✅ Latest |
| Edge | ✅ Latest |
| Mobile Browsers | ✅ iOS Safari, Chrome Mobile |

---

## 🎨 Design

### Color Scheme

| Type | Color | Hex Code |
|------|-------|----------|
| Primary (Background) | Slate 950 | `#0f172a` |
| Secondary (Cards) | Slate 800 | `#1e293b` |
| Navbar |  | `#f43098` |
| Accent | Orange 500 | `#f97316` |
| Text Primary | White | `#ffffff` |
| Text Secondary | Slate 400 | `#94a3b8` |

### Typography

| Purpose | Font Family |
|---------|-------------|
| Primary | System UI, -apple-system, sans-serif |
| Headings | Inherit from primary |
| Body Text | Inherit from primary |

### Wireframes

| Page | Wireframe |
|------|-----------|
| **Homepage** | ![Homepage Wireframe](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/wireframe1.png) |
| **Login** | ![Login Wireframe](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/wireframe2.png) |
| **Signup** | ![Signup Wireframe](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/wireframe3.png) |
| **Profile** | ![Profile Page Wireframe](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/wireframe4.png) |

---

## 🗂️ Entity-Relationship Diagram (ERD)

The database structure includes three main entities: **Users**, **Movies**, and **Reviews**

![ERD Diagram](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/erd.png)

---

## 📌 Project Board & Planning

### MoSCoW Prioritization

| Priority | Features |
|----------|----------|
| **Must Have** | Core authentication, movie search, reviews |
| **Should Have** | Profile customization, privacy settings |
| **Could Have** | Advanced filtering, watchlists |
| **Won't Have** | Social features, recommendation engine (v1) |

[View Project Board](https://github.com/users/rachel1davey/projects/7)

![MoSCoW Prioritization](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/noscow.png)

---

## 🏗️ Methodology

| Approach | Description |
|----------|-------------|
| **Agile Development** | Iterative sprints with regular feedback loops |
| **Continuous Testing** | Manual and automated tests for reliability |
| **User-Centered Design** | Focus on intuitive navigation and clean UI |

---

## 🛠️ Technologies Used

### Backend

| Technology | Purpose |
|------------|---------|
| Django 5.2 | Web framework |
| PostgreSQL | Production database |
| SQLite | Local development database |
| Django Allauth | Authentication system |
| Gunicorn | WSGI HTTP server |

### Frontend

| Technology | Purpose |
|------------|---------|
| HTML5 & CSS3 | Structure and styling |
| Tailwind CSS | Utility-first CSS framework |
| DaisyUI | Tailwind component library |
| JavaScript | Interactive features |

### APIs & Services

| Service | Purpose |
|---------|---------|
| TMDB API | Movie data and posters |
| Cloudinary | Image hosting and management |

### Development Tools

| Tool | Purpose |
|------|---------|
| Git & GitHub | Version control |
| Heroku | Deployment platform |
| Node.js & npm | Tailwind CSS compilation |

---

## 🚦 Getting Started

### Prerequisites

| Requirement | Version |
|-------------|---------|
| Python | 3.10+ |
| PostgreSQL | Latest |
| Node.js & npm | Latest |
| TMDB API key | Required |
| Cloudinary account | Optional |

### Local Setup

| Step | Command/Action |
|------|----------------|
| **1. Clone repository** | `git clone https://github.com/rachel1davey/movie_tracker_django.git`<br>`cd movie_tracker_django` |
| **2. Create virtual environment** | `python -m venv venv`<br>`source venv/bin/activate` (Linux/Mac)<br>`venv\Scripts\activate` (Windows) |
| **3. Install Python dependencies** | `pip install -r requirements.txt` |
| **4. Install Node dependencies** | `cd theme/static_src`<br>`npm install`<br>`npm run build`<br>`cd ../..` |
| **5. Set up environment variables** | Create `.env` file with required variables (see below) |
| **6. Run migrations** | `python manage.py migrate` |
| **7. Create superuser** | `python manage.py createsuperuser` (optional) |
| **8. Start development server** | `python manage.py runserver` |
| **9. Visit application** | `http://127.0.0.1:8000` |

### Environment Variables

Create a `.env` file in the root directory:

| Variable | Example Value | Description |
|----------|---------------|-------------|
| `SECRET_KEY` | `your-secret-key-here` | Django secret key |
| `DEBUG` | `True` | Debug mode (False in production) |
| `TMDB_API_KEY` | `your-tmdb-api-key` | TMDB API access key |
| `DATABASE_URL` | `sqlite:///db.sqlite3` | Database connection string |
| `EMAIL_BACKEND` | `django.core.mail.backends.console.EmailBackend` | Email backend configuration |
| `CLOUDINARY_URL` | `cloudinary://...` | Cloudinary configuration (optional) |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Allowed hosts for Django |

### Security Notes

| Setting | Production Value | Development Value |
|---------|------------------|-------------------|
| `DEBUG` | `False` | `True` |
| `SECRET_KEY` | Strong random string (env variable) | Any string (not committed) |
| `ALLOWED_HOSTS` | Your domain(s) | `localhost,127.0.0.1` |
| `CSRF_TRUSTED_ORIGINS` | `https://your-domain.com` | Not required |

---

## 🚀 Deployment

### Heroku Deployment Steps

| Step | Action | Command/Details |
|------|--------|-----------------|
| **1. Prepare requirements** | Ensure all dependencies listed | `pip freeze > requirements.txt` |
| **2. Create Procfile** | Add WSGI configuration | Create file with: `web: gunicorn moviebucket.wsgi` |
| **3. Configure buildpacks** | Set up Node.js and Python | `heroku buildpacks:clear`<br>`heroku buildpacks:add --index 1 heroku/nodejs`<br>`heroku buildpacks:add --index 2 heroku/python` |
| **4. Add post-build script** | Configure Tailwind compilation | Add to `package.json`: `"heroku-postbuild": "cd theme/static_src && npm install && npm run build"` |
| **5. Set environment variables** | Configure production settings | `heroku config:set SECRET_KEY=your-secret-key`<br>`heroku config:set DEBUG=False`<br>`heroku config:set TMDB_API_KEY=your-key`<br>`heroku config:set ALLOWED_HOSTS=your-app.herokuapp.com` |
| **6. Enable collectstatic** | Allow static file collection | `heroku config:unset DISABLE_COLLECTSTATIC` |
| **7. Deploy application** | Push to Heroku | `git push heroku main` |
| **8. Run migrations** | Set up database | `heroku run python manage.py migrate` |
| **9. Verify static files** | Check URLs serve correctly | Visit `/static/css/dist/styles.css` and `/static/js/toasts.js` |

---

## 🧪 Testing

### Manual Testing Coverage

| Test Area | Tests Performed |
|-----------|-----------------|
| **Authentication** | Signup, login, logout flows with validation |
| **Profile Management** | Create, read, update, delete operations |
| **Reviews** | Creation, editing, deletion, duplicate prevention |
| **Movie Search** | Search functionality, pagination, results display |
| **Edge Cases** | Empty fields, invalid data, boundary conditions |
| **Responsive Design** | Testing across mobile, tablet, and desktop devices |

### Validation Results

#### Accessibility - Lighthouse Scores

| Platform | Screenshot |
|----------|------------|
| **Desktop** | ![Lighthouse Desktop](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/lighthousedesktop.png) |
| **Mobile** | ![Lighthouse Mobile](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/lighthousemobile.png) |

#### Code Validation

| Language | Result | Screenshot |
|----------|--------|------------|
| **Python (PEP 8)** | ✅ All files pass PEP 8 standards | ![Python Validation](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/pythontest.png) |
| **HTML (W3C)** | ✅ All templates validated | ![HTML Validation](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/htmlcheck.png) |
| **CSS (W3C)** | ⚠️ Validator doesn't recognize Tailwind utility classes | ![CSS Validation](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/csscheck.png) |

---

## 🚧 Known Issues & Future Enhancements

### Known Issues

| Issue | Status |
|-------|--------|
| CSS Validator warnings for Tailwind utilities | ⚠️ Expected - Tailwind uses custom properties |

### Future Enhancements

| Feature | Priority |
|---------|----------|
| Watchlist functionality | High |
| Movie ratings system | High |
| Advanced search filters | Medium |
| Social features (follow users) | Medium |
| Movie recommendations | Low |
| Export reviews | Low |

---

## 🤖 AI Usage

| Usage Area | Description |
|------------|-------------|
| **User Stories** | AI assisted in generating and structuring user stories |
| **Debugging** | Help with troubleshooting complex issues |
| **Code Generation** | Minimal AI-generated code; core functionality written manually |
| **Deployment** | Cursor Agent used for Heroku deployment troubleshooting |
| **Documentation** | AI helped structure README and documentation |

---

## 🙏 Credits & Acknowledgments

### APIs & Services

| Service | Purpose | Link |
|---------|---------|------|
| TMDB API | Movie data and images | [Documentation](https://www.themoviedb.org/documentation/api) |
| Cloudinary | Image hosting and management | [Website](https://cloudinary.com/) |

### Frameworks & Libraries

| Technology | Purpose | Link |
|------------|---------|------|
| Django | Backend framework guidance | [Documentation](https://docs.djangoproject.com/) |
| Django Allauth | Authentication system | [Documentation](https://django-allauth.readthedocs.io/) |
| Tailwind CSS | CSS framework | [Website](https://tailwindcss.com/) |
| DaisyUI | Component library | [Website](https://daisyui.com/) |

### Resources

| Source | Contribution |
|--------|--------------|
| Code Institute | Project guidance and support |
| Stack Overflow | Community solutions and best practices |
| Django Community | Framework best practices and patterns |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📧 Contact

**Live Application:** [https://moviebucketdjango-03c8d5ee1edd.herokuapp.com/](https://moviebucketdjango-03c8d5ee1edd.herokuapp.com/)

**Repository:** [https://github.com/rachel1davey/movie_tracker_django](https://github.com/rachel1davey/movie_tracker_django)

For questions or feedback, please open an issue on the GitHub repository.

---

*Happy movie tracking! 🍿*
