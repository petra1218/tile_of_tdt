#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import sys
import coordinate
import math



url = r"http://t1.tianditu.cn/DataServer?T=%s"
#url = r"http://t1.tianditu.cn/DataServer?T=img_w&X=843&Y=388&l=10"

baseTileName = r"img_w&X=%d&Y=%d&l=%d"

baseTilePath = r"/home/petra/python/tile/beijing/%d/%s.map"

path = r"e:/tmp/cacheMap/img_w&X=843&Y=388&l=10.map"

#每张瓦片的像素
pixelPerTile = 256

#实际上是0级时，墨卡托的整体长度显示到一张瓦片上，瓦片的像素是256*256
#基础分辨率就是米每像素。
baseResolution = 20037508.3427892 * 2 / pixelPerTile

#墨卡托原点（-20037508.3427892， 20037508.3427892）
origin = (-20037508.3427892,20037508.3427892)

#计算瓦片的行列号，返回一个对儿
def getRowAndColume((x,y),level):
    '输入墨卡托坐标x，y，和需要计算的级别，返回包含当前坐标的瓦片的行列号'
    currResolution = baseResolution / math.pow( 2, level )
    meterPerTile = currResolution * pixelPerTile
    colume = math.ceil(( x - origin[0] )/ meterPerTile)
    row = math.ceil( origin[1] - y ) / meterPerTile
    tilename = baseTileName % (colume, row, level)
    return url % (tilename), baseTilePath % (level, tilename)

def makeUrl():
    pass

def makePath():
    pass

def schedule( a, b, c ):
    '''
        a:已经下载的数据块
        b:数据块的大小
        c:远程文件的大小
       '''
    per = 100.0 * a * b / c
    if per > 100 :
        per = 100
    print '%.2f%%' % per

def download( url, localpath ):
    urllib.urlretrieve(url = url, filename = localpath, reporthook = schedule ) 

def initParameter():
    print( "输入瓦片起/止级别和左上及右下角经纬度范围。" )
    tileMinLevel = raw_input( "输入瓦片的最小级别 ：" )
    tileMaxLevel = raw_input( "输入瓦片的最大级别 ：" )
    tileLeft = raw_input("输入瓦片范围 ：\n\t左 ：" )
    tileTop = raw_input("\t上 ：")
    tileRight = raw_input("\t右 ：")
    tileBottom = raw_input("\t下 ：")

def autoGrap(argc):
    tileMinLevel = string.atoi( argc[1] )
    tileMaxLevel = string.atoi( argc[2] )
    tileLeft = string.atof( argc[3] )
    tileTop = string.atof( argc[4] )
    tileRight = string.atof( argc[5] )
    tileBottom = string.atof( argc[6] )
    pass


#直接调用 tile.py 
if __name__ == "__main__":
    print(sys.argv)
    argvLen = len(sys.argv)
    print(argvLen)
    if argvLen == 1:#没输入参数，再分项输入
        initParameter()
    elif argvLen == 2 :
        tile = getRowAndColume(coordinate.Coordinate.lonLat2Mercator(116.39146944444444,39.906708333333334),18)
        if sys.argv[1] == 'test':#直接测试天安门
            print ( tile[0], tile[1] ) 
        elif sys.argv[1] == 'down':
            download(  tile[0], tile[1] )
    elif argvLen == 7 :#直接抓取参数顺序为 最小级别 最大级别 左 上 右 下
        print(sys.argv)
        autoGrap( sys.argv )
    else:
        print ('''
输入test来启动测试或输入其它合适参数:

直接抓取参数顺序为 最小级别 最大级别 左 上 右 下
''')
