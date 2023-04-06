from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pykakasi

html_data ="""
<tbody>
                        <tr class="bg_gelb_20">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/1">1</a>
                </td>
                                    <td class="zentriert">2022/08/07</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(7.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="マンチェスター・ユナイテッドFC" href="/manchester-united/spielplan/verein/985/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/985.png?lm=1457975903" title="マンチェスター・ユナイテッドFC" alt="マンチェスター・ユナイテッドFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="マンチェスター・ユナイテッドFC" href="/manchester-united/spielplan/verein/985/saison_id/2022">マンチェスターU</a>&nbsp;&nbsp;<span class="tabellenplatz">(14.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3837822" href="/%E3%83%9E%E3%83%B3%E3%83%81%E3%82%A7%E3%82%B9%E3%82%BF%E3%83%BC-%E3%83%A6%E3%83%8A%E3%82%A4%E3%83%86%E3%83%83%E3%83%89fc_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3837822"><span class="greentext">1:2 </span></a></td>
                                    <td colspan="8" class="zentriert">控え</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/2">2</a>
                </td>
                                    <td class="zentriert">2022/08/13</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(7.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="ニューカッスル・ユナイテッドFC" href="/newcastle-united/spielplan/verein/762/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/762.png?lm=1472921161" title="ニューカッスル・ユナイテッドFC" alt="ニューカッスル・ユナイテッドFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="ニューカッスル・ユナイテッドFC" href="/newcastle-united/spielplan/verein/762/saison_id/2022">ニューカッスル</a>&nbsp;&nbsp;<span class="tabellenplatz">(4.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3837830" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%AB%E3%83%83%E3%82%B9%E3%83%AB-%E3%83%A6%E3%83%8A%E3%82%A4%E3%83%86%E3%83%83%E3%83%89fc/index/spielbericht/3837830"><span class="">0:0 </span></a></td>
                                    <td class="zentriert"><a href="" title=""></a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">15'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/3">3</a>
                </td>
                                    <td class="zentriert">2022/08/21</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(8.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="ウェストハム・ユナイテッド" href="/west-ham-united/spielplan/verein/379/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/379.png?lm=1464675260" title="ウェストハム・ユナイテッド" alt="ウェストハム・ユナイテッド" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="ウェストハム・ユナイテッド" href="/west-ham-united/spielplan/verein/379/saison_id/2022">ウェストハム</a>&nbsp;&nbsp;<span class="tabellenplatz">(19.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3837843" href="/%E3%82%A6%E3%82%A7%E3%82%B9%E3%83%88%E3%83%8F%E3%83%A0-%E3%83%A6%E3%83%8A%E3%82%A4%E3%83%86%E3%83%83%E3%83%89_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3837843"><span class="greentext">0:2 </span></a></td>
                                    <td class="zentriert"><a href="" title=""></a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">1'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/4">4</a>
                </td>
                                    <td class="zentriert">2022/08/27</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(5.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="リーズ・ユナイテッドFC" href="/leeds-united/spielplan/verein/399/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/399.png?lm=1645652224" title="リーズ・ユナイテッドFC" alt="リーズ・ユナイテッドFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="リーズ・ユナイテッドFC" href="/leeds-united/spielplan/verein/399/saison_id/2022">リーズ</a>&nbsp;&nbsp;<span class="tabellenplatz">(3.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3837847" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%83%AA%E3%83%BC%E3%82%BA-%E3%83%A6%E3%83%8A%E3%82%A4%E3%83%86%E3%83%83%E3%83%89fc/index/spielbericht/3837847"><span class="greentext">1:0 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ウィンガー">LW</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">11'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/5">5</a>
                </td>
                                    <td class="zentriert">2022/08/30</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(4.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="フラムFC" href="/fc-fulham/spielplan/verein/931/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/931.png?lm=1556831687" title="フラムFC" alt="フラムFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="フラムFC" href="/fc-fulham/spielplan/verein/931/saison_id/2022">フラム</a>&nbsp;&nbsp;<span class="tabellenplatz">(11.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3837856" href="/%E3%83%95%E3%83%A9%E3%83%A0fc_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3837856"><span class="redtext">2:1 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ウィンガー">LW</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">27'</td>
                            </tr>
                <tr class="bg_gelb_20">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/6">6</a>
                </td>
                                    <td class="zentriert">2022/09/04</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(4.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="レスター・シティ" href="/leicester-city/spielplan/verein/1003/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1003.png?lm=1472229265" title="レスター・シティ" alt="レスター・シティ" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="レスター・シティ" href="/leicester-city/spielplan/verein/1003/saison_id/2022">レスター</a>&nbsp;&nbsp;<span class="tabellenplatz">(20.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3837974" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%83%AC%E3%82%B9%E3%82%BF%E3%83%BC-%E3%82%B7%E3%83%86%E3%82%A3/index/spielbericht/3837974"><span class="greentext">5:2 </span></a></td>
                                    <td colspan="8" class="zentriert">控え</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/9">9</a>
                </td>
                                    <td class="zentriert">2022/10/01</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(3.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="リヴァプールFC" href="/fc-liverpool/spielplan/verein/31/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/31.png?lm=1456567819" title="リヴァプールFC" alt="リヴァプールFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="リヴァプールFC" href="/fc-liverpool/spielplan/verein/31/saison_id/2022">リヴァプール</a>&nbsp;&nbsp;<span class="tabellenplatz">(7.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838014" href="/%E3%83%AA%E3%83%B4%E3%82%A1%E3%83%97%E3%83%BC%E3%83%ABfc_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3838014"><span class="">3:3 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">25'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/10">10</a>
                </td>
                                    <td class="zentriert">2022/10/08</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(3.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="トッテナム・ホットスパー" href="/tottenham-hotspur/spielplan/verein/148/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/148.png?lm=1544345801" title="トッテナム・ホットスパー" alt="トッテナム・ホットスパー" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="トッテナム・ホットスパー" href="/tottenham-hotspur/spielplan/verein/148/saison_id/2022">トッテナム</a>&nbsp;&nbsp;<span class="tabellenplatz">(4.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838020" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%83%88%E3%83%83%E3%83%86%E3%83%8A%E3%83%A0-%E3%83%9B%E3%83%83%E3%83%88%E3%82%B9%E3%83%91%E3%83%BC/index/spielbericht/3838020"><span class="redtext">0:1 </span></a></td>
                                    <td class="zentriert"><a href="" title=""></a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">23'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/11">11</a>
                </td>
                                    <td class="zentriert">2022/10/14</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(4.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="ブレントフォードFC" href="/fc-brentford/spielplan/verein/1148/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1148.png?lm=1625150543" title="ブレントフォードFC" alt="ブレントフォードFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="ブレントフォードFC" href="/fc-brentford/spielplan/verein/1148/saison_id/2022">ブレントフォード</a>&nbsp;&nbsp;<span class="tabellenplatz">(10.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838029" href="/%E3%83%96%E3%83%AC%E3%83%B3%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%89fc_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3838029"><span class="redtext">2:0 </span></a></td>
                                    <td class="zentriert"><a href="" title="右ミッドフィールダー">RM</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">45'</td>
                            </tr>
                <tr class="bg_rot_20">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/12">12</a>
                </td>
                                    <td class="zentriert">2022/10/18</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(4.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="ノッティンガム・フォレスト" href="/nottingham-forest/spielplan/verein/703/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/703.png?lm=1598890289" title="ノッティンガム・フォレスト" alt="ノッティンガム・フォレスト" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="ノッティンガム・フォレスト" href="/nottingham-forest/spielplan/verein/703/saison_id/2022">ノッテ・フォレスト</a>&nbsp;&nbsp;<span class="tabellenplatz">(20.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838053" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%83%8E%E3%83%83%E3%83%86%E3%82%A3%E3%83%B3%E3%82%AC%E3%83%A0-%E3%83%95%E3%82%A9%E3%83%AC%E3%82%B9%E3%83%88/index/spielbericht/3838053"><span class="">0:0 </span></a></td>
                                    <td colspan="8" class="zentriert">ベンチ外</td>
                            </tr>
                <tr class="bg_rot_20">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/13">13</a>
                </td>
                                    <td class="zentriert">2022/10/22</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(5.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="マンチェスター・シティFC" href="/manchester-city/spielplan/verein/281/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/281.png?lm=1467356331" title="マンチェスター・シティFC" alt="マンチェスター・シティFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="マンチェスター・シティFC" href="/manchester-city/spielplan/verein/281/saison_id/2022">マンチェスターC</a>&nbsp;&nbsp;<span class="tabellenplatz">(2.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838192" href="/%E3%83%9E%E3%83%B3%E3%83%81%E3%82%A7%E3%82%B9%E3%82%BF%E3%83%BC-%E3%82%B7%E3%83%86%E3%82%A3fc_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3838192"><span class="redtext">3:1 </span></a></td>
                                    <td colspan="8" class="zentriert">ベンチ外</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/14">14</a>
                </td>
                                    <td class="zentriert">2022/10/29</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(7.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="チェルシーFC" href="/fc-chelsea/spielplan/verein/631/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/631.png?lm=1628160548" title="チェルシーFC" alt="チェルシーFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="チェルシーFC" href="/fc-chelsea/spielplan/verein/631/saison_id/2022">チェルシー</a>&nbsp;&nbsp;<span class="tabellenplatz">(5.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838207" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%83%81%E3%82%A7%E3%83%AB%E3%82%B7%E3%83%BCfc/index/spielbericht/3838207"><span class="greentext">4:1 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert">1</td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">73'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/15">15</a>
                </td>
                                    <td class="zentriert">2022/11/05</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(6.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="ウルバーハンプトン・ワンダラーズ" href="/wolverhampton-wanderers/spielplan/verein/543/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/543.png?lm=1467496784" title="ウルバーハンプトン・ワンダラーズ" alt="ウルバーハンプトン・ワンダラーズ" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="ウルバーハンプトン・ワンダラーズ" href="/wolverhampton-wanderers/spielplan/verein/543/saison_id/2022">ウルバーハンプトン</a>&nbsp;&nbsp;<span class="tabellenplatz">(19.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838235" href="/%E3%82%A6%E3%83%AB%E3%83%90%E3%83%BC%E3%83%8F%E3%83%B3%E3%83%97%E3%83%88%E3%83%B3-%E3%83%AF%E3%83%B3%E3%83%80%E3%83%A9%E3%83%BC%E3%82%BA_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3838235"><span class="greentext">2:3 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert">1</td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">90'</td>
                            </tr>
                <tr class="bg_rot_20">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/16">16</a>
                </td>
                                    <td class="zentriert">2022/11/13</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(4.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="アストン・ヴィラFC" href="/aston-villa/spielplan/verein/405/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/405.png?lm=1469443765" title="アストン・ヴィラFC" alt="アストン・ヴィラFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="アストン・ヴィラFC" href="/aston-villa/spielplan/verein/405/saison_id/2022">アストン・ヴィラ</a>&nbsp;&nbsp;<span class="tabellenplatz">(13.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838237" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%82%A2%E3%82%B9%E3%83%88%E3%83%B3-%E3%83%B4%E3%82%A3%E3%83%A9fc/index/spielbericht/3838237"><span class="redtext">1:2 </span></a></td>
                                    <td colspan="8" class="zentriert">ベンチ外</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/17">17</a>
                </td>
                                    <td class="zentriert">2022/12/26</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(6.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="サウサンプトンFC" href="/fc-southampton/spielplan/verein/180/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/180.png?lm=1444560086" title="サウサンプトンFC" alt="サウサンプトンFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="サウサンプトンFC" href="/fc-southampton/spielplan/verein/180/saison_id/2022">サウサンプトン</a>&nbsp;&nbsp;<span class="tabellenplatz">(19.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838261" href="/%E3%82%B5%E3%82%A6%E3%82%B5%E3%83%B3%E3%83%97%E3%83%88%E3%83%B3fc_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3838261"><span class="greentext">1:3 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ウィンガー">LW</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">90'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/18">18</a>
                </td>
                                    <td class="zentriert">2022/12/31</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(5.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="アーセナルFC" href="/fc-arsenal/spielplan/verein/11/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/11.png?lm=1489787850" title="アーセナルFC" alt="アーセナルFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="アーセナルFC" href="/fc-arsenal/spielplan/verein/11/saison_id/2022">アーセナル</a>&nbsp;&nbsp;<span class="tabellenplatz">(1.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838263" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%82%A2%E3%83%BC%E3%82%BB%E3%83%8A%E3%83%ABfc/index/spielbericht/3838263"><span class="redtext">2:4 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert">1</td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">90'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/19">19</a>
                </td>
                                    <td class="zentriert">2023/01/03</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(6.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="エヴァートンFC" href="/fc-everton/spielplan/verein/29/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/29.png?lm=1445949846" title="エヴァートンFC" alt="エヴァートンFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="エヴァートンFC" href="/fc-everton/spielplan/verein/29/saison_id/2022">エヴァートン</a>&nbsp;&nbsp;<span class="tabellenplatz">(16.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838277" href="/%E3%82%A8%E3%83%B4%E3%82%A1%E3%83%BC%E3%83%88%E3%83%B3fc_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3838277"><span class="greentext">1:4 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert">1</td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">78'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/20">20</a>
                </td>
                                    <td class="zentriert">2023/01/14</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(6.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="リヴァプールFC" href="/fc-liverpool/spielplan/verein/31/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/31.png?lm=1456567819" title="リヴァプールFC" alt="リヴァプールFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="リヴァプールFC" href="/fc-liverpool/spielplan/verein/31/saison_id/2022">リヴァプール</a>&nbsp;&nbsp;<span class="tabellenplatz">(7.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838793" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%83%AA%E3%83%B4%E3%82%A1%E3%83%97%E3%83%BC%E3%83%ABfc/index/spielbericht/3838793"><span class="greentext">3:0 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">90'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/21">21</a>
                </td>
                                    <td class="zentriert">2023/01/21</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(5.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="レスター・シティ" href="/leicester-city/spielplan/verein/1003/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1003.png?lm=1472229265" title="レスター・シティ" alt="レスター・シティ" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="レスター・シティ" href="/leicester-city/spielplan/verein/1003/saison_id/2022">レスター</a>&nbsp;&nbsp;<span class="tabellenplatz">(15.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838787" href="/%E3%83%AC%E3%82%B9%E3%82%BF%E3%83%BC-%E3%82%B7%E3%83%86%E3%82%A3_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3838787"><span class="">2:2 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ウィンガー">LW</a></td>
                    <td class="zentriert">1</td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">90'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/22">22</a>
                </td>
                                    <td class="zentriert">2023/02/04</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(5.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="AFCボーンマス" href="/afc-bournemouth/spielplan/verein/989/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/989.png?lm=1457991811" title="AFCボーンマス" alt="AFCボーンマス" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="AFCボーンマス" href="/afc-bournemouth/spielplan/verein/989/saison_id/2022">ボーンマス</a>&nbsp;&nbsp;<span class="tabellenplatz">(18.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838773" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_afc%E3%83%9C%E3%83%BC%E3%83%B3%E3%83%9E%E3%82%B9/index/spielbericht/3838773"><span class="greentext">1:0 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert">1</td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">90'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/23">23</a>
                </td>
                                    <td class="zentriert">2023/02/11</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(5.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="クリスタル・パレスFC" href="/crystal-palace/spielplan/verein/873/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/873.png?lm=1457723287" title="クリスタル・パレスFC" alt="クリスタル・パレスFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="クリスタル・パレスFC" href="/crystal-palace/spielplan/verein/873/saison_id/2022">クリスタル・パレス</a>&nbsp;&nbsp;<span class="tabellenplatz">(12.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838768" href="/%E3%82%AF%E3%83%AA%E3%82%B9%E3%82%BF%E3%83%AB-%E3%83%91%E3%83%AC%E3%82%B9fc_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3838768"><span class="">1:1 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">90'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/24">24</a>
                </td>
                                    <td class="zentriert">2023/02/18</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(5.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="フラムFC" href="/fc-fulham/spielplan/verein/931/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/931.png?lm=1556831687" title="フラムFC" alt="フラムFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="フラムFC" href="/fc-fulham/spielplan/verein/931/saison_id/2022">フラム</a>&nbsp;&nbsp;<span class="tabellenplatz">(9.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838753" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%83%95%E3%83%A9%E3%83%A0fc/index/spielbericht/3838753"><span class="redtext">0:1 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">90'</td>
                            </tr>
                <tr class="bg_rot_20">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/25">25</a>
                </td>
                                    <td class="zentriert">2023/02/25</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(6.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="ニューカッスル・ユナイテッドFC" href="/newcastle-united/spielplan/verein/762/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/762.png?lm=1472921161" title="ニューカッスル・ユナイテッドFC" alt="ニューカッスル・ユナイテッドFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="ニューカッスル・ユナイテッドFC" href="/newcastle-united/spielplan/verein/762/saison_id/2022">ニューカッスル</a>&nbsp;&nbsp;<span class="tabellenplatz">(4.)</span></td>
                                <td class="zentriert"><a title="試合プレビュー" class="" href="/%E3%83%8B%E3%83%A5%E3%83%BC%E3%82%AB%E3%83%83%E3%82%B9%E3%83%AB-%E3%83%A6%E3%83%8A%E3%82%A4%E3%83%86%E3%83%83%E3%83%89fc_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3838748"><span class="">-:- </span></a></td>
                                    <td colspan="8" class="zentriert">情報なし</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/26">26</a>
                </td>
                                    <td class="zentriert">2023/03/04</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(6.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="ウェストハム・ユナイテッド" href="/west-ham-united/spielplan/verein/379/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/379.png?lm=1464675260" title="ウェストハム・ユナイテッド" alt="ウェストハム・ユナイテッド" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="ウェストハム・ユナイテッド" href="/west-ham-united/spielplan/verein/379/saison_id/2022">ウェストハム</a>&nbsp;&nbsp;<span class="tabellenplatz">(17.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838737" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%82%A6%E3%82%A7%E3%82%B9%E3%83%88%E3%83%8F%E3%83%A0-%E3%83%A6%E3%83%8A%E3%82%A4%E3%83%86%E3%83%83%E3%83%89/index/spielbericht/3838737"><span class="greentext">4:0 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert">1</td>
                    <td class="zentriert">1</td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">83'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/27">27</a>
                </td>
                                    <td class="zentriert">2023/03/11</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(6.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="リーズ・ユナイテッドFC" href="/leeds-united/spielplan/verein/399/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/399.png?lm=1645652224" title="リーズ・ユナイテッドFC" alt="リーズ・ユナイテッドFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="リーズ・ユナイテッドFC" href="/leeds-united/spielplan/verein/399/saison_id/2022">リーズ</a>&nbsp;&nbsp;<span class="tabellenplatz">(15.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838725" href="/%E3%83%AA%E3%83%BC%E3%82%BA-%E3%83%A6%E3%83%8A%E3%82%A4%E3%83%86%E3%83%83%E3%83%89fc_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3838725"><span class="">2:2 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert">1</td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">90'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/8">8</a>
                </td>
                                    <td class="zentriert">2023/03/15</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(3.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="クリスタル・パレスFC" href="/crystal-palace/spielplan/verein/873/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/873.png?lm=1457723287" title="クリスタル・パレスFC" alt="クリスタル・パレスFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="クリスタル・パレスFC" href="/crystal-palace/spielplan/verein/873/saison_id/2022">クリスタル・パレス</a>&nbsp;&nbsp;<span class="tabellenplatz">(12.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838000" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%82%AF%E3%83%AA%E3%82%B9%E3%82%BF%E3%83%AB-%E3%83%91%E3%83%AC%E3%82%B9fc/index/spielbericht/3838000"><span class="greentext">1:0 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert">1</td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">79'</td>
                            </tr>
                <tr class="bg_rot_20">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/28">28</a>
                </td>
                                    <td class="zentriert">2023/03/19</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(6.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="マンチェスター・ユナイテッドFC" href="/manchester-united/spielplan/verein/985/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/985.png?lm=1457975903" title="マンチェスター・ユナイテッドFC" alt="マンチェスター・ユナイテッドFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="マンチェスター・ユナイテッドFC" href="/manchester-united/spielplan/verein/985/saison_id/2022">マンチェスターU</a>&nbsp;&nbsp;<span class="tabellenplatz">(3.)</span></td>
                                <td class="zentriert"><a title="試合プレビュー" class="" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%83%9E%E3%83%B3%E3%83%81%E3%82%A7%E3%82%B9%E3%82%BF%E3%83%BC-%E3%83%A6%E3%83%8A%E3%82%A4%E3%83%86%E3%83%83%E3%83%89fc/index/spielbericht/3838714"><span class="">-:- </span></a></td>
                                    <td colspan="8" class="zentriert">情報なし</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/29">29</a>
                </td>
                                    <td class="zentriert">2023/04/01</td>
                    <td class="zentriert hauptlink">H</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(6.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="ブレントフォードFC" href="/fc-brentford/spielplan/verein/1148/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1148.png?lm=1625150543" title="ブレントフォードFC" alt="ブレントフォードFC" class="tiny_wappen"></a></td>
                    <td class="no-border-links hauptlink"><a title="ブレントフォードFC" href="/fc-brentford/spielplan/verein/1148/saison_id/2022">ブレントフォード</a>&nbsp;&nbsp;<span class="tabellenplatz">(8.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3838708" href="/%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3_%E3%83%96%E3%83%AC%E3%83%B3%E3%83%88%E3%83%95%E3%82%A9%E3%83%BC%E3%83%89fc/index/spielbericht/3838708"><span class="">3:3 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert">1</td>
                    <td class="zentriert"></td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">90'</td>
                            </tr>
                <tr class="">
                <td class="zentriert">
                    <a href="/%E3%83%97%E3%83%AC%E3%83%9F%E3%82%A2%E3%83%AA%E3%83%BC%E3%82%B0/spieltag/wettbewerb/GB1/saison_id/2022/spieltag/7">7</a>
                </td>
                                    <td class="zentriert">2023/04/04</td>
                    <td class="zentriert hauptlink">A</td>
                                            <td class="zentriert no-border-rechts"><a title="ブライトン&amp;ホーヴ・アルビオン" href="/brighton-amp-hove-albion/spielplan/verein/1237/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/1237.png?lm=1492718902" title="ブライトン&amp;ホーヴ・アルビオン" alt="ブライトン&amp;ホーヴ・アルビオン" class="tiny_wappen"></a></td>
                        <td class="zentriert no-border-links"><span class="tabellenplatz">(4.)</span></td>
                                        <td class="zentriert no-border-rechts"><a title="AFCボーンマス" href="/afc-bournemouth/spielplan/verein/989/saison_id/2022"><img src="https://tmssl.akamaized.net/images/wappen/tiny/989.png?lm=1457991811" title="AFCボーンマス" alt="AFCボーンマス" class="tiny_wappen"></a></td>
                    <td class="no-border-links "><a title="AFCボーンマス" href="/afc-bournemouth/spielplan/verein/989/saison_id/2022">ボーンマス</a>&nbsp;&nbsp;<span class="tabellenplatz">(13.)</span></td>
                                <td class="zentriert"><a title="" class="ergebnis-link" id="3837988" href="/afc%E3%83%9C%E3%83%BC%E3%83%B3%E3%83%9E%E3%82%B9_%E3%83%96%E3%83%A9%E3%82%A4%E3%83%88%E3%83%B3-amp-%E3%83%9B%E3%83%BC%E3%83%B4-%E3%82%A2%E3%83%AB%E3%83%93%E3%82%AA%E3%83%B3/index/spielbericht/3837988"><span class="greentext">0:2 </span></a></td>
                                    <td class="zentriert"><a href="" title="左ミッドフィールダー">LM</a></td>
                    <td class="zentriert"></td>
                    <td class="zentriert">1</td>
                                        <td class="zentriert"></td>
                    <td class="zentriert"></td>
                    <td class="zentriert"></td>
                                        <td class="rechts">90'</td>
                            </tr>
                </tbody>
"""

soup = BeautifulSoup(html_data, "html.parser")

matches = soup.find_all("tr")

opponents = []
play_times = []

# pykakasiの初期化
kks = pykakasi.kakasi()

for match in matches:
    opponent = match.find("td", {"class": "no-border-links hauptlink"})
    if opponent:
        # カタカナをローマ字に変換する
        kana_name = opponent.text.strip()
        romaji_name = kks.convert(kana_name)[0]['hepburn']
        opponents.append(romaji_name)

        play_time_td = match.find("td", {"class": "rechts"})
        if play_time_td:
            play_time = int(play_time_td.text.strip().replace("'", ""))
            play_times.append(play_time)
        elif "控え" in match.text:
            play_times.append(0)
        elif "ベンチ外" in match.text:
            play_times.append(-1)
        elif "情報なし" in match.text:
            play_times.append(-2)

plt.figure(figsize=(15, 5))
plt.bar(opponents, play_times, color='blue')
plt.xlabel("Opponents")
plt.ylabel("Play Time (minutes)")
plt.title("Play Time by Opponent")
plt.savefig("play_time_by_opponent.png")
plt.show()
