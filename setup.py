import platform
import subprocess
import sys

from tests.constants import RED, RESET


def run_command(command: str) -> None:
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing {command}: {e}")
        sys.exit(1)


def setup_environment() -> None:
    print("Setting up the environment...")

    os_name = platform.system()
    if os_name == "Windows":
        python_bin = "python"
        activate_script = ".venv\\Scripts\\activate"
        pip = "pip3"
    else:
        python_bin = "python3"
        activate_script = "source .venv/bin/activate"
        pip = "pip"

    major, minor = sys.version_info.major, sys.version_info.minor
    msg = f"The project is not tested on Python {major},{minor}"
    if major != 3 and minor < 11:
        print(msg)

    print("Creating virtual environment...")
    run_command(f"{python_bin} -m venv .venv")

    pip_upgrade = f"{pip} install --upgrade pip"
    poetry_install = f"{pip} install poetry"
    dependecy_install = "poetry install"

    commands = f"{activate_script} && \
        {python_bin} -m {pip_upgrade} && \
        {poetry_install} && \
        {dependecy_install}"

    run_command(commands)

    # fmt: off
    print(
        f"\n\n{RED}To activate the virtual environment, "
        f"type in terminal:{RESET}\n\033[32m{activate_script}{RESET}\n\n"
        "Setup complete!\n"
        "If you found this project useful, feel free "
        "to give the repository a star on GitHub!\n"
    )
    # fmt: on


if __name__ == "__main__":
    setup_environment()
