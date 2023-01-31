# This file is used to verify your http server acts as expected
# Run it with `python3 test.py``
import time
import requests

model_inputs = {
    'max_new_tokens': 91,
    'prompt': "'''def is_prime(element): '''Returns whether a number is prime.'''"}

# Run the model
t1 = time.time()
res = requests.post('http://localhost:8000/', json = model_inputs)
t2 = time.time()
print("Inference in ",t2-t1,"seconds")

print(res.json())