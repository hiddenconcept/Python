# Try to:
#
#     minimize the number of print() function invocations by inserting the \n sequence into the strings;
#     make the arrow twice as large (but keep the proportions)
#     duplicate the arrow, placing both arrows side by side; note: a string may be multiplied by using the following trick: "string" * 2 will produce "stringstring" (we'll tell you more about it soon)
#     remove any of the quotes, and look carefully at Python's response; pay attention to where Python sees an error ‒ is this the place where the error really exists?
#     do the same with some of the parentheses;
#     change any of the print words into something else, differing only in case (e.g., Print) ‒ what happens now?
#     replace some of the quotes with apostrophes; watch what happens carefully.

print("Original:")

print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

#Minimize the number of print() calls
print("Minimize the number of print() calls:")

print("    *\n   * *\n  *   *\n *     *\n***   ***\n  *   *\n  *   *\n  *****")

#2. Make the arrow twice as large
print("Make the arrow twice as large:")

print("        *\n"
      "       * *\n"
      "      *   *\n"
      "     *     *\n"
      "    *       *\n"
      "   *         *\n"
      "******     ******\n"
      "     *       *\n"
      "     *       *\n"
      "     *       *\n"
      "     *********")
#3. Duplicate the arrow side by side

print("Duplicate the arrow:")

print(("    *\n"
       "   * *\n"
       "  *   *\n"
       " *     *\n"
       "***   ***\n"
       "  *   *\n"
       "  *   *\n"
       "  *****\n") * 2)

#Print side by side
print("Duplicate arrow side by side")

print("    *    " * 2)
print("   * *   " * 2)
print("  *   *  " * 2)
print(" *     * " * 2)
print("***   ***" * 2)
print("  *   *  " * 2)
print("  *   *  " * 2)
print("  *****  " * 2)