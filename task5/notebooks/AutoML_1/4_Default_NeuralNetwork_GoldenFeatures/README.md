# Summary of 4_Default_NeuralNetwork_GoldenFeatures

[<< Go back](../README.md)


## Neural Network
- **n_jobs**: -1
- **dense_1_size**: 32
- **dense_2_size**: 16
- **learning_rate**: 0.05
- **explain_level**: 2

## Validation
 - **validation_type**: split
 - **train_ratio**: 0.75
 - **shuffle**: True
 - **stratify**: True

## Optimized metric
logloss

## Training time

148.0 seconds

## Metric details
|           |    score |     threshold |
|:----------|---------:|--------------:|
| logloss   | 0.236634 | nan           |
| auc       | 0.680723 | nan           |
| f1        | 0.197464 |   0.0975385   |
| accuracy  | 0.551717 |   0.0975385   |
| precision | 0.112555 |   0.0975385   |
| recall    | 1        |   4.59745e-06 |
| mcc       | 0.170441 |   0.0975385   |


## Metric details with threshold from accuracy metric
|           |    score |   threshold |
|:----------|---------:|------------:|
| logloss   | 0.236634 | nan         |
| auc       | 0.680723 | nan         |
| f1        | 0.197464 |   0.0975385 |
| accuracy  | 0.551717 |   0.0975385 |
| precision | 0.112555 |   0.0975385 |
| recall    | 0.803936 |   0.0975385 |
| mcc       | 0.170441 |   0.0975385 |


## Confusion matrix (at threshold=0.097538)
|              |   Predicted as 0 |   Predicted as 1 |
|:-------------|-----------------:|-----------------:|
| Labeled as 0 |            29794 |            26090 |
| Labeled as 1 |              807 |             3309 |

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
