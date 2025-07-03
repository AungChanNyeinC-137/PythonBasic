alien_0 = { 'color':'green' , 'points':5 }
print(alien_0['color'])
print(alien_0['points'])
new_point = str(alien_0['points'])
print("New point is : 0" + new_point)

#adding new key value pairs
alien_0['x_position'] = 25
alien_0['y_position'] = 10
x_position = str(alien_0['x_position'])
y_position = str(alien_0['y_position'])
print('X-position : '  + x_position + '\n Y-position : '+ y_position)

alien_1 = {}
alien_1['color'] = 'yellow'
alien_1['point'] = 25
alien_1['x_position'] = 20
alien_1['y_position'] = 10
print(alien_1)

#Modifying Values in a Dictionary

alien_1['point'] = 100
print('New point is '+ str(alien_1['point']))