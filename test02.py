#การรับค่าข้อมูลด้วยพิมพ์ python
name = input('ป้อนชื่อ : ')
yearBorn = input('ป้อนปีเกิด ค.ศ. : ')
print('..................................')
#ฟังก์ชั่นในการแปลงข้อมูลจากข้อความเป็นตัวเลข int( ), float( )
#
print(f'ยินดีต้อนรับ {name} เกิดปี {yearBorn} อายุ {2023 - int(yearBorn)}')
print('ยินดีต้อนรับ',name,'เกิดปี',yearBorn,'อายุ',2023 - int(yearBorn))
print('ยินดีต้อนรับ '+name+' เกิดปี'+yearBorn+' อายุ ' +str(2023 - int(yearBorn)))
print('ยินดีต้อนรับ {} เกิดปี {} อายุ {}'.format(name,yearBorn,2023 - int(yearBorn)))
print('ยินดีต้อนรับ %s เกิดปี %s อายุ %d' %(name,yearBorn,2023 - int(yearBorn)))

