## update the last_action_type file
import github

auth = github.Auth.Token("<fixme>")
g = github.Github(auth=auth)

repo = g.get_repo("lmaos-code/ruv_hackathon_2024")
# sleep
## DO THINGS WITH HPSM!!!!!

# update the last_action_type file
content = repo.get_contents("test.txt", ref="main") 
repo.update_file("test.txt", "committing files", "incident", sha=content.sha, branch="main")
