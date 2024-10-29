from pydantic import BaseModel
from typing import List

class TemplateSuggestion(BaseModel):
    template_name: str
    description: str
    variables: List[str]
