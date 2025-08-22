# Plantilla base Python

[![CI / build](https://github.com/CoderDeltaLAN/plantilla/actions/workflows/ci.yml/badge.svg)](https://github.com/CoderDeltaLAN/plantilla/actions)

Pequeña descripción del proyecto.  
Plantilla estándar: **Poetry + pre-commit + CI/CD + tests**.

---

## 🚀 Requisitos
- Python 3.12
- Poetry

---

## 🔧 Instalación

Clona el repositorio y entra en la carpeta:

```bash
git clone https://github.com/CoderDeltaLAN/gh-insights.git
cd gh-insights
poetry install
```

---

## 📊 Ejemplo de uso

Top repos de un usuario (ejemplo con Linus Torvalds):

```bash
poetry run python -m gh_insights top-repos torvalds --limit 3
```

Salida:

```
       Top repos por ⭐ de torvalds        
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━┳━━━━━━━━━━┓
┃ Repositorio         ┃     ⭐ ┃ Lenguaje ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━╇━━━━━━━━━━┩
│ torvalds/linux      │ 200440 │ C        │
│ torvalds/uemacs     │   1535 │ C        │
│ torvalds/test-tlb   │    809 │ C        │
└─────────────────────┴────────┴──────────┘
```

Lenguajes principales de un repo:

```bash
poetry run python -m gh_insights langs torvalds/linux
```

Salida:

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

## 📜 Licencia

Este proyecto está bajo la licencia MIT.

