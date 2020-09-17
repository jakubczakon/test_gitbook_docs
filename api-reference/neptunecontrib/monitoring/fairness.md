Module neptunecontrib.monitoring.fairness
=========================================

Functions
---------

    
`log_fairness_classification_metrics(y_true, y_pred_class, y_pred_score, sensitive_attributes, favorable_label, unfavorable_label, privileged_groups, unprivileged_groups, experiment=None, prefix='')`
:   Creates fairness metric charts, calculates fairness classification metrics and logs them to Neptune.
    
    Class-based metrics that are logged: 'true_positive_rate_difference','false_positive_rate_difference',
    'false_omission_rate_difference', 'false_discovery_rate_difference', 'error_rate_difference',
    'false_positive_rate_ratio', 'false_negative_rate_ratio', 'false_omission_rate_ratio',
    'false_discovery_rate_ratio', 'error_rate_ratio', 'average_odds_difference', 'disparate_impact',
    'statistical_parity_difference', 'equal_opportunity_difference', 'theil_index',
    'between_group_theil_index', 'between_all_groups_theil_index', 'coefficient_of_variation',
    'between_group_coefficient_of_variation', 'between_all_groups_coefficient_of_variation',
    'generalized_entropy_index', 'between_group_generalized_entropy_index',
    'between_all_groups_generalized_entropy_index'
    
    Charts are logged to the 'metric_by_group' channel: 'confusion matrix', 'TPR', 'TNR', 'FPR', 'FNR', 'PPV', 'NPV',
    'FDR', 'FOR', 'ACC', 'error_rate', 'selection_rate', 'power', 'precision', 'recall',
    'sensitivity', 'specificity'.
    
    Args:
        y_true (array-like, shape (n_samples)): Ground truth (correct) target values.
        y_pred_class (array-like, shape (n_samples)): Class predictions with values 0 or 1.
        y_pred_score (array-like, shape (n_samples)): Class predictions with values from 0 to 1. Default None.
        sensitive_attributes (pandas.DataFrame, shape (n_samples, k)): datafame containing only sensitive columns.
        favorable_label (str or int): label that is favorable, brings positive value to a person being classified.
        unfavorable_label (str or int): label that is unfavorable, brings positive value to a person being classified.
        privileged_groups (dict): dictionary with column names and list of values for those columns that
           belong to the privileged groups.
        unprivileged_groups (dict): dictionary with column names and list of values for those columns that
           belong to the unprivileged groups.
        experiment(`neptune.experiments.Experiment`): Neptune experiment. Default is None.
        prefix(str): Prefix that will be added before metric name when logged to Neptune.
    
    Examples:
        Train the model and make predictions on test.
        Log metrics and performance curves to Neptune::
    
            import neptune
            from neptunecontrib.monitoring.fairness import log_fairness_classification_metrics
    
            neptune.init()
            with neptune.create_experiment():
                log_fairness_classification_metrics(y_true, y_pred_class, y_pred_score, test[['race']],
                                                    favorable_label='granted_parole',
                                                    unfavorable_label='not_granted_parole',
                                                    privileged_groups={'race':['Caucasian']},
                                                    privileged_groups={'race':['African-American','Hispanic]},
                                                    )
    
        Check out this experiment https://ui.neptune.ai/jakub-czakon/model-fairness/e/MOD-92/logs.