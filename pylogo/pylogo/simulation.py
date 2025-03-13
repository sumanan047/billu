class Simulation:
    def __init__(self, model, time, **kwargs) -> None:
        self.model = model
        self.time = time

    def run(self):
        for _ in self.time:
            self.model.step()
            self._animation_hook()
            self.model.save()

    def _animation_hook(self):
        print("Animation Hook is getting called.")