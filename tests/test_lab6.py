import pathlib

LAB_PATH = pathlib.Path('Lab #6 - Speech recognition+ OpenAI')
SCRIPT_PATH = LAB_PATH / '1- Food ordering voice to text.py'

def test_notebooks_exist():
    notebooks = list(LAB_PATH.glob('*.ipynb'))
    assert notebooks, f"No notebooks found in {LAB_PATH}"

def test_voice_script_functions():
    text = SCRIPT_PATH.read_text(encoding='utf-8')
    assert 'def voice_to_text' in text, 'voice_to_text function missing'
    assert 'def call_openAI' in text, 'call_openAI function missing'
