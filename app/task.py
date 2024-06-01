from replicate.client import Client
from django.conf import settings
client = Client(api_token=settings.REPLICATE_API_TOKEN)

def tweet(x: str):
    stream = client.stream(
    ref = "meta/meta-llama-3-70b-instruct",
        input={
        "top_k": 0,
        "top_p": 0.9,
        "prompt": "rephrase this tweet for me, just the rephrase no intro " + str(x),
        "max_tokens": 512,
        "min_tokens": 0,
        "temperature": 0.6,
        "system_prompt": "You are a helpful assistant",
        "length_penalty": 1,
        "stop_sequences": "<|end_of_text|>,<|eot_id|>",
        "prompt_template": "<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n",
        "presence_penalty": 1.15,
        "log_performance_metrics": False
        },

    )

    full_response = []
    for chunk in stream:
        full_response.append(chunk)

    output_respond = []
    for output in full_response:
        output_respond.append(output)
