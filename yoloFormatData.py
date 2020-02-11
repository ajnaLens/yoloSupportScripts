def yoloFormat(number, filepath, logName):
    filepath = 'logs/2017-06-15-73/images/'
    filename =  format(number, "010") + '_2dbbox.txt'
    imgPath = format(number, "010")+'_rgb.png'
    annotationYoloLocation = 'yolo_data/'+logName+'/'

    try:
	    with open(filepath+filename) as json_file:  
		 data = json.load(json_file)
    # open a text file and store the labels 
	    fileYoloFormat = open(annotationYoloLocation + str(number) + '.txt', "a")
	    copyCommand = 'cp '+filepath+imgPath + ' '+annotationYoloLocation+str(number)+'.png'
	    os.system(copyCommand)
	    for label in data:
		  annotations = data[label]
		  x_max = annotations['x_max']
		  x_min = annotations['x_min']
		  y_max = annotations['y_max']
		  y_min = annotations['y_min']
		  if (y_max < 0) or (y_min <0):
		      raw_input()
		  dw = 1./width
		  dh = 1./height
		  x = (float(x_min) + float(x_max))/2.0
		  y = (float(y_min) + float(y_max))/2.0
		  w = float(x_max) - float(x_min)
		  h =float (y_max) - float(y_min)
		  #normalise x y w h for training of the darknet object detection algorithm
		  x = x*dw
		  w = w*dw
		  y = y*dh
		  h = h*dh
		  labelDec = int(1) - 1
		  stringToWrite = str(labelDec) + " "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)+"\n"
		  fileYoloFormat.write(stringToWrite)
	    print(data)
    except IOError:
          print('dne')
