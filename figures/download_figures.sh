#!/bin/bash
# Download publicly available figures for Saline Valley Field Guide
# All sources are US Government (public domain) or Open Access

set -e

echo "Creating directory structure..."
mkdir -p botanical
mkdir -p archaeological
mkdir -p maps
mkdir -p ethnographic

echo ""
echo "=== DOWNLOADING USDA/USFS BOTANICAL RESOURCES ==="

echo "Downloading sagebrush plant guide..."
curl -L -o botanical/artemisia_tridentata_plantguide.pdf \
  "https://plants.usda.gov/DocumentLibrary/plantguide/pdf/pg_artrs2.pdf"

echo "Downloading pinyon pine plant guide..."
curl -L -o botanical/pinus_monophylla_plantguide.pdf \
  "https://plants.usda.gov/DocumentLibrary/plantguide/pdf/pg_pimo.pdf"

echo "Downloading creosote bush seed manual..."
curl -L -o botanical/larrea_tridentata_seedmanual.pdf \
  "https://www.fs.usda.gov/nsl/Wpsm/Larrea.pdf"

echo "Downloading BLM creosote plant guide..."
curl -L -o botanical/blm_creosote_guide.pdf \
  "https://www.blm.gov/sites/default/files/docs/2025-02/Mojave-Desert-Plant-Guide-Creosote.pdf"

echo "Downloading USDA ARS creosote research..."
curl -L -o botanical/creosote_ars_research.pdf \
  "https://www.ars.usda.gov/ARSUserFiles/30980500/Creosote_Bush.pdf"

echo ""
echo "=== DOWNLOADING ARCHAEOLOGICAL RESOURCES ==="

echo "Downloading Robinson et al. (2020) Pinwheel Cave PNAS article..."
curl -L -o archaeological/robinson_2020_pinwheel_cave.pdf \
  "https://strathprints.strath.ac.uk/74709/1/Robinson_etal_PNAS_2020_Datura_quids_at_Pinwheel_Cave_California_provide_unambiguous_confirmation_of_the_ingestion.pdf"

echo ""
echo "=== DOWNLOADING ETHNOGRAPHIC RESOURCES ==="

echo "Downloading Owens Valley Paiute irrigation document..."
curl -L -o ethnographic/owens_valley_paiute_irrigation.pdf \
  "https://bishopvisitor.com/wp-content/uploads/2025/02/OV-Paiute-Irrigation.pdf"

echo "Downloading Wilke & Lawton agriculture paper..."
curl -L -o ethnographic/wilke_lawton_paiute_agriculture.pdf \
  "https://escholarship.org/content/qt0595h88m/qt0595h88m_noSplash_b02cb78eee95020c1ec45a5251e4211d.pdf"

echo "Downloading Indian Grinding Rock State Park brochure..."
curl -L -o ethnographic/indian_grinding_rock_brochure.pdf \
  "https://www.parks.ca.gov/pages/553/files/IndianGrindingRockFinalWebLayout020917.pdf"

echo ""
echo "=== DOWNLOADING MAP RESOURCES ==="

echo "Downloading USGS Death Valley NM historical map..."
curl -L -o maps/death_valley_usgs_1977.pdf \
  "https://store.usgs.gov/assets/MOD/StoreFiles/National_Parks_and_Monuments/43844_43845_CA_DeathValleyNM&Vic_1977_250K.pdf"

echo ""
echo "=== DOWNLOAD COMPLETE ==="
echo ""
echo "Downloaded files:"
find . -name "*.pdf" -type f | sort

echo ""
echo "=== MANUAL DOWNLOADS REQUIRED ==="
echo ""
echo "The following resources require manual download or have usage restrictions:"
echo ""
echo "1. Native Land Digital territorial maps:"
echo "   https://native-land.ca"
echo "   - Search: Eastern Mono, Western Shoshone, Northern Paiute"
echo "   - Export as PNG or use embedded iframe"
echo ""
echo "2. Smithsonian NMAI basket images:"
echo "   https://www.si.edu/openaccess"
echo "   - Search: 'Paiute basket' or 'Washoe basket'"
echo "   - Check individual image licenses"
echo ""
echo "3. Robinson et al. (2020) individual figures:"
echo "   https://pmc.ncbi.nlm.nih.gov/articles/PMC7733795/"
echo "   - Right-click figures to save"
echo "   - License: CC BY-NC-ND 4.0"
echo ""
echo "4. USGS J.W. Powell Collection basket:"
echo "   https://www.usgs.gov/media/images/native-american-basket-ca-1800-jw-powell-collection"
echo ""
