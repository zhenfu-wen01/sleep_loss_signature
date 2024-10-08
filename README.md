# sleep_loss_signature
This repository contains code and data for the paper: A neural signature of sleep loss in the human brain.

The main folder contains all the notebooks for the main analysis. The order to run the codes:
1. step01_classification_discovery_data.ipynb: conduct cross-validation on the discovery dataset, and further train a model use all data for generalization tests;
2. step02_classification_external_validation.ipynb: apply the trained model to external datasets;
3. step03_estimate_feature_patterns.ipynb: conduct bootstrop test to identify feature patterns significantly contributed to the classification model;
4. step04_plot_feature_patterns.ipynb: plot significant feature patterns.
5. step05_plot_feature_pattern_difference.ipynb: comparing feature patterns of sleep deprivation with other conditions.

The results folder is suppose to save figures generated in the above codes.
The data folder contains related data for the analysis.
To trained model is at /data/trained_model.pkl. It is ready to apply to external data which using the 442 region mask for region definition (included in the data folder). 
The estimated connectivity vectors of different datasets can be found at https://osf.io/ayj72/. Please download the data there to the /data folder to run the codes.

In case of any questions, please contact Zhenfu Wen (zhenfu.wen@uth.tmc.edu).
