# Saline Valley Region: Ethnobotany and Field Guide

Research materials for Ge136 field trip to Saline Valley, Death Valley National Park, California.

## Overview

This repository contains three complementary documents:

1. **Ethnobotany Report** - Traditional plant uses and rituals among Indigenous peoples
2. **Field Guide** - Geology, natural history, and logistics for the class field trip
3. **Field Synthesis** - 2-page summary with scientific mechanisms and practical instructions

## Indigenous Groups Covered

1. **Kawaiisu** - Tehachapi Mountains and southern Sierra Nevada
2. **Tubatulabal** - Upper Kern River Valley
3. **Newe Sogobia (Western Shoshone)** - Great Basin, Death Valley, Saline Valley
4. **Nüümü Witü (Eastern Mono/Monache)** - Owens Valley and eastern Sierra Nevada
5. **Nüümü (Northern Paiute)** - Owens Valley to northern Nevada/Oregon

## Contents

| File | Description |
|------|-------------|
| `saline-valley-ethnobotany.tex` | Full ethnobotany research report |
| `saline-valley-field-guide.tex` | Geology and natural history field guide |
| `desert-plants-field-synthesis.tex` | 2-page field synthesis with mechanisms |
| `references.bib` | Bibliography (BibTeX format) |
| `figures/` | Maps, botanical illustrations, archaeological figures |

## Figures Directory

The `figures/` directory contains source materials organized by category:

```
figures/
├── FIGURE_SOURCES.md      # Complete catalog with URLs and licenses
├── download_figures.sh    # Script to download public domain resources
├── botanical/             # USDA plant guides and illustrations
├── archaeological/        # Robinson et al. (2020) Pinwheel Cave study
├── ethnographic/          # Paiute irrigation, bedrock mortars
└── maps/                  # USGS topographic maps
```

### Downloaded Resources (Public Domain / Open Access)

| Category | Files | Source |
|----------|-------|--------|
| Botanical | Sagebrush, Pinyon, Creosote guides | USDA/USFS |
| Archaeological | Pinwheel Cave Datura study | PNAS (CC BY-NC-ND) |
| Ethnographic | Owens Valley irrigation documents | UC eScholarship |
| Maps | Death Valley NM 1977 | USGS |
| Maps | Indigenous Territories Map | Generated (matplotlib) |

Run `./figures/download_figures.sh` to download all available resources.

### Territory Map

`figures/maps/saline_valley_territories.png` - Custom-generated map showing simplified polygon boundaries for the five Indigenous groups (Kawaiisu, Tubatulabal, Western Shoshone, Eastern Mono, Northern Paiute) in the Saline Valley region. Generated using `figures/create_territory_map.py` based on ethnographic sources (Kroeber 1925, Steward 1933/1938, Zigmond 1981, Native Land Digital).

## Ethnobotany Topics

- Food plants (pinyon pine, acorns, seeds, roots, berries)
- Medicinal applications with pharmacological mechanisms
- Ceremonial uses (pine nut ceremonies, vision quests, Datura rituals)
- Material culture (basketry, construction, tools)
- Indigenous irrigation agriculture (Owens Valley Paiute)

## Field Synthesis Highlights

The 2-page synthesis includes peer-reviewed citations:

| Plant | Mechanism | Reference |
|-------|-----------|-----------|
| Sagebrush | TRPV3 receptor agonism; iNOS/NF-κB inhibition | Adams 2012; Rahman 2017 |
| Creosote | NDGA lipoxygenase inhibition; NRF2 activation | Rahman 2011 |
| Willow | Salicin → salicylic acid conversion pathway | Schmid 2001 |
| Datura | Muscarinic acetylcholine antagonism | Kohnen-Johannsen 2019 |

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
Import directly from GitHub - all documents compile with pdflatex + bibtex.

### Local Compilation

```bash
# Ethnobotany Report
pdflatex saline-valley-ethnobotany.tex
bibtex saline-valley-ethnobotany
pdflatex saline-valley-ethnobotany.tex
pdflatex saline-valley-ethnobotany.tex

# Field Guide
pdflatex saline-valley-field-guide.tex
pdflatex saline-valley-field-guide.tex

# Field Synthesis (2-page)
pdflatex desert-plants-field-synthesis.tex
pdflatex desert-plants-field-synthesis.tex
```

## Key References

### Pharmacology
- Adams, R.P. (2012). *J. Essential Oil Research* 24:341
- Rahman, S. et al. (2011). *Evidence-Based CAM* nep076
- Robinson, D.W. et al. (2020). *PNAS* 117:31207

### Geology
- Hardie, L.A. (1968). *Geochimica et Cosmochimica Acta* 32:1279
- Burchfiel, B.C. (1969). *CDMG Special Report* 99

### Ethnography
- Zigmond, M.L. (1981). *Kawaiisu Ethnobotany*. University of Utah Press.
- Kroeber, A.L. (1925). *Handbook of the Indians of California*
- Steward, J.H. (1930). *Papers Michigan Academy* 12:149

### Web Resources
- [Owens Valley Indian Water Commission](https://www.oviwc.org/)
- [Native Land Digital](https://native-land.ca/)
- [USDA PLANTS Database](https://plants.usda.gov/)
- [NPS Death Valley](https://www.nps.gov/deva/)

## Course

Ge136

## License

Educational use only. Figure sources retain original licenses (see `figures/FIGURE_SOURCES.md`).
