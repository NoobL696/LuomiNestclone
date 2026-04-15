from loguru import logger
from typing import List


class SkillRegistry:
    _skills = {}

    @classmethod
    def register(cls, skill_id: str, skill):
        cls._skills[skill_id] = skill

    @classmethod
    def get(cls, skill_id: str):
        return cls._skills.get(skill_id)

    @classmethod
    def list_all(cls) -> List[str]:
        return list(cls._skills.keys())
