alien_1 = {
    'x_position' : 0, 
    'y_position' : 100,
    'speed' : 'medium' 
    }
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else: 
    x_increment = 3
alien_1['x_position'] = alien_1['x_position'] + x_increment
print('New Position is :'+ str(alien_1['x_position']))
#removing key 
del alien_1['speed']
print(alien_1)