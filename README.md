# SymptoCare - AI Medical Specialist Recommendation System

SymptoCare is an intelligent cross-platform application designed to help users identify potential medical conditions based on their symptoms, recommend the appropriate medical specialists, and find nearby healthcare facilities. The platform features an AI-driven symptom checker, a curated directory of doctors and hospitals, an interactive guided health assessment, and a unified authentication system across Web and Android.

## Project Structure

The project consists of three main components:
- **`app frontend/`**: The native Android application (Java/XML).
- **`Web frontend/`**: The React web application (Vite/TailwindCSS).
- **`backend/`**: The Python Flask API powering the AI symptom checker, authentication, and data endpoints.

---

## 1. Backend Setup (Flask API)

The backend is built with Python and Flask, utilizing scikit-learn for the Random Forest classification model, and SQLite for unified authentication and user data.

### Requirements
- Python 3.8+
- pip

### Installation & Execution

1. **Navigate to the backend directory:**
   ```bash
   cd backend
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask server:**
   ```bash
   python app.py
   ```
   *The server will start on `http://0.0.0.0:5000`. On the first run, the ML model will train automatically based on the dataset (takes ~2-5 seconds).*

---

## 2. Web Frontend Setup (React)

The web frontend provides a premium, responsive dashboard for users to sign up, log in, and access their health tools.

### Requirements
- Node.js (v18+)
- npm

### Installation & Execution

1. **Navigate to the Web frontend directory:**
   ```bash
   cd "Web frontend"
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Run the development server:**
   ```bash
   npm run dev
   ```
   *The web app will be accessible at `http://localhost:5173`. Make sure the Flask backend is also running.*

---

## 3. Android Frontend Setup (Java)

The native Android application provides the on-the-go experience. It communicates with the same Flask API as the web app for a unified account experience.

### Requirements
- Android Studio (Electric Eel or newer recommended)
- Java 8 or Java 11
- Android SDK (API 34)

### Installation & Execution

1. **Open the Project:**
   - Launch Android Studio.
   - Select **Open** and choose the `app frontend` folder from the root of this project.

2. **Sync Gradle:**
   - Allow Android Studio to sync the Gradle files and download necessary dependencies.

3. **Configure Backend URL (Critical for physical devices):**
   - Open `app/src/main/java/com/simats/symptocareappfrontend/api/ApiClient.java`.
   - Update the `BASE_URL` to point to your backend. 
   - **For Emulator**: Use `http://10.0.2.2:5000/api/`
   - **For Physical USB Device (Recommended)**: Use `https://your-localtunnel-url.loca.lt/api/` (using a tool like `npx localtunnel --port 5000`) or configure ADB reverse port forwarding.

4. **Run the App:**
   - Click the green **Run** button (`Shift + F10`) to compile and install the application on your emulator or connected physical device.

---

## Features
* **Unified Authentication**: Accounts created on the Web or Android App instantly sync via the common Flask backend.
* **AI Symptom Checker**: Text or icon-based symptom input to predict potential diseases.
* **Specialist Recommendation**: Automatically maps predicted diseases to the appropriate medical specialist.
* **Doctor & Hospital Directories**: Browse, filter, and search through curated lists of healthcare providers.
* **Guided Body Scan**: Interactive assessment flow tailored to specific body areas (e.g., Digestive, Heart, Skin).
* **Health Articles & Wellness Check-in**: Integrated daily mood tracker and health education.
