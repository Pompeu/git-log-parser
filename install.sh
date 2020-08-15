#install git-log-parser

GIT_LOG_PARSER_FOLDER=~/.bin/git-log
mkdir -p $GIT_LOG_PARSER_FOLDER 

cd $GIT_LOG_PARSER_FOLDER

git clone https://github.com/Gabrielglvr/git-log-parser.git .

echo 'alias git-count="~/.bin/git-log/git-count.py"' >> ~/.bashrc

. ~/.bashrc
