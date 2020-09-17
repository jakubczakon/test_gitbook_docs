Module neptunecontrib.api.explainers
====================================

Functions
---------

    
`log_explainer(filename, explainer, experiment=None)`
:   Logs dalex explainer to Neptune.
    
    Dalex explainer is pickled and logged to Neptune.
    
    Args:
        filename (:obj:`str`): filename that will be used as an artifact's destination.
        explainer (:obj:`dalex.Explainer`): an instance of dalex explainer
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Examples:
        Start an experiment::
    
            import neptune
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/dalex-integration')
            neptune.create_experiment(name='logging explanations')
    
        Train your model and create dalex explainer::
    
            ...
            clf.fit(X, y)
    
            expl = dx.Explainer(clf, X, y, label="Titanic MLP Pipeline")
    
            log_explainer('explainer.pkl', expl)
    
    Note:
        Check out how the logged explainer looks in Neptune:
        `example experiment <https://ui.neptune.ai/o/shared/org/dalex-integration/e/DAL-48/artifacts>`_

    
`log_global_explanations(explainer, categorical_features=None, numerical_features=None, experiment=None)`
:   Logs global explanations from dalex to Neptune.
    
    Dalex explanations are converted to interactive HTML objects and then uploaded to Neptune
    as an artifact with path charts/{name}.html.
    
    The following explanations are logged: variable importance. If categorical features are specified partial dependence
    and accumulated dependence are also logged. Explanation charts are created and logged with default settings.
    To log charts with custom settings, create a custom chart and use `neptunecontrib.api.log_chart`.
    For more information about Dalex go to `Dalex Website <https://modeloriented.github.io/DALEX/>`_.
    
    Args:
        explainer (:obj:`dalex.Explainer`): an instance of dalex explainer
        categorical_features (:list): list of categorical features for which you want to create
            accumulated dependence plots.
        numerical_features (:list): list of numerical features for which you want to create
            partial dependence plots.
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Examples:
        Start an experiment::
    
            import neptune
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/dalex-integration')
            neptune.create_experiment(name='logging explanations')
    
        Train your model and create dalex explainer::
    
            ...
            clf.fit(X, y)
    
            expl = dx.Explainer(clf, X, y, label="Titanic MLP Pipeline")
            log_global_explanations(expl, categorical_features=["gender", "class"], numerical_features=["age", "fare"])
    
    Note:
        Check out how the logged explanations look in Neptune:
        `example experiment <https://ui.neptune.ai/o/shared/org/dalex-integration/e/DAL-48/artifacts?path=charts%2F>`_

    
`log_local_explanations(explainer, observation, experiment=None)`
:   Logs local explanations from dalex to Neptune.
    
    Dalex explanations are converted to interactive HTML objects and then uploaded to Neptune
    as an artifact with path charts/{name}.html.
    
    The following explanations are logged: break down, break down with interactions, shap, ceteris paribus,
    and ceteris paribus for categorical variables. Explanation charts are created and logged with default settings.
    To log charts with custom settings, create a custom chart and use `neptunecontrib.api.log_chart`.
    For more information about Dalex go to `Dalex Website <https://modeloriented.github.io/DALEX/>`_.
    
    Args:
        explainer (:obj:`dalex.Explainer`): an instance of dalex explainer
        observation (:obj): an observation that can be fed to the classifier for which the explainer was created
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Examples:
        Start an experiment::
    
            import neptune
    
            neptune.init(api_token='ANONYMOUS',
                         project_qualified_name='shared/dalex-integration')
            neptune.create_experiment(name='logging explanations')
    
        Train your model and create dalex explainer::
    
            ...
            clf.fit(X, y)
    
            expl = dx.Explainer(clf, X, y, label="Titanic MLP Pipeline")
    
            new_observation = pd.DataFrame({'gender': ['male'],
                                            'age': [25],
                                            'class': ['1st'],
                                            'embarked': ['Southampton'],
                                            'fare': [72],
                                            'sibsp': [0],
                                            'parch': 0},
                                           index=['John'])
    
            log_local_explanations(expl, new_observation)
    
    Note:
        Check out how the logged explanations look in Neptune:
        `example experiment <https://ui.neptune.ai/o/shared/org/dalex-integration/e/DAL-48/artifacts?path=charts%2F>`_