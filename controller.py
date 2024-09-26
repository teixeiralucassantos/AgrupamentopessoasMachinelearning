from model import GroupingModel
from scipy.optimize import linear_sum_assignment

class GroupingController:
    def __init__(self, data_path):
        self.model = GroupingModel(data_path)

    def run_clustering(self):
        X = self.model.preprocess_data()
        clusters, centers = self.model.determine_clusters(X)
        self.model.data['cluster'] = clusters

        num_people = len(self.model.data)
        group_size = 6
        num_groups = num_people // group_size

        cost_matrix = self.model.calculate_cost_matrix(X, centers)
        row_ind, col_ind = linear_sum_assignment(cost_matrix)

        groups = [[] for _ in range(num_groups)]
        for person_idx, group_idx in zip(row_ind, col_ind):
            groups[group_idx].append(person_idx)

        balanced_groups = self.model.balance_introversion(groups)

        # Handle remainders
        self.handle_remainders(num_people, groups, balanced_groups, row_ind)

        # Evaluate previous groupings and update parameters
        media_resultados = self.model.evaluate_previous_groupings()
        self.model.update_parameters(media_resultados)
        self.model.save_updated_parameters()

        return balanced_groups

    def handle_remainders(self, num_people, groups, balanced_groups, row_ind):
        remainder = num_people % 6
        if remainder > 0:
            remaining_people = list(set(range(num_people)) - set(row_ind))
            if remainder == 1:
                balanced_groups.append(remaining_people)
            else:
                for person_idx in remaining_people:
                    for group in balanced_groups:
                        if len(group) < 8:
                            group.append(person_idx)
                            break
