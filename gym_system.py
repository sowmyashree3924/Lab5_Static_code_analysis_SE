"""Manage gym class bookings, capacities, and roster exports."""

import json
from pathlib import Path

CLASS_CAPACITY = {"Yoga": 3, "HIIT": 2, "Spin": 4}
ROSTERS: dict[str, list[str]] = {}
ATTENDANCE_HISTORY: list[str] = []


def book_class(
    member_id: str,
    class_name: str,
    attendance_log: list[str] | None = None,
) -> bool:
    """Book a member into a class if a seat is available."""
    capacity = CLASS_CAPACITY.get(class_name, 0)
    roster = ROSTERS.setdefault(class_name, [])

    if capacity <= 0 or len(roster) >= capacity:
        print("Class full or unavailable:", class_name)
        return False

    roster.append(str(member_id))
    log = ATTENDANCE_HISTORY if attendance_log is None else attendance_log
    log.append(f"{member_id} -> {class_name}")
    return True


def cancel_booking(member_id: str, class_name: str) -> bool:
    """Cancel a member's booking, returning whether it was found."""
    roster = ROSTERS.get(class_name)
    if roster is None or str(member_id) not in roster:
        print("Nothing to cancel")
        return False

    roster.remove(str(member_id))
    return True


def set_capacity(class_name: str, seats: int) -> None:
    """Set a class capacity; negative capacities are rejected."""
    if seats < 0:
        raise ValueError("Class capacity cannot be negative")
    CLASS_CAPACITY[class_name] = seats


def add_members(class_name: str, count: int) -> None:
    """Add the requested number of guest members to a class."""
    if count < 0:
        raise ValueError("Guest count cannot be negative")

    roster = ROSTERS.setdefault(class_name, [])
    next_guest_number = len(roster)
    for index in range(count):
        book_class(f"GUEST-{next_guest_number + index}", class_name)


def export_roster(file_name: str = "gym_schedule.json") -> None:
    """Export all current rosters as formatted JSON."""
    output_path = Path(file_name)
    with output_path.open("w", encoding="utf-8") as output_file:
        json.dump(ROSTERS, output_file, indent=4)
        output_file.write("\n")


def clear_old_exports(prefix: str = "old_") -> int:
    """Remove matching JSON exports from the current directory safely."""
    if Path(prefix).name != prefix or prefix in {"", ".", ".."}:
        raise ValueError("Prefix must be a simple filename prefix")

    removed_count = 0
    for export_path in Path.cwd().glob(f"{prefix}*.json"):
        if export_path.is_file():
            export_path.unlink()
            removed_count += 1
    return removed_count


def show_rosters() -> None:
    """Print all class rosters."""
    for class_name, members in sorted(ROSTERS.items()):
        print(f"{class_name}: {', '.join(members)}")


def main() -> None:
    """Run a short demonstration of the gym booking system."""
    book_class("M1", "Yoga")
    book_class("M2", "Yoga")
    book_class("M3", "Yoga")
    book_class("M4", "Yoga")
    book_class("55", "HIIT")
    book_class("M5", "Pilates")

    try:
        set_capacity("Spin", -2)
    except ValueError as error:
        print("Invalid capacity:", error)

    add_members("Spin", 3)
    cancel_booking("M9", "Boxing")

    guest_count_text = input(
        "How many walk-in guests for HIIT? (Enter for 1): "
    ).strip()
    try:
        guest_count = int(guest_count_text) if guest_count_text else 1
        add_members("HIIT", guest_count)
    except ValueError:
        print("Please enter a non-negative whole number.")

    clear_old_exports()
    export_roster()
    show_rosters()


if __name__ == "__main__":
    main()
