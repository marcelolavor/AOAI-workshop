import pathlib

LAB_PATH = pathlib.Path('Lab #5 - Retrieval Augmented Generation in Azure')

def test_notebooks_exist():
    notebooks = list(LAB_PATH.rglob('*.ipynb'))
    assert notebooks, f"No notebooks found in {LAB_PATH}"
