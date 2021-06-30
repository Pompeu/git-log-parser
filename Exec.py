import os
import random
from GitFile import GitFile 

class Exec():
    def __init__(self, FindBaseGit):
        self.hashes = dict()
        self.files = list()
        self.findBaseGit = FindBaseGit

    def start(self):
        self.exec_git_log()
        self.open_write_flies()
        self.sort_files()
        self.write_files()
        self.print_results()

    def exec_git_log(self): 
        os.system(self.findBaseGit.log_comand())

    def open_write_flies(self):
        with open(self.findBaseGit.file_name, 'rt') as file:

            file_contents = file
            index = -1

            for line in file_contents:
                if("commit " in line):
                    index += 1
                    commit_hash = line[7:].strip()
                    self.hashes[index] = commit_hash

                if('\t' in line):
                    filename = line[2:].strip()
                    if('A' == line[0]):
                        self.files.append(GitFile(self.hashes[index], filename, 'A'))

                    if('M' == line[0]):
                        self.files.append(GitFile(self.hashes[index], filename, 'M'))

    def sort_files(self):
        if self.findBaseGit.can_sort():
            self.files.sort(key=lambda x: x.filename, reverse=True)
        else: 
            return self._shuffle_files()

        return self.files

    def _shuffle_files(self):
        return random.shuffle(self.files)

    def _filter_filtes_tipo(self, tipo):
        return filter(lambda x: x.tipo == tipo, self.files)

    def _count_files(self, tipo):
        return len(list(self._filter_filtes_tipo(tipo)))

    def _write_files_by_tipo(self):
        tipo_add = 'A'
        tipo_edit = 'M'

        with open(self.findBaseGit.commits_filename(tipo_add), "a") as cf:
            for f in  self._filter_filtes_tipo(tipo_add):
                path = self.findBaseGit.project_path.replace("https://fontes.intranet.bb.com.br", "")
                cf.write(f'{path}/{f.filename}#{f.hashcode[-10:]}\n')
                #cf.write(f'{self.findBaseGit.project_path}{self.findBaseGit.blob_path}{f.hashcode}/{f.filename}\n')
        with open(self.findBaseGit.commits_filename(tipo_edit), "a") as cf:
            for f in self._filter_filtes_tipo(tipo_edit):
                path = self.findBaseGit.project_path.replace("https://fontes.intranet.bb.com.br", "")
                cf.write(f'{path}/{f.filename}#{f.hashcode[-10:]}\n')
                #cf.write(f'{self.findBaseGit.project_path}{self.findBaseGit.blob_path}{f.hashcode}/{f.filename}\n')

    def write_files(self):
        if self.findBaseGit.can_write():
            self._write_files_by_tipo()

        os.remove(self.findBaseGit.file_name)


    def print_results(self):
        print("#####################################################################################################################################")
        print("\n")
        print(f'Foram realizados {self._count_files("A")} commits de crição no periodo de {self.findBaseGit.initial_date} a {self.findBaseGit.end_date}')
        print("\n")
        print(f'Foram realizados {self._count_files("M")} commits edição no periodo de {self.findBaseGit.initial_date} a {self.findBaseGit.end_date}')
        print("\n")

        if self.findBaseGit.can_write():
            print(f'Foi salvo um arquivo com na pasta raiz do projeto com o nome: {self.findBaseGit.commits_filename("A")}')
            print("\n")
            print(f'Foi salvo um arquivo com na pasta raiz do projeto com o nome: {self.findBaseGit.commits_filename("M")}')
            print("\n")

        print("#####################################################################################################################################")
