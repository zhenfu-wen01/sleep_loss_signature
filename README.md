# sleep_loss_signature
This repository contains code and data for the paper: A neural signature of sleep deprivation in the human brain.
The codes were tested in a PC with Ubuntu 20.04 OS, Python 3.9.18. 
The key python toolboxes including jupyterlab 4.0.12, scikit-learn 1.4.0, nilearn 0.10.2, pickle 4.0, numpy 1.26.3, pandas 2.2.0, scipy 1.12.0, seaborn 0.13.2, matplotlib 3.8.2. The Anaconda 23.11.0 was used to manage these toolboxes.

The main folder contains all the notebooks for replicating main results. The order to run the codes:
1. step01_classification_discovery_data.ipynb: conduct cross-validation on the discovery dataset, and further train a model use all data for generalization tests;
2. step02_classification_external_validation.ipynb: apply the trained model to external datasets;
3. step03_estimate_feature_patterns.ipynb: conduct bootstrop test to identify feature patterns significantly contributed to the classification model;
4. step04_plot_feature_patterns.ipynb: plot significant feature patterns.
5. step05_plot_feature_pattern_difference.ipynb: comparing feature patterns of sleep deprivation with other conditions.

The data folder contains related data for the analysis.
To trained model is at /data/trained_model.pkl. It is ready to apply to external data which using the 442 region mask for region definition (included in the data folder). 
The estimated connectivity vectors of different datasets can be found at https://osf.io/ayj72/. Please download the data there to the /data folder to run the codes.
A results folder is suppose to save figures generated in the above codes.

In case of any questions, please contact Zhenfu Wen (zhenfu.wen01@gmail.com).
