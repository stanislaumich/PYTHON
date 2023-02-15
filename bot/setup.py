from cx_Freeze import setup, Executable

setup(
    name = "LBOT",
    version = "0.1",
    description = "Bot",
    executables = [Executable("lbot.py")]
)