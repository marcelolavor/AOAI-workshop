import pathlib

LAB_PATH = pathlib.Path('Lab #4 - Create embeddings with Faiss and Langchain')

def test_notebooks_exist():
    notebooks = list(LAB_PATH.glob('*.ipynb'))
    assert notebooks, f"No notebooks found in {LAB_PATH}"
