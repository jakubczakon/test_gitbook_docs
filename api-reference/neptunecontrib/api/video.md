Module neptunecontrib.api.video
===============================

Functions
---------

    
`log_video(path_to_file, video_name=None, experiment=None)`
:   Logs a video file to 'artifacts/video' with player.
    
    Logs a video file to the 'artifacts/video' in the experiment, where you can play it directly from the browser.
    
    You can also download raw video file to the local machine.
    Just use "three vertical dots" located to the right from the player.
    
    Args:
        path_to_file (:obj:`str`): Path to video file.
        video_name (:obj:`str`, optional, default is ``None``): Name to be displayed in artifacts/video.
            | If `None`, file name is used.
        experiment (:obj:`neptune.experiments.Experiment`, optional, default is ``None``):
            | For advanced users only. Pass Neptune
              `Experiment <https://docs.neptune.ai/neptune-client/docs/experiment.html#neptune.experiments.Experiment>`_
              object if you want to control to which experiment data is logged.
            | If ``None``, log to currently active, and most recent experiment.
    
    Example:
    
        .. code:: python3
    
            log_video('video-file.mp4')
            log_video('/full/path/to/some/other/video/file.mp4')
            log_video('/full/path/to/some/other/video/file.mp4', 'my_video')
    
    Note:
        Check out how the logged video file looks in Neptune:
        `here <https://ui.neptune.ai/o/shared/org/showroom/e/
        SHOW-1542/artifacts?path=video%2F&file=jellyfish-25-mbps-hd-hevc.html>`_.
    
    Warning:
        Video files contribute to the storage usage. Be mindful with large video files.