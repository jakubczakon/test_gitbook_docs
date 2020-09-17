Module neptunecontrib.monitoring.keras
======================================

Classes
-------

`NeptuneMonitor(experiment=None, prefix='')`
:   Logs Keras metrics to Neptune.
    
    Goes over the `last_metrics` and `smooth_loss` after each batch and epoch
    and logs them to appropriate Neptune channels.
    
    See the example experiment here TODO
    
    Args:
        experiment: `neptune.Experiment`, optional:
            Neptune experiment. If not provided, falls back on the current
            experiment.
        prefix: str, optional:
            Prefix that should be added before the `metric_name`
            and `valid_name` before logging to the appropriate channel.
            Defaul is empty string ('').
    
    Examples:
    
        Now, create Neptune experiment, instantiate the monitor and pass
        it to callbacks::
    
            TODO update for keras
    
    Note:
        You need to have Keras or Tensorflow 2 installed on your computer to use this module.

    ### Ancestors (in MRO)

    * tensorflow.python.keras.callbacks.Callback

    ### Methods

    `on_batch_end(self, batch, logs=None)`
    :   A backwards compatibility alias for `on_train_batch_end`.

    `on_epoch_end(self, epoch, logs=None)`
    :   Called at the end of an epoch.
        
        Subclasses should override for any actions to run. This function should only
        be called during TRAIN mode.
        
        Arguments:
            epoch: Integer, index of epoch.
            logs: Dict, metric results for this training epoch, and for the
              validation epoch if validation is performed. Validation result keys
              are prefixed with `val_`.