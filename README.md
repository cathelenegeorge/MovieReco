# 🎬 Movie Recommendation System

A **Movie Recommendation System** built using **Streamlit**, **Pandas**, **Scikit-learn**, and **Cosine Similarity** to suggest movies based on genres. The dataset used is `imdb_top_1000.csv`, and posters are fetched directly from the dataset instead of using the OMDb API.

---

## 📌 Features
- Recommends movies based on the selected genre using **cosine similarity**.
- Fetches movie details such as **runtime, IMDb rating, certificate, director, cast, and summary**.
- Displays **movie posters** from the dataset.
- Simple and interactive **Streamlit UI** for easy access.

---

## 🚀 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/movie-recommendation-system.git
cd movie-recommendation-system
```

### 2️⃣ Create a Virtual Environment (Recommended)
```sh
python -m venv env
# Activate virtual environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Application
```sh
streamlit run app.py
```

The application will open in your default browser at **http://localhost:8501/**.

---

## 📂 Project Structure
```
📁 movie-recommendation-system/
├── 📄 app.py                # Main Streamlit app
├── 📂 data/
│   ├── imdb_top_1000.csv   # Movie dataset
├── 📄 requirements.txt      # Dependencies
├── 📄 README.md             # Project documentation
```

---

## 🛠️ Technologies Used
- **Python** 🐍
- **Pandas** 📊
- **Scikit-learn** 🤖
- **Streamlit** 🎨

---

## 📝 Usage Guide
1. **Select a Genre** from the dropdown.
2. Click **Recommend Movies**.
3. Get a list of recommended movies along with details & posters.

---

## 📌 Sample Output
```
🎬 Recommended Movies for Action:
1. The Dark Knight (Runtime: 152 min, IMDb: 9.0, Director: Christopher Nolan)
2. Mad Max: Fury Road (Runtime: 120 min, IMDb: 8.1, Director: George Miller)
...
```

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing
Feel free to fork, modify, and raise **pull requests**! If you find any issues, report them under **Issues**.

---


