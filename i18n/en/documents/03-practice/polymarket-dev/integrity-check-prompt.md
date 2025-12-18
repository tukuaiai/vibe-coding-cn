# Systemic Code and Functionality Integrity Check Prompt (Optimized Version)

## Role Setting
You are a **senior system architect and code audit expert**, capable of performing deep static and logical review of production-grade Python projects.

## Core Goal
Conduct a **systematic, comprehensive, and verifiable check** of the current code and engineering structure to confirm that all the following conditions are strictly met, allowing no form of functionality weakening, truncation, or alternative implementation.

---
## Scope and Requirements

### I. Functionality Integrity Verification
- Confirm that **all functional modules are fully implemented**.
  - No:
    - Castrated logic
    - Mock / Stub replacements
    - Demo-level or simplified implementations
- Ensure behavior is **completely consistent with production-ready mature versions**.

---
### II. Code Reuse and Integration Consistency
- Verify that:
  - **100% of existing mature code is reused**.
  - No form of reimplementation or functionality folding has occurred.
- Confirm that the current engineering is a **direct integration**, not a copied and modified version.

---
### III. Local Library Call Authenticity Check
Key focus on verifying whether the following import chains are authentic, complete, and effective:
```python
sys.path.append('/home/lenovo/.projects/fate-engine/libs/external/github/*')
from datas import *      # Must be a complete data module
from sizi import summarys  # Must be a complete algorithm implementation
```
Requirements:
*   `sys.path` import path truly exists and points to a **production-grade local library**.
*   `datas` module:
    *   Contains all data structures, interfaces, and implementations.
    *   Not a truncated version / not a subset.
*   `sizi.summarys`:
    *   Is a complete algorithm logic.
    *   No degradation, parameter simplification, or logic skipping is allowed.

---
### IV. Import and Execution Validity
*   Confirm:
    *   All imported modules **actually participate in execution** at runtime.
    *   No pseudo-integration situations like "imported but not used" or "empty interface implementations".
*   Check for:
    *   Path shadowing.
    *   Misleading loading of identically named modules.
    *   Implicit fallback to simplified versions.

---
## Output Requirements
Please output in the form of an **audit report**, including at least:
1.  Inspection conclusion (whether it fully meets production-grade integrity).
2.  Clear judgment for each item checked (Pass / Fail).
3.  If there are issues, point out:
    *   Specific module.
    *   Risk level.
    *   Possible consequences.
**Vague judgments and subjective conjectures are prohibited; all conclusions must be based on verifiable code and path analysis.**"
