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
