class PlayerFigures:
    def __init__(self):
        self._totalFigures: int = 0
        self._figures: int = 0

    def addNewFigure(self) -> None:
        if self._figures <= 10:
            self._figures += 1
            self._totalFigures -= 1

    def hasFigures(self, count: int) -> bool:
        return self._figures >= count

    @property
    def getTotalFigures(self) -> int:
        return self._totalFigures

    def takeFigures(self, count: int):
        self._figures -= count

    def newTurn(self):
        pass

    def state(self) -> str:
        pass
