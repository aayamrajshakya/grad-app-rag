# Graduate Application RAG

> [!NOTE]
> `deps.txt` contains general dependencies w/o version constraints, while `hard_deps.txt` includes strictly version-pinned dependencies. As such, the latter is more reliable.

I moved some utility files used throughout this project to separate branch(es) to keep the master branch organized.

Special thanks to @coleam00 for the [crawler script](https://github.com/coleam00/ottomator-agents/blob/main/crawl4AI-agent-v2/crawl4AI-examples/5-crawl_site_recursively.py), which I heavily modified and optimized to fit my needs.

---

## Build instructions

> Not sure about the steps for Windows machines. I use Linux ;)

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
