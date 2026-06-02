from typing import List, Union

from pydantic import BaseModel, ConfigDict
from pydantic_core import MISSING

from scripts.models.common.all_trait import AllTrait
from scripts.models.common.skill import Skill
from scripts.models.common.element import Element


class StatDict(BaseModel):
    model_config = ConfigDict(extra="forbid")
    skill: Union[List[Skill], MISSING] = MISSING
    trait: Union[List[AllTrait], MISSING] = MISSING
    element: Union[List[Element], MISSING] = MISSING
    must_have_both: Union[bool, MISSING] = MISSING
