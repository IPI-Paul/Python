import csv
import random
import time
from threading import Thread

class DataWriter(Thread):
    x_value = 0
    total_1 = 1000
    total_2 = 1000
    fieldnames = ["x_value", "total_1", "total_2"]

    def __init__(self) -> None:
        self.data_source = '../../../../../Source Files/csv/corey_sachafer_matplotlib_2_data_6.csv'
        self.t1 = Thread(target=self.run)

    def run(self):
        with open(self.data_source, 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            csv_writer.writeheader()

        while True:
            with open(self.data_source, 'a') as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
                
                info = {
                    "x_value": self.x_value,
                    "total_1": self.total_1,
                    "total_2": self.total_2
                }

                csv_writer.writerow(info)
                print(self.x_value, self.total_1, self.total_2)

                self.x_value += 1
                self.total_1 = self.total_1 + random.randint(-6, 8)
                self.total_2 = self.total_2 + random.randint(-5, 6)
            
            time.sleep(1)