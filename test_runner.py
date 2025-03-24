from student import Room, LuxuryRoom

def test_room_str():
    try:
        r = Room("Alice")
        output = str(r)
        return output == "Room booked for Alice", output
    except Exception as e:
        return False, f"Exception: {e}"

def test_luxury_str():
    try:
        lr = LuxuryRoom("Bob", 5)
        output = str(lr)
        return output == "Luxury Room booked for Bob with 5 minibar items", output
    except Exception as e:
        return False, f"Exception: {e}"

def test_del():
    try:
        r = Room("Charlie")
        del r
        return True, "Destructor called"
    except Exception as e:
        return False, f"Exception: {e}"

def test_issubclass():
    try:
        return issubclass(LuxuryRoom, Room), issubclass(LuxuryRoom, Room)
    except Exception as e:
        return False, f"Exception: {e}"

def run_all():
    tests = [
        ("TC1: Room __str__", test_room_str),
        ("TC2: LuxuryRoom __str__", test_luxury_str),
        ("TC3: Destructor", test_del),
        ("HTC1: issubclass check", test_issubclass)
    ]

    for name, fn in tests:
        try:
            passed, output = fn()
        except Exception as e:
            passed, output = False, f"Unhandled Exception: {e}"
        status = "Passed" if passed else "Failed"
        print(f"{name}: {status} | Output: {output}")

if __name__ == "__main__":
    run_all()
