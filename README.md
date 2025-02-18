<h1 align="center">Welcome to the Multilingual Dictionary & Translation Project 🚀</h1>
<h2 align="center">Search, Understand, and Translate Words with Ease</h2>

<div>
    <p><strong>🔍 Project Purpose:</strong> A Python-based dictionary tool that allows users to search for a word's meaning and translate it into their desired language.</p>
    <p><strong>🌍 Supported Languages:</strong> Translate meanings into multiple languages using Google Translate.</p>
    <p><strong>⚡ Core Features:</strong> Word meaning retrieval, multilingual translations, easy installation, and cross-platform compatibility.</p>
</div>

<br clear="right">

## ✨ Features

- **Word Meaning Lookup**: Retrieve the definition of any word instantly.
- **Multilingual Translation**: Translate the meaning into any supported language.
- **Google Translate API**: Uses `googletrans==4.0.0-rc1` for reliable translations.
- **Easy Installation**: Simple setup and ready to use in minutes.
- **Cross-Platform**: Works on Windows, macOS, and Linux.

## 🛠️ Technologies Used

<p align="center">
    <img src="https://skillicons.dev/icons?i=python" alt="Python" height="60">
</p>

### Backend
- **Python**: Core programming language for the script.
- **GoogleTrans**: Translation API module.

## 🚀 Getting Started

### Prerequisites
Ensure you have Python installed. To check:
```bash
python3 --version
```
If not installed, follow the steps below.

### Installation Steps

#### For macOS (Using Homebrew)
1. **Install Homebrew** (if not already installed):
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. **Install Python**:
```bash
brew install python
```
3. **Verify Python Installation**:
```bash
python3 --version
```
4. **Ensure Pip is Installed**:
```bash
python3 -m ensurepip --default-pip
```
5. **Upgrade Pip**:
```bash
python3 -m pip install --upgrade pip
```
6. **Install GoogleTrans Module**:
```bash
pip install googletrans==4.0.0-rc1
```

#### Alternative (Using Replit)
1. Open [Replit](https://replit.com/)
2. Create a new Python file.
3. Install the GoogleTrans module:
```bash
pip install googletrans==4.0.0-rc1
```
4. Run the Python script.

## 📁 Project Structure
```
Multilingual-Dictionary-Project/
├── README.md              # Project documentation
├── dictionary.py          # Main script for word lookup and translation
├── dictionary_data.json   # Stores dictionary-related data
├── trans.json             # Stores translation-related data
```

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---
<p align="center">Made with ❤️ for seamless word understanding and translation</p>

