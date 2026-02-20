#!/usr/bin/env python3
"""
Create a territorial map with geological/topographic basemap for the Saline Valley region.
Shows Basin and Range structure with shaded relief and major geological features.

Territories based on ethnographic sources: Kroeber (1925), Steward (1933, 1938),
Zigmond (1981), and Native Land Digital.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Polygon
from matplotlib.colors import LightSource, LinearSegmentedColormap
import numpy as np
from scipy import ndimage

# Set up the figure
fig, ax = plt.subplots(1, 1, figsize=(11, 13))

# Define the map extent (longitude, latitude)
lon_min, lon_max = -118.6, -116.8
lat_min, lat_max = 35.8, 37.8

# Create synthetic DEM representing Basin and Range topography
# Resolution: ~500m per pixel
nx, ny = 360, 400
x = np.linspace(lon_min, lon_max, nx)
y = np.linspace(lat_min, lat_max, ny)
X, Y = np.meshgrid(x, y)

# Base elevation (meters) - starts at ~1000m for valleys
elevation = np.ones((ny, nx)) * 1000

# Sierra Nevada (western edge) - rises to ~4000m
sierra_mask = X < -118.3
sierra_elev = 1500 + 2500 * np.exp(-((X + 118.5)**2) / 0.02)
elevation = np.where(sierra_mask, np.maximum(elevation, sierra_elev), elevation)

# Inyo Mountains (ridge between Owens Valley and Saline Valley)
# Centered around -117.9 to -117.7, running N-S
inyo_center = -117.85
inyo_width = 0.15
inyo_mask = (X > inyo_center - inyo_width) & (X < inyo_center + inyo_width)
inyo_elev = 1200 + 2000 * np.exp(-((X - inyo_center)**2) / 0.008)
# Taper at edges
inyo_taper = 1 - 0.3 * np.abs(Y - 36.8)
inyo_elev = inyo_elev * np.clip(inyo_taper, 0.5, 1)
elevation = np.where(inyo_mask | (np.abs(X - inyo_center) < 0.3),
                     np.maximum(elevation, inyo_elev), elevation)

# Panamint Range (between Panamint Valley and Death Valley)
# Centered around -117.1 to -117.0
panamint_center = -117.15
panamint_elev = 1000 + 2200 * np.exp(-((X - panamint_center)**2) / 0.012)
panamint_mask = (X > -117.4) & (X < -116.9) & (Y < 36.8)
elevation = np.where(panamint_mask, np.maximum(elevation, panamint_elev), elevation)

# White Mountains (northeastern)
white_center = -118.15
white_mask = (X > -118.4) & (X < -117.9) & (Y > 37.3)
white_elev = 1500 + 2200 * np.exp(-((X - white_center)**2) / 0.015)
elevation = np.where(white_mask, np.maximum(elevation, white_elev), elevation)

# Valleys/Basins (grabens) - lower elevations

# Owens Valley (deep graben, -100m at Owens Lake)
owens_center = -118.05
owens_mask = (X > -118.25) & (X < -117.9) & (Y < 37.0) & (Y > 36.0)
owens_elev = 800 - 400 * np.exp(-((X - owens_center)**2) / 0.01)
elevation = np.where(owens_mask, np.minimum(elevation, owens_elev + 400), elevation)

# Saline Valley (closed basin, ~300m floor)
saline_center_x, saline_center_y = -117.85, 36.75
saline_dist = np.sqrt((X - saline_center_x)**2 + ((Y - saline_center_y)/1.5)**2)
saline_mask = saline_dist < 0.25
saline_elev = 400 + 300 * saline_dist / 0.25
elevation = np.where(saline_mask, np.minimum(elevation, saline_elev), elevation)

# Eureka Valley
eureka_center_x, eureka_center_y = -117.65, 37.1
eureka_dist = np.sqrt((X - eureka_center_x)**2 + ((Y - eureka_center_y)/1.2)**2)
eureka_mask = eureka_dist < 0.15
eureka_elev = 900 + 200 * eureka_dist / 0.15
elevation = np.where(eureka_mask, np.minimum(elevation, eureka_elev), elevation)

# Death Valley (below sea level, -86m at Badwater)
dv_center_x, dv_center_y = -116.95, 36.4
dv_dist = np.sqrt(((X - dv_center_x)/0.8)**2 + ((Y - dv_center_y)/1.5)**2)
dv_mask = (X > -117.2) & (X < -116.8) & (Y > 35.8) & (Y < 37.0)
dv_elev = -50 + 500 * dv_dist
elevation = np.where(dv_mask, np.minimum(elevation, dv_elev + 200), elevation)

# Panamint Valley
pv_center_x, pv_center_y = -117.4, 36.1
pv_dist = np.sqrt((X - pv_center_x)**2 + ((Y - pv_center_y)/0.8)**2)
pv_mask = pv_dist < 0.2
pv_elev = 500 + 400 * pv_dist / 0.2
elevation = np.where(pv_mask, np.minimum(elevation, pv_elev), elevation)

# Smooth the terrain
elevation = ndimage.gaussian_filter(elevation, sigma=2)

# Add some noise for texture
noise = np.random.randn(ny, nx) * 50
noise = ndimage.gaussian_filter(noise, sigma=1.5)
elevation = elevation + noise

# Create hillshade
ls = LightSource(azdeg=315, altdeg=35)
hillshade = ls.hillshade(elevation, vert_exag=2, dx=1, dy=1)

# Create terrain colormap (hypsometric tints)
terrain_colors = [
    (0.0, '#2d5016'),   # Dark green (low valleys)
    (0.15, '#4a7c23'),  # Green
    (0.25, '#8cb369'),  # Light green
    (0.35, '#c9b857'),  # Yellow-tan
    (0.45, '#d4a84b'),  # Tan
    (0.55, '#c4956a'),  # Light brown
    (0.70, '#a67c52'),  # Brown
    (0.85, '#8b6543'),  # Dark brown
    (0.95, '#c5c5c5'),  # Gray (high peaks)
    (1.0, '#ffffff'),   # White (highest)
]
terrain_cmap = LinearSegmentedColormap.from_list('terrain_custom', terrain_colors)

# Normalize elevation for colormap
elev_min, elev_max = -100, 4000
elev_norm = np.clip((elevation - elev_min) / (elev_max - elev_min), 0, 1)

# Combine terrain colors with hillshade
terrain_rgb = terrain_cmap(elev_norm)[:, :, :3]
shaded = ls.shade_rgb(terrain_rgb, elevation, vert_exag=2, blend_mode='soft')

# Plot the basemap
ax.imshow(shaded, extent=[lon_min, lon_max, lat_min, lat_max],
          origin='lower', aspect='auto')

# Territory polygons (simplified boundaries)
kawaiisu = np.array([
    [-118.6, 35.8], [-118.6, 36.2], [-118.3, 36.4], [-117.8, 36.3],
    [-117.5, 36.0], [-117.2, 35.8], [-118.6, 35.8]
])

tubatulabal = np.array([
    [-118.6, 36.2], [-118.6, 36.7], [-118.3, 36.8], [-118.0, 36.6],
    [-118.3, 36.4], [-118.6, 36.2]
])

western_shoshone = np.array([
    [-117.8, 36.3], [-118.0, 36.6], [-117.8, 37.0], [-117.5, 37.3],
    [-117.2, 37.5], [-116.8, 37.5], [-116.8, 36.2], [-117.2, 35.8],
    [-117.5, 36.0], [-117.8, 36.3]
])

nuumu_witu = np.array([
    [-118.3, 36.8], [-118.6, 36.7], [-118.6, 37.4], [-118.4, 37.6],
    [-118.0, 37.5], [-117.8, 37.0], [-118.0, 36.6], [-118.3, 36.8]
])

nuumu = np.array([
    [-118.6, 37.4], [-118.6, 37.8], [-117.8, 37.8], [-117.2, 37.5],
    [-117.5, 37.3], [-117.8, 37.0], [-118.0, 37.5], [-118.4, 37.6],
    [-118.6, 37.4]
])

# Colors with transparency
colors = {
    'kawaiisu': '#E6550D',
    'tubatulabal': '#31A354',
    'western_shoshone': '#756BB1',
    'nuumu_witu': '#3182BD',
    'nuumu': '#E7298A'
}

alpha = 0.35

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
                   edgecolor='black', linewidth=1.8, alpha=alpha)
    ax.add_patch(poly)

# Add major faults (simplified Basin and Range normal faults)
fault_style = dict(color='#8B0000', linewidth=1.5, linestyle='--', alpha=0.7)

# Owens Valley Fault Zone (Sierra Nevada frontal fault)
ax.plot([-118.35, -118.25, -118.2, -118.15], [35.8, 36.5, 37.0, 37.8], **fault_style)

# Inyo Mountains Fault (east side)
ax.plot([-117.7, -117.65, -117.6], [36.0, 36.8, 37.5], **fault_style)

# Death Valley Fault Zone
ax.plot([-117.0, -116.95, -116.9, -116.85], [35.8, 36.3, 36.8, 37.3], **fault_style)

# Panamint Valley Fault
ax.plot([-117.35, -117.3, -117.25], [35.8, 36.3, 36.7], **fault_style)

# Add geographic features
places = {
    'Saline Valley': (-117.85, 36.75, 'bold'),
    'Death Valley': (-117.0, 36.5, 'normal'),
    'Owens Lake\n(dry)': (-117.95, 36.42, 'normal'),
    'Panamint Valley': (-117.38, 36.1, 'normal'),
    'Eureka Valley': (-117.65, 37.1, 'normal'),
}

for name, (lon, lat, weight) in places.items():
    if lon_min <= lon <= lon_max and lat_min <= lat <= lat_max:
        ax.plot(lon, lat, 'ko', markersize=5)
        fontweight = 'bold' if weight == 'bold' else 'normal'
        fontsize = 10 if weight == 'bold' else 8
        ax.annotate(name, (lon, lat), xytext=(6, 4),
                   textcoords='offset points', fontsize=fontsize,
                   fontweight=fontweight,
                   bbox=dict(boxstyle='round,pad=0.3', facecolor='white',
                            edgecolor='none', alpha=0.85))

# Mountain range labels
ax.text(-118.5, 37.15, 'SIERRA\nNEVADA', fontsize=9, fontweight='bold',
        rotation=70, ha='center', va='center', color='#333333',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.6, edgecolor='none'))
ax.text(-117.78, 36.95, 'INYO\nMTS', fontsize=8, fontweight='bold',
        rotation=80, ha='center', va='center', color='#333333',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.6, edgecolor='none'))
ax.text(-117.15, 36.35, 'PANAMINT\nRANGE', fontsize=8, fontweight='bold',
        rotation=75, ha='center', va='center', color='#333333',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.6, edgecolor='none'))
ax.text(-118.2, 37.55, 'WHITE\nMTS', fontsize=8, fontweight='bold',
        ha='center', va='center', color='#333333',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.6, edgecolor='none'))

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

# Add fault legend entry
from matplotlib.lines import Line2D
fault_line = Line2D([0], [0], color='#8B0000', linewidth=1.5,
                    linestyle='--', label='Major Faults')
legend_patches.append(fault_line)

ax.legend(handles=legend_patches, loc='lower right', fontsize=9,
          framealpha=0.95, edgecolor='black')

# Set axis properties
ax.set_xlim(lon_min, lon_max)
ax.set_ylim(lat_min, lat_max)

# Add gridlines
ax.grid(True, linestyle=':', alpha=0.4, color='white')

# Labels
ax.set_xlabel('Longitude', fontsize=11)
ax.set_ylabel('Latitude', fontsize=11)

# Format tick labels
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{abs(x):.1f}°W'))
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{x:.1f}°N'))

# Title
ax.set_title('Indigenous Territories of the Saline Valley Region\n'
             'Basin and Range Geological Province',
             fontsize=13, fontweight='bold', pad=15)

# Add source note
fig.text(0.5, 0.02,
         'Territories: Kroeber (1925), Steward (1933, 1938), Zigmond (1981) | '
         'Topography: Synthetic DEM representing Basin and Range structure',
         ha='center', fontsize=8, fontstyle='italic', color='#444444')

# North arrow
ax.annotate('', xy=(-116.95, 37.65), xytext=(-116.95, 37.45),
            arrowprops=dict(arrowstyle='->', lw=2, color='black'))
ax.text(-116.95, 37.7, 'N', fontsize=12, fontweight='bold', ha='center')

# Scale bar
scale_lon = -118.4
scale_lat = 35.92
scale_length = 0.5  # ~42 km at this latitude
ax.plot([scale_lon, scale_lon + scale_length], [scale_lat, scale_lat],
        'k-', linewidth=4)
ax.plot([scale_lon, scale_lon + scale_length], [scale_lat, scale_lat],
        'w-', linewidth=2)
ax.text(scale_lon + scale_length/2, scale_lat - 0.07, '~42 km',
        ha='center', fontsize=9, fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.2', facecolor='white', alpha=0.8, edgecolor='none'))

# Elevation colorbar
from mpl_toolkits.axes_grid1 import make_axes_locatable
sm = plt.cm.ScalarMappable(cmap=terrain_cmap,
                           norm=plt.Normalize(vmin=elev_min, vmax=elev_max))
sm.set_array([])
cax = fig.add_axes([0.15, 0.06, 0.25, 0.015])
cbar = plt.colorbar(sm, cax=cax, orientation='horizontal')
cbar.set_label('Elevation (m)', fontsize=9)
cbar.ax.tick_params(labelsize=8)

plt.tight_layout()
plt.subplots_adjust(bottom=0.11)

# Save
plt.savefig('/Users/isaac/Documents/Courses/Ge136/figures/maps/saline_valley_territories_geo.pdf',
            dpi=300, bbox_inches='tight')
plt.savefig('/Users/isaac/Documents/Courses/Ge136/figures/maps/saline_valley_territories_geo.png',
            dpi=300, bbox_inches='tight')

print("Geological basemap saved to:")
print("  figures/maps/saline_valley_territories_geo.pdf")
print("  figures/maps/saline_valley_territories_geo.png")
