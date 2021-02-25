from util import *
from rbm import RestrictedBoltzmannMachine 
from dbn import DeepBeliefNet
import matplotlib.pyplot as plt

if __name__ == "__main__":

    image_size = [28,28]
    train_imgs,train_lbls,test_imgs,test_lbls = read_mnist(dim=image_size, n_train=60000, n_test=10000)

    ''' restricted boltzmann machine 
    
    print ("\nStarting a Restricted Boltzmann Machine..")

    rbm = RestrictedBoltzmannMachine(ndim_visible=image_size[0]*image_size[1],
                                     ndim_hidden=200,
                                     is_bottom=True,
                                     image_size=image_size,
                                     is_top=False,
                                     n_labels=10,
                                     batch_size=20
    )

    n_iterations = int(20*(len(train_imgs)/rbm.batch_size))
    x, recon_loss = rbm.cd1(visible_trainset=train_imgs, n_iterations=n_iterations, avg_recon_loss=True)

    plt.plot(x, recon_loss)
    plt.show()
    '''
    ''' deep- belief net '''

    print ("\nStarting a Deep Belief Net..")
    
    dbn = DeepBeliefNet(sizes={"vis":image_size[0]*image_size[1], "hid":500, "pen":500, "top":2000, "lbl":10},
                        image_size=image_size,
                        n_labels=10,
                        batch_size=20
    )
    epochs = 10
    ''' greedy layer-wise training '''
    portion = int(len(train_imgs)/10)
    #portion_lbls = int(len(train_lbls)/10)
    train_imgs_test = train_imgs[:portion,:]
    train_lbls_test = train_lbls[:portion,:]
    # shuffle
    '''traindata_lbls = np.concatenate((train_imgs, train_lbls), axis=1)
    np.shuffle(traindata_lbls, axis=0)
    train_imgs = traindata_lbls[:,:-1]
    train_lbls = traindata_lbls[:,-1]'''
    n_iterations = int(epochs * (len(train_imgs) / dbn.batch_size))
    dbn.train_greedylayerwise(vis_trainset=train_imgs, lbl_trainset=train_lbls, n_iterations=n_iterations)

    #plt.plot(x, recon_loss)
    #plt.show()

    dbn.recognize(train_imgs, train_lbls)
    
    dbn.recognize(test_imgs, test_lbls)

    for digit in range(10):
        digit_1hot = np.zeros(shape=(1,10))
        digit_1hot[0,digit] = 1
        dbn.generate(digit_1hot, name="rbms")


"""
    ''' fine-tune wake-sleep training '''

    dbn.train_wakesleep_finetune(vis_trainset=train_imgs, lbl_trainset=train_lbls, n_iterations=10000)

    dbn.recognize(train_imgs, train_lbls)
    
    dbn.recognize(test_imgs, test_lbls)
    
    for digit in range(10):
        digit_1hot = np.zeros(shape=(1,10))
        digit_1hot[0,digit] = 1
        dbn.generate(digit_1hot, name="dbn")"""