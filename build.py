import json,pathlib
p=pathlib.Path(__file__).parent
# GAPEKA 2026 — Berlaku mulai 1 Desember 2026.
# Jam pada raw adalah jadwal sumber; angka 0 hanya untuk operasi identitas.
raw={
'r':'''R 53|Brawijaya|00:19|0|8 K1 NI + 1 M1 + 1 P|10
R 25|Muria|01:01|0|9 K1 NI + 1 M1 + 1 P|11
R 127|Pangandaran|01:33|0|1 K1 WIS + 3 K1 SS + 4 K3 SS + 1 M1 + 1 P|10
R 71F|Purwojaya|02:59|0|8 K1 NI + 1 M1 + 1 P|10
R 49|Gajayana|03:47|0|1 K1 LUX 26 + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG)|11
R 15|Argo Dwipangga|03:57|0|2 K1 LUX 26 + 7 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG)|11
R 19|Muria|04:16|0|9 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG)|11
R 3|Anggrek|04:47|0|1 T + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG)|11
R 41|Pandalungan|05:14|0|8 K1 SS + 1 M1 + 1 P + 1 B/BP|11
R 57|Sembrani|06:20|0|2 K1 LUX 26 + 8 K1 SS + 1 M1 + 1 P|12
R 125|Batavia|06:39|0|4 K1 SS(NG) + 4 K3 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG)|10
R 61|Manahan|06:56|0|1 K1 WIS + 8 K1 SS + 1 M1 + 1 P|11
R 79F|Gajayana Fak|09:35|0|8 K1 (NG) + 1 M1 + 1 P|10
R 51|Brawijaya|09:47|0|8 K1 NI + 1 M1 + 1 P|10
R 17|Muria|11:23|0|9 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG)|11
R 133|Parahyangan|14:08|0|1 K1 LUX 26 + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG)|11
R 75F|Borobudur|14:21|0|8 K1 (NG) + 1 M1 + 1 P|10
R 29|Taksaka|15:23|0|2 K1 LUX 26 + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG)|12
R 137|Parahyangan|15:40|0|8 K1 SS + 1 M1 + 1 P|10
R 13|Argo Lawu|15:57|0|2 K1 LUX 26 + 7 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG)|11
R 55|Sembrani|16:15|0|2 K1 LUX 26 + 8 K1 SS + 1 M1 + 1 P|12
R 1|Anggrek|16:40|0|1 T + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG)|11
R 59|Manahan|18:28|0|1 K1 WIS + 8 K1 SS + 1 M1 + 1 P|11
R 35|Argo Anjasmoro|19:05|0|8 K1 SS + 1 M1 + 1 P|10
R 45|Pandalungan 2|21:23|0|8 K1 SS + 1 M1 + 1 P|10
R 33|Taksaka|22:22|0|2 K1 LUX 26 + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG)|12''',
'm':'''LL 108|Langsir|00:25|0|
L 53-2|Brawijaya|00:45|0|
L 25-2|Muria|01:26|0|
L 127-2|Pangandaran|02:03|0|
L 71F-2|Purwojaya|03:24|0|
L 49-2|Gajayana|04:11|0|
L 15-2|Argo Dwipangga|04:40|0|
L 19-2|Muria|04:40|0|
L 3-2|Anggrek|05:37|0|
L 41-2|Pandalungan|05:37|0|
L 57-2|Sembrani|06:45|0|
L 125-2|Batavia|07:11|0|
L 61-2|Manahan|07:11|0|
L 79F-2|Gajayana Fak|09:50|0|
L 51-2|Brawijaya|10:09|0|
L 17-2|Muria|11:50|0|
L 133-2|Parahyangan|14:41|0|
L 75F-2|Borobudur|14:41|0|
L 29-2|Taksaka|15:42|0|
L 13-2|Argo Lawu|16:15|0|
L 137-2|Parahyangan|16:15|0|
L 55-2|Sembrani|16:43|0|
L 1-2|Anggrek|16:57|0|
L 59-2|Manahan|18:54|0|
L 35-2|Argo Anjasmoro|19:30|0|
L 45-2|Pandalungan 2|21:46|0|
L 33-2|Taksaka|22:45|0|''',
'd':'''LL 107|Langsir|01:22|0|
L 54-1|Brawijaya|03:59|0|
L 130-1|Papandayan|04:14|0|
L 26-1|Muria|04:59|0|
L 132-1|Parahyangan|05:09|0|
L 64F-1|Purwojaya|05:24|0|
L 32-1|Taksaka|05:29|0|
L 20-1|Muria|05:48|0|
L 138-1|Parahyangan|06:05|0|
L 16-1|Argo Dwipangga|06:40|0|
L 2-1|Anggrek|06:40|0|
L 56-1|Sembrani|07:04|0|
L 46-1|Pandalungan 2|07:45|0|
L 126-1|Batavia|08:08|0|
L 60-1|Manahan|09:08|0|
L 18-1|Muria|15:14|0|
L 52-1|Brawijaya|15:44|0|
L 76F-1|Borobudur|15:44|0|
L 58-1|Sembrani|16:56|0|
L 50-1|Gajayana|17:50|0|
L 4-1|Anggrek|18:18|0|
L 14-1|Argo Lawu|18:57|0|
L 42-1|Pandalungan|19:39|0|
L 34-1|Taksaka|20:19|0|
L 62-1|Manahan|21:18|0|
L 36-1|Argo Anjasmoro|22:11|0|
L 80F-1|Gajayana Fak|22:41|0|'''}

