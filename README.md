# CheckPawned - Email Breach Checker

A simple, secure, and free web application to check if an email address has been compromised in a data breach. This project uses the **XposedOrNot API** as a free alternative to HaveIBeenPwned.

## 🚀 How It Works

1.  **User Input**: The user enters an email address in the frontend interface.
2.  **Request**: The frontend sends a request to the local Flask backend.
3.  **API Call**: The backend makes a secure HTTP GET request to the **XposedOrNot API**.
4.  **Response Handling**:
    - If the email is **safe** (not found in breaches), the API returns a 404, which the backend translates to a "Safe" message.
    - If the email is **pwned** (found in breaches), the API returns a list of data breaches, which the backend formats and sends to the frontend.
5.  **Display**: The frontend displays a green success message (safe) or a red warning with the list of breaches.

---

## 📂 Project Structure

```
checkpawned/
│
├── backend/                # Server-side code
│   ├── app.py              # Main Flask application
│   ├── pyproject.toml      # UV project configuration and dependencies
│   ├── uv.lock             # Lockfile for reproducible builds
│   ├── .python-version     # Python version used by UV
│   └── .venv/              # Virtual environment managed by UV
│
├── frontend/               # Client-side code
│   ├── index.html          # Main User Interface
│   └── style.css           # Styling
│
└── README.md               # Project Documentation
```

---

## 🛠️ Dependencies

The project uses **uv** for dependency management. The main dependencies are:

*   **Flask**: A lightweight web framework for the backend server.
*   **requests**: To make HTTP calls to the external XposedOrNot API.
*   **flask-cors**: To allow the frontend (running in a browser) to communicate with the backend server (CORS support).
*   **python-dotenv**: To load environment variables (if needed).

---

## 🔗 API Information

The project relies on the **XposedOrNot API v1**.

*   **Base URL**: `https://api.xposedornot.com/v1/`
*   **Endpoint Used**: `/check-email/{email_address}`
    *   **Method**: `GET`
    *   **Auth**: No API Key required (Free).

**Code Location**:
The API call is implemented in `backend/app.py`:
```python
url = f"https://api.xposedornot.com/v1/check-email/{email}"
r = requests.get(url)
```

---

## ⚙️ Setup & Workflow

### 1. Backend Setup (using `uv`)

This project uses [uv](https://github.com/astral-sh/uv) for fast Python package management.

**Navigate to the backend folder:**
```bash
cd backend
```

## 🛠️ Setup & Installation

## Running the Project After Cloning

The backend uses `uv` for ultra-fast Python package management.

1.  Clone Repository
    ```bash
    git clone https://github.com/ayushjy/weather-pr.git
    cd YOUR_REPO_NAME
    ```

2.  Setup Backend Environment
    Navigate to backend folder:
    ```bash
    cd backend
    ```
3.  Recreate the exact environment from project metadata:
    ```bash
    uv sync
    ```
    This installs dependencies based on:
        pyproject.toml
        uv.lock
    and creates a local .venv.

4.  Run the application:
    ```bash
    uv run python main.py
    ```
    The server will start at `http://127.0.0.1:5000`.

### 2. Frontend Usage

1.  Go to the `frontend` folder.
2.  Open `index.html` in your web browser (you can double-click the file).
3.  Enter an email address and click **Check**.

---

## 🐛 Troubleshooting

*   **ModuleNotFoundError**: Run `uv sync` to ensure all dependencies are installed.
*   **Connection Refused**: Make sure the backend is running via `uv run python app.py`.
