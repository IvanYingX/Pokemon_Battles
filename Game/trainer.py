class Trainer:
    def __init__(self, pokemon):
        self.pokemon = pokemon

    def __getitem__(self, idx):
        return self.pokemon[idx]