import os, sys

wheel_list = []
wheel_list_dict = {}
wheel_list_text  = os.popen('pipdeptree -f').read()

print (wheel_list_text)

max_depth = 0

#check max_depth
for wheel in wheel_list_text.split('\n'):
    wheel = wheel.rstrip()

    if '@' in wheel:
        continue

    current_depth = 1
    while current_depth * '  ' in wheel:
        current_depth += 1
    
    max_depth = max(max_depth, current_depth)

for i in range(max_depth + 1):
    wheel_list.append([])

#store wheel names following depth
for wheel in wheel_list_text.split('\n'):
    wheel = wheel.rstrip()

    if '@' in wheel:
        continue

    current_depth = 1
    if current_depth * '  ' not in wheel:
        wheel_list[0].append(wheel.strip())
    else:
        while current_depth * '  ' in wheel:
            current_depth += 1
        wheel_list[current_depth-1].append(wheel.strip())

#print (wheel_list)

while len(wheel_list):
    wheel_depth = wheel_list.pop(-1)
    while len(wheel_depth):
        wheel = wheel_depth.pop(-1)
        os.system('pip wheel ' + wheel + ' --wheel-dir wheels')

#install just using downloaded files(move to wheel_folder inside)
#os.system('pip install --no-index --find-links . target_wheel_file')

    


        


        
    
