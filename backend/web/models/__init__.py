"""
确保 Django 加载 web app 时能导入所有模型。

当前项目把模型拆在 web/models/*.py 下，如果这里不显式导入，
Django 在导入 web.models 时可能不会自动加载子模块，从而导致
makemigrations / admin / 运行期行为不一致。
"""

from .user import UserProfile  # noqa: F401
from .character import Character  # noqa: F401

