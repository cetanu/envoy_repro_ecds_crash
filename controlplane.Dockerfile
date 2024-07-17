FROM python:3.12
ADD mock_controlplane.py .
CMD ["python", "mock_controlplane.py"]
