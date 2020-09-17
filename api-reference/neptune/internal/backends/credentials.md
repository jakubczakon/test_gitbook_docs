Module neptune.internal.backends.credentials
============================================

Classes
-------

`Credentials(api_token=None)`
:   It formats your Neptune api token to the format that can be understood by the Neptune Client.
    
    A constructor allowing you to pass the Neptune API token.
    
    Args:
        api_token(str): This is a secret API key that you can retrieve by running
            `$ neptune account api-token get`
    
    Attributes:
        api_token:  This is a secret API key that was passed at instantiation.
    
    Examples:
    
        >>> from neptune.internal.backends.credentials import Credentials
        >>> credentials=Credentials('YOUR_NEPTUNE_API_KEY')
    
        Alternatively you can create an environment variable by running:
    
        $ export NEPTUNE_API_TOKEN=YOUR_API_TOKEN
    
        which will allow you to use the same method without `api_token` parameter provided.
    
        >>> credentials=Credentials()
    
    Note:
        For security reasons it is recommended to provide api_token through environment variable `NEPTUNE_API_TOKEN`.
        You can do that by going to your console and running:
    
        $ export NEPTUNE_API_TOKEN=YOUR_API_TOKEN`
    
        Token provided through environment variable takes precedence over `api_token` parameter.

    ### Instance variables

    `api_token`
    :

    `api_url_opt`
    :

    `token_origin_address`
    :