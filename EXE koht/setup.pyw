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
                              "Block.pyw",
                              "BlockData.pyw",
                              "CollisionCheck.pyw",
                              "DeathScreen.pyw",
                              "FunctionalScreen.pyw",
                              "GameWindow.pyw",
                              "Level.pyw", 
                              "Player.pyw",
                              "Stage.pyw",
                              "StartScreen.pyw",
                              "WinScreen.pyw"
                              ]
            }
        },
    executables = [Executable(
        script = "YooAsura.pyw",
        icon = "Icon.ico"
        )
    ]
)
