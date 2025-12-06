Project: IntroMLCapstone
Author: Qifan Zhao
Date: December 2025

Description:
Machine learning capstone exploring bridge detection using geospatial features.

# IntroMLCapstone

IntroMLCapstone is a small capstone project scaffold for comparing three classical machine learning approaches (linear regression, polynomial regression, random forest) with two literature-inspired implementations for bridge detection and post-disaster infrastructure assessment using remote sensing. The objective is to use synthetic or sample tabular data for quick experimentation, then extend notebooks to work with VHR imagery and deep learning pipelines following the cited papers.

## Running the notebooks

1. Create a Python environment and install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Start JupyterLab / Jupyter Notebook in the repository root:
   ```
   jupyter lab
   ```
   or
   ```
   jupyter notebook
   ```

3. Open the notebooks in the `notebooks/` directory. Each notebook contains minimal template code and comments to guide development:
   - 01_linear_regression.ipynb
   - 02_polynomial_regression.ipynb
   - 03_random_forest.ipynb
   - 04_vhr_holistic_detection.ipynb
   - 05_tiered_disaster_detection.ipynb

4. Replace placeholder CSVs in `data/` with real datasets or extend preprocessing and data-loading pipelines in `src/utils.py`.

## Project Structure Overview

This repository contains all code, data, and documentation required to reproduce the experiments described in the capstone report. The project is organized using best practices for a machine learning pipeline, including modular code, clean notebook organization, and reproducible environment configuration.

IntroMLCapstone/
├── data/
│   ├── bridges_train.csv
│   ├── bridges_test.csv
│   └── features_sample.csv
│
├── notebooks/
│   ├── 01_linear_regression.ipynb
│   ├── 02_random_forest.ipynb
│   ├── 03_polynomial_regression.ipynb
│   ├── 04_bridge_detection_cnn.ipynb
│   └── 05_disaster_damage_pipeline.ipynb
│
├── src/
│   ├── utils.py
│   ├── preprocessing.py
│   └── model_helpers.py
│
├── requirements.txt
├── README.md
└── LICENSE (optional)

## Folder/ File Descriptions

## data folder

Contains training and testing datasets used in the project. These files include geospatially-derived features such as slope, flow accumulation, NLCD land-cover class, population density, and parcel attributes for bridge and non-bridge locations.

bridges_train.csv — labeled training samples (feature vectors with target = 1)

bridges_test.csv — evaluation samples (known private bridge points)

features_sample.csv — synthetic dataset used for notebook development

No raw imagery stored here due to size. Imagery inputs are referenced externally.

## notebooks folder

Each notebook corresponds to a single model experiment, satisfying the course requirement of five files (three classical ML, two from literature).

01_linear_regression.ipynb — baseline regression model

02_random_forest.ipynb — ensemble model with feature importance output

03_polynomial_regression.ipynb — nonlinear regression benchmark

04_bridge_detection_cnn.ipynb — implementation inspired by the “Learning to holistically detect bridges from large-size VHR imagery” paper

05_disaster_damage_pipeline.ipynb — simplified reproduction of “Rapid post-disaster infrastructure damage characterization" workflow

Each notebook loads data, preprocesses features, trains the model, evaluates performance (MSE/MAE), and produces visualizations.

## src folder

Standalone Python modules that support preprocessing, feature engineering, and modeling. These scripts ensure reusability and cleaner notebook code.

utils.py — helper functions to load CSVs, split data, and evaluate metrics

preprocessing.py — functions for normalization, encoding, and feature scaling

model_helpers.py — wrappers around scikit-learn training loops and grid search

Importable in notebooks using:
from src.utils import load_data

## requirements.txt

Lists all Python dependencies required to run the project, including:

numpy

pandas

scikit-learn

matplotlib

seaborn

Install using:
pip install -r requirements.txt

## README.md

You are reading it. Contains:

Project summary

Data sources

File/folder descriptions (this section!)

Instructions for running notebooks

Brief Description of Dataset Features

Paper citations placeholder


## Dataset features (short description)

The tabular placeholders use a small set of engineered features intended for quick prototyping:

- flow_acc: Flow accumulation measure (proxy for water/river influence).
- slope: Local terrain slope (degrees or percent).
- nlcd_class: Land cover class (e.g., National Land Cover Database codes).
- pop_density: Population density in the area.
- road_distance: Distance to nearest major road (meters).
- parcel_value: Estimated parcel or property value (currency).
- bridge: Binary label (0/1) indicating presence of a bridge (included in train/test CSVs).

The sample CSVs are minimal placeholders: fill with real values or link to VHR image pipelines for the literature-based notebooks.

## Papers / citations (placeholders)

- Learning to Holistically Detect Bridges from Large-Size VHR Remote Sensing Imagery (2022). [citation placeholder]
- Rapid Post-Disaster Infrastructure Damage Characterisation Using Remote Sensing and Deep Learning Technologies (2023). [citation placeholder]

Please replace the placeholders above with full bibliographic entries (BibTeX or DOI) when you integrate the actual implementations.

Happy experimenting! Pull requests and notebook improvements are welcome.
