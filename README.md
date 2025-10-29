# Graduate Application RAG

> [!NOTE]
> `deps.txt` contains general dependencies w/o version constraints, while `hard_deps.txt` includes strictly version-pinned dependencies.

I moved other scripts used throughout this project to separate branch(es) to keep the master branch organized.

---

## Build instructions

> ! Not sure of the steps for Windows machines

1) Create and activate a virtual environment (I use `venv`):
```console
python3 -m venv {your_env_name}
source {your_env_name}/bin/activate
```

2) Install dependencies (soft in this case):
```console
pip install --upgrade pip && pip install -r deps.txt
```

3) Run the chatbot interface:
```console
streamlit run st_chatbot.py
```
