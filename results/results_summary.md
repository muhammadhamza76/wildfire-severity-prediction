# Model Comparison Results

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
