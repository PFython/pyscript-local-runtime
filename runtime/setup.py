import shutil
import requests
from urllib.request import urlopen
from pathlib import Path
from log2d import Log

dir_path = Path(__file__).parent

downloads = """
    https://pyscript.net/latest/pyscript.js
    https://pyscript.net/latest/pyscript.css
    https://cdn.jsdelivr.net/pyodide/v0.21.3/full/pyodide.js
    https://cdn.jsdelivr.net/pyodide/v0.21.3/full/pyodide_py.tar
    https://cdn.jsdelivr.net/pyodide/v0.21.3/full/pyodide.asm.js
    https://cdn.jsdelivr.net/pyodide/v0.21.3/full/pyodide.asm.data
    https://cdn.jsdelivr.net/pyodide/v0.21.3/full/repodata.json
    https://cdn.jsdelivr.net/pyodide/v0.21.3/full/pyodide.asm.wasm
    https://cdn.jsdelivr.net/pyodide/v0.21.3/full/packaging-21.3-py3-none-any.whl
    https://cdn.jsdelivr.net/pyodide/v0.21.3/full/distutils.tar
    https://cdn.jsdelivr.net/pyodide/v0.21.3/full/micropip-0.1-py3-none-any.whl
    https://cdn.jsdelivr.net/pyodide/v0.21.3/full/pyparsing-3.0.9-py3-none-any.whl
""".split()

if __name__ == "__main__":
    Log("setup")
    for url in downloads:
        try:
            response = requests.get(url)
            filename = dir_path / url.split("/")[-1]
            with open(filename,'wb') as f:
                shutil.copyfileobj(response.raw, f)
            Log.setup.info(f"Downloaded: {filename.name}")
        except Exception as E:
            Log.setup.error(f"Failed to download: {filename.name}\n{E}")




