import kagglehub

# Download latest version
path = kagglehub.dataset_download("ziya07/youth-basketball-training")

print("Path to dataset files:", path)