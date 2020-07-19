#importing library to scrap a webpage
from bs4 import BeautifulSoup
import json
from json import dumps
import requests
from kafka import KafkaProducer
#A html table of mlb players
html_doc = """
<table class="suppress_all sortable stats_table now_sortable" id="leader_standard_W" data-cols-to-freeze="2"><caption> Table</caption><thead><tr><th class="right">Rank</th>
<th class="sort_default_asc">Player (yrs, age)</th>
<th class="right">Wins</th><th>Throws</th></tr></thead><tbody><tr data-row="0"><td class="right">1.</td><td csk="Colon,Bartolo"><a href="/players/c/colonba01.shtml"><strong>Bartolo&nbsp;Colon</strong></a>&nbsp;(21, 46)</td><td class="right">247</td><td class="right">R</td></tr>
<tr data-row="1"><td class="right">2.</td><td csk="Verlander,Justin"><a href="/players/v/verlaju01.shtml"><strong>Justin&nbsp;Verlander</strong></a>&nbsp;(15, 36)</td><td class="right">225</td><td class="right">R</td></tr>
<tr data-row="2"><td class="right">3.</td><td csk="Greinke,Zack"><a href="/players/g/greinza01.shtml"><strong>Zack&nbsp;Greinke</strong></a>&nbsp;(16, 35)</td><td class="right">205</td><td class="right">R</td></tr>
<tr data-row="3"><td class="right">4.</td><td csk="Lester,Jon"><a href="/players/l/lestejo01.shtml"><strong>Jon&nbsp;Lester</strong></a>&nbsp;(14, 35)</td><td class="right">190</td><td class="right">L</td></tr>
<tr data-row="4"><td class="right">5.</td><td csk="Scherzer,Max"><a href="/players/s/scherma01.shtml"><strong>Max&nbsp;Scherzer</strong></a>&nbsp;(12, 34)</td><td class="right">170</td><td class="right">R</td></tr>
<tr data-row="5"><td class="right">6.</td><td csk="Hernandez,Felix"><a href="/players/h/hernafe02.shtml"><strong>Felix&nbsp;Hernandez</strong></a>&nbsp;(15, 33)</td><td class="right">169</td><td class="right">R</td></tr>
<tr data-row="6"><td class="right">&nbsp;</td><td csk="Kershaw,Clayton"><a href="/players/k/kershcl01.shtml"><strong>Clayton&nbsp;Kershaw</strong></a>&nbsp;(12, 31)</td><td class="right">169</td><td class="right">L</td></tr>
<tr data-row="7"><td class="right">8.</td><td csk="Hamels,Cole"><a href="/players/h/hamelco01.shtml"><strong>Cole&nbsp;Hamels</strong></a>&nbsp;(14, 35)</td><td class="right">163</td><td class="right">L</td></tr>
<tr data-row="8"><td class="right">9.</td><td csk="Wainwright,Adam"><a href="/players/w/wainwad01.shtml"><strong>Adam&nbsp;Wainwright</strong></a>&nbsp;(14, 37)</td><td class="right">162</td><td class="right">R</td></tr>
<tr data-row="9"><td class="right">10.</td><td csk="Price,David"><a href="/players/p/priceda01.shtml"><strong>David&nbsp;Price</strong></a>&nbsp;(12, 33)</td><td class="right">150</td><td class="right">L</td></tr>
<tr data-row="10"><td class="right">11.</td><td csk="Porcello,Rick"><a href="/players/p/porceri01.shtml"><strong>Rick&nbsp;Porcello</strong></a>&nbsp;(11, 30)</td><td class="right">149</td><td class="right">R</td></tr>
<tr data-row="11"><td class="right">12.</td><td csk="Gonzalez,Gio"><a href="/players/g/gonzagi01.shtml"><strong>Gio&nbsp;Gonzalez</strong></a>&nbsp;(12, 33)</td><td class="right">130</td><td class="right">L</td></tr>
<tr data-row="12"><td class="right">13.</td><td csk="Cueto,Johnny"><a href="/players/c/cuetojo01.shtml"><strong>Johnny&nbsp;Cueto</strong></a>&nbsp;(12, 33)</td><td class="right">126</td><td class="right">R</td></tr>
<tr data-row="13"><td class="right">14.</td><td csk="Happ,J.A."><a href="/players/h/happja01.shtml"><strong>J.A.&nbsp;Happ</strong></a>&nbsp;(13, 36)</td><td class="right">121</td><td class="right">L</td></tr>
<tr data-row="14"><td class="right">15.</td><td csk="Bumgarner,Madison"><a href="/players/b/bumgama01.shtml"><strong>Madison&nbsp;Bumgarner</strong></a>&nbsp;(11, 29)</td><td class="right">119</td><td class="right">L</td></tr>
<tr data-row="15"><td class="right">16.</td><td csk="Jimenez,Ubaldo"><a href="/players/j/jimenub01.shtml"><strong>Ubaldo&nbsp;Jimenez</strong></a>&nbsp;(12, 35)</td><td class="right">114</td><td class="right">R</td></tr>
<tr data-row="16"><td class="right">17.</td><td csk="Liriano,Francisco"><a href="/players/l/liriafr01.shtml"><strong>Francisco&nbsp;Liriano</strong></a>&nbsp;(14, 35)</td><td class="right">112</td><td class="right">L</td></tr>
<tr data-row="17"><td class="right">&nbsp;</td><td csk="Strasburg,Stephen"><a href="/players/s/strasst01.shtml"><strong>Stephen&nbsp;Strasburg</strong></a>&nbsp;(10, 30)</td><td class="right">112</td><td class="right">R</td></tr>
<tr data-row="18"><td class="right">19.</td><td csk="Sale,Chris"><a href="/players/s/salech01.shtml"><strong>Chris&nbsp;Sale</strong></a>&nbsp;(10, 30)</td><td class="right">109</td><td class="right">L</td></tr>
<tr data-row="19"><td class="right">20.</td><td csk="Sanchez,Anibal"><a href="/players/s/sanchan01.shtml"><strong>Anibal&nbsp;Sanchez</strong></a>&nbsp;(14, 35)</td><td class="right">108</td><td class="right">R</td></tr>
<tr data-row="20"><td class="right">21.</td><td csk="Jackson,Edwin"><a href="/players/j/jacksed01.shtml"><strong>Edwin&nbsp;Jackson</strong></a>&nbsp;(17, 35)</td><td class="right">107</td><td class="right">R</td></tr>
<tr data-row="21"><td class="right">22.</td><td csk="Arrieta,Jake"><a href="/players/a/arrieja01.shtml"><strong>Jake&nbsp;Arrieta</strong></a>&nbsp;(10, 33)</td><td class="right">106</td><td class="right">R</td></tr>
<tr data-row="22"><td class="right">23.</td><td csk="Leake,Mike"><a href="/players/l/leakemi01.shtml"><strong>Mike&nbsp;Leake</strong></a>&nbsp;(10, 31)</td><td class="right">105</td><td class="right">R</td></tr>
<tr data-row="23"><td class="right">24.</td><td csk="Kluber,Corey"><a href="/players/k/klubeco01.shtml"><strong>Corey&nbsp;Kluber</strong></a>&nbsp;(9, 33)</td><td class="right">98</td><td class="right">R</td></tr>
<tr data-row="24"><td class="right">&nbsp;</td><td csk="Lynn,Lance"><a href="/players/l/lynnla01.shtml"><strong>Lance&nbsp;Lynn</strong></a>&nbsp;(8, 32)</td><td class="right">98</td><td class="right">R</td></tr>
<tr data-row="25"><td class="right">26.</td><td csk="Kennedy,Ian"><a href="/players/k/kenneia01.shtml"><strong>Ian&nbsp;Kennedy</strong></a>&nbsp;(13, 34)</td><td class="right">97</td><td class="right">R</td></tr>
<tr data-row="26"><td class="right">27.</td><td csk="Zimmermann,Jordan"><a href="/players/z/zimmejo02.shtml"><strong>Jordan&nbsp;Zimmermann</strong></a>&nbsp;(11, 33)</td><td class="right">95</td><td class="right">R</td></tr>
<tr data-row="27"><td class="right">28.</td><td csk="Cole,Gerrit"><a href="/players/c/colege01.shtml"><strong>Gerrit&nbsp;Cole</strong></a>&nbsp;(7, 28)</td><td class="right">94</td><td class="right">R</td></tr>
<tr data-row="28"><td class="right">29.</td><td csk="Volquez,Edinson"><a href="/players/v/volqued01.shtml"><strong>Edinson&nbsp;Volquez</strong></a>&nbsp;(14, 35)</td><td class="right">93</td><td class="right">R</td></tr>
<tr data-row="29"><td class="right">30.</td><td csk="Morton,Charlie"><a href="/players/m/mortoch02.shtml"><strong>Charlie&nbsp;Morton</strong></a>&nbsp;(12, 35)</td><td class="right">91</td><td class="right">R</td></tr>
<tr data-row="30"><td class="right">31.</td><td csk="Nova,Ivan"><a href="/players/n/novaiv01.shtml"><strong>Ivan&nbsp;Nova</strong></a>&nbsp;(10, 32)</td><td class="right">89</td><td class="right">R</td></tr>
<tr data-row="31"><td class="right">32.</td><td csk="Carrasco,Carlos"><a href="/players/c/carraca01.shtml"><strong>Carlos&nbsp;Carrasco</strong></a>&nbsp;(10, 32)</td><td class="right">85</td><td class="right">R</td></tr>
<tr data-row="32"><td class="right">&nbsp;</td><td csk="Miley,Wade"><a href="/players/m/mileywa01.shtml"><strong>Wade&nbsp;Miley</strong></a>&nbsp;(9, 32)</td><td class="right">85</td><td class="right">L</td></tr>
<tr data-row="33"><td class="right">34.</td><td csk="Cahill,Trevor"><a href="/players/c/cahiltr01.shtml"><strong>Trevor&nbsp;Cahill</strong></a>&nbsp;(11, 31)</td><td class="right">84</td><td class="right">R</td></tr>
<tr data-row="34"><td class="right">&nbsp;</td><td csk="Keuchel,Dallas"><a href="/players/k/keuchda01.shtml"><strong>Dallas&nbsp;Keuchel</strong></a>&nbsp;(8, 31)</td><td class="right">84</td><td class="right">L</td></tr>
<tr data-row="35"><td class="right">36.</td><td csk="Quintana,Jose"><a href="/players/q/quintjo01.shtml"><strong>Jose&nbsp;Quintana</strong></a>&nbsp;(8, 30)</td><td class="right">83</td><td class="right">L</td></tr>
<tr data-row="36"><td class="right">37.</td><td csk="Bailey,Homer"><a href="/players/b/baileho02.shtml"><strong>Homer&nbsp;Bailey</strong></a>&nbsp;(13, 33)</td><td class="right">80</td><td class="right">R</td></tr>
<tr data-row="37"><td class="right">&nbsp;</td><td csk="Samardzija,Jeff"><a href="/players/s/samarje01.shtml"><strong>Jeff&nbsp;Samardzija</strong></a>&nbsp;(12, 34)</td><td class="right">80</td><td class="right">R</td></tr>
<tr data-row="38"><td class="right">39.</td><td csk="Holland,Derek"><a href="/players/h/hollade01.shtml"><strong>Derek&nbsp;Holland</strong></a>&nbsp;(11, 32)</td><td class="right">78</td><td class="right">L</td></tr>
<tr data-row="39"><td class="right">40.</td><td csk="Chacin,Jhoulys"><a href="/players/c/chacijh01.shtml"><strong>Jhoulys&nbsp;Chacin</strong></a>&nbsp;(11, 31)</td><td class="right">77</td><td class="right">R</td></tr>
<tr data-row="40"><td class="right">&nbsp;</td><td csk="Teheran,Julio"><a href="/players/t/teherju01.shtml"><strong>Julio&nbsp;Teheran</strong></a>&nbsp;(9, 28)</td><td class="right">77</td><td class="right">R</td></tr>
<tr data-row="41"><td class="right">42.</td><td csk="Tanaka,Masahiro"><a href="/players/t/tanakma01.shtml"><strong>Masahiro&nbsp;Tanaka</strong></a>&nbsp;(6, 30)</td><td class="right">75</td><td class="right">R</td></tr>
<tr data-row="42"><td class="right">43.</td><td csk="Roark,Tanner"><a href="/players/r/roarkta01.shtml"><strong>Tanner&nbsp;Roark</strong></a>&nbsp;(7, 32)</td><td class="right">74</td><td class="right">R</td></tr>
<tr data-row="43"><td class="right">44.</td><td csk="Perez,Oliver"><a href="/players/p/perezol01.shtml"><strong>Oliver&nbsp;Perez</strong></a>&nbsp;(17, 37)</td><td class="right">72</td><td class="right">L</td></tr>
<tr data-row="44"><td class="right">45.</td><td csk="Bauer,Trevor"><a href="/players/b/bauertr01.shtml"><strong>Trevor&nbsp;Bauer</strong></a>&nbsp;(8, 28)</td><td class="right">70</td><td class="right">R</td></tr>
<tr data-row="45"><td class="right">&nbsp;</td><td csk="Corbin,Patrick"><a href="/players/c/corbipa01.shtml"><strong>Patrick&nbsp;Corbin</strong></a>&nbsp;(7, 29)</td><td class="right">70</td><td class="right">L</td></tr>
<tr data-row="46"><td class="right">&nbsp;</td><td csk="Gray,Sonny"><a href="/players/g/grayso01.shtml"><strong>Sonny&nbsp;Gray</strong></a>&nbsp;(7, 29)</td><td class="right">70</td><td class="right">R</td></tr>
<tr data-row="47"><td class="right">&nbsp;</td><td csk="Minor,Mike"><a href="/players/m/minormi01.shtml"><strong>Mike&nbsp;Minor</strong></a>&nbsp;(8, 31)</td><td class="right">70</td><td class="right">L</td></tr>
<tr data-row="48"><td class="right">49.</td><td csk="Fiers,Mike"><a href="/players/f/fiersmi01.shtml"><strong>Mike&nbsp;Fiers</strong></a>&nbsp;(9, 34)</td><td class="right">69</td><td class="right">R</td></tr>
<tr data-row="49"><td class="right">50.</td><td csk="Gibson,Kyle"><a href="/players/g/gibsoky01.shtml"><strong>Kyle&nbsp;Gibson</strong></a>&nbsp;(7, 31)</td><td class="right">67</td><td class="right">R</td></tr>
<tr class="thead" data-row="50"><th class="right">Rank</th>
<th class="sort_default_asc">Player (yrs, age)</th>
<th class="right">Wins</th><th>Throws</th></tr><tr data-row="51"><td class="right">&nbsp;</td><td csk="Norris,Bud"><a href="/players/n/norribu01.shtml"><strong>Bud&nbsp;Norris</strong></a>&nbsp;(10, 34)</td><td class="right">67</td><td class="right">R</td></tr>
<tr data-row="52"><td class="right">52.</td><td csk="deGrom,Jacob"><a href="/players/d/degroja01.shtml"><strong>Jacob&nbsp;deGrom</strong></a>&nbsp;(6, 31)</td><td class="right">66</td><td class="right">R</td></tr>
<tr data-row="53"><td class="right">53.</td><td csk="Hill,Rich"><a href="/players/h/hillri01.shtml"><strong>Rich&nbsp;Hill</strong></a>&nbsp;(15, 39)</td><td class="right">65</td><td class="right">L</td></tr>
<tr data-row="54"><td class="right">54.</td><td csk="Darvish,Yu"><a href="/players/d/darviyu01.shtml"><strong>Yu&nbsp;Darvish</strong></a>&nbsp;(7, 32)</td><td class="right">63</td><td class="right">R</td></tr>
<tr data-row="55"><td class="right">&nbsp;</td><td csk="Davis,Wade"><a href="/players/d/daviswa01.shtml"><strong>Wade&nbsp;Davis</strong></a>&nbsp;(11, 33)</td><td class="right">63</td><td class="right">R</td></tr>
<tr data-row="56"><td class="right">&nbsp;</td><td csk="Hendricks,Kyle"><a href="/players/h/hendrky01.shtml"><strong>Kyle&nbsp;Hendricks</strong></a>&nbsp;(6, 29)</td><td class="right">63</td><td class="right">R</td></tr>
<tr data-row="57"><td class="right">&nbsp;</td><td csk="Tomlin,Josh"><a href="/players/t/tomlijo01.shtml"><strong>Josh&nbsp;Tomlin</strong></a>&nbsp;(10, 34)</td><td class="right">63</td><td class="right">R</td></tr>
<tr data-row="58"><td class="right">58.</td><td csk="Odorizzi,Jake"><a href="/players/o/odorija01.shtml"><strong>Jake&nbsp;Odorizzi</strong></a>&nbsp;(8, 29)</td><td class="right">62</td><td class="right">R</td></tr>
<tr data-row="59"><td class="right">59.</td><td csk="Archer,Chris"><a href="/players/a/archech01.shtml"><strong>Chris&nbsp;Archer</strong></a>&nbsp;(8, 30)</td><td class="right">60</td><td class="right">R</td></tr>
<tr data-row="60"><td class="right">&nbsp;</td><td csk="Duffy,Danny"><a href="/players/d/duffyda01.shtml"><strong>Danny&nbsp;Duffy</strong></a>&nbsp;(9, 30)</td><td class="right">60</td><td class="right">L</td></tr>
<tr data-row="61"><td class="right">61.</td><td csk="Anderson,Brett"><a href="/players/a/anderbr04.shtml"><strong>Brett&nbsp;Anderson</strong></a>&nbsp;(11, 31)</td><td class="right">59</td><td class="right">L</td></tr>
<tr data-row="62"><td class="right">&nbsp;</td><td csk="Chen,Wei-Yin"><a href="/players/c/chenwe02.shtml"><strong>Wei-Yin&nbsp;Chen</strong></a>&nbsp;(8, 33)</td><td class="right">59</td><td class="right">L</td></tr>
<tr data-row="63"><td class="right">&nbsp;</td><td csk="Wacha,Michael"><a href="/players/w/wachami01.shtml"><strong>Michael&nbsp;Wacha</strong></a>&nbsp;(7, 27)</td><td class="right">59</td><td class="right">R</td></tr>
<tr data-row="64"><td class="right">64.</td><td csk="Martinez,Carlos"><a href="/players/m/martica04.shtml"><strong>Carlos&nbsp;Martinez</strong></a>&nbsp;(7, 27)</td><td class="right">58</td><td class="right">R</td></tr>
<tr data-row="65"><td class="right">&nbsp;</td><td csk="McHugh,Collin"><a href="/players/m/mchugco01.shtml"><strong>Collin&nbsp;McHugh</strong></a>&nbsp;(8, 32)</td><td class="right">58</td><td class="right">R</td></tr>
<tr data-row="66"><td class="right">66.</td><td csk="Hunter,Tommy"><a href="/players/h/hunteto02.shtml"><strong>Tommy&nbsp;Hunter</strong></a>&nbsp;(12, 32)</td><td class="right">56</td><td class="right">R</td></tr>
<tr data-row="67"><td class="right">&nbsp;</td><td csk="Paxton,James"><a href="/players/p/paxtoja01.shtml"><strong>James&nbsp;Paxton</strong></a>&nbsp;(7, 30)</td><td class="right">56</td><td class="right">L</td></tr>
<tr data-row="68"><td class="right">68.</td><td csk="Miller,Andrew"><a href="/players/m/millean01.shtml"><strong>Andrew&nbsp;Miller</strong></a>&nbsp;(14, 34)</td><td class="right">54</td><td class="right">L</td></tr>
<tr data-row="69"><td class="right">&nbsp;</td><td csk="Ryu,Hyun-Jin"><a href="/players/r/ryuhy01.shtml"><strong>Hyun-Jin&nbsp;Ryu</strong></a>&nbsp;(6, 32)</td><td class="right">54</td><td class="right">L</td></tr>
<tr data-row="70"><td class="right">70.</td><td csk="Anderson,Chase"><a href="/players/a/anderch01.shtml"><strong>Chase&nbsp;Anderson</strong></a>&nbsp;(6, 31)</td><td class="right">53</td><td class="right">R</td></tr>
<tr data-row="71"><td class="right">&nbsp;</td><td csk="Clippard,Tyler"><a href="/players/c/clippty01.shtml"><strong>Tyler&nbsp;Clippard</strong></a>&nbsp;(13, 34)</td><td class="right">53</td><td class="right">R</td></tr>
<tr data-row="72"><td class="right">&nbsp;</td><td csk="Cobb,Alex"><a href="/players/c/cobbal01.shtml"><strong>Alex&nbsp;Cobb</strong></a>&nbsp;(8, 31)</td><td class="right">53</td><td class="right">R</td></tr>
<tr data-row="73"><td class="right">&nbsp;</td><td csk="Jurrjens,Jair"><a href="/players/j/jurrjja01.shtml"><strong>Jair&nbsp;Jurrjens</strong></a>&nbsp;(8, 33)</td><td class="right">53</td><td class="right">R</td></tr>
<tr data-row="74"><td class="right">&nbsp;</td><td csk="Nola,Aaron"><a href="/players/n/nolaaa01.shtml"><strong>Aaron&nbsp;Nola</strong></a>&nbsp;(5, 26)</td><td class="right">53</td><td class="right">R</td></tr>
<tr data-row="75"><td class="right">&nbsp;</td><td csk="Perez,Martin"><a href="/players/p/perezma02.shtml"><strong>Martin&nbsp;Perez</strong></a>&nbsp;(8, 28)</td><td class="right">53</td><td class="right">L</td></tr>
<tr data-row="76"><td class="right">&nbsp;</td><td csk="Robertson,David"><a href="/players/r/roberda08.shtml"><strong>David&nbsp;Robertson</strong></a>&nbsp;(12, 34)</td><td class="right">53</td><td class="right">R</td></tr>
<tr data-row="77"><td class="right">&nbsp;</td><td csk="Wood,Alex"><a href="/players/w/woodal02.shtml"><strong>Alex&nbsp;Wood</strong></a>&nbsp;(7, 28)</td><td class="right">53</td><td class="right">L</td></tr>
<tr data-row="78"><td class="right">78.</td><td csk="Morrow,Brandon"><a href="/players/m/morrobr01.shtml"><strong>Brandon&nbsp;Morrow</strong></a>&nbsp;(12, 34)</td><td class="right">51</td><td class="right">R</td></tr>
<tr data-row="79"><td class="right">&nbsp;</td><td csk="Pineda,Michael"><a href="/players/p/pinedmi01.shtml"><strong>Michael&nbsp;Pineda</strong></a>&nbsp;(6, 30)</td><td class="right">51</td><td class="right">R</td></tr>
<tr data-row="80"><td class="right">&nbsp;</td><td csk="Rodriguez,Eduardo"><a href="/players/r/rodried05.shtml"><strong>Eduardo&nbsp;Rodriguez</strong></a>&nbsp;(5, 26)</td><td class="right">51</td><td class="right">L</td></tr>
<tr data-row="81"><td class="right">&nbsp;</td><td csk="Stroman,Marcus"><a href="/players/s/stromma01.shtml"><strong>Marcus&nbsp;Stroman</strong></a>&nbsp;(6, 28)</td><td class="right">51</td><td class="right">R</td></tr>
<tr data-row="82"><td class="right">82.</td><td csk="Milone,Tommy"><a href="/players/m/milonto01.shtml"><strong>Tommy&nbsp;Milone</strong></a>&nbsp;(9, 32)</td><td class="right">50</td><td class="right">L</td></tr>
<tr data-row="83"><td class="right">&nbsp;</td><td csk="Smith,Joe"><a href="/players/s/smithjo05.shtml"><strong>Joe&nbsp;Smith</strong></a>&nbsp;(13, 35)</td><td class="right">50</td><td class="right">R</td></tr>
<tr data-row="84"><td class="right">84.</td><td csk="Chatwood,Tyler"><a href="/players/c/chatwty01.shtml"><strong>Tyler&nbsp;Chatwood</strong></a>&nbsp;(8, 29)</td><td class="right">49</td><td class="right">R</td></tr>
<tr data-row="85"><td class="right">&nbsp;</td><td csk="Hudson,Daniel"><a href="/players/h/hudsoda01.shtml"><strong>Daniel&nbsp;Hudson</strong></a>&nbsp;(10, 32)</td><td class="right">49</td><td class="right">R</td></tr>
<tr data-row="86"><td class="right">86.</td><td csk="Kelly,Joe"><a href="/players/k/kellyjo05.shtml"><strong>Joe&nbsp;Kelly</strong></a>&nbsp;(8, 31)</td><td class="right">48</td><td class="right">R</td></tr>
<tr data-row="87"><td class="right">87.</td><td csk="Gausman,Kevin"><a href="/players/g/gausmke01.shtml"><strong>Kevin&nbsp;Gausman</strong></a>&nbsp;(7, 28)</td><td class="right">47</td><td class="right">R</td></tr>
<tr data-row="88"><td class="right">&nbsp;</td><td csk="Maeda,Kenta"><a href="/players/m/maedake01.shtml"><strong>Kenta&nbsp;Maeda</strong></a>&nbsp;(4, 31)</td><td class="right">47</td><td class="right">R</td></tr>
<tr data-row="89"><td class="right">&nbsp;</td><td csk="Ray,Robbie"><a href="/players/r/rayro02.shtml"><strong>Robbie&nbsp;Ray</strong></a>&nbsp;(6, 27)</td><td class="right">47</td><td class="right">L</td></tr>
<tr data-row="90"><td class="right">&nbsp;</td><td csk="Santiago,Hector"><a href="/players/s/santihe01.shtml"><strong>Hector&nbsp;Santiago</strong></a>&nbsp;(9, 31)</td><td class="right">47</td><td class="right">L</td></tr>
<tr data-row="91"><td class="right">&nbsp;</td><td csk="Syndergaard,Noah"><a href="/players/s/syndeno01.shtml"><strong>Noah&nbsp;Syndergaard</strong></a>&nbsp;(5, 26)</td><td class="right">47</td><td class="right">R</td></tr>
<tr data-row="92"><td class="right">92.</td><td csk="Eovaldi,Nathan"><a href="/players/e/eovalna01.shtml"><strong>Nathan&nbsp;Eovaldi</strong></a>&nbsp;(8, 29)</td><td class="right">46</td><td class="right">R</td></tr>
<tr data-row="93"><td class="right">&nbsp;</td><td csk="Pomeranz,Drew"><a href="/players/p/pomerdr01.shtml"><strong>Drew&nbsp;Pomeranz</strong></a>&nbsp;(9, 30)</td><td class="right">46</td><td class="right">L</td></tr>
<tr data-row="94"><td class="right">94.</td><td csk="LeBlanc,Wade"><a href="/players/l/leblawa01.shtml"><strong>Wade&nbsp;LeBlanc</strong></a>&nbsp;(11, 34)</td><td class="right">45</td><td class="right">L</td></tr>
<tr data-row="95"><td class="right">&nbsp;</td><td csk="Richards,Garrett"><a href="/players/r/richaga01.shtml"><strong>Garrett&nbsp;Richards</strong></a>&nbsp;(9, 31)</td><td class="right">45</td><td class="right">R</td></tr>
<tr data-row="96"><td class="right">96.</td><td csk="Cecil,Brett"><a href="/players/c/cecilbr01.shtml"><strong>Brett&nbsp;Cecil</strong></a>&nbsp;(10, 32)</td><td class="right">44</td><td class="right">L</td></tr>
<tr data-row="97"><td class="right">&nbsp;</td><td csk="Foltynewicz,Mike"><a href="/players/f/foltymi01.shtml"><strong>Mike&nbsp;Foltynewicz</strong></a>&nbsp;(6, 27)</td><td class="right">44</td><td class="right">R</td></tr>
<tr data-row="98"><td class="right">&nbsp;</td><td csk="Ross,Tyson"><a href="/players/r/rossty01.shtml"><strong>Tyson&nbsp;Ross</strong></a>&nbsp;(10, 32)</td><td class="right">44</td><td class="right">R</td></tr>
<tr data-row="99"><td class="right">&nbsp;</td><td csk="Stammen,Craig"><a href="/players/s/stammcr01.shtml"><strong>Craig&nbsp;Stammen</strong></a>&nbsp;(10, 35)</td><td class="right">44</td><td class="right">R</td></tr>
<tr data-row="100"><td class="right">&nbsp;</td><td csk="Wheeler,Zack"><a href="/players/w/wheelza01.shtml"><strong>Zack&nbsp;Wheeler</strong></a>&nbsp;(5, 29)</td><td class="right">44</td><td class="right">R</td></tr>

</tbody></table>
"""
producer = KafkaProducer(bootstrap_servers=['localhost:9099'])

