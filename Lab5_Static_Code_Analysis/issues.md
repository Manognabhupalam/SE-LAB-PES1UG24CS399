\# Lab 5 – Issue Identification and Fixes



| No. | Tool | Issue | Severity / Type | Fix Applied |

|---|---|---|---|---|

| 1 | Pylint | Missing module and function docstrings | Convention | Added documentation strings. |

| 2 | Pylint | camelCase naming | Convention | Changed function and variable names to snake\_case. |

| 3 | Pylint | Mutable default argument (`history=\[]`) | Warning | Used `history=None` and initialized a new list inside the function. |

| 4 | Pylint | Broad exception handling | Warning | Replaced `except Exception` with `except KeyError`. |

| 5 | Pylint | Simplifiable OR comparison | Refactoring | Used the `in` operator with a tuple. |

| 6 | Bandit | Unsafe temporary file creation (B306) | Medium | Replaced `tempfile.mktemp()` with `NamedTemporaryFile(delete=False)`. |

| 7 | Bandit | Shell command execution (B602) | High | Used an argument list, `shell=False`, and IP address validation. |

| 8 | Bandit | Weak random number generation (B311) | Low | Replaced `random.randint()` with `secrets.randbelow()`. |

| 9 | Flake8 | Missing whitespace around operator (E225) | Style | Added the required spaces. |

| 10 | Flake8 | Incorrect inline comment spacing (E261) | Style | Corrected comment spacing. |

| 11 | Flake8 | Missing whitespace after comma (E231) | Style | Added the required space. |

| 12 | Flake8 | Incorrect blank lines (E302/E305) | Style | Corrected blank lines around function definitions. |



\## Bandit Suppression Note



The final Bandit report identified no active issues. It also reported two potential checks explicitly disabled through `# nosec` comments. These suppressions are documented in the source code and should be reviewed if the relevant code changes.

