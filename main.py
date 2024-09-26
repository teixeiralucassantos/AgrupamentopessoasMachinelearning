from controller import GroupingController
from view import GroupingView

if __name__ == '__main__':
    data_path = 'dados.csv'
    controller = GroupingController(data_path)
    balanced_groups = controller.run_clustering()
    GroupingView.display_groups(balanced_groups, controller.model.data)
