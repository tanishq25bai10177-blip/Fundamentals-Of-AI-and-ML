# 🗑️ AI-Powered Waste Classifier  
## 📌 Overview  
This project is part of the **Bring Your Own Project (BYOP)** capstone for the *Fundamentals of AI and ML* course. It addresses the problem of **waste segregation** using a simple rule‑based classifier written entirely in Python.  

The program takes a waste item name as input and predicts its category (**Wet, Dry, Recyclable, Hazardous**) directly in the terminal. No external libraries are required, making it easy to run in any environment. 
---
## 🚀 Features  
- Expanded dataset of common waste items.  
- Direct input/output in the compiler (no web interface).  
- **No prior installation needed** — runs with plain Python.  
- Partial matching support (typing “banana” matches “banana peel”).  
---
## 🛠️ Tech Stack  
- Python (standard library only)  
---
## ⚙️ Setup & Execution  
1. Save the code as `app.py`.  
2. Run the program in your terminal:  
   ```bash
   python app.py
   ```  
---
## 📖 Usage  
1. When prompted, enter a waste item name (e.g., `banana peel`, `battery`, `tin can`).  
2. The program prints the predicted category.  

**Example:**  
```
Enter a waste item name: banana
Predicted Category: wet
```

```
Enter a waste item name: tin can
Predicted Category: recyclable
```

```
Enter a waste item name: expired medicine
Predicted Category: hazardous
```
## 🎯 Learning Outcomes  
- Applied classification concepts using a simple rule‑based approach.  
- Learned how to design a dataset and map items to categories.  
- Demonstrated AI/ML fundamentals without external dependencies.  
