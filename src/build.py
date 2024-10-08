import sys
from cx_Freeze import setup, Executable

version = "1.0.1"
#base = "console"
base = "gui"
build_options = {
    "packages": [
        'core',
        'core.widgets.yasb.power_menu',
        'core.widgets.yasb.volume',
        'core.widgets.yasb.weather',
        'core.widgets.yasb.memory',
        'core.widgets.yasb.cpu',
        'core.widgets.yasb.active_window',
        'core.widgets.yasb.applications',
        'core.widgets.yasb.battery',
        'core.widgets.yasb.clock',
        'core.widgets.yasb.custom',
        'core.widgets.yasb.github',
        'core.widgets.yasb.media',
        'core.widgets.yasb.wallpapers',
        'core.widgets.yasb.traffic',
        'core.widgets.komorebi.active_layout',
        'core.widgets.komorebi.workspaces',
        'core.widgets.yasb.wifi'
    ],
    "silent_level": 1,
    "excludes": ['PySide6'],
    "build_exe": "dist",
    "include_msvcr": True,
    "optimize": 1,
    "include_files": [
            ("assets/images/app_icon.png","lib/assets/images/app_icon.png")
        ]
}

directory_table = [
    ("ProgramMenuFolder", "TARGETDIR", "."),
    ("MyProgramMenu", "ProgramMenuFolder", "."),
]

msi_data = {
    "Directory": directory_table,
    "ProgId": [
        ("Prog.Id", None, None, "This is a description", "IconId", None),
    ],
    "Icon": [
        ("IconId", "assets/images/app_icon.ico"),
    ],
}

bdist_msi_options = {
    "data": msi_data,
    #"target_name": f"yasb_installer.msi",
    "upgrade_code": "{3f620cf5-07b5-47fd-8e37-9ca8ad14b608}",
    "add_to_path": False,
    "dist_dir": "dist/out",
    "initial_target_dir": r'[LocalAppDataFolder]\Yasb',
    "all_users": False,
    "summary_data": {
        "author": "AmN",
        "comments": "Yet Another Status Bar",
        "keywords": "windows; statusbar"
    }
}

executables = [
    Executable(
        "main.py",
        base=base,
        icon="assets/images/app_icon.ico",
        shortcut_name="Yasb",
        shortcut_dir="MyProgramMenu",
        copyright="Copyright (C) 2024 AmN",
        target_name="yasb.exe",
    )
]
setup(
    name="yasb",
    version=version,
    author="AmN",
    description="Yet Another Status Bar",
    executables=executables,
    options={
        "build_exe": build_options,
        "bdist_msi": bdist_msi_options,
    },
)