soup = BeautifulSoup(html_doc,"html.parser")
#print(soup.prettify())


with open("player_names.txt", "w") as p_MLB:
    for name in soup.find_all("strong"):
        pn = name.get_text()
        p_MLB.write(pn +"\n")
p_fullName = []
with open("player_names.txt","r") as pln:
    full_name = pln.readlines()
    for l in range(len(full_name)):
        fn = full_name[l].split("\n")
        p_fullName.append(fn)

for i in range(len(p_fullName)):
    p_fullName[i] = p_fullName[i][0]

#Use to remove special characters
for j in range(len(p_fullName)):
    p_fullName[j] = p_fullName[j].replace(u'\xa0', u' ')

for k in range(len(p_fullName)):
    p_fullName[k]=p_fullName[k].split(' ')
#print(p_fullName) used to check if names were in a list of lists

#Aquiring API keys
headers = {
    'x-rapidapi-host': "mlb-data.p.rapidapi.com",
    'x-rapidapi-key': "fc4574f919msh460904987f90a33p107739jsn8b427f521521"
    }

url = "https://mlb-data.p.rapidapi.com/json/named.search_player_all.bam"

for g in range(len(p_fullName)):
    querystring = {"sport_code":"'mlb'","active_sw": "'{active_sw}'".format(active_sw = 'Y'), "name_part":"'{name_part}%'".format(name_part = p_fullName[g][1])}
    response = requests.request("GET", url, headers=headers, params=querystring)
    producer.send('MLBpkTest', value=json.dumps(response.text).encode('utf-8'))
    