# 📊 GH Insights

[![Build](https://github.com/CoderDeltaLAN/gh-insights/actions/workflows/ci.yml/badge.svg)](https://github.com/CoderDeltaLAN/gh-insights/actions)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![Lint: Ruff](https://img.shields.io/badge/lint-ruff-46a2f1)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

CLI en **Python** para explorar **repositorios** y **lenguajes** de GitHub desde la terminal, con salida bonita usando **Rich**.  
Incluye entorno profesional: **Poetry**, **pre-commit** (Ruff/Black/MyPy), **pytest** y **CI/CD** en GitHub Actions.

---

## 🚀 Requisitos

- Python **3.12**
- **Poetry**

---

## 🔧 Instalación

Clona el repositorio e instala las dependencias:

```bash
git clone https://github.com/CoderDeltaLAN/gh-insights.git
cd gh-insights
poetry install
```

> Opcional (más cuota de API): exporta un token de GitHub antes de usar:
>
> ```bash
> export GITHUB_TOKEN=tu_token_personal
> ```

---

## 📖 Uso rápido

### 1) Top repos por ⭐ de un usuario

```bash
poetry run python -m gh_insights top-repos torvalds --limit 5
```

Ejemplo de salida:

```
       Top repos por ⭐ de torvalds        
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━┓
┃ Repositorio         ┃     ⭐ ┃ Lenguaje ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━┩
│ torvalds/linux      │ 200447 │ C        │
│ torvalds/uemacs     │   1535 │ C        │
│ torvalds/test-tlb   │    809 │ C        │
│ torvalds/pesconvert │    447 │ C        │
│ torvalds/1590A      │    401 │ OpenSCAD │
└─────────────────────┴────────┴──────────┘
```

### 2) Lenguajes de un repositorio

```bash
poetry run python -m gh_insights langs torvalds/linux
```

Ejemplo de salida:

```
     📊 Lenguajes en     
     torvalds/linux      
┏━━━━━━━━━━━━━━━┳━━━━━━━┓
┃ Lenguaje      ┃     % ┃
┡━━━━━━━━━━━━━━━╇━━━━━━━┩
│ C             │ 98.2% │
│ Assembly      │  0.7% │
│ Shell         │  0.4% │
└───────────────┴───────┘
```

---

## 🧪 Calidad de código

Ejecuta tests y validaciones locales:

```bash
# Tests
poetry run pytest -q

# Linters / formato / tipos
poetry run pre-commit run --all-files
```

---

## 🛠️ Desarrollo (estructura)

```
.
├── src/gh_insights/
│   ├── __init__.py
│   ├── __main__.py     # CLI (subcomandos: top-repos, langs)
│   └── api.py          # llamadas a la API de GitHub
├── tests/
│   ├── test_api.py
│   ├── test_cli.py
│   └── test_langs.py
├── .github/workflows/ci.yml
├── .pre-commit-config.yaml
├── pyproject.toml
└── README.md
```

---

## 🔄 CI/CD

El workflow **CI / build** valida automáticamente:
- Instalación con Poetry.
- **Ruff** (lint), **Black** (formato).
- **MyPy** (tipado).
- **pytest** (tests).

---

## 📜 Licencia

Este proyecto está bajo la licencia [MIT](LICENSE).
