# **Development Experience and Project Specification Organization Document**

## Table of Contents

1.  Variable Name Maintenance Solution
2.  File Structure and Naming Conventions
3.  Coding Style Guide
4.  System Architecture Principles
5.  Core Ideas of Program Design
6.  Microservices
7.  Redis
8.  Message Queue

---

# **1. Variable Name Maintenance Solution**

## 1.1 Create a "Comprehensive Variable Name File"

Establish a unified variable index file for AI and overall team maintenance.

### File content includes (format example):

| Variable Name | Variable Comment (Description) | Location (File Path)       | Frequency (Statistics) |
| :------------ | :----------------------------- | :------------------------- | :--------------------- |
| user_age      | User age                       | /src/user/profile.js       | 12                     |

### Purpose

*   Unified variable naming
*   Convenient global search
*   AI or human can uniformly manage and refactor
*   Reduce the risk of naming conflicts and unclear semantics

---

# **2. File Structure and Naming Conventions**

## 2.1 Subfolder Content

Each subdirectory needs to contain:

*   `agents` - Responsible for automation processes, prompts, agent logic
*   `claude.md` - Stores documentation, design ideas, and usage for the content of this folder

## 2.2 File Naming Rules

*   Use **lowercase English + underscore** or **camelCase** (depending on the language)
*   Filenames should reflect content responsibilities
*   Avoid abbreviations and ambiguous naming

Examples:

*   `user_service.js`
*   `order_processor.py`
*   `config_loader.go`

## 2.3 Variable and Definition Rules and Explanations

*   Naming should be as semantic as possible
*   Follow English grammatical logic (noun attributes, verb behaviors)
*   Avoid meaningless names like `a, b, c`
*   Constants use uppercase + underscore (e.g., `MAX_RETRY_COUNT`)

---

# **3. Coding Style Guide**

### 3.1 Single Responsibility

Each file, class, and function should be responsible for only one thing.

### 3.2 Reusable Functions / Constructs (Reusable Components)

*   Extract common logic
*   Avoid duplicate code (DRY)
*   Modularize, functionalize, and improve reuse value

### 3.3 Consumer / Producer / State (Variables) / Transformation (Functions)

System behavior should be clearly divided:

| Concept              | Description                               |
| :------------------- | :---------------------------------------- |
| Consumer             | Where external data or dependencies are received |
| Producer             | Where data is generated and results are output |
| State (Variables)    | Variables storing current system information |
| Transformation (Functions) | Logic for processing states and changing data |

Clearly distinguish **Input → Process → Output** and manage each stage independently.

### 3.4 Concurrency

*   Clearly distinguish shared resources
*   Avoid data races
*   Use locks or thread-safe structures when necessary
*   Distinguish between "concurrent processing" and "asynchronous processing"

---

# **4. System Architecture Principles**

### 4.1 First Clarify the Architecture

Before writing code, clarify:

*   Module division
*   Input/output
*   Data flow
*   Service boundaries
*   Technology stack
*   Dependencies

### 4.2 Understand Requirements → Keep It Simple → Automated Testing → Small Iterations

Rigorous development process:

1.  First understand the requirements
2.  Keep architecture and code simple
3.  Write maintainable automated tests
4.  Iterate in small steps, avoid big-bang development

---

# **5. Core Ideas of Program Design**

## 5.1 Start from the problem, not from the code

The first step in programming is always: **What problem are you solving?**

## 5.2 Break large problems into small problems (Divide & Conquer)

Decompose complex problems into small, independently achievable units.

## 5.3 KISS Principle (Keep It Simple, Stupid)

Reduce complexity, magic code, obscure tricks.

## 5.4 DRY Principle (Don't Repeat Yourself)

Reuse logic with functions, classes, modules; don't copy-paste.

## 5.5 Clear Naming

*   `user_age` is clearer than `a`
*   `get_user_profile()` is clearer than `gp()`
    Naming should reflect **purpose** and **semantics**.

## 5.6 Single Responsibility

A function handles only one task.

## 5.7 Code Readability First

The code you write is for others to understand, not to show off.

<h2>5.8 Appropriate Comments</h2>

Comments explain "why," not "how."

## 5.9 Make it work → Make it right → Make it fast

First make it run, then make it beautiful, then optimize performance.

## 5.10 Errors are friends, debugging is a mandatory course

Reading errors, checking logs, and tracing layers are core programmer skills.

## 5.11 Git version control is essential

Never keep code only locally.

## 5.12 Test your code

Untested code will eventually have problems.

## 5.13 Programming is long-term practice

Everyone has experienced:

*   Can't debug a bug
*   Feeling like striking gold when it passes
*   Eventually understanding others' code

Persistence makes one an expert.

---

# **6. Microservices**

Microservices are an architectural pattern that breaks down a system into multiple **independently developed, independently deployed, and independently scalable** services.

Characteristics:

*   Each service handles a business boundary (Bounded Context)
*   Services communicate via APIs (HTTP, RPC, MQ, etc.)
*   More flexible, more scalable, higher fault tolerance

---

# **7. Redis (Cache / In-memory Database)**

The role of Redis:

*   Greatly improves system "read performance" as a cache
*   Reduces database pressure
*   Provides capabilities such as counters, locks, queues, sessions
*   Makes the system faster, more stable, and more resilient

---

# **8. Message Queue**

Message queues are used for "asynchronous communication" between services.

Purpose:

*   Decoupling
*   Peak shaving and valley filling
*   Asynchronous task processing
*   Improve system stability and throughput
