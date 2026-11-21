"""Start the managed worker with only Capri's code and the pinned environment."""
from pathlib import Path
import runpy
import sys


if __name__ == '__main__':
    # The desktop launches with -I -S: sitecustomize and .pth hooks must not
    # import a different ONNX Runtime before the worker can select its DLL.
    root = Path(__file__).resolve().parents[2]
    venv_root = Path(sys.executable).parent.parent
    packages = next(venv_root.glob('lib/python*/site-packages'), venv_root / 'Lib' / 'site-packages')
    sys.path.extend((str(root), str(packages)))
    runpy.run_module('integrations.asr_runtime.worker', run_name='__main__')
