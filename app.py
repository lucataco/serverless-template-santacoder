import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Init is ran on server startup
# Load your model to GPU as a global variable here using the variable name "model"
def init():
    global model
    global tokenizer
    
    model_name = "bigcode/santacoder"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name, trust_remote_code=True).to("cuda")


# Inference is ran for every server call
# Reference your preloaded global model variable here.
def inference(model_inputs:dict) -> dict:
    global model
    global tokenizer

    # Parse out your arguments
    prompt = model_inputs.get('prompt', None)
    max_new = model_inputs.get('max_new_tokens', 10)
    if prompt == None:
        return {'message': "No prompt provided"}
    
    # Run the model
    inputs = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(inputs, max_new_tokens=max_new, pad_token_id=50256)
    result = tokenizer.decode(outputs[0])

    # Return the results as a dictionary
    return result
