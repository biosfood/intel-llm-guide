from transformers import AutoTokenizer, TextStreamer
from intel_extension_for_transformers.transformers import AutoModelForCausalLM

prompt = "Once upon a time, there existed a little girl,"

model_name="/opt/models/microsoft/phi-2/"

tokenizer = AutoTokenizer.from_pretrained(model_name, local_files_only=True)
inputs = tokenizer(prompt, return_tensors="pt").input_ids
streamer = TextStreamer(tokenizer)

model = AutoModelForCausalLM.from_pretrained(model_name, local_files_only=True, load_in_4bit=True)
outputs = model.generate(inputs, streamer=streamer, max_new_tokens=300)
print(outputs)
