
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