data=[]
for cat,rows in raw.items():
 for line in rows.splitlines():
  a=line.split('|'); h,m=map(int,a[2].split(':')); total=h*60+m-int(a[3]); t=total%1440
  data.append(dict(id=a[0],cat=cat,name=a[1],time=f'{t//60:02}:{t%60:02}',formation=a[4] if len(a)>4 else '',action='Dat' if cat!='m' else 'Ber',sourceTime=a[2],sourceDelta=None,scheduleDayOffset=total//1440))
  if cat=='r': data[-1]['carCount']=int(a[5])
data.sort(key=lambda d:(d['time'],d['cat'],d['id']))
for d in data:
 if d['id']=='LL 107':d['action']='Dat'
 if d['id']=='LL 108':d['action']='Ber'
(p/'data.js').write_text('// GAPEKA 2026 — Acuan berlaku mulai 1 Desember 2026.\n// Versi mandiri: seluruh database langsung aktif saat aplikasi dibuka.\nconst DEFAULT_DATA = '+json.dumps(data,ensure_ascii=False,indent=2)+';\n')
md='# Rekap jadwal JAKK — GAPEKA 2026\n\nAcuan berlaku mulai **1 Desember 2026**; database versi mandiri langsung aktif saat aplikasi dibuka.\n\nNomor dan jam: Rekap_JAKK_L_R_GAPEKA_2026 (2).pdf, halaman 1, 2, dan 4.\nNama, susunan stamformasi, dan jumlah kereta R datang: REKAP SF KA DAO JAKK.pdf, bagian A Kedatangan, halaman 1–2.\n\n## L DINAS DATANG\n\n| Nomor | Nama KA | Gerak | Jam | Stamformasi | Jumlah kereta |\n|---|---|---|---|---|---:|\n| LL 107 | Langsir | Dat | 01:22 | — | — |\n| L 54-1 | Brawijaya | Dat | 03:59 | — | — |\n| L 130-1 | Papandayan | Dat | 04:14 | — | — |\n| L 26-1 | Muria | Dat | 04:59 | — | — |\n| L 132-1 | Parahyangan | Dat | 05:09 | — | — |\n| L 64F-1 | Purwojaya | Dat | 05:24 | — | — |\n| L 32-1 | Taksaka | Dat | 05:29 | — | — |\n| L 20-1 | Muria | Dat | 05:48 | — | — |\n| L 138-1 | Parahyangan | Dat | 06:05 | — | — |\n| L 16-1 | Argo Dwipangga | Dat | 06:40 | — | — |\n| L 2-1 | Anggrek | Dat | 06:40 | — | — |\n| L 56-1 | Sembrani | Dat | 07:04 | — | — |\n| L 46-1 | Pandalungan 2 | Dat | 07:45 | — | — |\n| L 126-1 | Batavia | Dat | 08:08 | — | — |\n| L 60-1 | Manahan | Dat | 09:08 | — | — |\n| L 18-1 | Muria | Dat | 15:14 | — | — |\n| L 52-1 | Brawijaya | Dat | 15:44 | — | — |\n| L 76F-1 | Borobudur | Dat | 15:44 | — | — |\n| L 58-1 | Sembrani | Dat | 16:56 | — | — |\n| L 50-1 | Gajayana | Dat | 17:50 | — | — |\n| L 4-1 | Anggrek | Dat | 18:18 | — | — |\n| L 14-1 | Argo Lawu | Dat | 18:57 | — | — |\n| L 42-1 | Pandalungan | Dat | 19:39 | — | — |\n| L 34-1 | Taksaka | Dat | 20:19 | — | — |\n| L 62-1 | Manahan | Dat | 21:18 | — | — |\n| L 36-1 | Argo Anjasmoro | Dat | 22:11 | — | — |\n| L 80F-1 | Gajayana Fak | Dat | 22:41 | — | — |\n\n## L MANTAN PULANG\n\n| Nomor | Nama KA | Gerak | Jam | Stamformasi | Jumlah kereta |\n|---|---|---|---|---|---:|\n| LL 108 | Langsir | Ber | 00:25 | — | — |\n| L 53-2 | Brawijaya | Ber | 00:45 | — | — |\n| L 25-2 | Muria | Ber | 01:26 | — | — |\n| L 127-2 | Pangandaran | Ber | 02:03 | — | — |\n| L 71F-2 | Purwojaya | Ber | 03:24 | — | — |\n| L 49-2 | Gajayana | Ber | 04:11 | — | — |\n| L 15-2 | Argo Dwipangga | Ber | 04:40 | — | — |\n| L 19-2 | Muria | Ber | 04:40 | — | — |\n| L 3-2 | Anggrek | Ber | 05:37 | — | — |\n| L 41-2 | Pandalungan | Ber | 05:37 | — | — |\n| L 57-2 | Sembrani | Ber | 06:45 | — | — |\n| L 125-2 | Batavia | Ber | 07:11 | — | — |\n| L 61-2 | Manahan | Ber | 07:11 | — | — |\n| L 79F-2 | Gajayana Fak | Ber | 09:50 | — | — |\n| L 51-2 | Brawijaya | Ber | 10:09 | — | — |\n| L 17-2 | Muria | Ber | 11:50 | — | — |\n| L 133-2 | Parahyangan | Ber | 14:41 | — | — |\n| L 75F-2 | Borobudur | Ber | 14:41 | — | — |\n| L 29-2 | Taksaka | Ber | 15:42 | — | — |\n| L 13-2 | Argo Lawu | Ber | 16:15 | — | — |\n| L 137-2 | Parahyangan | Ber | 16:15 | — | — |\n| L 55-2 | Sembrani | Ber | 16:43 | — | — |\n| L 1-2 | Anggrek | Ber | 16:57 | — | — |\n| L 59-2 | Manahan | Ber | 18:54 | — | — |\n| L 35-2 | Argo Anjasmoro | Ber | 19:30 | — | — |\n| L 45-2 | Pandalungan 2 | Ber | 21:46 | — | — |\n| L 33-2 | Taksaka | Ber | 22:45 | — | — |\n\n## R DATANG JAKK\n\n| Nomor | Nama KA | Gerak | Jam | Stamformasi | Jumlah kereta |\n|---|---|---|---|---|---:|\n| R 53 | Brawijaya | Dat | 00:19 | 8 K1 NI + 1 M1 + 1 P | 10 |\n| R 25 | Muria | Dat | 01:01 | 9 K1 NI + 1 M1 + 1 P | 11 |\n| R 127 | Pangandaran | Dat | 01:33 | 1 K1 WIS + 3 K1 SS + 4 K3 SS + 1 M1 + 1 P | 10 |\n| R 71F | Purwojaya | Dat | 02:59 | 8 K1 NI + 1 M1 + 1 P | 10 |\n| R 49 | Gajayana | Dat | 03:47 | 1 K1 LUX 26 + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG) | 11 |\n| R 15 | Argo Dwipangga | Dat | 03:57 | 2 K1 LUX 26 + 7 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG) | 11 |\n| R 19 | Muria | Dat | 04:16 | 9 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG) | 11 |\n| R 3 | Anggrek | Dat | 04:47 | 1 T + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG) | 11 |\n| R 41 | Pandalungan | Dat | 05:14 | 8 K1 SS + 1 M1 + 1 P + 1 B/BP | 11 |\n| R 57 | Sembrani | Dat | 06:20 | 2 K1 LUX 26 + 8 K1 SS + 1 M1 + 1 P | 12 |\n| R 125 | Batavia | Dat | 06:39 | 4 K1 SS(NG) + 4 K3 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG) | 10 |\n| R 61 | Manahan | Dat | 06:56 | 1 K1 WIS + 8 K1 SS + 1 M1 + 1 P | 11 |\n| R 79F | Gajayana Fak | Dat | 09:35 | 8 K1 (NG) + 1 M1 + 1 P | 10 |\n| R 51 | Brawijaya | Dat | 09:47 | 8 K1 NI + 1 M1 + 1 P | 10 |\n| R 17 | Muria | Dat | 11:23 | 9 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG) | 11 |\n| R 133 | Parahyangan | Dat | 14:08 | 1 K1 LUX 26 + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG) | 11 |\n| R 75F | Borobudur | Dat | 14:21 | 8 K1 (NG) + 1 M1 + 1 P | 10 |\n| R 29 | Taksaka | Dat | 15:23 | 2 K1 LUX 26 + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG) | 12 |\n| R 137 | Parahyangan | Dat | 15:40 | 8 K1 SS + 1 M1 + 1 P | 10 |\n| R 13 | Argo Lawu | Dat | 15:57 | 2 K1 LUX 26 + 7 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG) | 11 |\n| R 55 | Sembrani | Dat | 16:15 | 2 K1 LUX 26 + 8 K1 SS + 1 M1 + 1 P | 12 |\n| R 1 | Anggrek | Dat | 16:40 | 1 T + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG) | 11 |\n| R 59 | Manahan | Dat | 18:28 | 1 K1 WIS + 8 K1 SS + 1 M1 + 1 P | 11 |\n| R 35 | Argo Anjasmoro | Dat | 19:05 | 8 K1 SS + 1 M1 + 1 P | 10 |\n| R 45 | Pandalungan 2 | Dat | 21:23 | 8 K1 SS + 1 M1 + 1 P | 10 |\n| R 33 | Taksaka | Dat | 22:22 | 2 K1 LUX 26 + 8 K1 SS(NG) + 1 M1 SS(NG) + 1 P SS(NG) | 12 |\n\nLL 108 adalah pengecualian Lok Langsir pada kelompok L Mantan Pulang, pukul 00:25. LL 107 datang pukul 01:22.\n\nPerbedaan nama pada R 13, R 15, dan R 45 mengikuti PDF stamformasi; nama lok pada kedua kelompok L tetap mengikuti PDF jadwal.\n'
(p/'REKAP-JADWAL.md').write_text(md)
