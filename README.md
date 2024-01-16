# intel-llm-guide
A guide on how to run large language models on intel CPUs with limited resources on a linux platform.

Please note that this guide is __still in development__, so some inaccuracies are expected.

## Prerequesites
Im am assuming you have an intel-CPU with an integrated graphics chip. I have tested and developed this guide using an `11th Gen Intel i7-1165G7` and 16 GB of RAM, but it should work with many more models. You might also want to check out the [intel extension for pytorch system requirements](https://github.com/intel/intel-extension-for-transformers/blob/main/docs/installation.md#system-requirements)

You should  also have the `python3` package installed (`sudo apt install python` or `sudo pacman -S python`).

### Virtual environment

First of all, create a new virtual python environment. This should probably be located in the `/opt` folder. My AI development environment path for example is `/opt/python-envs/AI`. After deciding on your environment path, run:

```bash
python -m venv <venv_folder>
```

To ativate this enironment, run `source <venv_folder>/bin/acitvate`. Because the `/opt` folder is normally not owned by the user, you might need to run `sudo chown $USER <venv_folder> -R` to give your user permission to use it.

To check if this step worked, check which file the python command points to now using `which python` and you should get a response of the form `<venv_folder>/bin/python`.

You will need to do this every time when using the environment, so maybe consider adding this line to your `.bashrc` but be careful as this might break other python dependencies.

## Dependencies
To install the `intel extensions for pytorch` and all other needed packages, run
```bash
pip install intel-extension-for-transformers torch tokenizers sentencepiece protobuf accelerate
```

## Huggingface models

To correctly use a language model from the [huggingface](https://huggingface.co/) server, you will first need to import all the modules:

```python
from transformers import AutoTokenizer, TextStreamer
from intel_extension_for_transformers.transformers import AutoModelForCausalLM
import torch
```

After this, a model can be loaded using `model = AutoModelForCausalLM.from_pretrained(model_name)`, but there is some __jank__ in the intel-extension-for-transformers module we have to take care of first:

### Dealing with the jank
First of all, you will need to download the model from the huggingface hub. You can do this either using `git` like this:
```bash
git lfs install
git clone git@hf.co:<MODEL ID>
```

Or you can also run the following bit of python code for your model:

```python
from intel_extension_for_transformers.transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(model_id)
```

This will download the model to your local machine. If you don't have enough RAM, this will probably either get killed automatically (if you are using `zsh`) or kill your machine. A way to circumvent this behaviour is to abort the piece of code when it enters the stage `Loading checkpoint shards`.

If you can and want to use the model in its full precisioan, you have now downloaded it and can go on and use it as you please. If you want to quantize it to optimize to use less CPU RAM, follow these steps:
