Module neptune.internal.notebooks.comm
======================================

Functions
---------

    
`send_checkpoint_created(notebook_id, notebook_path, checkpoint_id)`
:   Send checkpoint created message.
    
    Args:
        notebook_id (:obj:`str`): The notebook's id.
        notebook_path (:obj:`str`): The notebook's path.
        checkpoint_id (:obj:`str`): The checkpoint's path.
    
    
    Raises:
        `ImportError`: If ipykernel is not available.

Classes
-------

`MessageType()`
:   

    ### Class variables

    `CHECKPOINT_CREATED`
    :