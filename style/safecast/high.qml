<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis styleCategories="AllStyleCategories" simplifyLocal="1" simplifyDrawingTol="1" version="3.8.0-Zanzibar" minScale="1e+8" simplifyAlgorithm="0" simplifyMaxScale="1" maxScale="0" hasScaleBasedVisibilityFlag="0" labelsEnabled="0" simplifyDrawingHints="0" readOnly="1">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" forceraster="0" enableorderby="0" type="RuleRenderer">
    <rules key="{ef9c05bc-623f-4d54-87b1-65702532359b}">
      <rule filter="&quot;ader_microsvh&quot; >= 0.000000 AND &quot;ader_microsvh&quot; &lt;= 0.050000" label=" &lt; 0.05" symbol="0" key="{319c914e-16e4-49c1-ad5c-f6f6f40765c5}"/>
      <rule filter="&quot;ader_microsvh&quot; > 0.050000 AND &quot;ader_microsvh&quot; &lt;= 0.100000" label=" 0.05 - 0.10" symbol="1" key="{17f4fd94-3de5-45ee-b298-0a5dd554e98f}"/>
      <rule filter="&quot;ader_microsvh&quot; > 0.100000 AND &quot;ader_microsvh&quot; &lt;= 0.200000" label=" 0.10 - 0.20 " symbol="2" key="{04bd2c8c-39b7-42f7-92b0-349a09ccadc4}"/>
      <rule filter="&quot;ader_microsvh&quot; > 0.200000 AND &quot;ader_microsvh&quot; &lt;= 0.300000" label=" 0.20 - 0.30" symbol="3" key="{d79cefe2-a910-4eb1-93ea-84817efaf127}"/>
      <rule filter="&quot;ader_microsvh&quot; > 0.300000 AND &quot;ader_microsvh&quot; &lt;= 0.800000" label=" 0.30 - 0.80" symbol="4" key="{af276ca5-628b-4814-bc75-b15a0e50348d}"/>
      <rule filter="&quot;ader_microsvh&quot; > 0.800000 AND &quot;ader_microsvh&quot; &lt;= 1.000000" label=" 0.8 - 1 " symbol="5" key="{5fbbe992-0a0c-42be-b15e-5b6a3f7d8374}"/>
      <rule filter="&quot;ader_microsvh&quot; > 1.000000 AND &quot;ader_microsvh&quot; &lt;= 5.000000" label=" 1 - 5 " symbol="6" key="{76754177-11cb-490b-971e-dfbde6210768}"/>
      <rule filter="&quot;ader_microsvh&quot; > 5.000000 AND &quot;ader_microsvh&quot; &lt;= 10.000000" label=" 5 - 10 " symbol="7" key="{cb70567e-0e15-4d75-abf7-5f782d8a8469}"/>
      <rule filter="&quot;ader_microsvh&quot; > 10.000000 AND &quot;ader_microsvh&quot; &lt;= 70.000000" label=" 10 - 70 " symbol="8" key="{da5c8cff-dc86-4305-8558-525e1a445400}"/>
      <rule filter="ELSE" label="> 70" symbol="9" key="{eb4e8e8f-09c0-48f1-8165-8f8a1491cb19}"/>
    </rules>
    <symbols>
      <symbol name="0" force_rhr="0" alpha="1" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
          <prop v="0" k="angle"/>
          <prop v="0,0,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="no" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="1" force_rhr="0" alpha="1" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
          <prop v="0" k="angle"/>
          <prop v="0,0,157,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="no" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="2" force_rhr="0" alpha="1" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
          <prop v="0" k="angle"/>
          <prop v="0,59,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="no" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="3" force_rhr="0" alpha="1" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
          <prop v="0" k="angle"/>
          <prop v="0,217,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="no" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="4" force_rhr="0" alpha="1" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
          <prop v="0" k="angle"/>
          <prop v="119,135,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="no" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="5" force_rhr="0" alpha="1" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
          <prop v="0" k="angle"/>
          <prop v="255,0,232,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="no" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="6" force_rhr="0" alpha="1" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
          <prop v="0" k="angle"/>
          <prop v="255,0,75,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="no" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="7" force_rhr="0" alpha="1" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
          <prop v="0" k="angle"/>
          <prop v="255,184,0,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="no" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="8" force_rhr="0" alpha="1" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
          <prop v="0" k="angle"/>
          <prop v="255,255,113,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="0,0,0,0" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
      <symbol name="9" force_rhr="0" alpha="1" clip_to_extent="1" type="marker">
        <layer class="SimpleMarker" pass="0" enabled="1" locked="0">
          <prop v="0" k="angle"/>
          <prop v="255,255,255,255" k="color"/>
          <prop v="1" k="horizontal_anchor_point"/>
          <prop v="bevel" k="joinstyle"/>
          <prop v="circle" k="name"/>
          <prop v="0,0" k="offset"/>
          <prop v="3x:0,0,0,0,0,0" k="offset_map_unit_scale"/>
          <prop v="MM" k="offset_unit"/>
          <prop v="35,35,35,255" k="outline_color"/>
          <prop v="solid" k="outline_style"/>
          <prop v="0" k="outline_width"/>
          <prop v="3x:0,0,0,0,0,0" k="outline_width_map_unit_scale"/>
          <prop v="MM" k="outline_width_unit"/>
          <prop v="diameter" k="scale_method"/>
          <prop v="2" k="size"/>
          <prop v="3x:0,0,0,0,0,0" k="size_map_unit_scale"/>
          <prop v="MM" k="size_unit"/>
          <prop v="1" k="vertical_anchor_point"/>
          <data_defined_properties>
            <Option type="Map">
              <Option name="name" value="" type="QString"/>
              <Option name="properties"/>
              <Option name="type" value="collection" type="QString"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
  </renderer-v2>
  <customproperties>
    <property value="0" key="embeddedWidgets/count"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory diagramOrientation="Up" penAlpha="255" sizeType="MM" backgroundColor="#ffffff" scaleBasedVisibility="0" minimumSize="0" rotationOffset="270" scaleDependency="Area" backgroundAlpha="255" opacity="1" penWidth="0" penColor="#000000" lineSizeType="MM" labelPlacementMethod="XHeight" barWidth="5" width="15" minScaleDenominator="0" enabled="0" height="15" lineSizeScale="3x:0,0,0,0,0,0" sizeScale="3x:0,0,0,0,0,0" maxScaleDenominator="1e+8">
      <fontProperties style="tučné" description="Arial,14,-1,0,75,0,0,0,0,0,tučné"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings priority="0" showAll="1" dist="0" obstacle="0" placement="0" zIndex="0" linePlacementFlags="18">
    <properties>
      <Option type="Map">
        <Option name="name" value="" type="QString"/>
        <Option name="properties"/>
        <Option name="type" value="collection" type="QString"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="ader_microsvh">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="time_local">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="speed_kmph">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="dose_increment">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="time_cumulative">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="dose_cumulative">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="device">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="device_id">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="date_time">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="cpm">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pulses5s">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="pulses_total">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="validity">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="lat_deg">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="hemisphere">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="long_deg">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="east_west">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="altitude">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="gps_validity">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="sat">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="hdop">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="checksum">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias name="ADER (microSv/h)" index="0" field="ader_microsvh"/>
    <alias name="Local time" index="1" field="time_local"/>
    <alias name="Speed (km/h)" index="2" field="speed_kmph"/>
    <alias name="Increment DOSE" index="3" field="dose_increment"/>
    <alias name="Cumulative time" index="4" field="time_cumulative"/>
    <alias name="Cumulative DOSE" index="5" field="dose_cumulative"/>
    <alias name="Device" index="6" field="device"/>
    <alias name="Device ID" index="7" field="device_id"/>
    <alias name="Datetime" index="8" field="date_time"/>
    <alias name="CPM" index="9" field="cpm"/>
    <alias name="Pulses 5sec" index="10" field="pulses5s"/>
    <alias name="Pulses total" index="11" field="pulses_total"/>
    <alias name="Validity" index="12" field="validity"/>
    <alias name="Latitude (deg)" index="13" field="lat_deg"/>
    <alias name="Hemisphere" index="14" field="hemisphere"/>
    <alias name="Longitude (deg)" index="15" field="long_deg"/>
    <alias name="East/West" index="16" field="east_west"/>
    <alias name="Altitude" index="17" field="altitude"/>
    <alias name="GPS Validity" index="18" field="gps_validity"/>
    <alias name="Sat" index="19" field="sat"/>
    <alias name="HDOP" index="20" field="hdop"/>
    <alias name="CheckSum" index="21" field="checksum"/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default applyOnUpdate="0" expression="" field="ader_microsvh"/>
    <default applyOnUpdate="0" expression="" field="time_local"/>
    <default applyOnUpdate="0" expression="" field="speed_kmph"/>
    <default applyOnUpdate="0" expression="" field="dose_increment"/>
    <default applyOnUpdate="0" expression="" field="time_cumulative"/>
    <default applyOnUpdate="0" expression="" field="dose_cumulative"/>
    <default applyOnUpdate="0" expression="" field="device"/>
    <default applyOnUpdate="0" expression="" field="device_id"/>
    <default applyOnUpdate="0" expression="" field="date_time"/>
    <default applyOnUpdate="0" expression="" field="cpm"/>
    <default applyOnUpdate="0" expression="" field="pulses5s"/>
    <default applyOnUpdate="0" expression="" field="pulses_total"/>
    <default applyOnUpdate="0" expression="" field="validity"/>
    <default applyOnUpdate="0" expression="" field="lat_deg"/>
    <default applyOnUpdate="0" expression="" field="hemisphere"/>
    <default applyOnUpdate="0" expression="" field="long_deg"/>
    <default applyOnUpdate="0" expression="" field="east_west"/>
    <default applyOnUpdate="0" expression="" field="altitude"/>
    <default applyOnUpdate="0" expression="" field="gps_validity"/>
    <default applyOnUpdate="0" expression="" field="sat"/>
    <default applyOnUpdate="0" expression="" field="hdop"/>
    <default applyOnUpdate="0" expression="" field="checksum"/>
  </defaults>
  <constraints>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="ader_microsvh" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="time_local" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="speed_kmph" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="dose_increment" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="time_cumulative" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="dose_cumulative" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="device" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="device_id" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="date_time" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="cpm" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="pulses5s" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="pulses_total" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="validity" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="lat_deg" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="hemisphere" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="long_deg" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="east_west" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="altitude" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="gps_validity" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="sat" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="hdop" unique_strength="0"/>
    <constraint constraints="0" notnull_strength="0" exp_strength="0" field="checksum" unique_strength="0"/>
  </constraints>
  <constraintExpressions>
    <constraint exp="" desc="" field="ader_microsvh"/>
    <constraint exp="" desc="" field="time_local"/>
    <constraint exp="" desc="" field="speed_kmph"/>
    <constraint exp="" desc="" field="dose_increment"/>
    <constraint exp="" desc="" field="time_cumulative"/>
    <constraint exp="" desc="" field="dose_cumulative"/>
    <constraint exp="" desc="" field="device"/>
    <constraint exp="" desc="" field="device_id"/>
    <constraint exp="" desc="" field="date_time"/>
    <constraint exp="" desc="" field="cpm"/>
    <constraint exp="" desc="" field="pulses5s"/>
    <constraint exp="" desc="" field="pulses_total"/>
    <constraint exp="" desc="" field="validity"/>
    <constraint exp="" desc="" field="lat_deg"/>
    <constraint exp="" desc="" field="hemisphere"/>
    <constraint exp="" desc="" field="long_deg"/>
    <constraint exp="" desc="" field="east_west"/>
    <constraint exp="" desc="" field="altitude"/>
    <constraint exp="" desc="" field="gps_validity"/>
    <constraint exp="" desc="" field="sat"/>
    <constraint exp="" desc="" field="hdop"/>
    <constraint exp="" desc="" field="checksum"/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction value="{00000000-0000-0000-0000-000000000000}" key="Canvas"/>
  </attributeactions>
  <attributetableconfig actionWidgetStyle="dropDown" sortOrder="0" sortExpression="">
    <columns>
      <column name="ader_microsvh" width="-1" hidden="0" type="field"/>
      <column name="time_local" width="-1" hidden="0" type="field"/>
      <column name="speed_kmph" width="-1" hidden="0" type="field"/>
      <column name="dose_increment" width="-1" hidden="0" type="field"/>
      <column name="time_cumulative" width="-1" hidden="0" type="field"/>
      <column name="dose_cumulative" width="-1" hidden="0" type="field"/>
      <column name="device" width="-1" hidden="0" type="field"/>
      <column name="device_id" width="-1" hidden="0" type="field"/>
      <column name="date_time" width="-1" hidden="0" type="field"/>
      <column name="cpm" width="-1" hidden="0" type="field"/>
      <column name="pulses5s" width="-1" hidden="0" type="field"/>
      <column name="pulses_total" width="-1" hidden="0" type="field"/>
      <column name="validity" width="-1" hidden="0" type="field"/>
      <column name="lat_deg" width="-1" hidden="0" type="field"/>
      <column name="hemisphere" width="-1" hidden="0" type="field"/>
      <column name="long_deg" width="-1" hidden="0" type="field"/>
      <column name="east_west" width="-1" hidden="0" type="field"/>
      <column name="altitude" width="-1" hidden="0" type="field"/>
      <column name="gps_validity" width="-1" hidden="0" type="field"/>
      <column name="sat" width="-1" hidden="0" type="field"/>
      <column name="hdop" width="-1" hidden="0" type="field"/>
      <column name="checksum" width="-1" hidden="0" type="field"/>
      <column width="-1" hidden="1" type="actions"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <editform tolerant="1"></editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath></editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
