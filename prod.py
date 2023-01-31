# This file is used to verify your http server acts as expected
# Run it with `python3 test.py`
import time
import banana_dev as banana

api_key = "<YOUR_API_KEY>"
model_key = "<YOUR_MODEL_KEY>"

model_inputs = {
    'max_new_tokens': 91,
    'prompt': '''def is_prime(element):
    """Returns whether a number is prime."""'''}

# Run the model
t1 = time.time()
out = banana.run(api_key, model_key, model_inputs)
t2 = time.time()
print("Inference in ",t2-t1,"seconds")

print(out)