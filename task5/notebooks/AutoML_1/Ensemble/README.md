# Summary of Ensemble

[<< Go back](../README.md)


## Ensemble structure
| Model                            |   Weight |
|:---------------------------------|---------:|
| 3_Default_Xgboost                |        3 |
| 3_Default_Xgboost_GoldenFeatures |        2 |

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.201486 | nan           |
| auc       | 0.822858 | nan           |
| f1        | 0.347314 |   0.175358    |
| accuracy  | 0.930417 |   0.438295    |
| precision | 0.450751 |   0.438295    |
| recall    | 1        |   0.000620673 |
| mcc       | 0.297133 |   0.145456    |


## Metric details with threshold from accuracy metric
|           |     score |   threshold |
|:----------|----------:|------------:|
| logloss   | 0.201486  |  nan        |
| auc       | 0.822858  |  nan        |
| f1        | 0.114528  |    0.438295 |
| accuracy  | 0.930417  |    0.438295 |
| precision | 0.450751  |    0.438295 |
| recall    | 0.0655977 |    0.438295 |
| mcc       | 0.151817  |    0.438295 |


## Confusion matrix (at threshold=0.438295)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |            55555 |              329 |
| Labeled as 1 |             3846 |              270 |

## Learning curves
![Learning curves](learning_curves.png)
## Confusion Matrix

![Confusion Matrix](confusion_matrix.png)


## Normalized Confusion Matrix

![Normalized Confusion Matrix](confusion_matrix_normalized.png)


## ROC Curve

![ROC Curve](roc_curve.png)


## Kolmogorov-Smirnov Statistic

![Kolmogorov-Smirnov Statistic](ks_statistic.png)


## Precision-Recall Curve

![Precision-Recall Curve](precision_recall_curve.png)


## Calibration Curve

![Calibration Curve](calibration_curve_curve.png)


## Cumulative Gains Curve

![Cumulative Gains Curve](cumulative_gains_curve.png)


## Lift Curve

![Lift Curve](lift_curve.png)



[<< Go back](../README.md)