QGIS forms can have a Python function that is called when the form is
opened.

Use this function to add extra logic to your forms.

Enter the name of the function in the "Python Init function"
field.
An example follows:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
	geom = feature.geometry()
	control = dialog.findChild(QWidget, "MyLineEdit")
]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field name="ader_microsvh" editable="1"/>
    <field name="altitude" editable="1"/>
    <field name="checksum" editable="1"/>
    <field name="cpm" editable="1"/>
    <field name="date_time" editable="1"/>
    <field name="device" editable="1"/>
    <field name="device_id" editable="1"/>
    <field name="dose_cumulative" editable="1"/>
    <field name="dose_increment" editable="1"/>
    <field name="east_west" editable="1"/>
    <field name="gps_validity" editable="1"/>
    <field name="hdop" editable="1"/>
    <field name="hemisphere" editable="1"/>
    <field name="lat_deg" editable="1"/>
    <field name="long_deg" editable="1"/>
    <field name="pulses5s" editable="1"/>
    <field name="pulses_total" editable="1"/>
    <field name="sat" editable="1"/>
    <field name="speed_kmph" editable="1"/>
    <field name="time_cumulative" editable="1"/>
    <field name="time_local" editable="1"/>
    <field name="validity" editable="1"/>
  </editable>
  <labelOnTop>
    <field name="ader_microsvh" labelOnTop="0"/>
    <field name="altitude" labelOnTop="0"/>
    <field name="checksum" labelOnTop="0"/>
    <field name="cpm" labelOnTop="0"/>
    <field name="date_time" labelOnTop="0"/>
    <field name="device" labelOnTop="0"/>
    <field name="device_id" labelOnTop="0"/>
    <field name="dose_cumulative" labelOnTop="0"/>
    <field name="dose_increment" labelOnTop="0"/>
    <field name="east_west" labelOnTop="0"/>
    <field name="gps_validity" labelOnTop="0"/>
    <field name="hdop" labelOnTop="0"/>
    <field name="hemisphere" labelOnTop="0"/>
    <field name="lat_deg" labelOnTop="0"/>
    <field name="long_deg" labelOnTop="0"/>
    <field name="pulses5s" labelOnTop="0"/>
    <field name="pulses_total" labelOnTop="0"/>
    <field name="sat" labelOnTop="0"/>
    <field name="speed_kmph" labelOnTop="0"/>
    <field name="time_cumulative" labelOnTop="0"/>
    <field name="time_local" labelOnTop="0"/>
    <field name="validity" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>device_id</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>0</layerGeometryType>
</qgis>
