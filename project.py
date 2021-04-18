import utils


class Project:
    def __init__(self, config_path=utils.Path(__file__).with_name('config.yaml')):
        super(Project, self).__init__()

        self.stages = utils.eval_config(config_path)

    def __call__(self, image_path):
        info = image_path

        for stage_name in self.stages:
            info = self.stages[stage_name](image_path)

        return info.asdict()
