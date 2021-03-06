#!/usr/bin/python
# 
# \file directories.py
# \brief Directories configuration
# \date 2010-08-27 17:13GMT
# \author Jan Boon (Kaetemi)
# \date 2001-2005
# \author Nevrax
# Python port of game data build pipeline.
# Directories configuration.
# 
# NeL - MMORPG Framework <http://dev.ryzom.com/projects/nel/>
# Copyright (C) 2010  Winch Gate Property Limited
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 


# *** COMMON NAMES AND PATHS ***
EcosystemName = "sky"
EcosystemPath = "common/" + EcosystemName
ContinentName = EcosystemName
ContinentPath = EcosystemPath
CommonName = ContinentName
CommonPath = ContinentPath


# *** SOURCE DIRECTORIES LEVELDESIGN/WORLD ***
ContinentLeveldesignWorldDirectory = "" # DISABLED


# *** SOURCE DIRECTORIES IN THE DATABASE ***

# Shape directories
ShapeSourceDirectories = [ ]
ShapeSourceDirectories += [ "sky_v2/max" ]

# Maps directories
MapSourceDirectories = [ ]
MapSourceDirectories += [ "sky_v2/textures/textures" ]

MapUncompressedSourceDirectories = [ ]
MapUncompressedSourceDirectories += [ "sky_v2/textures/textures/desert" ]
MapUncompressedSourceDirectories += [ "sky_v2/textures/textures/forest" ]
MapUncompressedSourceDirectories += [ "sky_v2/textures/textures/jungle" ]
MapUncompressedSourceDirectories += [ "sky_v2/textures/textures/lacustre" ]
MapUncompressedSourceDirectories += [ "sky_v2/textures/setup/desert" ]
MapUncompressedSourceDirectories += [ "sky_v2/textures/setup/forest" ]
MapUncompressedSourceDirectories += [ "sky_v2/textures/setup/jungle" ]
MapUncompressedSourceDirectories += [ "sky_v2/textures/setup/lacustre" ]
MapUncompressedSourceDirectories += [ "sky_v2/textures/textures/nodds" ]

# Ligo directories
LigoBaseSourceDirectory = "landscape/ligo"

# Ig directories
IgLandSourceDirectories = [ ]
IgOtherSourceDirectories = [ ]
IgOtherSourceDirectories += [ "sky_v2/max" ]
IgPrimitiveSourceDirectories = [ ]

# Tiles root directory
TileRootSourceDirectory = "landscape/_texture_tiles"

# Displace directory
DisplaceSourceDirectory = "landscape/_texture_tiles/displace"

# Animation directories
AnimSourceDirectories = [ ]
AnimSourceDirectories += [ "sky_v2/max" ]


# *** LOOKUP DIRECTORIES WITHIN THE BUILD PIPELINE *** (TODO: use these instead of search_pathes in properties(_base).cfg)

# Ig lookup directories used by rbank
IgLookupDirectories = [ ]
IgLookupDirectories += [ CommonPath + "/ig_land" ]
IgLookupDirectories += [ CommonPath + "/ig_other" ]

# Shape lookup directories used by rbank
ShapeLookupDirectories = [ ]
# ShapeLookupDirectories += [ CommonPath + "/ps" ]
ShapeLookupDirectories += [ CommonPath + "/shape_optimized" ]
ShapeLookupDirectories += [ CommonPath + "/shape_with_coarse_mesh" ]

# Map lookup directories not yet used
MapLookupDirectories = [ ]
MapLookupDirectories += [ CommonPath + "/map_export" ]
MapLookupDirectories += [ CommonPath + "/map_uncompressed" ]

# Properties search paths
PropertiesExportBuildSearchPaths = [ ]
PropertiesExportBuildSearchPaths += ShapeLookupDirectories
PropertiesExportBuildSearchPaths += MapLookupDirectories
PropertiesExportBuildSearchPaths += [ "common/sfx/ps" ]
PropertiesExportBuildSearchPaths += [ "common/sfx/shape_optimized" ]
PropertiesExportBuildSearchPaths += [ "common/sfx/shape_with_coarse_mesh" ]
PropertiesExportBuildSearchPaths += [ "common/sfx/map_export" ]
PropertiesExportBuildSearchPaths += [ "common/sfx/map_uncompressed" ]


# *** EXPORT DIRECTORIES FOR THE BUILD PIPELINE ***

# Map directories
MapExportDirectory = CommonPath + "/map_export"
MapUncompressedExportDirectory = CommonPath + "/map_uncompressed"

