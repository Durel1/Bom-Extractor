# BOM Extractor PLM

## Description

BOM Extractor PLM is a Python-based engineering software project designed to import, validate, persist and analyze industrial Bills of Materials.

A BOM, or Bill of Materials, describes the hierarchical structure of a product, including its components, sub-assemblies, quantities, materials and weights. This project simulates a simplified PLM use case where product data must be extracted from files, validated according to business rules, stored in a relational database and analyzed through dedicated services.

The project was developed with a software engineering approach: clean architecture, SOLID principles, design patterns, unit tests, integration tests and Gitflow.

---

## Main Features

* Import BOM data from CSV files
* Import BOM data from JSON files
* Validate business rules before persistence
* Store parts in a relational SQL database
* Calculate the total weight of an assembly
* Analyze BOM structure:

  * total number of parts
  * materials used
  * number of parts by material
  * maximum tree depth
* Unit and integration testing with Pytest

---

## Technologies

* Python
* SQLAlchemy
* SQLite
* Pytest
* Pandas
* Git / Gitflow
* PlantUML

---

## Architecture

The project follows a simplified Clean Architecture approach.

```text
src/bom_extractor/

├── application/
│   ├── factories/
│   │   └── parser_factory.py
│   ├── interfaces/
│   │   ├── parser.py
│   │   └── repository.py
│   └── use_cases/
│       └── import_bom.py
│
├── domain/
│   └── services/
│       ├── weight_service.py
│       └── bom_analysis_service.py
│
├── infrastructure/
│   ├── parsers/
│   │   ├── csv_parser.py
│   │   └── json_parser.py
│   └── persistence/
│       ├── database.py
│       ├── entities.py
│       └── sql_repository.py
│
├── models.py
└── validator.py
```

---

## Design Patterns Used

### Repository Pattern

The project uses a repository interface to isolate the application from the database implementation.

```python
repository.save_all(parts)
```

The application depends on an abstraction, not directly on SQLAlchemy.

### Factory Pattern

The parser factory creates the correct parser depending on the file type.

```python
parser = ParserFactory.create("csv")
```

This makes the system extensible for future formats such as Excel or XML.

### Service Layer

Business algorithms are isolated in dedicated services:

* `WeightCalculationService`
* `BomAnalysisService`

This keeps business logic separate from parsing, persistence and presentation.

---

## SOLID Principles

### Single Responsibility Principle

Each component has one clear responsibility:

* Parser: reads input files
* Validator: checks business rules
* Repository: handles persistence
* Use Case: orchestrates the import process
* Services: perform business calculations

### Open / Closed Principle

New parsers can be added without modifying the use case.

### Dependency Inversion Principle

The use case depends on abstractions such as `BomParser` and `BomRepository`, not concrete implementations.

---

## Business Rules

Before saving a BOM, the system validates several rules:

* A part cannot have a negative weight
* A quantity must be strictly positive
* A part ID must be unique
* A parent part must exist
* A part cannot be its own parent
* A BOM must have exactly one root part

---

## Example BOM

```csv
part_id,name,parent_id,quantity,unit_weight,material
P001,Vélo,,1,0,ASSEMBLY
P002,Roue avant,P001,1,1.2,Aluminium
P003,Cadre,P001,1,2.5,Acier
P004,Pneu avant,P002,1,0.7,Caoutchouc
P005,Jante avant,P002,1,0.5,Aluminium
```

This represents the following structure:

```text
Vélo
├── Roue avant
│   ├── Pneu avant
│   └── Jante avant
└── Cadre
```

---

## Installation

Clone the project:

```bash
git clone https://github.com/your-username/bom-extractor-plm.git
cd bom-extractor-plm
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Tests

On Windows CMD:

```cmd
set PYTHONPATH=src
pytest
```

---

## Example Usage

```python
from bom_extractor.application.factories.parser_factory import ParserFactory
from bom_extractor.application.use_cases.import_bom import ImportBomUseCase
from bom_extractor.infrastructure.persistence.database import create_session_factory
from bom_extractor.infrastructure.persistence.sql_repository import SqlBomRepository
from bom_extractor.validator import BomValidator

Session = create_session_factory("sqlite:///bom.db")
session = Session()

parser = ParserFactory.create("csv")
validator = BomValidator()
repository = SqlBomRepository(session)

use_case = ImportBomUseCase(parser, validator, repository)
use_case.execute("data/sample_bom.csv")
```

---

## Tests

The project includes:

* Unit tests for the domain model
* Unit tests for business validation
* Unit tests for CSV and JSON parsers
* Unit tests for BOM analysis services
* Unit tests for weight calculation
* Integration tests for SQL persistence
* Integration tests for the import use case

---

## UML Diagram

The UML class diagram is available in:

```text
docs/uml_class_diagram.puml
```

It can be opened with PlantUML or a compatible VS Code extension.

---

## Engineering Approach

This project was built using a professional software engineering workflow:

1. Understand the business problem
2. Define business rules
3. Design the architecture
4. Write tests
5. Implement the feature
6. Refactor the code
7. Commit with clear Git messages
8. Document the system

---

## Future Improvements

* Add Excel parser
* Add XML parser
* Add a C++ module for intensive weight calculations
* Add a command-line interface
* Add Docker support
* Add CI/CD with GitHub Actions
* Add API layer with FastAPI

---

## Author

Durel Kenfack
Engineering student in Computer Science
Interested in software engineering, PLM systems and industrial digital transformation.
