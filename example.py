from transformers import AutoTokenizer, TextStreamer
from intel_extension_for_transformers.transformers import AutoModelForCausalLM

prompt = "Once upon a time, there existed a little girl,"

model_name="/opt/models/TinyLlama/TinyLlama-1.1B-Chat-v1.0/"

model_name="/home/lukas/.cache/huggingface/hub/models--Intel--neural-chat-7b-v3-3/snapshots/7b86016aa1d2107440c1928694a7bba926509887/"

tokenizer = AutoTokenizer.from_pretrained(model_name, local_files_only=True)
inputs = tokenizer(prompt, return_tensors="pt").input_ids
streamer = TextStreamer(tokenizer)

model = AutoModelForCausalLM.from_pretrained(model_name, local_files_only=True, load_in_4bit=True)
outputs = model.generate(inputs, streamer=streamer, max_new_tokens=300)
print(outputs)
