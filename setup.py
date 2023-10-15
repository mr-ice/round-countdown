from setuptools import setup

APP = ["Round Countdown.py"]
DATA_FILES = []
OPTIONS = {
    "packages": ["tkinter", "tkmacosx"],
    "iconfile": "RCIcon.icns",
    "plist": {
        "CFBundleDevelopmentRegion": "English",
        "CFBundleIdentifier": "org.riceclan.round-countdown",
        "CFBundleVersion": "1.0.0",
        "NSHumanReadableCopyright": "Copyright © 2023, Michael Rice, All Rights Reserved",
    },
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
