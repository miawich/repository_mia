import pandas as pd
big_df = pd.read_csv('/Users/miawichman/PycharmProjects/P2_SP20/FINAL/data.csv')

sixties = big_df.drop(['1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967','1968', '1969'], axis=1)
df = sixties.drop(['1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984'], axis=1)
# isolating the immunization variables
df2 = df.drop(df.index[:129])
df3 = df2.drop(df2.index[6:345])
df4 = df3.drop(df3.index[12:351])
df5 = df4.drop(df4.index[18:357])
df6 = df5.drop(df5.index[24:363])
df7 = df6.drop(df6.index[30:369])
df8 = df7.drop(df7.index[36:375])
df9 = df8.drop(df8.index[42:381])
df10 = df9.drop(df9.index[48:387])
df11 = df10.drop(df10.index[54:393])
df12 = df11.drop(df11.index[60:399])
df13 = df12.drop(df12.index[66:405])
df14 = df13.drop(df13.index[72:411])
df15 = df14.drop(df14.index[78:417])
df16 = df15.drop(df15.index[84:423])
df17 = df16.drop(df16.index[90:429])
df18 = df17.drop(df17.index[96:435])
df19 = df18.drop(df18.index[102:441])
df20 = df19.drop(df19.index[108:447])
df21 = df20.drop(df20.index[114:453])
df22 = df21.drop(df21.index[120:459])
df23 = df22.drop(df22.index[126:465])
df24 = df23.drop(df23.index[132:471])
df25 = df24.drop(df24.index[138:477])
df26 = df25.drop(df25.index[144:483])
df27 = df26.drop(df26.index[150:489])
df28 = df27.drop(df27.index[156:495])
df29 = df28.drop(df28.index[162:501])
df30 = df29.drop(df29.index[168:507])
df31 = df30.drop(df30.index[174:513])
df32 = df31.drop(df31.index[180:519])
df33 = df32.drop(df32.index[186:525])
df34 = df33.drop(df33.index[192:531])
df35 = df34.drop(df34.index[198:537])
df36 = df35.drop(df35.index[204:543])
df37 = df36.drop(df36.index[210:549])
df38 = df37.drop(df37.index[216:555])
df39 = df38.drop(df38.index[222:561])
df40 = df39.drop(df39.index[228:567])
df41 = df40.drop(df40.index[234:573])
df42 = df41.drop(df41.index[240:579])
df43 = df42.drop(df42.index[246:585])
df44 = df43.drop(df43.index[252:591])
df45 = df44.drop(df44.index[258:597])
df46 = df45.drop(df45.index[264:603])
df47 = df46.drop(df46.index[270:609])
df48 = df47.drop(df47.index[276:615])
df49 = df48.drop(df48.index[282:621])
df50 = df49.drop(df49.index[288:627])
df51 = df50.drop(df50.index[294:633])
df52 = df51.drop(df51.index[300:639])
df53 = df52.drop(df52.index[306:645])
df54 = df53.drop(df53.index[312:651])
df55 = df54.drop(df54.index[318:657])
df56 = df55.drop(df55.index[324:663])
df57 = df56.drop(df56.index[330:669])
df58 = df57.drop(df57.index[336:675])
df59 = df58.drop(df58.index[342:681])
df60 = df59.drop(df59.index[348:687])
df61 = df60.drop(df60.index[354:693])
df62 = df61.drop(df61.index[360:699])
df63 = df62.drop(df62.index[366:705])
df64 = df63.drop(df63.index[372:711])
df65 = df64.drop(df64.index[378:717])
df66 = df65.drop(df65.index[384:723])
df67 = df66.drop(df66.index[390:729])
df68 = df67.drop(df67.index[396:735])
df69 = df68.drop(df68.index[402:741])
df70 = df69.drop(df69.index[408:747])
df71 = df70.drop(df70.index[414:753])
df72 = df71.drop(df71.index[420:759])
df73 = df72.drop(df72.index[426:765])
df74 = df73.drop(df73.index[432:771])
df75 = df74.drop(df74.index[438:777])
df76 = df75.drop(df75.index[444:783])
df77 = df76.drop(df76.index[450:789])
df78 = df77.drop(df77.index[456:795])
df79 = df78.drop(df78.index[462:801])
df80 = df79.drop(df79.index[468:807])
df81 = df80.drop(df80.index[474:813])
df82 = df81.drop(df81.index[480:819])
df83 = df82.drop(df82.index[486:825])
df84 = df83.drop(df83.index[492:831])
df85 = df84.drop(df84.index[498:837])
df86 = df85.drop(df85.index[504:843])
df87 = df86.drop(df86.index[510:849])
df88 = df87.drop(df87.index[516:855])
df89 = df88.drop(df88.index[522:861])
df90 = df89.drop(df89.index[528:867])
df91 = df90.drop(df90.index[534:873])
df92 = df91.drop(df91.index[540:879])
df93 = df92.drop(df92.index[546:885])
df94 = df93.drop(df93.index[552:891])
df95 = df94.drop(df94.index[558:897])
df96 = df95.drop(df95.index[564:903])
df97 = df96.drop(df96.index[570:909])
df98 = df97.drop(df97.index[576:915])
df99 = df98.drop(df98.index[582:921])
df100 = df99.drop(df99.index[588:927])
df101 = df100.drop(df100.index[594:933])
df102 = df101.drop(df101.index[600:939])
df103 = df102.drop(df102.index[606:945])
df104 = df103.drop(df103.index[612:951])
df105 = df104.drop(df104.index[618:957])
df106 = df105.drop(df105.index[624:963])
df107 = df106.drop(df106.index[630:969])
df108 = df107.drop(df107.index[636:975])
df109 = df108.drop(df108.index[642:981])
df110 = df109.drop(df109.index[648:987])
df111 = df110.drop(df110.index[654:993])
df112 = df111.drop(df111.index[660:999])
df113 = df112.drop(df112.index[666:1005])
df114 = df113.drop(df113.index[672:1011])
df115 = df114.drop(df114.index[678:1017])
df116 = df115.drop(df115.index[684:1023])
df117 = df116.drop(df116.index[690:1029])
df118 = df117.drop(df117.index[696:1035])
df119 = df118.drop(df118.index[702:1041])
df120 = df119.drop(df119.index[708:1047])
df121 = df120.drop(df120.index[714:1053])
df122 = df121.drop(df121.index[720:1059])
df123 = df122.drop(df122.index[726:1065])
df124 = df123.drop(df123.index[732:1071])
df125 = df124.drop(df124.index[738:1077])
df126 = df125.drop(df125.index[744:1083])
df127 = df126.drop(df126.index[750:1089])
df128 = df127.drop(df127.index[756:1095])
df129 = df128.drop(df128.index[762:1101])
df130 = df129.drop(df129.index[768:1107])
df131 = df130.drop(df130.index[774:1113])
df132 = df131.drop(df131.index[780:1119])
df133 = df132.drop(df132.index[786:1125])
df134 = df133.drop(df133.index[792:1131])
df135 = df134.drop(df134.index[798:1137])
df136 = df135.drop(df135.index[804:1143])
df137 = df136.drop(df136.index[810:1149])
df138 = df137.drop(df137.index[816:1155])
df139 = df138.drop(df138.index[822:1161])
df140 = df139.drop(df139.index[828:1167])
df141 = df140.drop(df140.index[834:1173])
df142 = df141.drop(df141.index[840:1179])
df143 = df142.drop(df142.index[846:1185])
df144 = df143.drop(df143.index[852:1191])
df145 = df144.drop(df144.index[858:1197])
df146 = df145.drop(df145.index[864:1203])
df147 = df146.drop(df146.index[870:1209])
df148 = df147.drop(df147.index[876:1215])
df149 = df148.drop(df148.index[882:1221])
df150 = df149.drop(df149.index[888:1227])
df151 = df150.drop(df150.index[894:1233])
df152 = df151.drop(df151.index[900:1239])
df153 = df152.drop(df152.index[906:1245])
df154 = df153.drop(df153.index[912:1251])
df155 = df154.drop(df154.index[918:1257])
df156 = df155.drop(df155.index[924:1263])
df157 = df156.drop(df156.index[930:1269])
df158 = df157.drop(df157.index[936:1275])
df159 = df158.drop(df158.index[942:1281])
df160 = df159.drop(df159.index[948:1287])
df161 = df160.drop(df160.index[954:1293])
df162 = df161.drop(df161.index[960:1299])
df163 = df162.drop(df162.index[966:1305])
df164 = df163.drop(df163.index[972:1311])
df165 = df164.drop(df164.index[978:1317])
df166 = df165.drop(df165.index[984:1323])
df167 = df166.drop(df166.index[990:1329])
df168 = df167.drop(df167.index[996:1335])
df169 = df168.drop(df168.index[1002:1341])
df170 = df169.drop(df169.index[1008:1347])
df171 = df170.drop(df170.index[1014:1353])
df172 = df171.drop(df171.index[1020:1359])
df173 = df172.drop(df172.index[1026:1365])
df174 = df173.drop(df173.index[1032:1371])
df175 = df174.drop(df174.index[1038:1377])
df176 = df175.drop(df175.index[1044:1383])
df177 = df176.drop(df176.index[1050:1389])
df178 = df177.drop(df177.index[1056:1395])
df179 = df178.drop(df178.index[1062:1401])
df180 = df179.drop(df179.index[1068:1407])
df181 = df180.drop(df180.index[1074:1413])
df182 = df181.drop(df181.index[1080:1419])
df183 = df182.drop(df182.index[1086:1425])
df184 = df183.drop(df183.index[1092:1431])
df185 = df184.drop(df184.index[1098:1437])
df186 = df185.drop(df185.index[1104:1443])
df187 = df186.drop(df186.index[1110:1449])
df188 = df187.drop(df187.index[1116:1455])
df189 = df188.drop(df188.index[1122:1461])
df190 = df189.drop(df189.index[1128:1467])
df191 = df190.drop(df190.index[1134:1473])
df192 = df191.drop(df191.index[1140:1479])
df193 = df192.drop(df192.index[1146:1485])
df194 = df193.drop(df193.index[1152:1491])
df195 = df194.drop(df194.index[1158:1497])
df196 = df195.drop(df195.index[1164:1503])
df197 = df196.drop(df196.index[1170:1509])
df198 = df197.drop(df197.index[1176:1515])
df199 = df198.drop(df198.index[1182:1521])
df200 = df199.drop(df199.index[1188:1527])
df201 = df200.drop(df200.index[1194:1533])
df202 = df201.drop(df201.index[1200:1539])
df203 = df202.drop(df202.index[1206:1545])
df204 = df203.drop(df203.index[1212:1551])
df205 = df204.drop(df204.index[1218:1557])
df206 = df205.drop(df205.index[1224:1563])
df207 = df206.drop(df206.index[1230:1569])
df208 = df207.drop(df207.index[1236:1575])
df209 = df208.drop(df208.index[1242:1581])
df210 = df209.drop(df209.index[1248:1587])
df211 = df210.drop(df210.index[1254:1593])
df212 = df211.drop(df211.index[1260:1599])
df213 = df212.drop(df212.index[1266:1605])
df214 = df213.drop(df213.index[1272:1611])
df215 = df214.drop(df214.index[1278:1617])
df216 = df215.drop(df215.index[1284:1623])
df217 = df216.drop(df216.index[1290:1629])
df218 = df217.drop(df217.index[1296:1635])
df219 = df218.drop(df218.index[1302:1641])
df220 = df219.drop(df219.index[1308:1647])
df221 = df220.drop(df220.index[1314:1653])
df222 = df221.drop(df221.index[1320:1659])
df223 = df222.drop(df222.index[1326:1665])
df224 = df223.drop(df223.index[1332:1671])
df225 = df224.drop(df224.index[1338:1677])
df226 = df225.drop(df225.index[1344:1683])
df227 = df226.drop(df226.index[1350:1689])
df228 = df227.drop(df227.index[1356:1695])
df229 = df228.drop(df228.index[1362:1701])
df230 = df229.drop(df229.index[1368:1707])
df231 = df230.drop(df230.index[1374:1713])
df232 = df231.drop(df231.index[1380:1719])
df233 = df232.drop(df232.index[1386:1725])
df234 = df233.drop(df233.index[1392:1731])
df235 = df234.drop(df234.index[1398:1737])
df236 = df235.drop(df235.index[1404:1743])
df237 = df236.drop(df236.index[1410:1749])
df238 = df237.drop(df237.index[1416:1755])
df239 = df238.drop(df238.index[1422:1761])
df240 = df239.drop(df239.index[1428:1767])
df241 = df240.drop(df240.index[1434:1773])
df242 = df241.drop(df241.index[1440:1779])
df243 = df242.drop(df242.index[1446:1785])
df244 = df243.drop(df243.index[1452:1791])
df245 = df244.drop(df244.index[1458:1797])
df246 = df245.drop(df245.index[1464:1803])
df247 = df246.drop(df246.index[1470:1809])
df248 = df247.drop(df247.index[1476:1815])
df249 = df248.drop(df248.index[1482:1821])
df250 = df249.drop(df249.index[1488:1827])
df251 = df250.drop(df250.index[1494:1833])
df252 = df251.drop(df251.index[1500:1839])
df253 = df252.drop(df252.index[1506:1845])
df254 = df253.drop(df253.index[1512:1851])
df255 = df254.drop(df254.index[1518:1857])
df256 = df255.drop(df255.index[1524:1863])
df257 = df256.drop(df256.index[1530:1869])
df258 = df257.drop(df257.index[1536:1875])
df259 = df258.drop(df258.index[1542:1881])
df260 = df259.drop(df259.index[1548:1887])