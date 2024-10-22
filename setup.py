from setuptools import setup

setup(
    name="VocaScribe",
    version="0.1",
    py_modules=["vocascribe"],
    install_requires=[
        "build",
        "SpeechRecognition",
        "gTTS",
        "pydub",
        "ffmpeg",
    ],  # Add any other dependencies here
    entry_points={
        "console_scripts": [
            "vscribe=vocascribe:main",
        ],
    },
    author="Jake Johnson",
    author_email="",  # Omitted for privacy
    description="A very simple tool to transcribe audio files to text.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ofalltrades/VocaScribe",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    project_urls={
        "Issues": "https://github.com/ofalltrades/VocaScribe/issues",
    },
)
