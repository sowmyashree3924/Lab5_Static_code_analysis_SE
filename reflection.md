# Reflection – Static Code Analysis

## 1. What was the most critical issue found?
The most critical issue was constructing a shell command using string concatenation in `clear_old_exports()`. Passing a variable into a shell command can make the operation unsafe and platform-dependent. I replaced it with Python's `pathlib` file operations and validated the filename prefix.

## 2. How did static analysis improve the code?
Static analysis helps identify defects and risky patterns before the program is executed. It also improves naming, exception handling, resource management, readability, and consistency. Fixing the findings makes the booking system easier to test and maintain.

## 3. Why is a mutable default argument problematic?
A mutable default object is created once when the function is defined and is reused across calls. This can cause data from one call to unexpectedly appear in another. Using `None` and creating/selecting the intended list inside the function avoids that hidden shared-default behavior.

## 4. Why should broad exception handling be avoided?
A bare `except:` catches almost every exception, including errors unrelated to the expected condition. This can hide bugs and make debugging difficult. The revised cancellation function checks whether the class and member exist and returns a clear result instead.

## 5. What did I learn?
I learned that static analysis complements runtime testing: it can point out risky code, style problems, and maintainability concerns early. I also learned to verify tool output after each change rather than assuming that code is clean because it runs.
