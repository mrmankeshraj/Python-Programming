import pywhatkit as py

txt = """DEPRECATION: PyTweening is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
Running setup.py install for PyTweening ... done
DEPRECATION: pyrect is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
Running setup.py install for pyrect ... done
DEPRECATION: pyperclip is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
Running setup.py install for pyperclip ... done
DEPRECATION: pygetwindow is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
Running setup.py install for pygetwindow ... done
DEPRECATION: mouseinfo is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
Running setup.py install for mouseinfo ... done
DEPRECATION: pyautogui is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
Running setup.py install for pyautogui ... done
DEPRECATION: wikipedia is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
Running setup.py install for wikipedia ... done
Successfully installed Flask-2.2.3 Jinja2-3.1.2 MarkupSafe-2.1.2 Pillow-9.4.0 PyTweening-1.0.4 Werkzeug-2.2.3 beautifulsoup4-4.11.2 certifi-2022.12.7 charset-normalizer-3.1.0 click-8.1.3 colorama-0.4.6 idna-3.4 itsdangerous-2.1.2 mouseinfo-0.1.3 pyautogui-0.9.53 pygetwindow-0.0.9 pymsgbox-1.0.9 pyperclip-1.8.2 pyrect-0.2.0 pyscreeze-0.1.28 pywhatkit-5.4
requests-2.28.2 soupsieve-2.4 urllib3-1.26.15 wikipedia-1.4.0."""

py.text_to_handwriting(txt, "to_handwriting.png", [255,0,0])
print("Text Successfully Downloaded as Handwritten Text")