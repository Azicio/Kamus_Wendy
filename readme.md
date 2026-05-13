
```markdown
# ⚖️ Kamus Saku Pemasyarakatan

**An Indonesian–English correctional‑services glossary, built by a translator intern and a systems‑minded developer.**

[![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.57-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Status](https://img.shields.io/badge/status-production-success)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()

> “Ini adalah edisi pertama Kamus Pemasyarakatan bahasa Indonesia – Inggris yang dibuat oleh Wendy Nahaklay selaku peserta magang di bidang Penerjemah.”

---

## 🧠 Overview

**Kamus Saku Pemasyarakatan** (Correctional Pocket Dictionary) is a mobile‑first, searchable glossary of over 120 specialized Indonesian terms used in prisons, probation offices, and legal contexts, each paired with its English equivalent and a concise legal definition.

Built as a standalone web application with **Streamlit**, it serves as a daily reference tool for translators, correctional officers, and legal interns. The app can also be updated directly by its users — no coding required.

👉 **[Live Demo](https://your-streamlit-url.streamlit.app/)** *(replace with your actual URL after deployment)*

---

## ✨ Key Features

- 🔍 **Instant search** – Type in Indonesian or English to find terms immediately.
- 📚 **Browse by category** – Nine logical sections covering everything from institutional structure to security procedures.
- 📖 **Full definitions** – Each term includes a legally drafted explanatory paragraph, sourced from real‑world documents.
- ➕ **Add new terms** – A built‑in form allows non‑developers to expand the dictionary; changes are saved directly to the JSON database.
- 🎨 **Professional UI** – A clean, dark‑blue theme that looks equally good on a desktop, tablet, or mobile phone.
- 📁 **Portable data** – All glossary data lives in a single `kamus_pemasyarakatan.json` file, making it easy to share, version‑control, or repurpose.

---

## 📸 Screenshots

| Home & Search | Browse by Category |
|---------------|---------------------|
| ![Search](screenshots/search.png) | ![Browse](screenshots/browse.png) |

| Add New Term |
|--------------|
| ![Add](screenshots/add.png) |

*(Add your own screenshots to a `screenshots/` folder and update these paths.)*

---

## 🗂️ Data Structure

The entire dictionary is stored in a single JSON file (`kamus_pemasyarakatan.json`) with the following structure:

```json
{
  "A. Struktur & Kelembagaan": [
    ["Balai Pemasyarakatan (Bapas)", "Probation Office", "Unit pelaksana teknis..."],
    ...
  ],
  "B. Status & Subjek Hukum": [...]
}
```

Each entry is a list of three strings:
[Indonesian term, English translation, Legal definition]

Categories can be added, renamed, or removed by editing the JSON file — or by using the in‑app form.

---

🧰 Tech Stack

· Frontend / Web app: Streamlit
· Backend logic: Python (dictionary loading, saving, search)
· Data storage: JSON (no database required)
· Custom styling: Injected CSS for a professional correctional‑themed look

---

🚀 Getting Started

Option 1: Run locally (Pydroid 3 or Terminal)

1. Clone this repository or copy the files to your device.
2. Make sure kamus_pemasyarakatan.json is in the same folder as Kamus_Wendy.py.
3. Install Streamlit:
   ```bash
   pip install streamlit
   ```
4. Run the app:
   ```bash
   streamlit run Kamus_Wendy.py
   ```

Option 2: Deploy to Streamlit Cloud

1. Fork this repository to your GitHub account.
2. Go to share.streamlit.io, link your GitHub, and select the repository.
3. Set the main file path as Kamus_Wendy.py.
4. Click Deploy — your app will be live in under a minute.

No secrets or environment variables are required.

---

🧩 How This Project Was Built

The Kamus Wendy began as a module inside Azicio’s Tech Lab, a personal dashboard for heavy‑machinery operations. After refining the glossary engine — search, collapsible categories, and JSON persistence — it was extracted into its own standalone app.

The project was a collaboration between:

· Wendy Nahaklay – Translator Intern, domain expert who curated and proofread all terms.
· Azicio – Lead Operator & Systems Designer, who engineered the “Box Strategy” architecture and connected the user interface to the data.
· Gemini (Google) – AI architect that designed the initial Streamlit structure and UI layout.
· Seek / DeepSeek – Debugger specialist who hardened the data pipeline, merged duplicate categories, and cleaned the glossary for production.

---

📖 Portfolio Value

If you're a recruiter, fellow developer, or a public‑service innovator viewing this, here’s what the project demonstrates:

· Real‑world problem solving – Built for an actual translation internship in the correctional service.
· Clean, maintainable code – A single Python file + one JSON data source; minimal dependencies.
· User‑friendly design – No training required; a complete novice can search or add terms.
· Scalability – The same engine can be repurposed for any bilingual glossary (law, medicine, ecology) by simply swapping the JSON.

---

📬 Contact

Created by Azicio and Wendy Nahaklay.
For questions, suggestions, or collaboration, reach out through GitHub.

---

Built with endurance in the cab, curiosity in the command line, and a passion for language in the field.

```
