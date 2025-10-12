# 🎬 moviebucket

A personal movie tracker and review platform. Discover, track, and review your favorite films with a clean, responsive interface.

---

## 🚀 Features

- **Browse Movies:** Explore trending and popular titles using the TMDb API.
-- **Reviews:** Write, edit, and view reviews. Duplicate reviews are prevented.
-- **Profile Customization:** Update your avatar and bio. View your reviews.
- **Responsive Design:** Optimized for all devices with Tailwind CSS and DaisyUI.

---

## 🧑‍💻 User Experience

- Simple, intuitive navigation.
- Fast search and filtering.
- Seamless authentication and profile management.
- Clean, modern UI.

---

### 📝  User Stories

| Category                     | User Story |
|------------------------------|------------|
| **Authentication & Profiles** | As a user, I want to register for an account so that I can manage my profile and reviews. |
|                              | As a user, I want to log in and log out so that I can securely access my account. |
|                              | As a user, I want a profile page so that I can share information about myself. |
|                              | As a user, I want to manage my profile privacy settings. |
| **Search & Movie Details**    | As a user, I want to search for movies so that I can quickly find ones I’m interested in. |
|                              | As a user, I want to click on a movie from the search results so that I can view its details. |
|                              | As a user, I want to see posters, titles, and descriptions so that I can recognize the movie. |
| **Saved Movies (removed)**   | Watchlist functionality has been removed from this version. |
| **Reviews**                  | As a user, I want to leave a review on a movie so that I can share my opinion. |
|                              | As a user, I want to see other users’ reviews so that I can discover what people think before watching. |
|                              | As a user, I want to delete my own reviews so that I can manage my contributions. |
| **Profiles & Community**     | As a user, I want to click on a reviewer’s username so that I can view their profile. |
|                              | As a user, I want to see another user's public contributions so that I can get recommendations. |
| **Deployment & Reliability** | As a user, I want the site to be live on the web so that I can access it without installing anything. |
|                              | As a developer, I want the app to run with `DEBUG=False` so that it’s production-ready. |

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
- [Homepage Wireframe](#)
- [Profile Page Wireframe](#)
- [Review Page Wireframe](#)

---

## 🗂️ Entity-Relationship Diagram (ERD)

Entities: **Users**, **Movies**, **Reviews**

![ERD Diagram](#)

---

## 🏗️ Methodology

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

---

## 🧪 Testing

- Manual and automated unit tests.
-- Edge case validation for reviews.
- Responsive UI testing across devices.

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
