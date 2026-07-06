# 🐛 BROKEN – Module 05, Lesson 43 (Set Operations)
# Using '-' operator on sets incorrectly? Actually set difference is '-' but must use sets, not lists.
# This script tries to do list difference.
a = [1,2,3]
b = [3,4,5]
c = a - b   # ❌ TypeError: unsupported operand type(s) for -: 'list' and 'list'
