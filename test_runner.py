from student import Room, LuxuryRoom

def test_room_str():
    r = Room("Alice")
    output = str(r)
    return output == "Room booked for Alice", output

def test_luxury_str():
    lr = LuxuryRoom("Bob", 5)
    output = str(lr)
    return output == "Luxury Room booked for Bob with 5 minibar items", output

def test_del():
    r = Room("Charlie")
    try:
        del r
        return True, "Destructor called"
    except Exception as e:
        return False, str(e)

def test_issubclass():
    return issubclass(LuxuryRoom, Room), issubclass(LuxuryRoom, Room)

def run_all():
    tests = [
        ("TC1: Room __str__", test_room_str),
        ("TC2: LuxuryRoom __str__", test_luxury_str),
        ("TC3: Destructor", test_del),
        ("HTC1: issubclass check", test_issubclass)
    ]

    for name, fn in tests:
        passed, output = fn()
        status = "✅ Passed" if passed else "❌ Failed"
        print(f"{name}: {status} | Output: {output}")

if __name__ == "__main__":
    run_all()
