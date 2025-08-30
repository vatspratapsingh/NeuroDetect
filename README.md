# NeuroDetect: Parkinson's Disease Detection using Machine Learning

A machine learning project for early detection of Parkinson's Disease using voice/speech analysis.

## Overview

This project implements multiple ML algorithms to predict Parkinson's disease based on acoustic features extracted from voice recordings. Early detection is crucial for effective treatment.

## Features

- Multiple ML Algorithms: SVM, K-Nearest Neighbors, Random Forest, Decision Trees
- Two Datasets: Kaggle dataset (195 samples) and Google dataset (5,875 samples)
- Comprehensive Analysis: Feature engineering, model comparison, performance metrics
- Real-time Prediction: Ready-to-use prediction pipeline

## Dataset

### Kaggle Dataset (parkinsons dataset 1.csv)
- Size: 195 samples
- Features: 16 acoustic features
- Target: Binary classification (0 = No Parkinson's, 1 = Has Parkinson's)

### Google Dataset (parkinsons dataset 2.csv)
- Size: 5,875 samples
- Features: 16 acoustic features
- Target: Binary classification

## Installation

1. Clone the repository
```bash
git clone https://github.com/vatspratapsingh/NeuroDetect.git
cd NeuroDetect
```

2. Install required packages
```bash
pip install -r requirements.txt
```

3. Launch Jupyter Notebook
```bash
jupyter notebook
```

## Usage

### Running the Analysis

1. Kaggle Dataset Analysis:
```bash
jupyter notebook notebooks/parkinsons_Disease_detection_Using_Kaggle_Dataset.ipynb
```

2. Google Dataset Analysis:
```bash
jupyter notebook notebooks/parkinsons_Disease_detection_Using_GOOGLE_Dataset.ipynb
```

## Results

### Model Performance Summary

| Dataset | Model | Accuracy | Precision | Recall | F1-Score |
|---------|-------|----------|-----------|--------|----------|
| Kaggle | SVM | 87.18% | 86.49% | 100% | 92.75% |
| Kaggle | KNN | 87.18% | 90.91% | 93.75% | 92.31% |
| Google | SVM | 70.72% | 97.62% | 10.68% | 19.25% |
| Google | KNN | 81.87% | 77.85% | 62.24% | 69.18% |

### Key Findings

- Best Performance: K-Nearest Neighbor achieved 81.87% accuracy on Google dataset
- Dataset Impact: Smaller Kaggle dataset showed better overall performance
- Class Imbalance: Google dataset shows significant class imbalance

## Author

**Vats Pratap Singh**
- GitHub: [@vatspratapsingh](https://github.com/vatspratapsingh)
- Project Link: [https://github.com/vatspratapsingh/NeuroDetect](https://github.com/vatspratapsingh/NeuroDetect)

## License

This project is licensed under the MIT License.
