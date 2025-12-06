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

## Project structure

- data/ — placeholder CSV files for train/test/sample.
- notebooks/ — minimal Jupyter notebook templates for experiments and literature reproductions.
- src/ — helper utilities (e.g., src/utils.py).
- requirements.txt — Python dependencies.
- README.md — this file.

Happy experimenting! Pull requests and notebook improvements are welcome.
