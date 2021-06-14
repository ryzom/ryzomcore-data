#!/usr/bin/python
# 
# \file config.py
# \brief Process configuration
# \date 2010-05-24 06:30GMT
# \author Jan Boon (Kaetemi)
# Python port of game data build pipeline.
# Process configuration.
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

# *** PROCESS CONFIGURATION ***


# *** PROCESS CONFIG ***
ProcessToComplete = [ ]
ProcessToComplete += [ "properties" ]
ProcessToComplete += [ "ligo" ]
ProcessToComplete += [ "zone" ]
ProcessToComplete += [ "ig" ]
ProcessToComplete += [ "zone_light" ]
ProcessToComplete += [ "rbank" ]
ProcessToComplete += [ "ig_light" ]
ProcessToComplete += [ "ps" ]
ProcessToComplete += [ "ai_wmap" ]
ProcessToComplete += [ "cartographer" ]
ProcessToComplete += [ "pz" ]


# *** ECOSYSTEM AND CONTINENT NAMES ***

EcosystemName = "desert"
EcosystemPath = "ecosystems/" + EcosystemName
ContinentName = "r2_desert"
ContinentPath = "continents/" + ContinentName
CommonName = ContinentName
CommonPath = ContinentPath


# *** LANDSCAPE NAME ***
LandscapeName = ContinentName

# *** CONTINENT FILE ***
ContinentSheet = ContinentName
ContinentFile = ContinentName + "/" + ContinentSheet + ".continent"



# *** SHAPE EXPORT OPTIONS ***

# Compute lightmaps ?
ShapeExportOptExportLighting = "true"

# Cast shadow in lightmap ?
ShapeExportOptShadow = "true"

# Lighting limits. 0 : normal, 1 : soft shadows
ShapeExportOptLightingLimit = 0

# Lightmap lumel size
ShapeExportOptLumelSize = "0.25"

# Oversampling value. Can be 1, 2, 4 or 8
ShapeExportOptOversampling = 1

# Does the lightmap must be generated in 8 bits format ?
ShapeExportOpt8BitsLightmap = "false"

# Does the lightmaps export must generate logs ?
ShapeExportOptLightmapLog = "true"

# Coarse mesh texture mul size
TextureMulSizeValue = "1.5"

BuildShadowSkinEnabled = False

ClodConfigFile = ""

# *** COARSE MESH TEXTURE NAME ***
CoarseMeshTextureNames = [ ]

# *** BANK EXPORT OPTIONS ***

# *** POSTFIX USED BY THE MULTIPLE TILES SYSTEM ***
MultipleTilesPostfix = [ ]
MultipleTilesPostfix += [ "_sp" ]
MultipleTilesPostfix += [ "_su" ]
MultipleTilesPostfix += [ "_au" ]
MultipleTilesPostfix += [ "_wi" ]

# Name of the tilebank to use
BankTileBankName = EcosystemName


# *** LIGO OPTIONS ***
LigoExportLand = ContinentName + ".land"
LigoExportOnePass = 0
LigoExportColormap = "colormap_" + ContinentName + ".tga"
LigoExportHeightmap1 = "big_" + ContinentName + ".tga"
LigoExportZFactor1 = "1.0"
LigoExportHeightmap2 = "noise_" + ContinentName + ".tga"
LigoExportZFactor2 = "0.5"
LigoTileBankFile = "landscape/_texture_tiles/" + EcosystemName + "/" + EcosystemName + ".bank"

# *** ZONE REGIONS ( up-left, down-right ) ***
ZoneRegions = [ ] 
ZoneRegions += [ [ "6_fb" ] + [ "67_hk" ] ]

# *** RBANK OPTIONS ***

# Options
RBankVerbose = 1
RBankConsistencyCheck = 0
RbankReduceSurfaces = 1
RbankSmoothBorders = 1
RbankComputeElevation = 0
RbankComputeLevels = 1
RbankLinkElements = 1
RbankCutEdges = 1
RbankUseZoneSquare = 0

# Region to compute ( ALPHA UPPER CASE! )
RbankZoneUl = "5_FA"
RbankZoneDr = "68_HL"

# Output names
RbankRbankName = LandscapeName

# *** MAPS OPTIONS ***
ReduceBitmapFactor = 0
# list all panoply files
MapPanoplyFileList = None
# name of the .hlsbank to build.
MapHlsBankFileName = None

# *** AI WMAP OPTIONS ***
AiWmapContinentName = ContinentName
AiWmapVerbose = 0
AiWmapStartPoints = [ ]
AiWmapStartPoints += [ ContinentName + " 22791 -1289" ]
AiWmapStartPoints += [ ContinentName + " 25980 -2015" ]
AiWmapStartPoints += [ ContinentName + " 28070 -2340" ]
AiWmapStartPoints += [ ContinentName + " 22383 -1512" ]
AiWmapStartPoints += [ ContinentName + " 28923 -1434" ]
AiWmapStartPoints += [ ContinentName + " 26950 -2015" ]
AiWmapStartPoints += [ ContinentName + " 27600 -1924" ]
AiWmapStartPoints += [ ContinentName + " 25050 -2650" ]
AiWmapStartPoints += [ ContinentName + " 25880 -2630" ]
AiWmapStartPoints += [ ContinentName + " 27760 -2700" ]
AiWmapStartPoints += [ ContinentName + " 24257 -1520" ]
AiWmapStartPoints += [ ContinentName + " 28942 -1919" ]
AiWmapStartPoints += [ ContinentName + " 23250 -1840" ]
AiWmapStartPoints += [ ContinentName + " 27915 -1875" ]
AiWmapStartPoints += [ ContinentName + " 23305 -2454" ]
AiWmapStartPoints += [ ContinentName + " 23452 -1050" ]
AiWmapStartPoints += [ ContinentName + " 29554 -1468" ]
AiWmapStartPoints += [ ContinentName + " 22304 -1856" ]
AiWmapStartPoints += [ ContinentName + " 23730 -2280" ]
AiWmapStartPoints += [ ContinentName + " 24560 -2015" ]
AiWmapStartPoints += [ ContinentName + " 27814 -1375" ]
AiWmapStartPoints += [ ContinentName + " 30629 -2300" ]
AiWmapStartPoints += [ ContinentName + " 21500 -1830" ]
AiWmapStartPoints += [ ContinentName + " 26650 -2650" ]
AiWmapStartPoints += [ ContinentName + " 29510 -2040" ]
AiWmapStartPoints += [ ContinentName + " 26694 -1485" ]
AiWmapStartPoints += [ ContinentName + " 25523 -1500" ]
AiWmapStartPoints += [ ContinentName + " 25206 -2118" ]
AiWmapStartPoints += [ ContinentName + " 21845 -2475" ]
AiWmapStartPoints += [ ContinentName + " 22627 -2480" ]
AiWmapStartPoints += [ ContinentName + " 26051 -1405" ]
AiWmapStartPoints += [ ContinentName + " 30818 -1487" ]

# *** PZ OPTIONS ***
PackedZoneCWMap = ContinentName + "_0.cwmap2"

# *** CARTOGRAPHER OPTIONS ***
CartographerContinent = ContinentName
IslandsXmlFile = ContinentName + "_islands.xml"
