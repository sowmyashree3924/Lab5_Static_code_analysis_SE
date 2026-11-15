# Lab 5: Static Code Analysis

This lab improves the quality, security, and style of the gym booking program using Pylint, Bandit, and Flake8.

## Project files

- `gym_system.py` – revised Python program.
- `issues.md` – issue and remediation table.
- `reflection.md` – reflection answers.
- `reports/before/` – baseline reports to be captured from the original version.
- `reports/after/` – final reports to be generated after fixes.

## Windows PowerShell setup

Run these commands from the repository folder:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install pylint bandit flake8
```

If PowerShell blocks activation, use this for the current terminal only:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

## Capture the baseline (before fixes)

Keep a copy of the original assigned file as `gym_system_before.py` before replacing it with the corrected version. Run:

```powershell
python -m pylint gym_system_before.py | Tee-Object reports\before\pylint.txt
python -m bandit -r gym_system_before.py -f txt | Tee-Object reports\before\bandit.txt
python -m flake8 gym_system_before.py --statistics | Tee-Object reports\before\flake8.txt
```

These are the actual before-state reports required by the lab. Do not label reports generated from the corrected file as baseline reports.

## Analyze the corrected program

```powershell
python -m pylint gym_system.py --score=y | Tee-Object reports\after\pylint.txt
python -m bandit -r gym_system.py -f txt | Tee-Object reports\after\bandit.txt
python -m flake8 gym_system.py --statistics | Tee-Object reports\after\flake8.txt
```

Pylint target: score greater than 9.5/10. Bandit: no unresolved findings. Flake8: no reported violations. If a tool reports an issue, fix it and rerun all three tools. The final report files should contain the real command output from your environment.

## Runtime check

```powershell
python -m py_compile gym_system.py
python gym_system.py
```

Enter `1` when prompted. The program should reject the fourth Yoga booking, report the invalid negative Spin capacity, and export `gym_schedule.json` in the current directory.

## Required commit sequence

The lab asks for three separate commits corresponding to the tools. After each corresponding analysis/fix/report is complete, stage only the relevant files and commit:

```powershell
git add gym_system.py reports\after\pylint.txt
git commit -m "Fix code quality issues identified by Pylint"

git add gym_system.py reports\after\bandit.txt
git commit -m "Fix security issues identified by Bandit"

git add gym_system.py reports\after\flake8.txt issues.md reflection.md README.md reports\before\
git commit -m "Fix style issues and document static analysis"
```

Avoid committing generated files such as `.venv`, `__pycache__`, or `gym_schedule.json`.
