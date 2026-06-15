# AutoPKa
Simple script for pH value calculation. Entering acid pKa, concentration and base equivalent, you'll get pH value of solution immediately.
This Python script, **AutoPKa**, solves acid-base chemistry problems by calculating pH/pOH values using the **secant method** for numerical root-finding.

## Key Functionality:

1. **Input Phase**: Collects pKa/pKb values and concentrations for multiple acids/bases, plus the concentration of added base/acid and two initial pH/pOH estimates.

2. **Core Algorithm**: 
   - Defines a function `f(Hplus)` that represents the charge balance equation in solution
   - Uses the **secant method** (an iterative root-finding technique) to converge on the correct [H⁺] concentration
   - Runs two separate iterations from different starting points

3. **Helper Functions**:
   - `multiply(l,b)`: Multiplies the first `b` elements of a list
   - `g(Hplus,Ka,i)`: Calculates the contribution of the i-th acid/base to the charge balance

4. **Output**: Reports the final pH/pOH value (formatted to 5 decimal places), iteration count, and CPU time in milliseconds.

5. **Error Handling**: Catches convergence failures and prompts the user to adjust initial values if needed.

The script includes a humorous random message at the end (incomplete in the snippet shown).
