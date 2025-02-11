# Music Genre Classification using KNN

Team no:-03

Team Details

1.G.V.GUNASEKHAR (TL) 

2.B.SRUJANA

3.M.SAIBABU

4.K.PRUDHVI

5.V.HEMANTHRAJU



## Abstract
A machine learning system that automatically classifies music tracks into different genres using the K-Nearest Neighbors (KNN) algorithm. The system analyzes audio features like tempo, spectral characteristics, and rhythm patterns to categorize songs into genres such as rock, jazz, classical, hip-hop, and more.

## Why This Project?
Music streaming platforms handle millions of tracks, making manual genre classification impractical. This project provides an automated solution that:
- Helps organize large music libraries efficiently
- Enables better music recommendation systems
- Assists in music discovery and playlist generation
- Supports content creators in proper track categorization

## Process
1. Data Collection & Preprocessing
   - Extract audio features using librosa library
   - Convert audio signals into numerical features (MFCCs, spectral centroid, chroma features)
   - Normalize and scale features for consistent processing

2. Model Implementation
   - Split dataset into training and testing sets
   - Apply KNN algorithm with optimal k-value
   - Train model using feature vectors and genre labels

3. Evaluation & Optimization
   - Measure accuracy, precision, and recall
   - Fine-tune hyperparameters
   - Cross-validate results

## Required Technology & Algorithms
- Python 3.x
- Libraries: librosa, scikit-learn, numpy, pandas
- Audio processing techniques: FFT, MFCC extraction
- K-Nearest Neighbors algorithm
- Feature scaling and normalization methods

## Conclusion
The KNN-based music genre classification system provides a reliable solution for automated music categorization. With an accuracy of [X]%, it demonstrates the effectiveness of using audio feature analysis and machine learning for music classification tasks. The system's modular design allows for easy integration into larger music management systems.




 


