Module neptunecontrib.monitoring.metrics
========================================

Functions
---------

    
`expand_prediction(prediction)`
:   Expands 1D binary prediction for positive class.
    
    Args:
        prediction (array-like, shape (n_samples)):
            Estimated targets as returned by a classifier.
    
    Returns:
        prediction (array-like, shape (n_samples, 2)):
            Estimated targets for both negative and positive class.

    
`log_binary_classification_metrics(y_true, y_pred, threshold=0.5, experiment=None, prefix='')`
:   Creates metric charts and calculates classification metrics and logs them to Neptune.
    
    Class-based metrics that are logged: 'accuracy', 'precision', 'recall', 'f1_score', 'f2_score',
    'matthews_corrcoef', 'cohen_kappa', 'true_positive_rate', 'true_negative_rate', 'positive_predictive_value',
    'negative_predictive_value', 'false_positive_rate', 'false_negative_rate', 'false_discovery_rate'
    For each class-based metric, a curve with metric/threshold is logged to 'metrics_by_threshold' channel.
    
    Losses that are logged: 'brier_loss', 'log_loss'
    
    Other metrics that are logged: 'roc_auc', 'ks_statistic', 'avg_precision'
    
    Curves that are logged: 'roc_auc', 'precision_recall_curve', 'ks_statistic_curve', 'cumulative_gain_curve',
    'lift_curve',
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred (array-like, shape (n_samples, 2)): Predictions for classes 0 and 1 with values from 0 to 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        threshold (float): Threshold that calculates a class for class-based metrics. Default is 0.5.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Log metrics and performance curves to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_binary_classification_metrics
    
            neptune.init()
            with neptune.create_experiment():
                log_binary_classification_metrics(y_test, y_test_pred, threshold=0.5)
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.

    
`log_brier_loss(y_true, y_pred_pos, experiment=None, prefix='')`
:   Calculates and logs brier loss to Neptune.
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred_pos (array-like, shape (n_samples)): Score predictions with values from 0 to 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Logs Brier score to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_brier_loss
    
            neptune.init()
            with neptune.create_experiment():
                log_brier_loss(y_test, y_test_pred[:,1])
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.

    
`log_class_metrics(y_true, y_pred_class, experiment=None, prefix='')`
:   Calculates and logs all class-based metrics to Neptune.
    
    Metrics that are logged: 'accuracy', 'precision', 'recall', 'f1_score', 'f2_score', 'matthews_corrcoef',
    'cohen_kappa', 'true_positive_rate', 'true_negative_rate', 'positive_predictive_value',
    'negative_predictive_value', 'false_positive_rate', 'false_negative_rate', 'false_discovery_rate'
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred_class (array-like, shape (n_samples)): Class predictions with values 0 or 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Log class metrics to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_class_metrics
    
            neptune.init()
            with neptune.create_experiment():
                log_class_metrics(y_test, y_test_pred[:,1]>0.5)
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.

    
`log_class_metrics_by_threshold(y_true, y_pred_pos, experiment=None, channel_name='metrics_by_threshold', prefix='')`
:   Creates metric/threshold charts for each metric and logs them to Neptune.
    
    Metrics for which charsta re created and logged are: 'accuracy', 'precision', 'recall', 'f1_score', 'f2_score',
    'matthews_corrcoef', 'cohen_kappa', 'true_positive_rate', 'true_negative_rate', 'positive_predictive_value',
    'negative_predictive_value', 'false_positive_rate', 'false_negative_rate', 'false_discovery_rate'
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred_pos (array-like, shape (n_samples)): Score predictions with values from 0 to 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        channel_name(str): name of the neptune channel. Default is 'metrics_by_threshold'.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Logs metric/threshold charts to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_class_metrics_by_threshold
    
            neptune.init()
            with neptune.create_experiment():
                log_class_metrics_by_threshold(y_test, y_test_pred[:,1])
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.

    
`log_classification_report(y_true, y_pred_class, experiment=None, channel_name='metric_charts', prefix='')`
:   Creates a figure with classifiction report table and logs it in Neptune.
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred_class (array-like, shape (n_samples)): Class predictions with values 0 or 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        channel_name(str): name of the neptune channel. Default is 'metric_charts'.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Log classification report to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_classification_report
    
            neptune.init()
            with neptune.create_experiment():
                log_classification_report(y_test, y_test_pred[:,1]>0.5)
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.

    
`log_confusion_matrix(y_true, y_pred_class, experiment=None, channel_name='metric_charts', prefix='')`
:   Creates a confusion matrix figure and logs it in Neptune.
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred_class (array-like, shape (n_samples)): Class predictions with values 0 or 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        channel_name(str): name of the neptune channel. Default is 'metric_charts'.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Log confusion matrix to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_confusion_matrix
    
            neptune.init()
            with neptune.create_experiment():
                log_confusion_matrix(y_test, y_test_pred[:,1]>0.5)
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.

    
`log_cumulative_gain(y_true, y_pred, experiment=None, channel_name='metric_charts', prefix='')`
:   Creates cumulative gain chart and logs it to Neptune.
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred (array-like, shape (n_samples, 2)): Predictions for classes 0 and 1 with values from 0 to 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        channel_name(str): name of the neptune channel. Default is 'metric_charts'.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Create and log cumulative gain chart to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_cumulative_gain
    
            neptune.init()
            with neptune.create_experiment():
                log_cumulative_gain(y_test, y_test_pred)
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.

    
`log_ks_statistic(y_true, y_pred, experiment=None, channel_name='metric_charts', prefix='')`
:   Creates and logs KS statistics curve and KS statistics score to Neptune.
    
    Kolmogorov-Smirnov statistics chart can be calculated for true positive rates (TPR) and true negative rates (TNR)
    for each threshold and plotted on a chart.
    The maximum distance from TPR to TNR can be treated as performance metric.
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred (array-like, shape (n_samples, 2)): Predictions for classes 0 and 1 with values from 0 to 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        channel_name(str): name of the neptune channel. Default is 'metric_charts'.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Create and log KS statistics curve and KS statistics score to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_ks_statistic
    
            neptune.init()
            with neptune.create_experiment():
                log_ks_statistic(y_test, y_test_pred)
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.

    
`log_lift_curve(y_true, y_pred, experiment=None, channel_name='metric_charts', prefix='')`
:   Creates cumulative gain chart and logs it to Neptune.
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred (array-like, shape (n_samples, 2)): Predictions for classes 0 and 1 with values from 0 to 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        channel_name(str): name of the neptune channel. Default is 'metric_charts'.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Create and log lift curve chart to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_lift_curve
    
            neptune.init()
            with neptune.create_experiment():
                log_lift_curve(y_test, y_test_pred)
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.

    
`log_log_loss(y_true, y_pred, experiment=None, prefix='')`
:   Creates and logs Precision Recall curve and Average precision score to Neptune.
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred (array-like, shape (n_samples, 2)): Predictions for classes 0 and 1 with values from 0 to 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Logs log-loss to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_log_loss
    
            neptune.init()
            with neptune.create_experiment():
                log_log_loss(y_test, y_test_pred)
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.

    
`log_precision_recall_auc(y_true, y_pred, experiment=None, channel_name='metric_charts', prefix='')`
:   Creates and logs Precision Recall curve and Average precision score to Neptune.
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred (array-like, shape (n_samples, 2)): Predictions for classes 0 and 1 with values from 0 to 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        channel_name(str): name of the neptune channel. Default is 'metric_charts'.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Logs Precision Recall curve and Average precision score to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_precision_recall_auc
    
            neptune.init()
            with neptune.create_experiment():
                log_precision_recall_auc(y_test, y_test_pred)
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.

    
`log_prediction_distribution(y_true, y_pred_pos, experiment=None, channel_name='metric_charts', prefix='')`
:   Generates prediction distribution plot from predictions and true labels.
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred_pos (array-like, shape (n_samples)): Score predictions with values from 0 to 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        channel_name(str): name of the neptune channel. Default is 'metric_charts'.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Plot prediction distribution::
    
            from neptunecontrib.monitoring.metrics import log_prediction_distribution
    
            log_prediction_distribution(y_test, y_test_pred[:, 1])

    
`log_roc_auc(y_true, y_pred, experiment=None, channel_name='metric_charts', prefix='')`
:   Creates and logs ROC AUC curve and ROCAUC score to Neptune.
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred (array-like, shape (n_samples, 2)): Predictions for classes 0 and 1 with values from 0 to 1.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        channel_name(str): name of the neptune channel. Default is 'metric_charts'.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test::
    
            from sklearn.datasets import make_classification
            from sklearn.ensemble import RandomForestClassifier
            from sklearn.model_selection import train_test_split
            from sklearn.metrics import classification_report
    
            X, y = make_classification(n_samples=2000)
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
    
            y_test_pred = model.predict_proba(X_test)
    
        Logs ROCAUC curve and ROCAUC score to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.metrics import log_roc_auc
    
            neptune.init()
            with neptune.create_experiment():
                log_roc_auc(y_test, y_test_pred)
    
        Check out this experiment https://ui.neptune.ai/o/neptune-ai/org/binary-classification-metrics/e/BIN-101/logs.