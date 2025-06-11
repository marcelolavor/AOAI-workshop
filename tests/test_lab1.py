import pathlib

LAB_PATH = pathlib.Path('Lab #1 - Connect to OpenAI and ask questions')

def test_notebooks_exist():
    notebooks = list(LAB_PATH.glob('*.ipynb'))
    assert notebooks, f"No notebooks found in {LAB_PATH}"
