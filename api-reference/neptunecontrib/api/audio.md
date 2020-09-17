Module neptunecontrib.api.audio
===============================

Functions
---------

    
`log_audio(path_to_file, audio_name=None, experiment=None)`
:   Logs audio file to 'artifacts/audio' with player.
    
    Logs audio file to the 'artifacts/audio' in the experiment, where you can play it directly from the browser.
    You can also download raw audio file to the local machine.
    Just use "three vertical dots" located to the right from the player.
    
    Args:
        path_to_file (:obj:`str`): Path to audio file.
        audio_name (:obj:`str`, optional, default is ``None``): Name to be displayed in artifacts/audio.
            | If `None`, file name is used.
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Example:
    
        .. code:: python3
    
            log_audio('audio-file.wav')
            log_audio('/full/path/to/some/other/audio/file.mp3')
            log_audio('/full/path/to/some/other/audio/file.mp3', 'my_audio')
    
    Note:
        Check out how the logged audio file looks in Neptune:
        `here <https://ui.neptune.ai/o/shared/org/showroom/e/SHOW-1485/artifacts?path=audio%2F>`_.