import geopandas as gpd
import numpy as np
from application.db import db_postgis, get_cursor
from shapely.geometry import Point, Polygon

class Timezone:

    gdf = None

    def __init__(self):
        pass

    def get_all(self):
        cur = get_cursor()
        sql = "SELECT tzid FROM timezones_world WHERE tzid != 'uninhabited';"
        cur.execute(sql)
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append(row[0])
        cur.close()
        return result

    def get_timezone_world(self, lon, lat):
        cur = get_cursor()
        sql = '''
                SELECT 
                    tzid
                FROM
                    timezones_world
                WHERE
                    ST_Contains(geom, ST_MakePoint(''' + str(lon) + ''', ''' + str(lat) + '''))
                LIMIT 1
                OFFSET 0;
            '''
        cur.execute(sql)
        rows = cur.fetchall()
        result = {}
        for row in rows:
            result["timezone"] = row[0]
        cur.close()
        return result

    def get_timezone_utc(self, lon, lat):
        cur = get_cursor()
        sql = '''
                SELECT 
                    name
                FROM
                    timezones_utc
                WHERE
                    ST_Contains(geom, ST_MakePoint(''' + str(lon) + ''', ''' + str(lat) + '''))
                LIMIT 1
                OFFSET 0;
            '''
        cur.execute(sql)
        rows = cur.fetchall()
        result = {}
        for row in rows:
            result["timezone"] = "UTC" + row[0]
        cur.close()
        return result

    def set_gdf_utc_raw(self):
        boundary = 10 ** -10 # need because neigbours boundary are the same
        print(boundary)
        left = -180.0
        right = -172.5
        utc_polygons = []
        utc_offsets = []
        for i in range(-12, 12):
            p = Polygon(
                [
                    (left, 90.0),
                    (right - boundary, 90.0),
                    (right - boundary, -90.0),
                    (left, -90.0)
                ]
            )
            utc_polygons.append(p)
            utc_offsets.append('UTC' + '{:+d}'.format(i))

            left = right
            right += 15.0 if i < 12 else 7.5

        self.gdf = gpd.GeoDataFrame()
        self.gdf['offset'] = utc_offsets
        self.gdf['geometry'] = utc_polygons
        self.gdf = self.gdf.set_geometry('geometry')

    def get_timezone_utc_raw(self, lon, lat):
        location = Point(lon, lat)

        result = {}

        try:
            self.set_gdf_utc_raw()
        except:
            return result

        for index, row in self.gdf.iterrows():
            if location.within(row['geometry']) or location.touches(row['geometry']):
                return {
                    "timezone": row['offset']
                }

        return result