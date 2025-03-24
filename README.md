# 🏨 Hotel Room Allocation System

## 🎯 Concepts Tested
✅ `__init__`, `__str__`, `__del__`  
✅ Constructor with/without/default arguments  
✅ Inheritance & Method Resolution Order (MRO)  
✅ Method overriding and `super()` usage  

## 📌 Problem Statement
Design a hotel management system that models room allocation.  
Create a base class `Room` and a subclass `LuxuryRoom` to demonstrate:
- Constructor overloading
- Destructor invocation
- Method overriding
- Use of `super()` in constructors and string representations

## 📌 Operations

### 1. Base Class: `Room`
```python
class Room:
    def __init__(self, guest_name: str = "Guest"): ...
    def __str__(self) -> str: ...
    def __del__(self): ...
```

### 2. Subclass: `LuxuryRoom`
```python
class LuxuryRoom(Room):
    def __init__(self, guest_name: str, minibar_items: int): ...
    def __str__(self) -> str: ...
```

## ✅ Sample Visible Test Cases

### TC1: Base Room String Output
```python
r = Room("Alice")
print(str(r))
# Expected:
# Room constructor called for Alice
# Room booked for Alice
```

### TC2: Luxury Room String Override
```python
lr = LuxuryRoom("Bob", 5)
print(str(lr))
# Expected:
# Room constructor called for Bob
# LuxuryRoom constructor called for Bob
# Luxury Room booked for Bob with 5 minibar items
```

### TC3: Destructor Invocation
```python
r = Room("Charlie")
del r
# Expected:
# Room constructor called for Charlie
# Room destructor called for Charlie
```
