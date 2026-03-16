# 🌿 Leaf Health Detection (Plant Disease Detection)

## 📌 Project Overview

Leaf Health Detection is a simple computer vision project that detects whether a plant leaf is **healthy or possibly diseased** based on the amount of green color present in the leaf image.

The project uses **Python and OpenCV** to process the image, convert it into HSV color space, and calculate the ratio of green pixels. If the green ratio is high, the leaf is considered healthy; otherwise, it may be diseased.

This project demonstrates basic **image processing and plant health analysis using computer vision**.

---

## 🚀 Features

* Image processing using **OpenCV**
* HSV color space conversion
* Green color detection using masking
* Health classification based on green pixel ratio
* Simple and easy-to-understand algorithm

---

## 🛠️ Technologies Used

* Python
* OpenCV
* NumPy

---

## 📂 Project Structure

```
Leaf-Health-Detection
│
├── LeafDetection.py      # Main Python script
├── leaf1.jpeg            # Sample leaf image
├── README.md             # Project documentation
```

---

## ⚙️ Installation

1️⃣ Clone the repository

```
git clone https://github.com/your-username/Leaf-Health-Detection.git
```

2️⃣ Navigate to the project folder

```
cd Leaf-Health-Detection
```

3️⃣ Install required libraries

```
pip install opencv-python numpy
```

---

## ▶️ How to Run the Project

Run the Python script:

```
python LeafDetection.py
```

The program will:

* Load the leaf image
* Detect green areas
* Calculate the green ratio
* Display whether the leaf is **Healthy 🌿 or Diseased 🍂**

---

## 📊 How It Works

1. Load the leaf image using OpenCV
2. Resize the image for consistent processing
3. Convert the image from **BGR to HSV color space**
4. Detect green color using HSV range
5. Calculate the ratio of green pixels
6. Classify the leaf health based on the ratio

---

## 🖼️ Output

The program displays:

* Original Leaf Image
* Green Mask Detection
* Leaf Health Result in the console

Example Output:

```
Green Ratio: 0.65
Leaf is Healthy 🌿
```

---

## 📈 Future Improvements

* Use **CNN with TensorFlow for accurate disease detection**
* Train model on **PlantVillage dataset**
* Add **multiple disease classification**
* Create **web or mobile application**

---

## 👨‍💻 Author

**Ankit Singh**

Data Analytics & Computer Vision Enthusiast
Interested in Machine Learning, Computer Vision, and Data Visualization.

---
