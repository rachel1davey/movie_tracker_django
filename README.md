# 🎬 moviebucket

A personal movie tracker and review platform. Discover, track, and review your favorite films with a clean, responsive interface.

---

## 🚀 Features


---

## 🧑‍💻 User Experience

- Simple, intuitive navigation.
- Fast search and filtering.
- Seamless authentication and profile management.
- Clean, modern UI.

---

### 📝  User Stories

| Category                     | User Story | Expected outcome | Pass / Fail |
|------------------------------|------------|------------------|-------------|
| **Authentication & Profiles** | As a user, I want to register for an account so that I can manage my profile and reviews. | Signup flows create a user account; console email backend used when DEBUG=True (no SMTP required). | Pass |
|                              | As a user, I want to log in and log out so that I can securely access my account. | Login/logout works and toasts show on both actions. | Pass |
|                              | As a user, I want a profile page so that I can share information about myself. | Profile page exists; avatar shows placeholder when Cloudinary is not configured. | Pass |
|                              | As a user, I want to manage my profile privacy settings. | Basic profile settings page present; privacy toggles depend on implementation. | Pass |
| **Search & Movie Details**    | As a user, I want to search for movies so that I can quickly find ones I’m interested in. | Search bar returns results and supports pagination. | Pass |
|                              | As a user, I want to click on a movie from the search results so that I can view its details. | Movie detail pages render with poster, title, synopsis, and reviews. | Pass |
|                              | As a user, I want to see posters, titles, and descriptions so that I can recognize the movie. | Posters use TMDb `w500` images and are sized consistently. | Pass |
| **Reviews**                  | As a user, I want to leave a review on a movie so that I can share my opinion. | Users can create reviews; duplicate prevention in place. | Pass |
|                              | As a user, I want to see other users’ reviews so that I can discover what people think before watching. | Reviews listed on movie detail pages and user profiles. | Pass |
|                              | As a user, I want to delete my own reviews so that I can manage my contributions. | Users can delete their own reviews; toasts appear on delete. | Pass |
| **Profiles & Community**     | As a user, I want to click on a reviewer’s username so that I can view their profile. | Reviewer username links to profile pages. | Pass |
|                              | As a user, I want to see another user's public contributions so that I can get recommendations. | Public reviews and profile info shown; some privacy settings may be partial. | Pass |
| **Deployment & Reliability** | As a user, I want the site to be live on the web so that I can access it without installing anything. | App deploys to Heroku; ensure Tailwind is built and `collectstatic` runs during build. | Pass |
|                              | As a developer, I want the app to run with `DEBUG=False` so that it’s production-ready. | Settings support DEBUG=False and console email backend switched off in production; ensure SECRET_KEY present. | Pass |

---

## 🎯 Goals

- Deliver a personalized movie tracking experience.
- Enable authenticated users to review and manage movies.
- Prevent duplicate reviews.
- Maintain a clean, responsive design.

---

## 🎨 Design

**Color Scheme**
- Primary: `#1e293b`
- Secondary: `#64748b`
- Accent: `#fbbf24`

**Typography**
- Main font: Inter
- Secondary font: Roboto

**Wireframes**
- [Homepage Wireframe](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/wireframe1.png)
- [Login Wireframe] (https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/wireframe2.png)
- [Signup Wireframe] (https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/wireframe3.png)
- [Profile Page Wireframe](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/wireframe4.png)

---

## 🗂️ Entity-Relationship Diagram (ERD)

Entities: **Users**, **Movies**, **Reviews**