# Shape directories
ShapeTagExportDirectory = CommonPath + "/shape_tag"
ShapeNotOptimizedExportDirectory = CommonPath + "/shape_not_optimized"
ShapeWithCoarseMeshExportDirectory = CommonPath + "/shape_with_coarse_mesh"
ShapeLightmapNotOptimizedExportDirectory = CommonPath + "/shape_lightmap_not_optimized"
ShapeAnimExportDirectory = CommonPath + "/shape_anim"

# Ig directories
IgStaticLandExportDirectory = CommonPath + "/ig_static_land" # Landscape IG eported from 3dsmax not elevated by the heightmap
IgStaticOtherExportDirectory = CommonPath + "/ig_static_other" # Village or construction IGs exported from 3dsmax
IgStaticTagExportDirectory = CommonPath + "/ig_static_tag" # Tag for exported 3dsmax files

# Zone directories
ZoneWeldBuildDirectory = CommonPath + "/zone_weld"
ZoneDependBuildDirectory = CommonPath + "/zone_depend"
ZoneLightWaterShapesLightedExportDirectory = CommonPath + "/zone_lwsl_temp" #fixme
ZoneLightBuildDirectory = CommonPath + "/zone_lighted" #fixme
ZoneLightDependBuildDirectory = CommonPath + "/zone_lighted_depend" #fixme
ZoneLightIgLandBuildDirectory = CommonPath + "/zone_lighted_ig_land" #fixme

# Animation directories
AnimExportDirectory = CommonPath + "/anim_export"
AnimTagExportDirectory = CommonPath + "/anim_tag"


# *** BUILD DIRECTORIES FOR THE BUILD PIPELINE ***

# Map directories
MapBuildDirectory = CommonPath + "/map"
MapPanoplyBuildDirectory = CommonPath + "/map_panoply"
MapPanoplyHlsInfoBuildDirectory = CommonPath + "/map_panoply_hls_info"
MapPanoplyHlsBankBuildDirectory = CommonPath + "/map_panoply_hls_bank"
MapPanoplyCacheBuildDirectory = CommonPath + "/map_panoply_cache"
MapTagBuildDirectory = CommonPath + "/map_tag"

# Shape directories
ShapeClodtexBuildDirectory = CommonPath + "/shape_clodtex_build"
ShapeOptimizedBuildDirectory = CommonPath + "/shape_optimized"
ShapeWithCoarseMeshBuildDirectory = CommonPath + "/shape_with_coarse_mesh_builded"
ShapeLightmapBuildDirectory = CommonPath + "/shape_lightmap"
ShapeLightmap16BitsBuildDirectory = CommonPath + "/shape_lightmap_16_bits"

# Ig directories 
IgElevLandPrimBuildDirectory = CommonPath + "/ig_elev_land_prim" # landscape IG generated by the prim exporter (already elevated by the land exporter)
IgElevLandLigoBuildDirectory = CommonPath + "/ig_elev_land_ligo" # Landscape IG found in ligo bricks from 3dsmax elevated by the heightmap
IgElevLandStaticBuildDirectory = CommonPath + "/ig_elev_land_static" # Landscape IG eported from 3dsmax elevated by the heightmap
IgTempLandMergeBuildDirectory = CommonPath + "/ig_temp_land_merge"
IgTempLandCompareBuildDirectory = CommonPath + "/ig_temp_land_compare" # Tmp final IG directory for landscape IGs before comparison
IgLandBuildDirectory = CommonPath + "/ig_land" # Final IG directory for landscape IGs
IgOtherBuildDirectory = CommonPath + "/ig_other" # Final IG directory for village or construction IGs
IgOtherLightedBuildDirectory = CommonPath + "/ig_other_lighted"

# Farbank directories
FarbankBuildDirectory = CommonPath + "/farbank"

# Ligo directories
LigoZoneBuildDirectory = CommonPath + "/ligo_zones"
LigoIgLandBuildDirectory = CommonPath + "/ligo_ig_land" # Landscape IG found in ligo bricks not elevated by the heightmap
LigoIgOtherBuildDirectory = CommonPath + "/ligo_ig_other" # Village or construction IGs exported from ligo landscape

# Animation directories
AnimBuildDirectory = CommonPath + "/anim"


# *** INSTALL DIRECTORIES IN THE CLIENT DATA ***

# Map directory
MapInstallDirectory = CommonName
BitmapInstallDirectory = MapInstallDirectory

# Shape directory
ShapeInstallDirectory = CommonName

# Lightmap directory
LightmapInstallDirectory = CommonName

# Animation directory
AnimInstallDirectory = CommonName

# Ig directory
IgInstallDirectory = CommonName
