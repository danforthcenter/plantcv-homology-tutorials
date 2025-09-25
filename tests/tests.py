import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def test_notebook(tmpdir):
    """Test the notebook."""
    tmp = tmpdir.mkdir('sub')
    # Open the notebook
    with open("acute_plm_tutorial_1.ipynb", "r") as f:
        nb = nbformat.read(f, as_version=4)

    # Process the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": os.getcwd()}})

    # Save the executed notebook
    out_nb = os.path.join(tmp, "executed_notebook.ipynb")
    with open(out_nb, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    assert os.path.exists(out_nb)


def test_notebook2(tmpdir):
    """Test the notebook."""
    tmp = tmpdir.mkdir('sub')
    # Open the notebook
    with open("acute_plm_tutorial_2.ipynb", "r") as f:
        nb = nbformat.read(f, as_version=4)

    # Process the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": os.getcwd()}})

    # Save the executed notebook
    out_nb = os.path.join(tmp, "executed_notebook.ipynb")
    with open(out_nb, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    assert os.path.exists(out_nb)
    

def test_notebook3(tmpdir):
    """Test the notebook."""
    tmp = tmpdir.mkdir('sub')
    # Open the notebook
    with open("acute_plm_tutorial_3.ipynb", "r") as f:
        nb = nbformat.read(f, as_version=4)

    # Process the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": os.getcwd()}})

    # Save the executed notebook
    out_nb = os.path.join(tmp, "executed_notebook.ipynb")
    with open(out_nb, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    assert os.path.exists(out_nb)
    
    
def test_notebook4(tmpdir):
    """Test the notebook."""
    tmp = tmpdir.mkdir('sub')
    # Open the notebook
    with open("acute_plm_tutorial_4.ipynb", "r") as f:
        nb = nbformat.read(f, as_version=4)

    # Process the notebook
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")
    ep.preprocess(nb, {"metadata": {"path": os.getcwd()}})

    # Save the executed notebook
    out_nb = os.path.join(tmp, "executed_notebook.ipynb")
    with open(out_nb, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    assert os.path.exists(out_nb)