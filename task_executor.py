import threading
import logging
from datetime import datetime
from github import Github
from config import GITHUB_TOKEN

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TaskExecutor:
    def __init__(self):
        self.github = Github(GITHUB_TOKEN)
        self.tasks = {}
        
    def create_issue(self, repo_name, title, body):
        try:
            repo = self.github.get_user().get_repo(repo_name)
            issue = repo.create_issue(title=title, body=body)
            return f'Issue created: {issue.html_url}'
        except Exception as e:
            return f'Error: {str(e)}'
    
    def list_repos(self):
        try:
            repos = self.github.get_user().get_repos()
            return [repo.name for repo in repos]
        except Exception as e:
            return []
