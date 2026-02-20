# Saline Valley Region: Ethnobotany and Field Guide

Research materials for Ge136 field trip to Saline Valley, Death Valley National Park, California.

## Overview

This repository contains two complementary documents:

1. **Ethnobotany Report** - Traditional plant uses and rituals among Indigenous peoples
2. **Field Guide** - Geology, natural history, and logistics for the class field trip

## Indigenous Groups Covered

1. **Kawaiisu** - Tehachapi Mountains and southern Sierra Nevada
2. **Tubatulabal** - Upper Kern River Valley
3. **Newe Sogobia (Western Shoshone)** - Great Basin, Death Valley, Saline Valley
4. **Nüümü Witü (Eastern Mono/Monache)** - Owens Valley and eastern Sierra Nevada
5. **Nüümü (Northern Paiute)** - Owens Valley to northern Nevada/Oregon

## Contents

| File | Description |
|------|-------------|
| `saline-valley-ethnobotany.tex` | Ethnobotany research report |
| `saline-valley-field-guide.tex` | Geology and natural history field guide |
| `references.bib` | Bibliography (BibTeX format) |
| `README.md` | This file |

## Ethnobotany Topics

- Food plants (pinyon pine, acorns, seeds, roots, berries)
- Medicinal applications (sagebrush, yerba santa, jimsonweed)
- Ceremonial uses (pine nut ceremonies, vision quests, Datura rituals)
- Material culture (basketry, construction, tools)
- Indigenous irrigation agriculture (Owens Valley Paiute)
- Trade networks connecting mountain and desert communities

## Field Guide Topics

### Geology
- Basin and Range tectonics and graben formation
- Paleozoic stratigraphy (thickest section in western U.S.)
- Waucoban type locality (Precambrian-Cambrian boundary)
- Evaporite mineralogy and playa processes
- Fault-controlled hot springs

### Natural History
- Vegetation zones (creosote bush to alpine)
- Desert wildlife (bighorn sheep, pupfish, raptors)
- Aeolian geomorphology (sand dunes)

### Cultural History
- Salt tram (National Register of Historic Places)
- Borax mining operations
- Indigenous trade networks

## Compilation

### For Overleaf
Import directly from GitHub - both documents will compile with pdflatex + bibtex.

### Local Compilation

**Ethnobotany Report:**
```bash
pdflatex saline-valley-ethnobotany.tex
bibtex saline-valley-ethnobotany
pdflatex saline-valley-ethnobotany.tex
pdflatex saline-valley-ethnobotany.tex
```

**Field Guide:**
```bash
pdflatex saline-valley-field-guide.tex
pdflatex saline-valley-field-guide.tex
```

## Key References

### Geology
- Hardie, L.A. (1968). The origin of the Recent non-marine evaporite deposit of Saline Valley. *Geochimica et Cosmochimica Acta* 32: 1279-1301.
- Burchfiel, B.C. (1969). Geology of the Dry Mountain quadrangle. *CDMG Special Report* 99.

### Ethnography
- Zigmond, M.L. (1981). *Kawaiisu Ethnobotany*. University of Utah Press.
- Voegelin, E.W. (1938). Tubatulabal Ethnography. *UC Anthropological Records* 2(1).
- Rhode, D. (2002). *Native Plants of Southern Nevada: An Ethnobotany*. University of Utah Press.

### Web Resources
- [Owens Valley Indian Water Commission](https://www.oviwc.org/)
- [Native Memory Project](https://nativememoryproject.org/)
- [NHMU Ethnobotanical Guide](https://nhmu.utah.edu/native-plants)
- [NPS Death Valley](https://www.nps.gov/deva/)

## Course

Ge136

## License

Educational use only.