![ERD Diagram](https://github.com/rachel1davey/movie_tracker_django/blob/main/assets/readme/erd.png)

---

## 📌 Project Board & Planning

- Add a public GitHub Project board and paste the link here (e.g. https://github.com/<you>/<repo>/projects/1)
- Make sure your board has at least three columns (To do / In progress / Done).
- Map user stories to cards and label priorities with MoSCoW (Must, Should, Could, Won't).

Project board link: [[PROJECT BOARD LINK](https://github.com/users/rachel1davey/projects/7)]

## � User Experience & Screenshots

- Document main user journeys (signup → profile → review; login → search → review actions).
- Add screenshots (place in `docs/screenshots/`):
    - `docs/screenshots/homepage.png`
    - `docs/screenshots/profile.png`
    - `docs/screenshots/movie_detail.png`


## �🏗️ Methodology

- **Agile Development:** Iterative sprints with regular feedback.
- **Continuous Testing:** Manual and automated tests for reliability.

---

## 🛠️ Technologies Used

- **Backend:** Django 5.2
- **Database:** PostgreSQL (Production), SQLite (Local)
- **Frontend:** HTML, CSS, Tailwind CSS, DaisyUI
- **Authentication:** Django Allauth
- **API:** TMDb API

---

## 🚦 Getting Started

### Local Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/moviebucket.git
    cd moviebucket
    ```
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run migrations and start the server:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

### Deployment

- [Add deployment instructions here, e.g., Heroku, Vercel, etc.]

### Heroku (Tailwind) notes

If you deploy to Heroku and use the Tailwind build pipeline, make sure the compiled CSS is produced during slug compilation so `collectstatic` can include it. Two common approaches:

1) Multi-buildpack (recommended)

    - Add the Node.js buildpack before the Python buildpack so npm runs first and outputs compiled CSS into `theme/static/css/dist`:

        ```bash
        heroku buildpacks:clear
        heroku buildpacks:add --index 1 heroku/nodejs
        heroku buildpacks:add --index 2 heroku/python
        ```

    - In `theme/static_src/package.json` ensure `build` script runs PostCSS/Tailwind and writes to `../static/css/dist/styles.css` (this repo already includes that script).

    - Add a `heroku-postbuild` script in the root `package.json` (or in the theme package.json) to run the Tailwind build during slug compile.

2) Pre-build locally and commit compiled assets (quick, less ideal)

    - Run `npm run build` in `theme/static_src` locally and commit the generated `theme/static/css/dist/styles.css` to the repository. This avoids needing Node in the Heroku build but increases repo size and maintenance burden.

3) Ensure `collectstatic` runs during build

    - If you previously disabled collectstatic on Heroku, unset that setting:

        ```bash
        heroku config:unset DISABLE_COLLECTSTATIC
        ```

After deployment, verify these URLs on your live site return the correct content-type (not HTML):

- `/static/css/dist/styles.css` — should return text/css
- `/static/js/toasts.js` — should return application/javascript

If you want, I can add a small `heroku-postbuild` script example or commit the compiled CSS for you.

### Environment & Deployment notes

- Create a `.env` file for local development (do NOT commit it). Add a `.env.example` to the repo with placeholders.
- Required environment variables (example):
    - SECRET_KEY=your-secret-key
    - DEBUG=True
    - TMDB_API_KEY=your-tmdb-api-key
    - DATABASE_URL=sqlite:///db.sqlite3 (or your production DB URL)
    - EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend

- For production:
    - Set `DEBUG=False` and ensure a secure `SECRET_KEY` is set through environment variables.
    - Configure database and static/media storage (Postgres, Cloudinary, etc.)
    - Collect static files and use a WSGI server like Gunicorn.


---

## 🧪 Testing

- Manual and automated unit tests.
-- Edge case validation for reviews.
- Responsive UI testing across devices.

### Quick manual testing checklist

- Register a new user and confirm signup toast shows.
- Log in and out, confirm toasts show for both actions.
- Create, edit, delete a review and confirm toasts and UI changes for each.
- Try to edit/delete a review while logged out and confirm you are blocked.

### Accessibility & Validation

- Run Lighthouse (Chrome DevTools) and address any critical accessibility/performance issues.
- Validate HTML using the Nu HTML Checker (v.Nu) on the main pages.


---

## 🤖 AI Usage

- AI assisted in generating user stories and debugging.
- Minimal AI-generated code.
- Cursor Agent used for Heroku deployment troubleshooting.

---

## 🙏 Credits

- [TMDb API](https://www.themoviedb.org/documentation/api) for movie data.
- [Django Documentation](https://docs.djangoproject.com/) for backend guidance.
- [Tailwind CSS](https://tailwindcss.com/) and [DaisyUI](https://daisyui.com/) for frontend styling.

---

## 📄 License

[MIT License](LICENSE)

---

*Happy movie tracking!*

---


