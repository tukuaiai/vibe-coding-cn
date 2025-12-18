# Production Incident Record: Strong/Weak Self-Assessment Standard Conflict

-   **Date**: 2025-12-17
-   **Impact**: Users reported contradictions in "strength judgment: slightly weak" and "strong self-assessment: strong" for the same Bazi chart, leading to misleading advice on favorable elements and a decrease in trust.
-   **Root Cause**: The code simultaneously output two sets of strength/weakness algorithm results—
    -   External library bazi-1 weak determination (`_calc_wuxing_scores.weakStrong`, including Changsheng/Diwang weights).
    -   Local self-written simplified algorithm `_calc_strength` (only counts Three Pillars' mutual generation and overcoming).
    Both were displayed in the report, leading to inconsistent standards.
-   **Resolution**: Removed local `_calc_strength` usage, unified to external library's weak determination as the sole source; report standards were unified accordingly.
-   **Code Change**: `services/telegram-service/src/bazi_calculator.py`
    -   `strength` only takes `wx_scores['weakStrong']`; deleted `_calc_strength` call and implementation.
-   **Subsequent Actions**:
    1.  Regression testing: Randomly check 10 Bazi charts to confirm a single strong/weak standard consistent with bazi-1's original output.
    2.  Add unit tests: Verify abnormal prompts when `weakStrong` is absent (currently no fallback).
    3.  Review other indicators (e.g., favorable elements, patterns) for potential dual-standard outputs.
    4.  **Mandatory Specification**: Forbid the introduction of any "self-written alternative algorithms" for core judgments (body strength/weakness, favorable elements, deities, patterns, etc.); must directly call the calculation results of external native libraries. Violators will be considered to have crossed a production red line.
