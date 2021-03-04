#-------------------(시가,고가,저가,종가)예제 데이터--------------------------#
btc_nkt_dataset=(
([100,100,100,100]),
([100,110,100,110]),
([100,120,100,120]),
([100,120,100,115]),
([100,130,100,130]),
([100,140,100,140]),
([100,140,100,125]),
([100,140,100,100]),
([100,140,95,95]),
([100,140,85,85]),
([100,140,85,135]),
([100,145,85,145]),
([100,145,50,50]),
([100,145,50,75])
)
#---------------------------데이터 출력----------------------#
print("--------------------데이터 출력--------------------")
for data in btc_nkt_dataset:
    # data[0] data[1] data[2] data[3]
    # 시가     고가    저가     종가
    print(data)

#-------------------------- 데이터 패킹-------------#
data1= tuple(btc_nkt_dataset)
print("--------------튜플로 패킹하기----------------")
for num in data1:
    print(data1[num])

#--------------------언패킹 -------------------#
open_vl=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]      #데이터 언패킹을 위한 배열 공간 할당
high_vl=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
low_vl=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
close_vl=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]


print("-------------------데이터 언패킹-------------- ")
for number in range(14):
    open_vl[number],high_vl[number],low_vl[number],close_vl[number] = data1[number]
    
    print("시가 : ",open_vl[number],"고가 : ",high_vl[number],"저가 : ",low_vl[number],"종가 : ",close_vl[number])

#-----------------------------------------------------------------------------------------------------------------#

