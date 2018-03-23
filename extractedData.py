import datetime


class extract():
	def data(self):
		now = datetime.datetime.now()

		day = now.day

		file = open("C:\\Users\\Samrat\\Desktop\\IOTProject\\smart_notifier\\static\\Entered_Data\\"+str(day)+".txt","r+")
		dict1 = dict()

		for line in file:
			file_list = line.split(',')
			file_time = file_list[2]
			if(file_time in dict1.keys()):
				list1 = dict1[file_time]
				event = file_list[1]
				classify = file_list[3]
				list2 = [event, classify]
				list1.append(list2)
				dict1[file_time] = list1
			else:
				list1 = []
				event = file_list[1]
				classify = file_list[3]
				list2 = [event, classify]
				list1.append(list2)
				dict1[file_time] = list1
		
		return dict1
	# for keys,values in dict1.items():
	#     print(keys)
	#     print(values)

	def very_important_events(self):
		now = datetime.datetime.now()

		day = now.day
		events = []
		file = open("C:\\Users\\Samrat\\Desktop\\IOTProject\\smart_notifier\\static\\Entered_Data\\"+str(day)+".txt","r+")
		dict1 = dict()

		for line in file:
			file_list = line.split(',')
			importantance = file_list[3]
			# print(type(importantance))
			if(importantance.split('_')[0] == "Very"):
				# print("Ys")
				events.append(line)

		return events


	def important_events(self):
		# print("Hello")
		now = datetime.datetime.now()

		day = now.day
		events = []
		file = open("C:\\Users\\Samrat\\Desktop\\IOTProject\\smart_notifier\\static\\Entered_Data\\"+str(day)+".txt","r+")
		dict1 = dict()

		for line in file:
			file_list = line.split(',')
			importantance = file_list[3]
			# print(importantance)
			if(importantance[0] == "I"):
				# print("Ys")
				events.append(line)

		return events

		
