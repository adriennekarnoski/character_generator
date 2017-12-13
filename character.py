"""Create a character class."""


class Character(object):
    """Create a character."""

    def __init__(self, name=None):
        self.name = name

    def _basics(self, class_choice, species):
        """Select the basics for the character."""
        self.class_choice = class_choice
        self.species = species

    def _subclasses(self, subclass):
        """Pick the subclass for the given class."""
        self.subclass = subclass

    def _armor():
        """."""


if __name__ == '__main__':
    name = input('Please enter a name for your character: ')
    c_choices = ['titan', 'warlock', 'hunter']
    class_choice = input('Please enter a class for your character.\n The options are:\nTitan,\nHunter,\nWarlock: ').lower()
    if class_choice not in c_choices:
        print('Please pick a class for your character')
    species = input('Please enter a species.\n The options are:\nHuman,\nExo,\nAwoken: ')
    new_character = Character(name)
    new_character._basics(class_choice, species)
