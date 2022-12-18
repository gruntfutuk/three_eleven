def is_yes(prompt:str="Yes or No?", default:bool=None) -> bool:
    """ prompt user and only accept answer that is in AFFIRMATION or REJECTION sets
    and return True or False accordingly; return alone can be accepted if default
    set to either True or False in which case the default is returned """
    while True:
        response = input(prompt).strip().casefold()
        if not response and default is not None:
            return default
        if response in AFFIRMATION:
            return True
        if response in REJECTION:
            return False
        print('Sorry, I did not understand that')


AFFIRMATION = frozenset(('y', 'yes', 'yup', 'yeh', 'ok', '1'))
REJECTION = frozenset(('n', 'no', 'nah', 'nope', '0'))
