import pathlib

LAB_PATH = pathlib.Path('Lab #3 - Ask your SQL DB questions in English')

def test_notebooks_exist():
    notebooks = list(LAB_PATH.glob('*.ipynb'))
    assert notebooks, f"No notebooks found in {LAB_PATH}"
