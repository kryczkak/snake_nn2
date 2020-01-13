import keras
import gc
from keras.models import Sequential
from keras.layers import Dense
import keract


import numpy

class Blanka():

    def __init__(self):
        self.neurons_ativations = {}
        self.weights = []
        self.seed = numpy.random.seed(7)



        self.model = Sequential()
        self.model.add(Dense(6, input_dim=6, activation='relu'))
        self.model.add(Dense(6, activation='relu', name='layer_one'))  # relu
        self.model.add(Dense(6, activation='relu'))  # relu
        self.model.add(Dense(6, activation='relu'))  # relu
        self.model.add(Dense(6, activation='relu'))  # relu
        self.model.add(Dense(4, activation='softmax'))



    def create_model(self):

        dataset = numpy.loadtxt('statsJ.csv', delimiter=',')
        x = dataset[:,0:6].astype(float)
        #x = numpy.sign(x)
        y = dataset[:,6:7]

        self.model.compile(loss='sparse_categorical_crossentropy', optimizer='RMSprop', metrics=['accuracy'])
        self.model.fit(x, y, epochs=500, batch_size=500)

        scores = self.model.evaluate(x, y)
        print ('\n%s: % 2f%%' % (self.model.metrics_names[1], scores[1]*100))

        for layer in self.model.layers:
            weights = []
            layer_weights = layer.get_weights()[0]
            for i in range (0, len(layer_weights)):
                weights.append(list(layer_weights[i]))
            self.weights.append(weights)
        self.weights.pop(0)
        #self.weights = self.model.get_weights()[0]




    def chose_dir(self, stats):
        test = numpy.array(stats).reshape(1,6)
        #test = numpy.sign(test)
        dir = self.model.predict_classes(test)
        print (test)
        #print (dir)

        #self.input = test

        #get_nth_layer_output = keras.backend.function([self.model.layers[0].input],
        #                                 [self.model.layers[3].output])
        #layer_output = get_nth_layer_output(test)[0]
        #self.neurons_ativations = []
        #all_layers = []
        #for i in range(1,len(self.model.layers)):
        #get_nth_layer_output = keras.backend.function([self.model.layers[0].input, keras.backend.learning_phase()], [self.model.layers[0].output])
        #layer_output = get_nth_layer_output([test,0])[0]
        #   all_layers = all_layers.append(layer_output)
        #print(layer_output)
        #print('------------------------------------------')

        self.neurons_ativations  = keract.get_activations(self.model, test)


        new_x, new_y = 1, 0

        if dir[0] == 0:
            new_x, new_y = 1,0
        if dir[0] == 1:
            new_x, new_y = -1,0
        if dir[0] == 2:
            new_x, new_y = 0,-1
        if dir[0] == 3 :
            new_x, new_y = 0, 1


        return new_x,new_y

    def get_neurons_ativations(self):
        self.neurons_ativations = []
        for layer in self.model.layers:
            get_nth_layer_output = keras.backend.function([self.model.layers[0].input], [layer.output])
            self.neurons_ativations.append(get_nth_layer_output(self.input)[0])
        return self.neurons_ativations

        #get_nth_layer_output = keras.backend.function([self.model.layers[0].input], [self.model.layers[3].output])
        #layer_output = get_nth_layer_output(test)[0]



    def clear_model(self):
        keras.backend.clear_session()
        gc.collect()
        del self.model