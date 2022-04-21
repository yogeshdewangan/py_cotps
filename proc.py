#Using the digits data set from sklearn:
from sklearn import datasets

digits = datasets.load_digits()
print(digits.target)
print(type(digits.target), type(digits.data))

def select_data(data, target, labels = [0,1]):


    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    print(f'The labels for the first 5 entries: {digits.target[:5]}')
    print(data[0:5])

    binaryDigits = [(d, t) for (d, t) in zip(data, target) if t <= 1]
    bd, bt = zip(*binaryDigits)
    print(f'The targets for the first 5 binary entries: {bt[:5]}')


def split_data(data, target, test_size = 0.25, random_state = 21):
    bin_dig, bin_tar = select_data(data, digits.target)
    print(f'The targets for the first 5 binary entries: {bin_tar[:5]}')
    # Selecting on 6's and 7's:
    dig67, tar67 = select_data(data, digits.target, labels=[6, 7])
    print(f"The targets for the first 5 6's & 7's entries: {tar67[:5]}")
    # Selecting on evens:
    dig_even, tar_even = select_data(data, digits.target, labels=[0, 2, 4, 6, 8])
    print(f"The targets for the first 5 even entries: {tar_even[:5]}")


def fit_model(x_train, y_train, model_type='logreg'):
    for m in ['nbayes', 'svm', 'rforest']:
        log_pkl = fit_model(x_train, y_train, model_type=m)
        log_cmatrix = score_model(log_pkl, x_test, y_test)
        print(f'The confusion matrix for {m} is:\n {log_cmatrix}')

def predict_model(mod_pkl, xes):
    x_train, x_test, y_train, y_test = split_data(bin_dig, bin_tar, test_size=0.5)
    log_pkl = fit_model(x_train, y_train)
    y_predict = predict_model(log_pkl, x_train)
    log_cmatrix = score_model(log_pkl, x_test, y_test)
    print(f'prediction: y_predict\nconfusion matrix:\n log_cmatrix')

def score_model(mod_pkl,xes,yes):
    for m in ['nbayes', 'svm', 'rforest']:
        log_pkl = fit_model(x_train, y_train, model_type=m)
        log_cmatrix = score_model(log_pkl, x_test, y_test)
        print(f'The confusion matrix for {m} is:\n {log_cmatrix}')

def compare_models(data, target, test_size = 0.25, random_state = 21, models = ['logreg','nbayes','svm','rforest']):
    best_mod, best_score = compare_models(dig67, tar67, test_size=0.9, random_state=22)
    print(f"The best model for the 6 and 7's dataset is {best_mod} with score {best_score}.")