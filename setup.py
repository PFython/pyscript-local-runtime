import shutil
import requests
from pathlib import Path

dir_path = Path(__file__).parent

downloads = r"""https://pyscript.net/latest/pyscript.js
https://pyscript.net/latest/pyscript.css
https://cdn.jsdelivr.net/pyodide/v0.21.2/full/pyodide.js
https://cdn.jsdelivr.net/pyodide/v0.21.2/full/pyodide_py.tar
https://cdn.jsdelivr.net/pyodide/v0.21.2/full/pyodide.asm.js
https://cdn.jsdelivr.net/pyodide/v0.21.2/full/pyodide.asm.data
https://cdn.jsdelivr.net/pyodide/v0.21.2/full/repodata.json
https://cdn.jsdelivr.net/pyodide/v0.21.2/full/pyodide.asm.wasm
https://cdn.jsdelivr.net/pyodide/v0.21.2/full/packaging-21.3-py3-none-any.whl
https://cdn.jsdelivr.net/pyodide/v0.21.2/full/distutils.tar
https://cdn.jsdelivr.net/pyodide/v0.21.2/full/micropip-0.1-py3-none-any.whl""".split()

if __name__ == "__main__":
    for url in downloads:
        response = requests.get(url)
        filename = dir_path / url.split("/")[-1]
        with open(filename,'wb') as f:
            shutil.copyfileobj(response.raw, f)


