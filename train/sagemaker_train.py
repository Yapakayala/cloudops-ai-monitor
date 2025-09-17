from sagemaker.pytorch import PyTorch

estimator = PyTorch(
    entry_point="train.py",
    role="SageMakerRole",
    framework_version="1.12",
    instance_type="ml.m5.large",
    py_version="py38",
)
estimator.fit({"train": "s3://your-bucket/train"})
