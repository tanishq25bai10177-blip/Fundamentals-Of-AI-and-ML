# 🗑️ AI-Powered Waste Classifier
## 📌 Overview
This project is for the **Bring Your Own Project (BYOP)** capstone of the *Fundamentals of AI and ML* course. It deals with the issue of **waste segregation** in hostels, educational institutions, etc., using **AI/ML concepts** such as supervised learning, clustering, and natural language processing. It classifies the waste items into various types such as Wet, Dry, Recyclable, or Hazardous, depending on whether the image of the waste item is uploaded or the name of the waste item is entered in the system. This can promote the use of sustainable waste management in our environment. 
---
## 🚀 Features
- **Image Classification (Computer Vision)**: Image of waste item uploaded, and the type of waste item is predicted.  
- **Text-Based Classification (NLP)**: Name of the waste item entered, and the type of waste item is classified.  
- **Clustering (Unsupervised Learning)**: Waste items are grouped together in the case of missing labels.  
- **Knowledge Base Search**: Waste items can be searched for in the knowledge base.  
- **Feedback Loop**: The user can provide feedback to improve the model.  
---
## 🛠️ Tech Stack
- Python
- TensorFlow/PyTorch
- scikit-learn
- Flask/Streamlit
- OpenCV/PIL
---
## ⚙️ Installation & Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/ai-waste-classifier.git
   cd ai-waste-classifier
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the application:  
   ```bash
   python src/app.py
   ```
---
## 📖 Usage  
- **Image Input**: Upload a photo of waste → system predicts category.  
- **Text Input**: Type item name (e.g., “banana peel”) → system predicts category.  
- **Knowledge Base**: Search for disposal rules of common items.  
---
## 🎯 Learning Outcomes  
- Applied **supervised learning** for classification.  
- Used **unsupervised learning (clustering)** for grouping unlabeled data.  
- Built a **knowledge representation system** for waste rules.  
- Explored **NLP techniques** for text-based classification.  
- Learned deployment basics with a simple web interface.  
---
## 📜 License  
This project is for educational purposes as part of the *Fundamentals of AI and ML* course.
