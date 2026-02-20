# Figure Sources for Saline Valley Field Guide

This document catalogs maps, botanical illustrations, and photographs available for the field guide and ethnobotany report. All sources are public domain, Creative Commons, or government publications (USDA, USGS, NPS, BLM).

---

## 1. MAPS

### 1.1 Saline Valley Topographic Map
- **Source**: BLM Surface Management Status Map
- **URL**: https://publiclands.org/products/map_saline_valley_ca_surface_management
- **Scale**: 1:100,000
- **Coverage**: Saline Valley, Inyo Mountains, Death Valley NP Wilderness
- **Use**: Regional orientation, access routes

### 1.2 Death Valley National Park Map
- **Source**: USGS / National Park Service
- **URL**: https://www.usgs.gov/media/images/death-valley-national-park-map
- **Use**: Park context, showing Saline Valley position

### 1.3 Tribal Territory Maps
- **Source**: Native Land Digital
- **URL**: https://native-land.ca
- **Territories**:
  - Nüümü Witü (Eastern Mono/Monache)
  - Newe (Western Shoshone)
  - Northern Paiute
- **License**: Creative Commons (check specific terms)
- **Use**: Cultural geography context

### 1.4 California Native American Digital Atlas
- **Source**: California Native American Heritage Commission
- **URL**: https://nahc.ca.gov/cp/
- **Note**: Educational use only; not for official territorial determination
- **Use**: Tribal distribution overview

### 1.5 Steward's Owens Valley Irrigation Map (1933)
- **Source**: UC Berkeley Anthropology Library
- **Reference**: Steward, J.H. (1933) *Ethnography of the Owens Valley Paiute*
- **Description**: Hand-drawn map of Paiute irrigation ditch networks from tribal informant memory
- **Use**: Historical irrigation documentation

---

## 2. BOTANICAL ILLUSTRATIONS

### 2.1 Big Sagebrush (*Artemisia tridentata*)
- **Source**: USDA PLANTS Database / Forest Service
- **URL**: https://plants.usda.gov/DocumentLibrary/plantguide/pdf/pg_artrs2.pdf
- **Figure**: Figure 1 - Basin big sagebrush photograph
- **License**: Public domain (US Government)

### 2.2 Creosote Bush (*Larrea tridentata*)
- **Source**: USDA Forest Service National Seed Laboratory
- **URL**: https://www.fs.usda.gov/nsl/Wpsm/Larrea.pdf
- **Figure**: Figure 1 - Single carpel illustration (×8 magnification)
- **License**: Public domain (US Government)

- **Source**: BLM Mojave Desert Plant Guide
- **URL**: https://www.blm.gov/sites/default/files/docs/2025-02/Mojave-Desert-Plant-Guide-Creosote.pdf
- **License**: Public domain (US Government)

### 2.3 Singleleaf Pinyon (*Pinus monophylla*)
- **Source**: USDA PLANTS Database
- **URL**: https://plants.usda.gov/DocumentLibrary/plantguide/pdf/pg_pimo.pdf
- **License**: Public domain (US Government)

- **Source**: USDA Forest Service Silvics of North America
- **URL**: https://www.srs.fs.usda.gov/pubs/misc/ag_654/volume_1/pinus/monophylla.htm
- **Content**: Distribution map, botanical description
- **License**: Public domain (US Government)

### 2.4 Sacred Datura (*Datura wrightii*)
- **Source**: USDA PLANTS Database
- **URL**: https://plants.usda.gov/home/plantProfile?symbol=DAWR2
- **Note**: Use with appropriate caution warnings
- **License**: Public domain (US Government)

### 2.5 Willow (*Salix* spp.)
- **Source**: USDA PLANTS Database
- **URL**: https://plants.usda.gov/home/plantProfile?symbol=SALIX
- **License**: Public domain (US Government)

---

## 3. ARCHAEOLOGICAL FIGURES

### 3.1 Pinwheel Cave Datura Rock Art
- **Source**: Robinson et al. (2020) PNAS 117:31207
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC7733795/
- **Figures available**:
  - Figure 1: Interior of cave during laser scanning; Pinwheel painting
  - Figure 2: Unfurling flower of *D. wrightii* (photo: Melissa Dabulamanzi)
  - Figure 3: LC-MS alkaloid analysis results
  - Figure 4: SEM analysis of quids
- **License**: Open access (Creative Commons Attribution-NonCommercial-NoDerivatives 4.0)
- **Citation required**: Yes

### 3.2 Full PDF available
- **URL**: https://strathprints.strath.ac.uk/74709/1/Robinson_etal_PNAS_2020_Datura_quids_at_Pinwheel_Cave_California_provide_unambiguous_confirmation_of_the_ingestion.pdf

