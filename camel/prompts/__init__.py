# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
#  Enhanced by Startr.Team (2024)
# =========== Copyright 2024 @  Startr LLC   All Rights Reserved. ===========
from .base import TextPrompt, CodePrompt, TextPromptDict
from .task_prompt_template import TaskPromptTemplateDict
from .prompt_templates import PromptTemplateGenerator

__all__ = [
    "TextPrompt",
    "TextPromptDict",
    "TaskPromptTemplateDict",
    "PromptTemplateGenerator",
]
