# pyscript-local-runtime

This repository gives a template for running PyScript and all its runtime dependencies locally e.g. to create browser extensions using Python, or offline web apps using PyScript without internet access.

To download the runtime files on Linux/Posix using wget...
```shell
cd runtime
source setup.sh
```

To download the runtime files on Windows (with Python and requests):
```
cd runtime
python setup.py
```

## **EXAMPLE CHROME EXTENSION**
![](popup.png)

This example is a simple Chrome Extension which creates a Popup box, renders the time using Python's `datetime` module, and sends a message to the Console.


* The Python script is wrapped inside some simple HTML boiler-plate code in `index.html`.
* On completion, `index.html` runs the JavaScript file `finished.js`.
* PyScript runtime files are in `/runtime`
* Icons are in `/images`
* Other magic required for Chrome to recognise this as an extension are in `manifest.json`.

`index.html` must include a `<py-config>` block as follows:

```html
<py-config>
      [[runtimes]]
      src = "runtime/pyodide.js"
      name = "pyodide-0.21.3"
      lang = "python"
</py-config>
```

And also these two lines to load PyScript locally into the browser:
```html
<link rel="stylesheet" href="runtime/pyscript.css" />
<script defer src="runtime/pyscript.js"></script>
```

Now you're ready to load the unpacked extension into Chrome and run it [following this tutorial](https://www.codeinwp.com/blog/how-to-write-a-chrome-extension/#:~:text=After%20you%20have%20your%20manifest%20file%20in%20place%2C%20you%20can%20load%20up%20your%20extension%20in%20the%20Chrome%20browser%3A).

Further information about getting started with Chrome Exentions is available [here](https://developer.chrome.com/docs/extensions/mv3/getstarted/).

All the best,
Pete

https://github.com/PFython

## **CREDITS**

A big "Thank You" to https://github.com/tedpatrick (Engineering Manager at Anaconda) for pointing me in the right direction.

If this code helps you save time and focus on more important things, please feel free to to show your appreciation by starring the repository on Github.

I'd also be delighted if you wanted to:

<a href="https://www.buymeacoffee.com/pfython" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/arial-yellow.png" alt="Buy Me A Coffee" width="217px" ></a>

