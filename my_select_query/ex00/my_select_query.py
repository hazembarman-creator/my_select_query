import csv
from io import StringIO

class MySelectQuery:
    reader = csv.reader('')
    f_dict = {}
    f_list = []

    def __init__ (self, param_1):
        csv_file = StringIO(param_1)
        self.reader = csv.reader(csv_file)
        self.f_list = next(self.reader)
        self.f_dict = {i:self.f_list[i] for i in range (len(self.f_list))}

    def where(self, column_name, criteria):
        for key, value in self.f_dict.items():
            if value == column_name:
                index_selected = key
        for row in self.reader:
            if row[index_selected] == criteria:
                answer_list = []
                answer_string = ",".join(row)
                answer_list.append(answer_string)
                return answer_list
                