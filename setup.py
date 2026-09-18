import os, subprocess, shutil

BASE = r'C:\Users\Hamza\Documents\fire-pred'
NOTEBOOK_SRC = os.path.join(BASE, 'wildfire-severity-prediction.ipynb')

# Create folders
os.makedirs(os.path.join(BASE, 'notebook'), exist_ok=True)
os.makedirs(os.path.join(BASE, 'results'), exist_ok=True)
os.makedirs(os.path.join(BASE, 'data'), exist_ok=True)
print("Folders created")

# Copy notebook
dest = os.path.join(BASE, 'notebook', 'wildfire_severity_prediction.ipynb')
if os.path.exists(NOTEBOOK_SRC):
    shutil.copy(NOTEBOOK_SRC, dest)
    print("Notebook copied to notebook/")
else:
    print("Notebook not found — add it manually to notebook/ folder")

# README
with open(os.path.join(BASE, 'README.md'), 'w', encoding='utf-8') as f:
    f.write("""
## Feature Selection
No manual feature picking. Three data-driven methods:
1. Mutual Information scoring — rank all 33 features by label correlation
2. VIF redundancy removal — iteratively drop multicollinear features (threshold VIF > 10)
3. SHAP baseline confirmation — keep only features with non-zero contribution

Final feature set: 16 features selected purely by statistical methods.

## Methods
| Step | Technique |
|---|---|
| Missing data | Median imputation |
| Split | Stratified 80/20 random split |
| Cross-validation | StratifiedKFold 5-fold |
| Tuning | Grid Search |
| Models | Logistic Regression, Random Forest, XGBoost, LightGBM |
| Uncertainty | Bootstrap 95% CI (500 iterations) |
| Calibration | Calibration curve + Brier Score |
| Explainability | SHAP beeswarm on best model |

## Results
| Model | AUROC | 95% CI | AUPRC | Brier | F1 |
|---|---|---|---|---|---|
| XGBoost | 0.769 | [0.759, 0.778] | 0.702 | 0.185 | 0.598 |
| LightGBM | 0.766 | [0.757, 0.775] | 0.699 | 0.186 | 0.599 |
| Random Forest | 0.753 | [0.743, 0.763] | 0.671 | 0.195 | 0.591 |
| Logistic Regression | 0.618 | [0.607, 0.628] | 0.476 | 0.239 | 0.363 |

Best model: XGBoost — AUROC 0.769, AUPRC 0.702, Brier 0.185

## Key Finding
Remoteness, fire cause, and state are the strongest predictors of fire severity.
Remote fires receive delayed suppression response and grow disproportionately large
— consistent with wildfire management literature.

## Leakage Prevention
Dropped before modeling: fire_size, fire_size_class, fire_mag (derived from
fire_size), putout_time (known only after fire ends), containment dates (post-event).

## Limitations
- 55k subsample of full 1.88M US fire records
- Weather features are pre-fire period averages not real-time conditions
- Model predicts size class not spread rate or suppression difficulty
- US fires only, 1992-2015

## How to Reproduce
1. Download: kaggle.com/datasets/capcloudcoder/us-wildfire-data-plus-other-attributes
2. Upload to Kaggle as private dataset
3. Open notebook/wildfire_severity_prediction.ipynb in Kaggle and run all cells

## Tools
Python, pandas, scikit-learn, XGBoost, LightGBM, SHAP, matplotlib, statsmodels
""")
print("README.md written")

# Results summary
with open(os.path.join(BASE, 'results', 'results_summary.md'), 'w', encoding='utf-8') as f:
    f.write("""# Model Comparison Results

## Dataset
- Records: 55,367 total
- Train: 44,293 | Test: 11,074
- Large fire rate: 34%
- Features: 16 (selected by MI + VIF + SHAP)

## Final Comparison Table
| Model | AUROC | 95% CI | AUPRC | Brier | Sensitivity | Precision | F1 | Threshold |
|---|---|---|---|---|---|---|---|---|
| XGBoost | 0.769 | [0.759, 0.778] | 0.702 | 0.185 | 0.699 | 0.523 | 0.598 | 0.45 |
| LightGBM | 0.766 | [0.757, 0.775] | 0.699 | 0.186 | 0.698 | 0.525 | 0.599 | 0.45 |
| Random Forest | 0.753 | [0.743, 0.763] | 0.671 | 0.195 | 0.681 | 0.522 | 0.591 | 0.45 |
| Logistic Regression | 0.618 | [0.607, 0.628] | 0.476 | 0.239 | 0.867 | 0.363 | 0.512 | 0.10 |

## Feature Selection Summary
- MI threshold: 0.01
- VIF threshold: 10 (iterative removal)
- SHAP threshold: 0.001 mean absolute SHAP
- Final 16 features: remoteness, stat_cause_descr, state, dstation_m,
  Wind_cont, Temp_cont, Hum_pre_7, wstation_usaf, Hum_cont,
  disc_date_pre, wstation_wban, Prec_pre_30, Vegetation,
  disc_pre_year, Prec_cont, wstation_eyear

## SHAP Top Predictors
1. remoteness — distance from city, proxy for response delay
2. stat_cause_descr — fire cause (lightning fires grow larger)
3. state — regional fire behavior and suppression capacity
4. dstation_m — distance to weather station
5. Wind_cont — wind speed during containment period
""")
print("results/results_summary.md written")

# Gitignore
with open(os.path.join(BASE, '.gitignore'), 'w', encoding='utf-8') as f:
    f.write("""*.csv
*.zip
*.gz
*.sqlite
data/
__pycache__/
*.pyc
.env
.DS_Store
.ipynb_checkpoints/
""")
print(".gitignore written")

# Git
def run(cmd):
    subprocess.run(cmd, shell=True, cwd=BASE)

print("\nRunning git commands...")
run('git init')
run('git add .')
run('git commit -m "Initial commit wildfire severity prediction project"')
run('gh repo create muhammadhamza76/wildfire-severity-prediction --public --source=. --remote=origin --push')

print("\nDone! Live at: https://github.com/muhammadhamza76/wildfire-severity-prediction")