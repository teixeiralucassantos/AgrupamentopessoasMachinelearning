class GroupingView:
    @staticmethod
    def display_groups(groups, data):
        for i, group in enumerate(groups):
            print(f"Grupo {i+1}:")
            print(data.iloc[group])
            print("\n")
