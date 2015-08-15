# -*- coding: utf-8 -*-
import math

class Coordinate:
    ''
    @staticmethod
    def lonLat2Mercator(lon, lat ):
        x = lon * 20037508.342789/180
        y = math.log( math.tan((90+lat)*math.pi/360))/(math.pi/180)
        y *= 20037508.34789/180
        return x, y
    
if __name__ == "__main__":
    print( '''
此模块用来进行wgs84经纬度与墨卡托间相互转换。
测试输入为：116.39146944444444,39.906708333333334
           ''' )
    x,y = Coordinate.lonLat2Mercator( 116.39146944444444,39.906708333333334)
    print( x, y)
