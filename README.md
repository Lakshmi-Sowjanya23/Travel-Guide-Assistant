# 🌍 Travel Guide Assistant

A lightweight **travel recommendation system** that provides fast, personalized destination suggestions using **compressed destination guides** and **text similarity matching**. Designed for **low latency**, simplicity, and challenge/demo use cases.

---

## 🚀 Features

* 📦 Compressed destination summaries (keyword-based guides)
* 🔍 Personalized recommendations from user input
* 📊 Similarity score-based ranking
* ⚡ Fast response using TF-IDF & cosine similarity
* 🌐 Simple and clean web interface (Streamlit)
* 🧠 No heavy ML models or databases

---

## 🛠️ Tech Stack

* **Python**
* **Pandas**
* **Scikit-learn**
* **Streamlit**

---

## 📁 Project Structure

```
TRAVEL_GUIDE_ASSISTANT/
│
├── data/
│   └── destinations.csv
│
├── requirements.txt
└── travel_recommender.py
```

---

## 📊 Dataset

The system uses **compressed destination guides**, where each destination is represented by a short keyword-based summary instead of long reviews.
This reduces computation and improves response speed.

Example:

```
Goa → Beach nightlife budget water sports
```

---

## ⚙️ Installation & Setup

1. Clone the repository:

```bash
git clone <your-repo-url>
cd travel_guide_assistant
```

2. Create & activate virtual environment (optional but recommended)

3. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run travel_recommender.py
```

Open in browser:

```
http://localhost:8501
```

---

## ✍️ Usage

Enter a travel preference such as:

```
beach calm budget
```

The system returns **top-ranked destinations** along with **similarity scores**.

---

## 🧠 How It Works

1. Destination summaries are vectorized using **TF-IDF**
2. User input is converted into a vector
3. **Cosine similarity** is calculated
4. Destinations are ranked by relevance score
5. Top results are displayed instantly

---

## 🎯 Use Cases

* Travel recommendation demos
* ML / AI mini projects
* Hackathons & coding challenges
* Academic project submissions

---

## ✅ Advantages

* Low latency
* Easy to understand & explain
* Minimal dependencies
* Scalable for more destinations

---

## 📌 Future Enhancements

* Add filters (budget, travel type)
* User profile preferences
* Interactive UI components
* Deployment on cloud platforms

---

