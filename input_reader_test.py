from input_reader import read_float, read_int
import inspect


# Hier die Definitionen von read_float und read_int einfügen

# Testfälle für read_float
def test_read_float_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3.14")
    assert read_float("Enter a float: ") == 3.14


def test_read_float_invalid_input(monkeypatch, capsys):
    inputs = iter(["no number", "3.14"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert read_float("Enter a float: ") == 3.14
    captured = capsys.readouterr()
    assert "Please, enter a real number!" in captured.out


def test_read_float_out_of_bounds(monkeypatch, capsys):
    # Hinzufügen eines zusätzlichen, gültigen Werts am Ende des Iterators
    inputs = iter(["4.5", "2.5", "3.5"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert read_float("Enter a float: ", lower_bound=3.0, upper_bound=4.0) == 3.5

    captured = capsys.readouterr()
    # Überprüfen auf beide Fehlermeldungen und erfolgreiche Eingabe
    assert "Please, enter a number less than or equal to 4.0" in captured.out
    assert "Please, enter a number greater than or equal to 3.0" in captured.out


def test_read_float_at_bounds(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "3.0")
    assert read_float("Enter a float: ", lower_bound=3.0, upper_bound=4.0) == 3.0


# Testfälle für read_int
def test_read_int_valid_input(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "42")
    assert read_int("Enter an int: ") == 42


def test_read_int_invalid_input(monkeypatch, capsys):
    inputs = iter(["not a number", "42"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    assert read_int("Enter an int: ") == 42
    captured = capsys.readouterr()
    assert "Please, enter a whole number!" in captured.out


def test_read_int_out_of_bounds(monkeypatch, capsys):
    # Hinzufügen eines zusätzlichen, gültigen Werts am Ende des Iterators
    inputs = iter(["50", "10", "30"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert read_int("Enter an int: ", lower_bound=20, upper_bound=40) == 30

    captured = capsys.readouterr()
    # Überprüfen auf beide Fehlermeldungen und erfolgreiche Eingabe
    assert "Please, enter a number less than or equal to 40" in captured.out
    assert "Please, enter a number greater than or equal to 20" in captured.out


def test_read_int_at_bounds(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "20")
    assert read_int("Enter an int: ", lower_bound=20, upper_bound=40) == 20


def test_docstring_contains_param_and_return_read_float():
    docstring = inspect.getdoc(read_float)
    assert docstring is not None, "Docstring fehlt"

    # Überprüfen, ob für jeden Parameter ein @param Tag vorhanden ist
    params = inspect.signature(read_float).parameters
    for param in params:
        assert f"param {param}:" in docstring, f"Docstring fehlt param für {param}"

    # Überprüfen, ob ein @return Tag vorhanden ist
    assert "return:" in docstring, "Docstring fehlt return"


def test_docstring_contains_param_and_return_read_int():
    docstring = inspect.getdoc(read_float)
    assert docstring is not None, "Docstring fehlt"

    # Überprüfen, ob für jeden Parameter ein @param Tag vorhanden ist
    params = inspect.signature(read_float).parameters
    for param in params:
        assert f"param {param}:" in docstring, f"Docstring fehlt param für {param}"

    # Überprüfen, ob ein @return Tag vorhanden ist
    assert "return:" in docstring, "Docstring fehlt return"