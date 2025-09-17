from setuptools import setup, find_packages

setup(
    name="cloudops-ai-monitor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "torch",
        "torchvision",
        "pandas",
        "numpy",
        "scikit-learn",
        "pydantic",
        "openai",
        "sagemaker",
        "boto3",
        "streamlit",
    ],
    entry_points={
        "console_scripts": [
            "cloudops-ai-monitor=api.main:app",
        ],
    },
    author="Your Name",
    description="AI-powered CloudOps monitoring system with ML + GenAI explanations",
    license="MIT",
)
