import datetime
import re
import os

class FindBaseGit():

    def __init__(self, initial_date, end_date, git_author, no_write, sort):
        self._parse_dates(initial_date, end_date)
        self.git_author = git_author 
        self.file_name = 'tmp.git.log'
        self.blob_path = '/-/blob/'
        self.project_path = self.get_url('./')
        self.no_write = no_write 
        self.sort = sort 

    def dir_list(self, folder):
        return list(filter(lambda filename: os.path.isdir(os.path.join(os.path.abspath("."), filename)) and not filename.startswith('.'), filenames))

    def get_url(self, folder):
        with open(folder + ".git/config", 'r') as files:
            lines_with_url = filter(lambda line : 'url' in line, files)
            return list(map(lambda x: x.split('=')[1].strip().replace('.git', ''), lines_with_url))[0]

    def log_comand(self):
        return f'git --no-pager log --since "{self.initial_date}" --until "{self.end_date}" --name-status --author="{self.git_author}" > {self.file_name}'

    def commits_filename(self, tipo):
        if tipo == 'A':
            return f'{self.git_author}_{self.initial_date}_{self.end_date}_commits_create.txt'
        return f'{self.git_author}_{self.initial_date}_{self.end_date}_commits_edit.txt'

    def _parse_dates(self, initial_date, end_date):
        [day_init, month_init, year_init] = map(int, initial_date.split('/'))
        [day_end, month_end, year_end] = map(int, end_date.split('/'))
        initial_date_to_validate = datetime.date(year_init, month_init, day_init)
        end_date_to_validate = datetime.date(year_end, month_end, day_end)

        if self.validate_range(initial_date_to_validate, end_date_to_validate ):
            self._format_date(initial_date_to_validate, end_date_to_validate)

    def _format_date(self, initial_date, end_date):
        format_date = "%d %m %Y"
        self.initial_date = initial_date.strftime(format_date)
        self.end_date = end_date.strftime(format_date)

    def validate_key(self):
        if re.compile("^c[0-9]{7}$").fullmatch(self.git_author) is not None:
            return True

        raise Exception("git_author is valid try 'cNumber(7)', like your internal key")

    def validate_range(self, initial_date_to_validate, end_date_to_validate):
        if initial_date_to_validate < end_date_to_validate:
            return True

        raise Exception("init_date need lower of end_date")  

    def is_valid_params(self):
        return self.validate_key()

    def can_write(self):
        return self.no_write == 'yes'

    def can_sort(self):
        return self.sort == 'yes'
