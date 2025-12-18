# General Project Architecture Template

## 1️⃣ Standard Structure for Python Web/API Projects

```
project_name/
├── README.md                 # Project README
├── LICENSE                   # Open-source license
├── requirements.txt          # Dependency management (pip)
├── pyproject.toml           # Modern Python project configuration (recommended)
├── setup.py                 # Package installation script (if packaged as a library)
├── .gitignore              # Git ignore file
├── .env                    # Environment variables (not committed to Git)
├── .env.example            # Example environment variables
├── CLAUDE.md              # Claude persistent context
├── AGENTS.md              # Codex persistent context
├── Sublime-Text.txt                   # For requirements and notes, for self-reference, and CLI session recovery commands ^_^
│
├── docs/                   # Documentation directory
│   ├── api.md             # API documentation
│   ├── development.md     # Development guide
│   └── architecture.md    # Architecture description
│
├── scripts/               # Script tools
│   ├── deploy.sh          # Deployment script
│   ├── backup.sh          # Backup script
│   └── init_db.sh         # Database initialization
│
├── tests/                 # Test code
│   ├── __init__.py
│   ├── conftest.py        # pytest configuration
│   ├── unit/              # Unit tests
│   ├── integration/       # Integration tests
│   └── test_config.py     # Configuration tests
│
├── src/                   # Source code (recommended)
│   ├── __init__.py
│   ├── main.py           # Program entry point
│   ├── app.py            # Flask/FastAPI application
│   ├── config.py         # Configuration management
│   │
│   ├── core/             # Core business logic
│   │   ├── __init__.py
│   │   ├── models/       # Data models
│   │   ├── services/     # Business services
│   │   └── utils/        # Utility functions
│   │
│   ├── api/              # API interface layer
│   │   ├── __init__.py
│   │   ├── v1/           # Version 1
│   │   └── dependencies.py
│   │
│   ├── data/             # Data processing
│   │   ├── __init__.py
│   │   ├── repository/   # Data access layer
│   │   └── migrations/   # Database migrations
│   │
│   └── external/         # External services
│       ├── __init__.py
│       ├── clients/      # API clients
│       └── integrations/ # Integration services
│
├── logs/                  # Log directory (not committed to Git)
│   ├── app.log
│   └── error.log
│
└── data/                  # Data directory (not committed to Git)
    ├── raw/               # Raw data
    ├── processed/         # Processed data
    └── cache/             # Cache
```

**Use Cases**: Flask/FastAPI Web applications, RESTful API services, Web backends

---

## 2️⃣ Standard Structure for Data Science/Quant Projects

```
project_name/
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── .env
├── .env.example
├── CLAUDE.md              # Claude persistent context
├── AGENTS.md              # Codex persistent context
├── Sublime-Text.txt                   # For requirements and notes, for self-reference, and CLI session recovery commands ^_^
│
├── docs/                   # Documentation directory
│   ├── notebooks/         # Jupyter documentation
│   └── reports/           # Analysis reports
│
├── notebooks/             # Jupyter Notebook
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
│
├── scripts/               # Script tools
│   ├── train_model.py     # Training script
│   ├── backtest.py        # Backtest script
│   ├── collect_data.py    # Data collection
│   └── deploy_model.py    # Model deployment
│
├── tests/                 # Tests
│   ├── test_data/
│   └── test_models/
│
├── configs/               # Configuration files
│   ├── model.yaml
│   ├── database.yaml
│   └── trading.yaml
│
├── src/                   # Source code
│   ├── __init__.py
│   │
│   ├── data/              # Data processing module
│   │   ├── __init__.py
│   │   ├── collectors/    # Data collectors
│   │   ├── processors/    # Data cleaning
│   │   ├── features/      # Feature engineering
│   │   └── loaders.py     # Data loaders
│   │
│   ├── models/            # Model module
│   │   ├── __init__.py
│   │   ├── strategies/    # Trading strategies
│   │   ├── backtest/      # Backtest engine
│   │   └── risk/          # Risk management
│   │
│   ├── utils/             # Utility module
│   │   ├── __init__.py
│   │   ├── logging.py     # Log configuration
│   │   ├── database.py    # Database tools
│   │   └── api_client.py  # API client
│   │
│   └── core/              # Core module
│       ├── __init__.py
│       ├── config.py      # Configuration management
│       ├── signals.py     # Signal generation
│       └── portfolio.py   # Portfolio
│
├── data/                  # Data directory (Git ignored)
│   ├── raw/               # Raw data
│   ├── processed/         # Processed data
│   ├── external/          # External data
│   └── cache/             # Cache
│
├── models/                # Model files (Git ignored)
│   ├── checkpoints/       # Checkpoints
│   └── exports/           # Exported models
│
└── logs/                  # Logs (Git ignored)
    ├── trading.log
    └── errors.log
```

