import utils
from abstract.dto import DTO
from abstract.project import Project


class CVProject(Project):
    def __init__(self, config_path: str = None):
        super(CVProject, self).__init__(config_path)
        self.stages = utils.eval_config(self.config_path)

    def run(self, image_path: str) -> dict:
        info = image_path

        for stage_name in self.stages:
            info = self.stages[stage_name](info)

        return DTO._asdict(info)
