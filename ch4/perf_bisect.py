import random
import string
import pickle


class PhonebookCreator:
    def get_random_name(self):
        letters = string.ascii_letters
        randint = random.randint(4, 12)
        return "".join([random.choice(letters) for i in range(randint)])

    def get_random_phone_number(self):
        return random.randint(1000000, 10000000)

    def create_phonebook_list(self): 
        phonebook_list = [
            (self.get_random_name(), self.get_random_phone_number()) for i in range(5000000)
        ]
        sorted_phonebook = sorted(phonebook_list, key=lambda tup: tup[0])
        
        del phonebook_list

        return sorted_phonebook
    
    def create_and_save_phonebook_list(self):
        with open("phonebook_list.pickle", "wb") as file:
            pickle.dump(self.create_phonebook_list(), file)

    def create_phonebook_dict(self, phonebook_list):
        phonebook_dict = { tup[0]: tup[1]  for tup in phonebook_list }

        return phonebook_dict
    
    def save_pickle(self, data, file_name):
        with open(file_name, "wb") as file:
            pickle.dump(data, file)
    
    def main(self):
        phonebook_list = self.create_phonebook_list()
        phonebook_dict = self.create_phonebook_dict(phonebook_list)
        self.save_pickle(phonebook_list, "phonebook_list.pickle")
        self.save_pickle(phonebook_dict, "phonebook_dict.pickle")

def peep():
    with open("phonebook_list.pickle", "rb") as file:
        print(pickle.load(file)[-1])

    # with open("phonebook_dict.pickle", "rb") as file:
    #     for i, (k, v) in enumerate(pickle.load(file).items()):
    #         print(k, v)
    #         break


class Searcher:
    def search_linear(self, name, phonebook_list):
        for element in phonebook_list:
            if name == element[0]:
                return element[1]
        
        return None


def run_linear():
    with open("phonebook_list.pickle", "rb") as file:
        phonebook_list = pickle.load(file)
    
    print(Searcher().search_linear("zzzzGqNaGTJ", phonebook_list))

def run_dict():
    with open("phonebook_dict.pickle", "rb") as file:
        phonebook_dict = pickle.load(file)
    
    print(phonebook_dict["zzzzGqNaGTJ"])




if __name__ == "__main__":
    pass
    # PhonebookCreator().main()

            

