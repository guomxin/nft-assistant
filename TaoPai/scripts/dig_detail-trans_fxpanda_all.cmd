rem %1-detail tag, %2-start_date, %3-end_date

cd ..

rem 1. generate details
python detail_conflux_contract.py fxpandaall %1

rem 2. dig info for ANY&CHUANSHUO
python diginfo_from_details_conflux.py fxpandaall 1 data/_details_conflux_fxpandaall_result_%1.csv ^
30001,35656;40001,40103;50001,61873;64001,64308;65001,65308;66001,66308 ANY %1
python diginfo_from_details_conflux.py fxpandaall 1 data/_details_conflux_fxpandaall_result_%1.csv ^
35041,35656;40001,40103;61524,61873;64001,64308;65001,65308;66001,66308 CHUANSHUO %1

rem 3. dig info for fullset
rem python diginfo_from_details_conflux.py fxpandaall 2 data/_details_conflux_fxpandaall_result_%1.csv 3001,10000 18 N18 %1

rem 4. dig count in circulation
python diginfo_from_details_conflux.py fxpandaall 3 data/_details_conflux_fxpandaall_result_%1.csv %1

rem 5. analyze tranctions
python transaction_conflux_contract_online.py fxpandaall %2 %3 ^
30001,33624;33625,35040;35041,35656;50001,56704;56705,57880;57881,58680;58681,58880;60001,61523;61524,61873;40001,40103;^
64001,64308;65001,65308;66001,66308 ^
PUTONG;XIYOU;CHUANSHUO;PUTONG;XIYOU;PUTONG;XIYOU;XIYOU;CHUANSHUO;CHUANSHUO;CHUANSHUO;CHUANSHUO;CHUANSHUO %1

cd scripts