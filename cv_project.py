from abstract.dto import DTO
from abstract.project import Project
from dto.info import Info
from utils.config import CfgNode


class CVProject(Project):
    def __init__(self, config_path: str = None):
        super(CVProject, self).__init__(config_path)
        config = CfgNode.load_yaml_with_base(str(self.config_path))
        self.stages, _ = config.eval()

    def run(self, image_path: str) -> dict:
        info = Info(image_path=image_path)

        for stage_name in self.stages:
            info = self.stages[stage_name](info)

        return DTO._asdict(info)
