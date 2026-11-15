# Static Code Analysis – Issues and Fixes

Target: `gym_system.py`

| # | Tool / category | Original issue | Risk / impact | Fix applied | Priority |
|---|---|---|---|---|---|
| 1 | Pylint / correctness | `len(roster) > capacity` allowed one extra booking | Class could exceed its seat limit | Changed condition to `len(roster) >= capacity` and rejects unavailable classes | High |
| 2 | Pylint / Python design | Mutable default `attendance_log=[]` was shared between calls | State could leak between bookings | Replaced with `None` and selected a module-level history list when omitted | Medium |
| 3 | Bandit / command injection | `os.system("rm -f " + prefix + "*.json")` built a shell command from a variable | Shell metacharacters could alter the command; command was not portable | Replaced shell execution with `Path.glob()` and `Path.unlink()`, and validated the prefix | High |
| 4 | Pylint / exception handling | Bare `except:` in cancellation swallowed unrelated errors | Unexpected programming errors were hidden | Removed broad exception handling and checked the roster/member explicitly | Medium |
| 5 | Pylint / resource handling | Export file was opened without a context manager or explicit close | File handles could remain open and data might not flush promptly | Used `Path.open()` with `with` and UTF-8 encoding | Medium |
| 6 | Flake8 / naming | `addMembers` did not follow snake_case | Inconsistent Python naming style | Renamed to `add_members` | Low |
| 7 | Correctness / validation | Negative capacity and guest count were accepted | Invalid class configuration and input | Added `ValueError` validation and handled invalid interactive input | Medium |
| 8 | Maintainability | `main()` ran whenever the module was imported | Importing the module unexpectedly prompted users and changed files | Added the `if __name__ == "__main__"` guard | Medium |
| 9 | Maintainability | Unused `os` import after removing shell execution | Unnecessary dependency/import | Removed `os` | Low |

## Verification status

The source has been reviewed and Python syntax/runtime checks can be run locally. Pylint, Bandit, and Flake8 reports must be generated in the student's Windows virtual environment because this execution environment could not reach the Python package index to install those tools. No tool scores or clean scan results are fabricated here.