---

## 4. ETHNOGRAPHIC PHOTOGRAPHS

### 4.1 Bedrock Mortars
- **Source**: Indian Grinding Rock State Historic Park (Chaw'se)
- **URL**: https://www.parks.ca.gov/pages/553/files/IndianGrindingRockFinalWebLayout020917.pdf
- **Description**: 1,185 mortar holes in marbleized limestone
- **License**: California State Parks (check usage terms)

- **Source**: Wikipedia Commons
- **URL**: https://en.wikipedia.org/wiki/Bedrock_mortar
- **License**: Various Creative Commons

### 4.2 Paiute/Washoe Basketry
- **Source**: Smithsonian National Museum of the American Indian
- **URL**: https://americanindian.si.edu/collections-search
- **Search terms**: "Paiute basket", "Washoe basket", "Dat So La Lee"
- **License**: Check Smithsonian Open Access terms
- **Open Access Portal**: https://www.si.edu/openaccess

- **Source**: USGS J.W. Powell Collection
- **URL**: https://www.usgs.gov/media/images/native-american-basket-ca-1800-jw-powell-collection
- **License**: Public domain (US Government)

### 4.3 Owens Valley Historical Photographs
- **Source**: Eastern California Museum, Independence CA
- **Source**: UC Berkeley Bancroft Library
- **Note**: May require permission for reproduction

---

## 5. GEOLOGICAL FIGURES

### 5.1 Basin and Range Tectonics Diagram
- **Source**: USGS Professional Papers / Educational materials
- **Search**: USGS Basin Range extension diagram
- **License**: Public domain (US Government)

### 5.2 Saline Valley Salt Flat
- **Source**: Death Valley NPS Photo Gallery
- **URL**: https://www.nps.gov/deva/learn/photosmultimedia/photogallery.htm
- **License**: Public domain (US Government)

### 5.3 Evaporite Mineral Zonation
- **Reference**: Hardie, L.A. (1968) Geochimica et Cosmochimica Acta 32:1279
- **Note**: May need to recreate diagram based on published data

---

## 6. DOWNLOAD INSTRUCTIONS

### USDA Plant Guides (PDF)
```bash
# Create figures directory
mkdir -p figures/botanical

# Download USDA Plant Guides
curl -o figures/botanical/sagebrush_pg.pdf \
  "https://plants.usda.gov/DocumentLibrary/plantguide/pdf/pg_artrs2.pdf"

curl -o figures/botanical/pinyon_pg.pdf \
  "https://plants.usda.gov/DocumentLibrary/plantguide/pdf/pg_pimo.pdf"

curl -o figures/botanical/creosote_usfs.pdf \
  "https://www.fs.usda.gov/nsl/Wpsm/Larrea.pdf"
```

### Robinson et al. (2020) PNAS Article
```bash
mkdir -p figures/archaeological

curl -o figures/archaeological/robinson_2020_datura.pdf \
  "https://strathprints.strath.ac.uk/74709/1/Robinson_etal_PNAS_2020_Datura_quids_at_Pinwheel_Cave_California_provide_unambiguous_confirmation_of_the_ingestion.pdf"
```

### BLM Maps
```bash
mkdir -p figures/maps

# Check BLM store for downloadable versions
# https://www.blm.gov/maps
```

---

## 7. FIGURE PLACEMENT IN LATEX

### Suggested Figure Locations

| Section | Figure | Source |
|---------|--------|--------|
| Introduction | Saline Valley regional map | BLM/USGS |
| Introduction | Tribal territories overlay | Native Land Digital |
| Healing - Sagebrush | *A. tridentata* photograph | USDA Plant Guide |
| Healing - Creosote | *L. tridentata* carpel illustration | USFS Seed Lab |
| Rituals - Toloache | Pinwheel Cave rock art | Robinson et al. 2020 |
| Rituals - Toloache | *D. wrightii* flower unfurling | Robinson et al. 2020 |
| Rituals - Pine Nut | *P. monophylla* photograph | USDA Plant Guide |
| Material Culture | Paiute coiled basket | Smithsonian NMAI |
| Material Culture | Bedrock mortar site | CA State Parks |
| Material Culture | Steward irrigation map | UC Berkeley |

---

## 8. CITATION REQUIREMENTS

All figures must be cited according to source requirements:

- **USDA/USGS/NPS/BLM**: Public domain; credit agency
- **Smithsonian Open Access**: Follow SI Open Access terms
- **PNAS Open Access**: CC BY-NC-ND 4.0; cite authors
- **Native Land Digital**: Credit and link to native-land.ca
- **Wikipedia Commons**: Follow individual image license

---

*Document compiled for Ge136 Saline Valley Field Trip*
