import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, MaxAbsScaler

from keras.models import Sequential, Model
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense, Dropout

from keras.callbacks import EarlyStopping, ModelCheckpoint, TensorBoard

# 데이터 불러오기
x = np.load('./data/x_data.npy')
y = np.load('./data/y_data.npy')
x_pred = np.load('./data/x_pred.npy')

print("x.shape :", x.shape) # (200, 64, 64, 3)
print("y.shape :", y.shape) # (200, 2)
print("x_pred.shape :", x_pred.shape) # (20, 64, 64, 3)



from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size = 0.2, random_state = 77, shuffle = True
)

print("x_train.shape :", x_train.shape)  # (160, 64, 64, 3)
print("x_test.shape :", x_test.shape)    # (40, 64, 64, 3)
print("y_train.shape :", y_train.shape)  # (160, 2)
print("y_test.shape :", y_test.shape)    # (40, 2)


# 데이터 전처리
# scaling(하기 전, 다시 2차원으로 reshape 해 줘야 함)

# 64 x 64
x_train = x_train.reshape(x_train.shape[0], 64*64*3)
x_test = x_test.reshape(x_test.shape[0], 64*64*3)

# 100 x 100
# x_train = x_train.reshape(x_train.shape[0], 100*100*3)
# x_test = x_test.reshape(x_test.shape[0], 100*100*3)


scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# print(x_test)

print("x_train.shape :", x_train.shape) # (160, 12288)

# 2. 모델 구성

### 함수형 ###
input1 = Input(shape = (12288, ))
x = Dense(150)(input1)
x = Dense(300)(x)
x = Dropout(0.3)(x)
x = Dense(500)(x)
x = Dropout(0.3)(x)
x = Dense(700)(x)
x = Dropout(0.5)(x)
x = Dense(900)(x)
x = Dropout(0.5)(x)
x = Dense(200)(x)
x = Dense(10)(x)
output1 = Dense(2, activation = 'sigmoid')(x)


model = Model(inputs = input1, outputs = output1) 

model.summary()

# 3. 컴파일, 훈련
# es = EarlyStopping(monitor = 'loss', patience = 10, mode = 'auto')
# modelpath = './model/{epoch:02d}--{acc:.4f}.hdf5'
# cp = ModelCheckpoint(filepath = modelpath, monitor = 'acc', save_best_only = True, mode = 'auto')
# tb_hist = TensorBoard(log_dir = 'graph', histogram_freq = 0, write_graph = True, write_image = True)

model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['acc'])

model.fit(x_train, y_train, epochs = 100, batch_size = 10, validation_split = 0.3,verbose = 1)


# es + cp
# model.fit(x_train, y_train, epochs = 300, batch_size = 10, validation_split = 0.3,verbose = 1, 
                                                        #    callbacks = [es, cp])

# tb_hist
# hist = model.fit(x_train, y_train, epochs = 100, batch_size = 10, validation_split = 0.2, verbose = 1
#                                    callbacks = [tb_hist] )


# 4. 평가, 예측
loss, acc = model.evaluate(x_test, y_test, batch_size = 10)

print("loss :", loss)
print("acc :", acc)

x_pred = x_pred.reshape(x_pred.shape[0], 64*64*3)
y_pred = model.predict(x_pred)

print(np.argmax(y_pred, axis = 1))
print(y_pred.shape)
