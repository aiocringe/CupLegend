from setuptools import setup, find_packages

setup(
    name="cuplegend",
    version="0.1.0",
    description="Python библиотека для работы с Cup Legend API",
    author="aiocringe",
    author_email="aiocringe@hotmail.com",
    url="https://github.com/aiocringe/CupLegend",  # ссылка на проект (GitHub/Docs)
    packages=find_packages(),         # автоматически находит все пакеты
    install_requires=[
        "requests>=2.0.0",
        "pydantic>=2.0.0",
    ],
    python_requires=">=3.9",          # минимальная версия Python
    classifiers=[                     # метаданные для PyPI
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords="cup legend api sdk",
)
