import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.cluster import KMeans
from scipy.optimize import linear_sum_assignment
import pickle
import os

class GroupingModel:
    def __init__(self, data_path, params_path='training_params.pkl'):
        self.data = pd.read_csv(data_path)
        self.params = self.load_parameters(params_path)
        self.categorical_columns = ['Objetivo', 'Trabalho', 'Setor_Atuacao', 
                                     'Frase_Representacao', 'Assunto1', 
                                     'Assunto2', 'Assunto3', 'Religiao', 
                                     'Acontecimento', 'Culinaria1', 
                                     'Culinaria2', 'Culinaria3', 'Abertura', 
                                     'Bebida1', 'Bebida2', 'Bebida3', 
                                     'Restricao', 'Racionalidade']
        self.numerical_columns = ['Conexao', 'Introversao', 'Saideiro']

    def load_parameters(self, filename='training_params.pkl'):
        try:
            with open(filename, 'rb') as f:
                params = pickle.load(f)
        except FileNotFoundError:
            params = {
                'n_clusters': None,
                'weights': None,
                'learning_rate': 0.1
            }
        return params

    def save_parameters(self, filename='training_params.pkl'):
        with open(filename, 'wb') as f:
            pickle.dump(self.params, f)

    def preprocess_data(self):
        encoder = OneHotEncoder()
        encoded_categorical = encoder.fit_transform(self.data[self.categorical_columns]).toarray()

        scaler = StandardScaler()
        scaled_numerical = scaler.fit_transform(self.data[self.numerical_columns])

        return np.hstack((encoded_categorical, scaled_numerical))

    def determine_clusters(self, X):
        if self.params['n_clusters'] is None:
            self.params['n_clusters'] = len(self.data) // 6
        kmeans = KMeans(n_clusters=self.params['n_clusters'])
        return kmeans.fit_predict(X), kmeans.cluster_centers_

    def calculate_cost_matrix(self, X, kmeans_centers):
        num_people = len(X)
        num_groups = self.params['n_clusters']
        cost_matrix = np.zeros((num_people, num_groups))
        for i in range(num_people):
            for j in range(num_groups):
                cost_matrix[i, j] = np.linalg.norm(X[i] - kmeans_centers[j])
        return cost_matrix

    def balance_introversion(self, groups):
        balanced_groups = []
        for group in groups:
            introverts = [p for p in group if self.data.iloc[p]['Introversao'] <= 5]
            extroverts = [p for p in group if self.data.iloc[p]['Introversao'] > 5]
            while len(introverts) > 3:
                extroverts.append(introverts.pop())
            while len(extroverts) > 3:
                introverts.append(extroverts.pop())
            balanced_groups.append(introverts + extroverts)
        return balanced_groups

    def evaluate_previous_groupings(self):
        if os.path.exists('resultado.xlsx'):
            resultados = pd.read_excel('resultado.xlsx', usecols=[0], skiprows=[0]).values.flatten()
            return np.mean(resultados) if len(resultados) > 0 else 0
        return 0

    def update_parameters(self, media_resultados):
        if self.params['weights'] is None:
            self.params['weights'] = np.ones(self.data.shape[1])
        self.params['weights'] += self.params['learning_rate'] * media_resultados

    def save_updated_parameters(self):
        self.save_parameters()
