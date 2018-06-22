from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

class SVC:
	def fit(self,data):
		self.data = data

		opt_dict = {}

		transforms = [[1,1],[-1,1],[-1,-1],[1,-1]]

		all_data = []

		for yi in self.data:
			#print(yi)
			for featureset in self.data[yi]:
				#print(featureset)
				for feature in featureset:
					all_data.append(feature)
		
		#print(all_data)

		self.max_feature_value = max(all_data)
		self.min_feature_value = min(all_data)

		#print self.max_feature_value
		#print self.min_feature_value

		all_data = None

		step_size = [self.max_feature_value*0.1,
					 self.max_feature_value*0.01,
					 self.max_feature_value*0.001]

		#print(step_size)

		b_range_multiple = 5
		b_multiple = 5

		latest_optimum =self.max_feature_value*10

		for step in step_size:
			#print(step)
			w = np.array([latest_optimum,latest_optimum])
			#print(w)
			optimized = False
			while not optimized:
				for b in np.arange(-1*(self.max_feature_value*b_range_multiple),(self.max_feature_value*b_range_multiple),(step*b_multiple)):
					#print(b)
					for transformation in transforms:
						w_t = w*transformation
						found_option = True

						for i in self.data:
							for xi in self.data[i]:
								yi  = i
								if not yi*(np.dot(xi,w_t)+b) >=1:
									found_option = False
						
						if found_option:
							opt_dict[np.linalg.norm(w_t)] = [w_t,b]

				if w[0]<0:
					optimized = True
					print('KEERTHIs SVM HAS OPTIMIZED ONE STEP')
				else:
					w = w - step

				norms = sorted([n for n in opt_dict])
				#print norms
				opt_choice = opt_dict[norms[0]]
				#print opt_choice
				self.w = opt_choice[0]
				#print self.w
				self.b = opt_choice[1]
				#print self.b

				latest_optimum  = opt_choice[0][0]+step*2

	
	def predict(self,features):
		#sign(x.w + b)
		classification = np.sign(np.dot(np.array(features),self.w) + self.b)
		print classification

		return classification 




data_sets = {-1:[[1,7],[2,8],[3,8]],1:[[5,1],[6,-1],[7,3]]}

svmclf = SVC()

svmclf.fit(data_sets)

svmclf.predict([4,8])
