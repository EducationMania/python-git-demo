import os
import pickle
import sys

COMMITS_PATH = './get/commit.pkl'
EXCLUDE_DIR = 'get'

def safe_pickle_load(path):
    if (
     not os.path.isfile(path) or 
     os.path.getsize(path) == 0
    ):
        return {}
    with open(path, 'rb') as f:
        return pickle.load(f)

def get_demo_dir():
    return os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )

def clean_demo_dir():
    demo_dir = get_demo_dir()
    for item in os.listdir(demo_dir):
        if item == EXCLUDE_DIR:
            continue
        item_path = os.path.join(
            demo_dir, item
        )
        if os.path.isfile(item_path):
            os.remove(item_path)


def write_commit(commit, commits):
    commit_data = commits.get(
        commit
    )
    if commit_data is None:
        raise ValueError(
          f"Commit '{commit}' not found."
        )
    for flnm, ctnt in  commit_data.items():
        with open(flnm, 'wb') as f:
            f.write(ctnt)

def build_commit(commit, commits):
    demo_dir = get_demo_dir()
    commit_content = {}
    for item in os.listdir(demo_dir):
        item_path = os.path.join(
            demo_dir, item
        )
        if os.path.isfile(item_path):
            with open(item_path, 'rb') as f:
                commit_content[item] = f.read()
    commits[commit] = commit_content
    with open(COMMITS_PATH, 'wb') as f:
        pickle.dump(commits, f)

def switch(commit, commits):
    clean_demo_dir()
    write_commit(commit, commits)

def commit_it(commit, commits):
    build_commit(commit, commits)

def main():
    commits = safe_pickle_load(
        COMMITS_PATH
    )
    if len(sys.argv) < 3:
        print(
         "Usage: script.py [commit|switch] <commit_name>")
        sys.exit(1)

    command, commit_name = (
        sys.argv[1], sys.argv[2]
    )

    try:
        if command == 'commit':
            commit_it(commit_name, commits)
        elif command == 'switch':
            switch(commit_name, commits)
        else:
            print('Invalid command. Use "commit" or "switch".')
            sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()
