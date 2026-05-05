import platform
import sys

from config import settings


def create_allure_environment_file():
    os_info = f"os_info = {platform.system()}, {platform.release()}"
    python_version = f"python_version = {sys.version}"

    items = [f"{key} = {value}" for key, value in settings.model_dump().items()]
    properties = '\n'.join(items) + f"\n{os_info}\n{python_version}"

    with open(settings.allure_results_dir.joinpath('environment.properties'), 'w+') as file:
        file.write(properties)
