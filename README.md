# File Commit Switcher

A lightweight Python utility to "commit" and "switch" file states in a directory — like a minimal version control system using `pickle`.

## 📦 Features

- Save (commit) the current state of files in a directory.
- Switch between previously saved file states.
- Ignores the `get/` directory to avoid overwriting script data.
- Supports binary files.

## 📁 Project Structure

```
.
├── get/
│   ├── get.py         # Main script
│   └── commit.pkl     # Stores commit data (generated automatically)
├── README.md          # This file
```

## 🚀 Usage

Run the script from the `get/` folder:

```bash
python get.py [commit|switch] <commit_name>
```

### 💾 Example: Commit a State

```bash
python get.py commit initial_version
```

### 🔄 Example: Switch to a Saved State

```bash
python get.py switch initial_version
```

## ⚠ Notes

- All files in the parent directory (excluding `get/`) are deleted and restored when switching commits.
- Commits are saved in `get/commit.pkl`.
- Useful for quickly saving and restoring file versions for demos or experiments.

## 🧪 Requirements

- Python 3.x

No external dependencies are required.

## 📄 License

MIT License (add your license here if needed).
