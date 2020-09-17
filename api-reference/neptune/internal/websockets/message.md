Module neptune.internal.websockets.message
==========================================

Classes
-------

`AbortMessage()`
:   

    ### Ancestors (in MRO)

    * neptune.internal.websockets.message.Message

    ### Static methods

    `from_json(json_value)`
    :

    `get_type()`
    :

    ### Methods

    `body_to_json(self)`
    :

`ActionInvocationMessage(action_id, action_invocation_id, argument)`
:   

    ### Ancestors (in MRO)

    * neptune.internal.websockets.message.Message

    ### Static methods

    `from_json(json_value)`
    :

    `get_type()`
    :

    ### Methods

    `body_to_json(self)`
    :

`Message()`
:   

    ### Descendants

    * neptune.internal.websockets.message.AbortMessage
    * neptune.internal.websockets.message.ActionInvocationMessage

    ### Class variables

    `MESSAGE_BODY`
    :

    `MESSAGE_TYPE`
    :

    ### Static methods

    `from_json(json_value)`
    :

    `get_type()`
    :

    ### Methods

    `body_to_json(self)`
    :

`MessageClassRegistry()`
:   

    ### Class variables

    `MESSAGE_CLASSES`
    :

`MessageType()`
:   

    ### Class variables

    `ABORT`
    :

    `ACTION_INVOCATION`
    :

    `NEW_CHANNEL_VALUES`
    :