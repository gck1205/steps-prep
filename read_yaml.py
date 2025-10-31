import yaml

if __name__ == "__main__":
    with open(r'C:\Users\chaitanya.garigipati\OneDrive - Accenture\Documents\steps-prep\data_files\bio.yaml', 'r') as file:
        data = yaml.safe_load(file)
        print(data['projects'][1]['technologies'][1])