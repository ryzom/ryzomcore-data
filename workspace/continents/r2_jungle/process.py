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
ProcessToComplete += [ "map" ]
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

EcosystemName = "jungle"
EcosystemPath = "ecosystems/" + EcosystemName
ContinentName = "r2_jungle"
ContinentPath = "continents/" + ContinentName
CommonName = ContinentName
CommonPath = ContinentPath

ParentName = "zorai"
ParentPath = "continents/" + ParentName


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
LigoExportExtendCoords = 1
LigoTileBankFile = "landscape/_texture_tiles/" + EcosystemName + "/" + EcosystemName + ".bank"

# *** ZONE REGIONS ( up-left, down-right ) ***
ZoneRegions = [ ] 
ZoneRegions += [ [ "69_hm" ] + [ "130_jv" ] ]

# *** RBANK OPTIONS ***

# Options
RBankVerbose = 0
RBankConsistencyCheck = 0
RbankReduceSurfaces = 1
RbankSmoothBorders = 1
RbankComputeElevation = 0
RbankComputeLevels = 1
RbankLinkElements = 1
RbankCutEdges = 1
RbankUseZoneSquare = 0

# Region to compute ( ALPHA UPPER CASE! )
RbankZoneUl = "68_HL"
RbankZoneDr = "131_JV"

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
AiWmapStartPoints += [ ContinentName + " 31300 -11100" ] # 1
AiWmapStartPoints += [ ContinentName + " 32203 -11283" ] # 2
AiWmapStartPoints += [ ContinentName + " 33100 -11200" ] # 3
AiWmapStartPoints += [ ContinentName + " 33840 -11000" ] # 4
AiWmapStartPoints += [ ContinentName + " 33768 -11279" ] # 5
AiWmapStartPoints += [ ContinentName + " 34426 -11339" ] # 6
AiWmapStartPoints += [ ContinentName + " 35300 -11200" ] # 7
AiWmapStartPoints += [ ContinentName + " 36200 -11200" ] # 8
AiWmapStartPoints += [ ContinentName + " 36694 -11144" ] # 9
AiWmapStartPoints += [ ContinentName + " 37600 -11200" ]
AiWmapStartPoints += [ ContinentName + " 38400 -11200" ]
AiWmapStartPoints += [ ContinentName + " 39235 -11288" ]
AiWmapStartPoints += [ ContinentName + " 40200 -11220" ] # 13
AiWmapStartPoints += [ ContinentName + " 40700 -11200" ]
AiWmapStartPoints += [ ContinentName + " 31300 -12000" ]
AiWmapStartPoints += [ ContinentName + " 32200 -12000" ]
AiWmapStartPoints += [ ContinentName + " 33000 -12000" ]
AiWmapStartPoints += [ ContinentName + " 34000 -12000" ]
AiWmapStartPoints += [ ContinentName + " 35000 -12000" ]
AiWmapStartPoints += [ ContinentName + " 35720 -12100" ] # 20
AiWmapStartPoints += [ ContinentName + " 36600 -12000" ]
AiWmapStartPoints += [ ContinentName + " 37400 -12000" ]
AiWmapStartPoints += [ ContinentName + " 38200 -12000" ]
AiWmapStartPoints += [ ContinentName + " 39000 -12000" ]
AiWmapStartPoints += [ ContinentName + " 39723 -12066" ]
AiWmapStartPoints += [ ContinentName + " 40600 -12000" ]
AiWmapStartPoints += [ ContinentName + " 31250 -12750" ] # 27
AiWmapStartPoints += [ ContinentName + " 31600 -12550" ]
AiWmapStartPoints += [ ContinentName + " 31753 -12934" ]
AiWmapStartPoints += [ ContinentName + " 32318 -12599" ]
AiWmapStartPoints += [ ContinentName + " 33151 -12888" ] # 31
AiWmapStartPoints += [ ContinentName + " 33700 -12700" ]
AiWmapStartPoints += [ ContinentName + " 34300 -13000" ]
AiWmapStartPoints += [ ContinentName + " 35260 -12700" ] # 34
AiWmapStartPoints += [ ContinentName + " 35800 -12800" ] # 35
AiWmapStartPoints += [ ContinentName + " 36800 -12800" ]
AiWmapStartPoints += [ ContinentName + " 37700 -12800" ]
AiWmapStartPoints += [ ContinentName + " 38320 -12800" ]
AiWmapStartPoints += [ ContinentName + " 39000 -12800" ] # 39
AiWmapStartPoints += [ ContinentName + " 39800 -12800" ]
AiWmapStartPoints += [ ContinentName + " 40800 -12800" ] # 41
AiWmapStartPoints += [ ContinentName + " 31300 -13650" ] # 42
AiWmapStartPoints += [ ContinentName + " 32100 -13600" ] # 43
AiWmapStartPoints += [ ContinentName + " 32800 -13600" ]
AiWmapStartPoints += [ ContinentName + " 33600 -13600" ]
AiWmapStartPoints += [ ContinentName + " 34200 -13600" ]
AiWmapStartPoints += [ ContinentName + " 35250 -13450" ] # 47
AiWmapStartPoints += [ ContinentName + " 36000 -13500" ]
AiWmapStartPoints += [ ContinentName + " 36650 -13500" ]
AiWmapStartPoints += [ ContinentName + " 37400 -13600" ]
AiWmapStartPoints += [ ContinentName + " 38100 -13500" ]
AiWmapStartPoints += [ ContinentName + " 38700 -13500" ]
AiWmapStartPoints += [ ContinentName + " 39500 -13500" ]

# *** PZ OPTIONS ***
PackedZoneCWMap = ContinentName + "_0.cwmap2"

# *** CARTOGRAPHER OPTIONS ***
CartographerContinent = ContinentName
IslandsXmlFile = ContinentName + "_islands.xml"
CartographerSeasonSuffixes = [ "_sp" ]
