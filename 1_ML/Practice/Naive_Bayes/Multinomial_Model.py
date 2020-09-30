'''
Multinomial Model
'''

import numpy as np

class MultinomialModel(object):
    '''
    Naive bayes classifier for multinomial models
    The Multinomial Naive Bayes classifier is suitable for classification with discrete features


    Parameters
    ----------
    * alpha: float, optional (default=1.0)
        Setting alpha=0 for no smoothing
        Setting 0<alpha<1 is called Lidstone smoothing
        Setting alpha=1 is called Laplace smoothing

    * fit_prior: boolean
        Whether to learn class prior probabilities or not
        If False, a uniform prior will be used
    
    * class_prior: array-like, size(n_classes)
        Prior probabilities of the classes
        If specified, the priors are not adjusted according to the data
    

    Attributes
    ----------
    * fit(X,y):
        X and y are array-like, represent features and labels
        call fit() method to train Naive Bayes classifier

    * predict(X):

    '''

    def __init__(self, alpha=1.0, fit_prior=True, class_prior=None):
        self.alpha = alpha
        self.fit_prior = fit_prior
        self.class_prior = class_prior
        self.classes = None
        self.conditional_prob = None


    def _calculate_feature_prob(self, feature):
        unique_features = np.unique(feature)
        total_num = float(len(feature))
        value_prob = {}
        for k in unique_features:
            value_prob[k] = ((np.sum(np.equal(feature, k)) + self.alpha) / (total_num + len(unique_features)*self.alpha))
        return value_prob

    
    def fit(self, X, y):
        self.classes = np.unique(y)

        # calculate class prior probabilities: P(y=c_k)
        if self.class_prior == None:
            class_num = len(self.classes)
            if not self.fit_prior: # if fit_prior = False ---> uniform prior
                self.class_prior = [1.0/class_num for _ in range(class_num)] # uniform prior
            else:
                self.class_prior = []
                sample_num = float(len(y))
                for c in self.classes:
                    c_num = np.sum(np.equal(y, c)) # N_{y_k}
                    self.class_prior.append((c_num + self.alpha) / (sample_num + class_num*self.alpha))

        # calculate conditional probability: P(x_i|y=c_k)
        self.conditional_prob = {}
        # like {c_0: {x_0: {value0: 0.1, value1: 0.3, ...}, x_1:{...}, ...}, c_1: {...}, ...}
        for c in self.classes: # c_i
            self.conditional_prob[c] = {}
            for i in range(len(X[0])): # for each feature
                feature = X[np.equal(y, c)][:, i]
                self.conditional_prob[c][i] = self._calculate_feature_prob(feature)
        return self

    
    # given values_prob {value0: 0.1, value1:0.3, ...} and target_value
    # return the probability of target_value
    def _get_xi_prob(self, values_prob, target_value):
        return values_prob[target_value]

    
    # predict a single sample based on (calss_prior, conditional_prob)
    def _predict_single_sample(self, x):
        label = -1
        max_posterior_prob = 0
    
        # for each category, calculate its posterior probability: class_prior*conditional_prob
        for c_index in range(len(self.classes)):
            current_class_prior = self.class_prior[c_index]
            current_conditional_prob = 1.0
            feature_prob = self.conditional_prob[self.classes[c_index]]
            i = 0
            for feature_i in feature_prob.keys():
                current_class_prior *= self._get_xi_prob(feature_prob[feature_i], x[i])
                i+=1
            
            # compare posterior probability and update max_posterior_prob, label
            if current_class_prior * current_conditional_prob > max_posterior_prob:
                max_posterior_prob = current_class_prior * current_conditional_prob
                label = self.classes[c_index]
        return label


    # predict samples (also single sample)
    def predict(self, X):
        if X.ndim == 1:
            return self._predict_single_sample(X)
        else:
            # classify each sample
            labels = []
            for i in range(X.shape[0]):
                label = self._predict_single_sample(X[i])
                labels.append(label)
            return labels


## TEST ##

X = np.array([
    [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3],
    [4,5,5,4,4,4,5,5,6,6,6,5,5,6,6]
])

X = X.T
y = np.array([-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1])

nb = MultinomialModel(alpha=1.0, fit_prior=True)
nb.fit(X,y)

print(nb.predict(np.array([2,4])))