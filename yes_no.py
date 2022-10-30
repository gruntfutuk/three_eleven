    def is_yes(prompt):
        while True:
            response = input(prompt).strip().casefold()
            if response in AFFIRMATION:
                return True
            if response in REJECTION:
                return False
            print('Sorry, I did not understand that')


    AFFIRMATION = frozenset(('y', 'yes', 'yup', 'yeh', 'ok', '1'))
    REJECTION = frozenset(('n', 'no', 'nah', 'nope', '0'))
