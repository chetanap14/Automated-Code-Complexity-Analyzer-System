import pycodestyle

def check_pep8(file_path):
    """
    Check the Python file for PEP8 style issues.
    Returns a list of warnings with line numbers.
    """
    style_guide = pycodestyle.StyleGuide(quiet=True)
    report = style_guide.check_files([file_path])
    
    warnings = []
    for error in report.get_statistics(''):
        warnings.append(error)
    
    return warnings
