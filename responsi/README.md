# Penjelasan

Pada program dibawah kita membaca dataset dari .csv agar dapat divisualisasi datasetnya, dan dapat dilihat pada program serta hasil outputnya dibawah.

```python
import pandas as pd

df = pd.read_csv('annual-enterprise-survey-2020-financial-year-provisional.csv')
print(df.head(6))
```
Output
```
Year Industry_aggregation_NZSIOC Industry_code_NZSIOC Industry_name_NZSIOC  \
0  2020                     Level 1                99999       All industries   
1  2020                     Level 1                99999       All industries   
2  2020                     Level 1                99999       All industries   
3  2020                     Level 1                99999       All industries   
4  2020                     Level 1                99999       All industries   
5  2020                     Level 1                99999       All industries   
6  2020                     Level 1                99999       All industries   
7  2020                     Level 1                99999       All industries   
8  2020                     Level 1                99999       All industries   
9  2020                     Level 1                99999       All industries   

                Units Variable_code  \
0  Dollars (millions)           H01   
1  Dollars (millions)           H04   
2  Dollars (millions)           H05   
3  Dollars (millions)           H07   
4  Dollars (millions)           H08   
5  Dollars (millions)           H09   
6  Dollars (millions)           H10   
7  Dollars (millions)           H11   
8  Dollars (millions)           H12   
9  Dollars (millions)           H13   

                                     Variable_name      Variable_category  \
0                                     Total income  Financial performance   
1  Sales, government funding, grants and subsidies  Financial performance   
2                Interest, dividends and donations  Financial performance   
3                             Non-operating income  Financial performance   
4                                Total expenditure  Financial performance   
5                           Interest and donations  Financial performance   
6                                   Indirect taxes  Financial performance   
7                                     Depreciation  Financial performance   
8                          Salaries and wages paid  Financial performance   
9                         Redundancy and severance  Financial performance   

     Value                             Industry_code_ANZSIC06  
0  733,258  ANZSIC06 divisions A-S (excluding classes K633...  
1  660,630  ANZSIC06 divisions A-S (excluding classes K633...  
2   54,342  ANZSIC06 divisions A-S (excluding classes K633...  
3   18,285  ANZSIC06 divisions A-S (excluding classes K633...  
4  654,872  ANZSIC06 divisions A-S (excluding classes K633...  
5   32,730  ANZSIC06 divisions A-S (excluding classes K633...  
6    7,509  ANZSIC06 divisions A-S (excluding classes K633...  
7   26,821  ANZSIC06 divisions A-S (excluding classes K633...  
8  119,387  ANZSIC06 divisions A-S (excluding classes K633...  
9      305  ANZSIC06 divisions A-S (excluding classes K633... 
```

kita menampilkan data csv yang telah kita download diinternet dengan menggunakan interpreter python, diatas meliputi dari data financial pada tahun 2020.