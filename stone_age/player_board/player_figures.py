class PlayerFigures:

    _total_figures: int = 40

    def __init__(self):
        self._figures: int = 0

    def add_new_figure(self) -> bool:
        if self._figures < 10 and self.get_total_figures > 0:
            self._figures += 1
            PlayerFigures._total_figures -= 1
            return True
        return False

    def has_figures(self, count: int) -> bool:
        return self._figures >= count

    @property
    def get_total_figures(self) -> int:
        return PlayerFigures._total_figures

    def take_figures(self, count: int) -> bool:
        if self._figures >= count:
            self._figures -= count
            return True
        return False

    def new_turn(self):
        pass

    def state(self) -> str:
        pass
