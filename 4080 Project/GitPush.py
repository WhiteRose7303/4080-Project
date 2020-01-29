from git import Repo
CommitM = input('Prompt :')
PATH_OF_GIT_REPO = r'C:\Users\hadar\source\repos\WhiteRose7303\Flask-Project-H_O\.git'  # make sure .git folder is properly configured
COMMIT_MESSAGE = CommitM

def git_push():
    try:
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')    

git_push()