Module neptunecontrib.monitoring.xgboost
========================================

Functions
---------

    
`neptune_callback(log_model=True, log_importance=True, max_num_features=None, log_tree=(0,), experiment=None, **kwargs)`
:   XGBoost callback for Neptune experiments.
    
    This is XGBoost callback that automatically logs training and evaluation metrics, feature importance chart,
    visualized trees and trained Booster to Neptune.
    
    Check Neptune documentation for the `full example <https://docs.neptune.ai/integrations/xgboost.html>`_.
    
    Make sure you created an experiment before you start XGBoost training using ``neptune.create_experiment()``
    (`check our docs <https://docs.neptune.ai/neptune-client/docs/project.html
    #neptune.projects.Project.create_experiment>`_).
    
    Integration works with ``xgboost>=0.82``.
    
    Tip:
        Use this `Google Colab <https://colab.research.google.com/github/neptune-ai/neptune-colab-examples
        /blob/master/xgboost-integration.ipynb>`_ to try it without further ado.
    
    Args:
        log_model (:obj:`bool`, optional, default is ``True``):
            | Log booster to Neptune after last boosting iteration.
            | If you run xgb.cv, log booster for all folds.
        log_importance (:obj:`bool`, optional, default is ``True``):
            | Log feature importance to Neptune as image after last boosting iteration.
            | Specify number of features using ``max_num_features`` parameter below.
            | If you run xgb.cv, log feature importance for each folds' booster.
        max_num_features (:obj:`int`, optional, default is ``None``):
            | Plot top ``max_num_features`` features on the importance plot.
            | If ``None``, plot all features.
        log_tree (:obj:`list` of :obj:`int`, optional, default is ``[1,]``):
            | Log specified trees to Neptune as images after last boosting iteration.
            | If you run xgb.cv, log specified trees for each folds' booster.
            | Default is to log first tree.
            | If ``None``, do not log any tree.
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
        kwargs:
            Parametrize XGBoost functions used in this callback:
            `xgboost.plot_importance <https://xgboost.readthedocs.io/en/latest/python/python_api.html
            ?highlight=plot_tree#xgboost.plot_importance>`_
            and `xgboost.to_graphviz <https://xgboost.readthedocs.io/en/latest/python/python_api.html
            ?highlight=plot_tree#xgboost.to_graphviz>`_.
    
    Returns:
        :obj:`callback`, function that you can pass directly to the XGBoost callbacks list, for example to the
        ``xgboost.cv()``
        (`see docs <https://xgboost.readthedocs.io/en/latest/python/python_api.html?highlight=plot_tree#xgboost.cv>`_)
        or ``XGBClassifier.fit()``
        (`check docs <https://xgboost.readthedocs.io/en/latest/python/python_api.html?highlight=plot_tree
        #xgboost.XGBClassifier.fit>`_).
    
    Note:
        If you use early stopping, make sure to log model, feature importance and trees on your own.
        Neptune logs these artifacts only after last iteration, which you may not reach because of early stop.
    
    Examples:
        ``xgb.train`` examples
    
        .. code:: python3
    
            # basic usage
            xgb.train(param, dtrain, num_round, watchlist,
                      callbacks=[neptune_callback()])
    
            # do not log model
            xgb.train(param, dtrain, num_round, watchlist,
                      callbacks=[neptune_callback(log_model=False)])
    
            # log top 5 features' importance chart
            xgb.train(param, dtrain, num_round, watchlist,
                      callbacks=[neptune_callback(max_num_features=5)])
    
        ``xgb.cv`` examples
    
        .. code:: python3
    
            # log 5 trees per each folds' booster
            xgb.cv(param, dtrain, num_boost_round=num_round, nfold=7,
                   callbacks=neptune_callback(log_tree=[0,1,2,3,4]))
    
            # log only metrics
            xgb.cv(param, dtrain, num_boost_round=num_round, nfold=7,
                   callbacks=[neptune_callback(log_model=False,
                                               log_importance=False,
                                               max_num_features=None,
                                               log_tree=None)])
    
            # log top 5 features per each folds' booster
            xgb.cv(param, dtrain, num_boost_round=num_round, nfold=7,
                   callbacks=[neptune_callback(log_model=False,
                                               max_num_features=3,
                                               log_tree=None)])
    
        ``sklearn`` API examples
    
        .. code:: python3
    
            # basic usage with early stopping
            xgb.XGBRegressor().fit(X_train, y_train,
                                   early_stopping_rounds=10,
                                   eval_metric=['mae', 'rmse', 'rmsle'],
                                   eval_set=[(X_test, y_test)],
                                   callbacks=[neptune_callback()])
    
            # do not log model
            clf = xgb.XGBRegressor()
            clf.fit(X_train, y_train,
                    eval_metric=['mae', 'rmse', 'rmsle'],
                    eval_set=[(X_test, y_test)],
                    callbacks=[neptune_callback(log_model=False)])
            y_pred = clf.predict(X_test)
    
            # log 8 trees
            reg = xgb.XGBRegressor(**params)
            reg.fit(X_train, y_train,
                    eval_metric=['mae', 'rmse', 'rmsle'],
                    eval_set=[(X_test, y_test)],
                    callbacks=[neptune_callback(log_tree=[0,1,2,3,4,5,6,7])])