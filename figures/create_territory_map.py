#!/usr/bin/env python3
"""
Create a simplified territorial map of Indigenous groups in the Saline Valley region.
Territories based on ethnographic sources: Kroeber (1925), Steward (1933, 1938),
Zigmond (1981), and Native Land Digital.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon, FancyBboxPatch
from matplotlib.collections import PatchCollection
import numpy as np

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(10, 12))

# Define the map extent (longitude, latitude)
# Centered on Saline Valley region
lon_min, lon_max = -118.6, -116.8
lat_min, lat_max = 35.8, 37.8

# Territory polygons (simplified boundaries based on ethnographic sources)
# Coordinates as (longitude, latitude) pairs

# Kawaiisu - Tehachapi Mountains and southern Sierra Nevada foothills
# Southern portion of map
kawaiisu = np.array([
    [-118.6, 35.8],
    [-118.6, 36.2],
    [-118.3, 36.4],
    [-117.8, 36.3],
    [-117.5, 36.0],
    [-117.2, 35.8],
    [-118.6, 35.8]
])

# Tubatulabal - Upper Kern River Valley (west-central)
tubatulabal = np.array([
    [-118.6, 36.2],
    [-118.6, 36.7],
    [-118.3, 36.8],
    [-118.0, 36.6],
    [-118.3, 36.4],
    [-118.6, 36.2]
])

# Western Shoshone (Newe Sogobia) - Death Valley, Saline Valley, eastern portion
# This is the Timbisha/Panamint Shoshone territory
western_shoshone = np.array([
    [-117.8, 36.3],
    [-118.0, 36.6],
    [-117.8, 37.0],
    [-117.5, 37.3],
    [-117.2, 37.5],
    [-116.8, 37.5],
    [-116.8, 36.2],
    [-117.2, 35.8],
    [-117.5, 36.0],
    [-117.8, 36.3]
])

# Eastern Mono/Monache (Nuumu Witu) - Owens Valley and eastern Sierra
nuumu_witu = np.array([
    [-118.3, 36.8],
    [-118.6, 36.7],
    [-118.6, 37.4],
    [-118.4, 37.6],
    [-118.0, 37.5],
    [-117.8, 37.0],
    [-118.0, 36.6],
    [-118.3, 36.8]
])

# Northern Paiute (Nuumu) - Northern Owens Valley extending north
nuumu = np.array([
    [-118.6, 37.4],
    [-118.6, 37.8],
    [-117.8, 37.8],
    [-117.2, 37.5],
    [-117.5, 37.3],
    [-117.8, 37.0],
    [-118.0, 37.5],
    [-118.4, 37.6],
    [-118.6, 37.4]
])

# Colors with transparency
colors = {
    'kawaiisu': '#E6550D',      # Orange
    'tubatulabal': '#31A354',   # Green
    'western_shoshone': '#756BB1',  # Purple
    'nuumu_witu': '#3182BD',    # Blue
    'nuumu': '#E7298A'          # Pink
}

alpha = 0.4

# Plot territories
territories = [
    (kawaiisu, 'kawaiisu', 'Kawaiisu'),
    (tubatulabal, 'tubatulabal', 'Tubatulabal'),
    (western_shoshone, 'western_shoshone', 'Newe Sogobia\n(Western Shoshone)'),
    (nuumu_witu, 'nuumu_witu', 'Nüümü Witü\n(Eastern Mono)'),
    (nuumu, 'nuumu', 'Nüümü\n(Northern Paiute)')
]

for coords, key, label in territories:
    poly = Polygon(coords, closed=True, facecolor=colors[key],
                   edgecolor='black', linewidth=1.5, alpha=alpha)
    ax.add_patch(poly)

# Add key geographic features as points
places = {
    'Saline Valley': (-117.85, 36.75),
    'Death Valley': (-117.0, 36.5),
    'Owens Lake': (-117.95, 36.45),
    'Mono Lake': (-119.0, 38.0),  # Off map but direction indicated
    'Panamint Valley': (-117.4, 36.1),
    'Eureka Valley': (-117.65, 37.1),
}

# Plot places within map bounds
for name, (lon, lat) in places.items():
    if lon_min <= lon <= lon_max and lat_min <= lat <= lat_max:
        ax.plot(lon, lat, 'ko', markersize=6)
        # Adjust text position based on location
        if name == 'Saline Valley':
            ax.annotate(name, (lon, lat), xytext=(5, 5),
                       textcoords='offset points', fontsize=9, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                                edgecolor='none', alpha=0.8))
        elif name == 'Owens Lake':
            ax.annotate(name, (lon, lat), xytext=(-40, -15),
                       textcoords='offset points', fontsize=8,
                       bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                                edgecolor='none', alpha=0.7))
        else:
            ax.annotate(name, (lon, lat), xytext=(5, -10),
                       textcoords='offset points', fontsize=8,
                       bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                                edgecolor='none', alpha=0.7))

# Add mountain ranges as text labels (rotated)
ax.text(-118.5, 37.1, 'Sierra Nevada', fontsize=8, fontstyle='italic',
        rotation=70, ha='center', va='center', color='#555555')
ax.text(-117.35, 36.9, 'Inyo\nMountains', fontsize=7, fontstyle='italic',
        ha='center', va='center', color='#555555')
ax.text(-117.15, 36.35, 'Panamint\nRange', fontsize=7, fontstyle='italic',
        ha='center', va='center', color='#555555')

# Create legend
legend_patches = [
    mpatches.Patch(facecolor=colors['kawaiisu'], edgecolor='black',
                   alpha=alpha, label='Kawaiisu'),
    mpatches.Patch(facecolor=colors['tubatulabal'], edgecolor='black',
                   alpha=alpha, label='Tubatulabal'),
    mpatches.Patch(facecolor=colors['western_shoshone'], edgecolor='black',
                   alpha=alpha, label='Newe Sogobia (Western Shoshone)'),
    mpatches.Patch(facecolor=colors['nuumu_witu'], edgecolor='black',
                   alpha=alpha, label='Nüümü Witü (Eastern Mono)'),
    mpatches.Patch(facecolor=colors['nuumu'], edgecolor='black',
                   alpha=alpha, label='Nüümü (Northern Paiute)'),
]

ax.legend(handles=legend_patches, loc='lower right', fontsize=9,
          framealpha=0.95, edgecolor='black')

# Set axis properties
ax.set_xlim(lon_min, lon_max)
ax.set_ylim(lat_min, lat_max)
ax.set_aspect('equal')

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.3)

# Labels
ax.set_xlabel('Longitude (°W)', fontsize=10)
ax.set_ylabel('Latitude (°N)', fontsize=10)

# Format tick labels
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{abs(x):.1f}°W'))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1f}°N'))

# Title
ax.set_title('Indigenous Territories of the Saline Valley Region\n'
             'Simplified boundaries based on ethnographic sources',
             fontsize=12, fontweight='bold', pad=15)

# Add source note
fig.text(0.5, 0.02,
         'Sources: Kroeber (1925), Steward (1933, 1938), Zigmond (1981), Native Land Digital',
         ha='center', fontsize=8, fontstyle='italic', color='#666666')

# Add north arrow
ax.annotate('', xy=(-116.95, 37.65), xytext=(-116.95, 37.45),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.text(-116.95, 37.7, 'N', fontsize=12, fontweight='bold', ha='center')

# Add scale bar (approximate at this latitude)
# 1 degree longitude ≈ 85 km at 37°N
scale_lon = -118.4
scale_lat = 35.95
scale_length = 0.5  # degrees, roughly 42 km
ax.plot([scale_lon, scale_lon + scale_length], [scale_lat, scale_lat],
        'k-', linewidth=3)
ax.text(scale_lon + scale_length/2, scale_lat - 0.08, '~42 km',
        ha='center', fontsize=8)

plt.tight_layout()
plt.subplots_adjust(bottom=0.08)

# Save in multiple formats
plt.savefig('/Users/isaac/Documents/Courses/Ge136/figures/maps/saline_valley_territories.pdf',
            dpi=300, bbox_inches='tight')
plt.savefig('/Users/isaac/Documents/Courses/Ge136/figures/maps/saline_valley_territories.png',
            dpi=300, bbox_inches='tight')

print("Map saved to:")
print("  figures/maps/saline_valley_territories.pdf")
print("  figures/maps/saline_valley_territories.png")
