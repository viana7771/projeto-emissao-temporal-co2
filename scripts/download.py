import kagglehub

# Download latest version
path = kagglehub.dataset_download("ravindrasinghrana/carbon-co2-emissions")

print("Path to dataset files:", path)