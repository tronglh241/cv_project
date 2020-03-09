import utils


class Project(object):
    def __init__(self, config_path=utils.Path(__file__).with_name('config.yaml')):
        super(Project, self).__init__()

        config = utils.load_yaml(config_path)
        self.number_detector = utils.create_instance(config['number_detection'])

    def __call__(self, image_path):
        info, = self.number_detector(image_path)

        return info.asdict()