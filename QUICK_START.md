# Quick Start Guide

## Prerequisites
- Python 3.8 or higher
- pip package manager

## Installation (3 steps)

### 1. Clone the repository
```bash
git clone https://github.com/vatspratapsingh/NeuroDetect.git
cd NeuroDetect
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Jupyter Notebook
```bash
jupyter notebook
```

## Running the Analysis

### Option 1: Kaggle Dataset (Recommended for beginners)
- Open `notebooks/parkinsons_Disease_detection_Using_Kaggle_Dataset.ipynb`
- Run all cells to see the complete analysis
- Best performance: 87.18% accuracy

### Option 2: Google Dataset (Advanced)
- Open `notebooks/parkinsons_Disease_detection_Using_GOOGLE_Dataset.ipynb`
- Run all cells for comprehensive analysis
- Best performance: 81.87% accuracy

## Expected Results

### Kaggle Dataset Results
- **SVM**: 87.18% accuracy, 86.49% precision, 100% recall
- **KNN**: 87.18% accuracy, 90.91% precision, 93.75% recall

### Google Dataset Results
- **SVM**: 70.72% accuracy, 97.62% precision, 10.68% recall
- **KNN**: 81.87% accuracy, 77.85% precision, 62.24% recall

## Troubleshooting

### Common Issues

1. **Package not found error**
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

2. **Jupyter not found**
   ```bash
   pip install jupyter
   ```

3. **Dataset path issues**
   - Make sure you're running notebooks from the project root directory
   - Update file paths in notebooks if needed

### Getting Help
- Check the main [README.md](README.md) for detailed documentation
- Review [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) for file organization
- Open an issue on GitHub for bugs or questions
