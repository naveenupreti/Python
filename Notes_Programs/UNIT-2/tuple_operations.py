# ============================================================
# Program: Tuple Operations Demonstration
# Purpose: To show which operations work or don’t work on tuples
# ============================================================

print("=== OPERATIONS ON TUPLES ===")

# Create two sample tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
print("Original tuples:")
print("t1 =", t1)
print("t2 =", t2)

# --- 1️⃣ Concatenation ---
print("\n1️⃣ Concatenation (+ operator)")
result = t1 + t2
print("t1 + t2 =", result)  # (1, 2, 3, 4, 5, 6)
print("✅ Concatenation works on tuples")

# --- 2️⃣ Merging ---
print("\n2️⃣ Merging")
print("# Tuples are immutable, merging is done using +")
merged = t1 + t2
print("Merged tuple:", merged)
print("✅ Merging works (via +) but original tuples remain unchanged")

# --- 3️⃣ Conversion ---
print("\n3️⃣ Conversion Works")
print("list(t1) ->", list(t1))
print("set(t1)  ->", set(t1))
print("✅ Conversion from tuple to other types works")

# --- 4️⃣ Aliasing ---
print("\n4️⃣ Aliasing")
alias = t1
print("alias:", alias)
print("t1:", t1)
print("✅ Aliasing works (same object reference)")
# But we cannot modify either, since tuples are immutable

# --- 5️⃣ Cloning ---
print("\n5️⃣ Cloning")
clone = tuple(t1)
print("clone:", clone)
print("t1 is clone ->", t1 is clone)
print("✅ Cloning possible but both look same (since immutable)")

# --- 6️⃣ Searching ---
print("\n6️⃣ Searching Elements")
print("2 in t1 ->", 2 in t1)
print("10 in t1 ->", 10 in t1)
print("✅ Searching using 'in' works fine")

# --- 7️⃣ Identity ---
print("\n7️⃣ Identity")
print("t1 is alias ->", t1 is alias)
print("t1 is clone ->", t1 is clone)
print("✅ Identity check works")

# --- 8️⃣ Comparison ---
print("\n8️⃣ Comparison")
print("(1, 2, 3) == (1, 2, 3) ->", (1, 2, 3) == (1, 2, 3))
print("(1, 2, 3) < (2, 0, 0) ->", (1, 2, 3) < (2, 0, 0))
print("✅ Comparison (<, >, ==) works on tuples")

# --- 9️⃣ Emptiness ---
print("\n9️⃣ Emptiness Check")
empty_tuple = ()
print("not empty_tuple ->", not empty_tuple)
print("not t1 ->", not t1)
print("✅ Emptiness check works using 'not tuple'")

# --- Summary ---
print("\n" + "="*70)
print("🎯 SUMMARY OF OPERATIONS ON TUPLES")
print("- Concatenation (+): ✅")
print("- Merging (+): ✅")
print("- Conversion: ✅")
print("- Aliasing: ✅")
print("- Cloning: ✅")
print("- Searching (in): ✅")
print("- Identity (is): ✅")
print("- Comparison (<,>): ✅")
print("- Emptiness (not): ✅")
print("="*70)
