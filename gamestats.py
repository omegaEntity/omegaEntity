class GameStats:
    """storing statistics for the alien invasion"""
    def __init__(self, settings):
        """initialize the stats."""
        self.settings = settings
        self.reset_stats()
        self.score = 0
        self.high_score = 0

    def reset_stats(self):
        """resets the stats available"""
        self.ships_left = self.settings.ship_limit
        self.game_running = False
        self.level = 1
