# model_config.py

# Define the model name to be used from Hugging Face
MODEL_NAME = "meta-llama/Meta-Llama-3-8B"

# Set the maximum length for generated responses
MAX_LENGTH = 100

# Set the number of beams for beam search (if needed)
NUM_BEAMS = 5

# Define temperature for controlling the randomness of predictions
TEMPERATURE = 0.7

# Set whether to use top-k sampling (if needed)
TOP_K = 50

# Set whether to use top-p sampling (if needed)
TOP_P = 0.9

# Optionally, define batch size for efficient processing
BATCH_SIZE = 8