**Use Cases**: Quantitative trading, machine learning, data analysis, AI research

---

## 3️⃣ Monorepo (Multi-Project Repository) Standard Structure

```
project_name-monorepo/
├── README.md
├── LICENSE
├── .gitignore
├── .gitmodules           # Git submodules
├── docker-compose.yml    # Docker orchestration
├── CLAUDE.md              # Claude persistent context
├── AGENTS.md              # Codex persistent context
├── Sublime-Text.txt                   # This is a file, for requirements and notes, for self-reference, and CLI session recovery commands ^_^
│
├── docs/                 # Global documentation
│   ├── architecture.md
│   └── deployment.md
│
├── scripts/              # Global scripts
│   ├── build_all.sh
│   ├── test_all.sh
│   └── deploy.sh
│
├── backups/                 # Backup files
│   ├── archive/             # Old backup files
│   └── gz/                  # Gzip backup files
│
├── services/             # Microservice directory
│   │
│   ├── user-service/     # User service
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── src/
│   │   └── tests/
│   │
│   ├── trading-service/  # Trading service
│   │   ├── Dockerfile
│   │   ├── requirements.txt
│   │   ├── src/
│   │   └── tests/
│   ...
│   └── data-service/     # Data service
│       ├── Dockerfile
│       ├── requirements.txt
│       ├── src/
│       └── tests/
│
├── libs/                 # Shared libraries
│   ├── common/           # Common modules
│   │   ├── utils/
│   │   └── models/
│   ├── external/         # Third-party libraries (immutable, call only)
│   └── database/         # Database access library
│
├── infrastructure/       # Infrastructure
│   ├── terraform/        # Cloud resource definition
│   ├── kubernetes/       # K8s configuration
│   └── nginx/            # Reverse proxy configuration
│
└── monitoring/           # Monitoring system
    ├── prometheus/       # Metrics collection
    ├── grafana/          # Visualization
    └── alertmanager/     # Alerts
```

**Use Cases**: Microservice architecture, large projects, team collaboration

---

## 4️⃣ Standard Structure for Full-Stack Web Applications

```
project_name/
├── README.md
├── LICENSE
├── .gitignore
├── docker-compose.yml    # Frontend and backend orchestration
├── CLAUDE.md              # Claude persistent context
├── AGENTS.md              # Codex persistent context
├── Sublime-Text.txt                   # This is a file, for requirements and notes, for self-reference, and CLI session recovery commands ^_^
│
├── frontend/             # Frontend directory
│   ├── public/           # Static assets
│   ├── src/              # Source code
│   │   ├── components/   # React/Vue components
│   │   ├── pages/        # Pages
│   │   ├── store/        # State management
│   │   └── utils/        # Utilities
│   ├── package.json      # NPM dependencies
│   └── vite.config.js    # Build configuration
│
└── backend/              # Backend directory
    ├── requirements.txt
    ├── Dockerfile
    ├── src/
    │   ├── api/          # API interfaces
    │   ├── core/         # Business logic
│   │   └── models/       # Data models
    └── tests/
```

**Use Cases**: Full-stack applications, SPA single-page applications, frontend/backend separated projects

---

## 📌 Core Design Principles

### 1. Separation of Concerns
```
API → Service → Data Access → Database
Clear at a glance, clear hierarchy
```

### 2. Testability
```
Each module is independently testable
Dependencies can be mocked
```

### 3. Configurability
```
Configuration separated from code
Environment variables > Configuration files > Default values
```

### 4. Maintainability
```
Self-documenting code
Reasonable file naming
Clear directory structure
```

### 5. Version Control Friendly (Git-Friendly)
```
data/, logs/, models/ added to .gitignore
Only commit source code and configuration examples
```

