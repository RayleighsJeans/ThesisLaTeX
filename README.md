# PhD Thesis: Impurity Transport and Radiation at Wendelstein 7-X

LaTeX thesis project for fusion plasma physics research at the W7-X stellarator.

## Quick Start

**Build THESIS (main document):**
```bash
cd THESIS
./compile
```

**Build COLLOQUIUM (defense presentation):**
```bash
cd COLLOQUIUM
latexmk -pdf slides.tex
```

## Project Structure

- `THESIS/` - PhD thesis document (pdflatex + biber)
- `COLLOQUIUM/` - Defense presentation (lualatex + minted)
- `REPORTS/` - Historical progress reports
- `POSTERS/` - Conference posters
- `PRESENTATIONS/` - Various presentations
- `.bob/` - AI assistant rules and context

## Documentation

- **[AGENTS.md](AGENTS.md)** - Build commands and non-obvious architecture patterns
- **[.bob/THESIS_CONTEXT.md](.bob/THESIS_CONTEXT.md)** - Scientific background, physics terminology, and notation conventions
- **[.bob/custom_modes.yaml](.bob/custom_modes.yaml)** - Custom LaTeX editing mode with syntax validation

## Key Features

- **Custom Import System**: Content files override templates automatically
- **Property-Based Configuration**: Lisp-like property system controls document structure
- **Custom Math Commands**: `\ix{}`, `\diff`, `\tenpo{}` for consistent notation
- **Template Variants**: Multiple titlepage/layout options via properties

## Scientific Context

This thesis focuses on bolometry diagnostics and real-time radiation feedback control at the Wendelstein 7-X stellarator. Key research areas:

- Bolometer diagnostic system (94 channels, ~5cm spatial resolution)
- Real-time radiation feedback control (achieved f_rad≥85%)
- Impurity transport and seeding strategies
- Tomographic reconstruction of 2D radiation profiles

See [.bob/THESIS_CONTEXT.md](.bob/THESIS_CONTEXT.md) for detailed physics background.