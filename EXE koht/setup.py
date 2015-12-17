import sys
from cx_Freeze import setup, Executable

setup(
    
    name = "Yoo Asura",
    version = "1.0",
    author = "Juta Mae & Mark Henri Pedoson",
    options = {
        "build_exe": {
            "packages": ["pygame", "os", "time"],
            "include_files": ["data/",
                              "Block.py",
                              "BlockData.py",
                              "CollisionCheck.py",
                              "DeathScreen.py",
                              "FunctionalScreen.py",
                              "GameWindow.py",
                              "Level.py", 
                              "Player.py",
                              "Stage.py",
                              "StartScreen.py",
                              "WinScreen.py"
                              ]
            }
        },
    executables = [Executable(
        script = "YooAsura.py",
        icon = "Icon.ico"
        )
    ]
)
