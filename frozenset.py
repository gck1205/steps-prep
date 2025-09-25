"""
Frozen sets in Python are immutable objects that only support methods and operators 
that produce a result without affecting the frozen set or sets to which they are applied. 
While elements of a set can be modified at any time, elements of the frozen set remain the 
same after creation.
"""
# Same as {"a", "b","c"}
normal_set = set(["a", "b","c"])

print("Normal Set")
print(normal_set)

# A frozen set
frozen_set = frozenset(["e", "f", "g"])

print("\nFrozen Set")
print(frozen_set)

# Uncommenting below line would cause error as
# we are trying to add element to a frozen set
# frozen_set.add("h")