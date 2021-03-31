# Install

Installation process for Linux, Mac and Windows WSL users:

### 1. Create virtual environment:

```
$ python -m venv .venv
```

Do it only when you creating project. Dont create it each time.

Sometimes it could be `python3`, `py`, `py3`

### 2. Activating virtual environment:

```
$ source .venv/bin/activate
```

### 3. Install libraries:

```
$ pip install -r requirements.txt
```

# Usage

Add your URLS in urls.txt

Run script by typing:

```
python main.py
```

As a response you will get `url`|`closest timestamp` if web.archive contains snapshot for this page OR `url`|`no response` if not
