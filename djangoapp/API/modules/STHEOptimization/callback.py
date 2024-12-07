from pymoo.core.callback import Callback

class MyCallback(Callback):
    def __init__(self):
        super().__init__()
        self.generation = 0

    def notify(self, algorithm):
        self.generation += 1
        # logger.info(f"Geração: {self.generation}")
        # logger.info("População atual:")
        # for ind in algorithm.pop.get("X"):
        #     logger.info(ind)