# In this file, we define download_model
# It runs during container build time to get model weights built into the container

from transformers import AutoModelForCausalLM, AutoTokenizer

def download_model():
    # do a dry run of loading the huggingface model, which will download weights
    model_name = "bigcode/santacoder"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True)

if __name__ == "__main__":
    download_model()