# -*- coding: utf-8 -*-
"""
Dibuat oleh : BEBEN GRAHA PUTRA
"""
import arcpy

def competitorscomplementrev2():  # competitors_complement_rev2

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    arcpy.ImportToolbox(r"c:\users\beben\appdata\local\programs\arcgis\pro\Resources\ArcToolbox\toolboxes\Analysis Tools.tbx")
    outlet = arcpy.GetParameterAsText(0)
    poi_competitors_or_complement = arcpy.GetParameterAsText(1)

    # Process: Generate Drive Time Trade Areas (Generate Drive Time Trade Areas) (ba)
    driving_time_result = arcpy.GetParameterAsText(2)
    arcpy.ba.GenerateDriveTimeTradeArea(in_features=outlet, out_feature_class=driving_time_result, distance_type="Driving Time", distances=[5, 10], units="MINUTES", id_field="", dissolve_option="OVERLAP", remove_overlap="KEEP_OVERLAP", travel_direction="TOWARD_STORES", time_of_day="", time_zone="TIME_ZONE_AT_LOCATION", search_tolerance="", polygon_detail="STANDARD", input_method="VALUES", expression="")

    # Process: Clip (Clip) (analysis)
    competitors_catchments = arcpy.GetParameterAsText(3)
    arcpy.analysis.Clip(in_features=poi_competitors_or_complement, clip_features=driving_time_result, out_feature_class=competitors_catchments, cluster_tolerance="")

    # Process: Generate Origin-Destination Links (Generate Origin-Destination Links) (analysis)
    spider_analysist = arcpy.GetParameterAsText(4)
    arcpy.analysis.GenerateOriginDestinationLinks(origin_features=outlet, destination_features=competitors_catchments, out_feature_class=spider_analysist, origin_group_field="", destination_group_field="", line_type="PLANAR", num_nearest=500, search_distance=1500, distance_unit="METERS", aggregate_links="NO_AGGREGATE", sum_fields=[])

    # Process: Spatial Join (Spatial Join) (analysis)
    competitor_complement_data_in_catchment_area_business = arcpy.GetParameterAsText(5)
    arcpy.analysis.SpatialJoin(target_features=spider_analysist, join_features=poi_competitors_or_complement, out_feature_class=competitor_complement_data_in_catchment_area_business, join_operation="JOIN_ONE_TO_ONE", join_type="KEEP_ALL", field_mapping="", match_option="INTERSECT", search_radius="1 Meters", distance_field_name="")

if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(scratchWorkspace=r"D:\Fellowship Program - Esri Indonesia\tes_gis_engineer\geoprocessing\geoprocessing.gdb", workspace=r"D:\Fellowship Program - Esri Indonesia\tes_gis_engineer\geoprocessing\geoprocessing.gdb"):
        competitorscomplementrev2()
