# 🧠 NeuroDetect: AI-Powered Parkinson's Disease Detection

**Advanced machine learning system for early detection of Parkinson's Disease using voice/speech analysis and acoustic biomarkers.**

## 🎯 About NeuroDetect

NeuroDetect is a cutting-edge AI system that leverages machine learning algorithms to analyze voice patterns and detect early signs of Parkinson's Disease. Using advanced acoustic feature extraction and multiple ML models, it provides accurate, non-invasive screening capabilities for neurological disorders.

## 🚀 Key Features

- **Multiple ML Algorithms**: SVM, K-Nearest Neighbors, Random Forest, Decision Trees
- **Two Datasets**: Kaggle dataset (195 samples) and Google dataset (5,875 samples)
- **Comprehensive Analysis**: Feature engineering, model comparison, performance metrics
- **Real-time Prediction**: Ready-to-use prediction pipeline
- **Clinical Applications**: Non-invasive screening tool for healthcare professionals

## 📊 Dataset Information

### 🎯 Kaggle Dataset (parkinsons dataset 1.csv)
- **Size**: 195 samples
- **Features**: 16 acoustic biomarkers
- **Target**: Binary classification (0 = Healthy, 1 = Parkinson's Disease)
- **Use Case**: Research and validation

### 🔬 Google Dataset (parkinsons dataset 2.csv)
- **Size**: 5,875 samples
- **Features**: 16 acoustic biomarkers
- **Target**: Binary classification
- **Use Case**: Production and clinical applications

## 🛠️ Installation

### Quick Setup
```bash
# Clone NeuroDetect
git clone https://github.com/vatspratapsingh/NeuroDetect.git
cd NeuroDetect

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter Notebook
jupyter notebook
```

## 📖 Usage

### Running NeuroDetect Analysis

#### 🎯 For Beginners (Kaggle Dataset)
```bash
jupyter notebook notebooks/parkinsons_Disease_detection_Using_Kaggle_Dataset.ipynb
```

#### 🔬 For Advanced Users (Google Dataset)
```bash
jupyter notebook notebooks/parkinsons_Disease_detection_Using_GOOGLE_Dataset.ipynb
```

## 📈 Performance Results

### 🏆 Model Performance Summary

| Dataset | Model | Accuracy | Precision | Recall | F1-Score |
|---------|-------|----------|-----------|--------|----------|
| 🎯 Kaggle | SVM | **87.18%** | 86.49% | **100%** | 92.75% |
| 🎯 Kaggle | KNN | **87.18%** | **90.91%** | 93.75% | **92.31%** |
| 🔬 Google | SVM | 70.72% | **97.62%** | 10.68% | 19.25% |
| 🔬 Google | KNN | **81.87%** | 77.85% | 62.24% | 69.18% |

### 🔍 Key Findings

- **🏆 Best Performance**: K-Nearest Neighbor achieved **81.87%** accuracy on Google dataset
- **📊 Dataset Impact**: Smaller Kaggle dataset showed better overall performance
- **⚖️ Class Imbalance**: Google dataset shows significant class imbalance affecting model performance
- **🎯 Clinical Relevance**: Models achieve clinically relevant performance for screening applications

## 👨‍💻 Author

**Vats Pratap Singh**
- GitHub: [@vatspratapsingh](https://github.com/vatspratapsingh)
- Project Link: [https://github.com/vatspratapsingh/NeuroDetect](https://github.com/vatspratapsingh/NeuroDetect)

## 📄 License

This project is licensed under the MIT License.

---

⭐ **Star this repository if you find NeuroDetect helpful!**