---

## 🎯 Best Practice Recommendations

1.  **Use `src/` directory**: Place source code in a dedicated `src` directory to avoid top-level clutter.
2.  **Relative imports**: Consistently use `from src.module import thing` for imports.
3.  **Test coverage**: Ensure core business logic has unit and integration tests.
4.  **Document first**: Write `README.md` for important modules.
5.  **Environment isolation**: Use virtualenv or conda to create isolated environments.
6.  **Explicit dependencies**: All dependencies written to `requirements.txt` and versions locked.
7.  **Configuration management**: Use a combination of environment variables + configuration files.
8.  **Logging levels**: DEBUG, INFO, WARNING, ERROR, FATAL.
9.  **Error handling**: Do not swallow exceptions; have a complete error chain.
10. **Code style**: Use black for formatting, flake8 for checking.

---

## 🔥 .gitignore Recommended Template

```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
*.egg-info/
dist/
build/

# Environment
.env
.venv/
env/
venv/
ENV/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# Data
data/
*.csv
*.json
*.db
*.sqlite
*.duckdb

# Logs
logs/
*.log

# Models
models/
*.h5
*.pkl

# Temporary files
tmp/
temp/
*.tmp
.DS_Store
```

---

## 📚 Technology Selection Reference

| Scenario | Recommended Tech Stack |
| :------- | :--------------------- |
| Web API  | FastAPI + Pydantic + SQLAlchemy |
| Data Processing | Pandas + NumPy + Polars |
| Machine Learning | Scikit-learn + XGBoost + LightGBM |
| Deep Learning | PyTorch + TensorFlow |
| Databases | PostgreSQL + Redis |
| Message Queue | RabbitMQ / Kafka |
| Task Queue | Celery |
| Monitoring | Prometheus + Grafana |
| Deployment | Docker + Docker Compose |
| CI/CD | GitHub Actions / GitLab CI |

---

## 📝 File Template Examples

### requirements.txt
```txt
# Core dependencies
fastapi==0.104.1
uvicorn[standard]==0.24.0
pydantic==2.5.0

# Database
sqlalchemy==2.0.23
alembic==1.12.1
psycopg2-binary==2.9.9

# Testing
pytest==7.4.3
pytest-cov==4.1.0
pytest-asyncio==0.21.1

# Utilities
python-dotenv==1.0.0
loguru==0.7.2

# Development (optional)
black==23.11.0
flake8==6.1.0
mypy==1.7.1
```

### pyproject.toml (Recommended for modern Python projects)
```toml
[project]
name = "Project Name"
version = "0.1.0"
description = "Project Description"
authors = [{name = "Author", email = "email@example.com"}]
dependencies = [
    "fastapi>=0.104.0",
    "uvicorn[standard]>=0.24.0",
    "sqlalchemy>=2.0.0",
]

[project.optional-dependencies]
dev = ["pytest", "black", "flake8", "mypy"]

[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

---

## ✅ New Project Checklist

When starting a new project, ensure the following are completed:

- [ ] Create README.md, including project overview and usage instructions.
- [ ] Create LICENSE file, clarifying the open-source license.
- [ ] Set up Python virtual environment (venv/conda).
- [ ] Create requirements.txt and lock dependency versions.
- [ ] Create .gitignore, excluding sensitive and unnecessary files.
- [ ] Create .env.example, explaining required environment variables.
- [ ] Design directory structure, adhering to the principle of separation of concerns.
- [ ] Create basic configuration files.
- [ ] Set up code formatter (black).
- [ ] Set up code checker (flake8/ruff).
- [ ] Write the first test case.
- [ ] Set up Git repository and commit initial code.
- [ ] Create CHANGELOG.md, recording version changes.

---

In **programming / software development**, **Project Architecture / Software Architecture** refers to:

> **The design solution for how a project is broken down, organized, communicated, and evolved at the "overall level"**
> —it determines how code is layered, how modules are divided, how data flows, and how the system expands and is maintained.

---

## One-Sentence Understanding

**Project Architecture = Deciding "where the code goes, how modules connect, and how responsibilities are divided" before writing any specific business code.**

---

## I. What Problems Does Project Architecture Primarily Solve?

Project architecture is not about "coding skills," but about solving these **higher-level problems**:

*   📦 How to organize code to avoid chaos?
*   🔁 How do modules communicate?
*   🧱 Which parts can be modified independently without affecting the whole?
*   🚀 How will the project be extended in the future?
*   🧪 How to facilitate testing, debugging, and deployment?
*   👥 How to collaborate without stepping on each other's code?

---

## II. What Does Project Architecture Generally Include?

### 1️⃣ Directory Structure (Most Intuitive)

```text
project/
├── src/
│   ├── main/
│   ├── services/
│   ├── models/
│   ├── utils/
│   └── config/
├── tests/
├── docs/
└── README.md
```

👉 Determines **"where different types of code are placed"**.

---

### 2️⃣ Layered Design (Core)

The most common is **Layered Architecture**:

```text
Presentation Layer (UI / API)
   ↓
Business Logic Layer (Service)
   ↓
Data Access Layer (DAO / Repository)
   ↓
Database / External Systems
```

**Rules:**

*   Upper layers can call lower layers.
*   Lower layers cannot depend on upper layers.

---

### 3️⃣ Module Partitioning (Responsibility Boundaries)

For example, a trading system:

```text
- market_data   # Market data
- strategy      # Strategy
- risk          # Risk control
- order         # Order placement
- account       # Account
```

👉 Each module:

*   Does only one type of thing.
*   Aims for low coupling, high cohesion.

---

### 4️⃣ Data and Control Flow

*   Where does the data come from?
*   Who is responsible for processing?
*   Who is responsible for storage?
*   Who is responsible for external output?

For example:

```text
WebSocket → Data Cleaning → Indicator Calculation → AI Scoring → SQLite → API → Frontend
```

---

### 5️⃣ Technology Selection (Part of Architecture)

*   Programming languages (Python / Java / Go)
*   Frameworks (FastAPI / Spring / Django)
*   Communication methods (HTTP / WebSocket / MQ)
*   Storage (SQLite / Redis / PostgreSQL)
*   Deployment (Local / Docker / Cloud)

---

## III. Common Project Architecture Types (Essential for Beginners)

### 1️⃣ Monolithic Architecture

```text
One project, one process
```

**Suitable for:**

*   Personal projects
*   Prototypes
*   Small systems

**Advantages:**

*   Simple
*   Easy to debug

**Disadvantages:**

*   Difficult to scale later

---

### 2️⃣ Layered Architecture (Most Common)

```text
Controller → Service → Repository
```

**Suitable for:**

*   Web backends
*   Business systems

---

### 3️⃣ Modular Architecture

```text
core + plugins
```

**Suitable for:**

*   Pluggable systems
*   Strategy / indicator systems

👉 **Very suitable for quant, AI analysis you are doing.**

---

### 4️⃣ Microservice Architecture (Advanced)

```text
Each service is an independent process + API communication
```

**Suitable for:**

*   Large teams
*   High concurrency
*   Long-term evolution

❌ **Not recommended for beginners to start with.**

---

## IV. Understanding with a "Real Example" (Close to what you are doing now)

Suppose you are building a **Binance Futures AI Analysis System**:

```text
backend/
├── data/
│   └── binance_ws.py        # Market data subscription
├── indicators/
│   └── vpvr.py
├── strategy/
│   └── signal_score.py
├── storage/
│   └── sqlite_writer.py
├── api/
│   └── http_server.py
└── main.py
```

This is **project architecture design**:

*   Each folder is responsible for one thing.
*   Replaceable, testable.
*   Later, if you want to connect a Telegram Bot / Web frontend, you don't need to rewrite the core.

---

## V. Common Misconceptions for Beginners ⚠️

❌ Starting with microservices
❌ All code in one file
❌ Architecture pursuing "seniority" rather than "maintainability"
❌ Starting to write code without clearly thinking about data flow

---

## VI. Suggested Learning Path (Very Important)

If you are learning CS now, this order is highly recommended:

1.  **First write runnable projects (imperfect).**
2.  **Code becomes messy → then learn architecture.**
3.  Learn:

    *   Module decomposition
    *   Layering
    *   Dependency direction
4.  Then learn:

    *   Design patterns
    *   Microservices / message queues

---

**Version**: 1.0
**Update Date**: 2025-11-24
**Maintained by**: CLAUDE, CODEX, KIMI
