# Console Hangman Game

A Python-based command-line implementation of the classic Hangman game.
This project was developed to demonstrate understanding of Python fundamentals, **Object-Oriented Programming (OOP)**, and file I/O operations.

[日本語の説明はこちら (Japanese Version)](#console-hangman-game-日本語)

---

## Overview
This is a two-player interactive game where:
1. **Player 1** sets a secret word and the difficulty level (number of allowed wrong guesses).
2. The screen clears to hide the secret word.
3. **Player 2** attempts to guess the word character by character.

## Key Features
* **Object-Oriented Design**: The game logic is encapsulated within the `HangmanGame` class for better maintainability and readability.
* **Input Validation**: Robust error handling for user inputs (e.g., preventing non-alphabetic characters, numbers, or empty inputs).
* **Customizable Difficulty**: Users can set the number of allowed mistakes (between 6 and 11).
* **Dynamic Visuals**: The game reads external `.txt` files to display the ASCII art state of the Hangman corresponding to the remaining lives.

## How to Run

### Prerequisites
* Python 3.x

### Installation
1. Clone this repository.
   ```bash
   git clone https://github.com/YOUR_USERNAME/hangman-game.git
   ```
2. Navigate to the project directory.
   ```bash
   cd hangman-game
   ```

### Usage
Run the script from the terminal:

```bash
python project.py
```

Ensure that all `Hangman_xx.txt` files are in the same directory as the script.

## File Structure

```text
.
├── project.py          # Main game script
├── Hangman_00.txt      # ASCII art assets
├── ...
├── Hangman_11.txt
└── README.md           # Documentation
```

## Future Improvements
* Implement a single-player mode using a random word generator API or a local dictionary.
* Add Unit Tests (using `unittest` or `pytest`) to verify game logic.

<br>

---

<br>

# Console Hangman Game (日本語)

Pythonで作成したコマンドラインベースのハングマンゲームです。
Pythonの基礎構文に加え、**オブジェクト指向プログラミング（OOP）**やファイル操作の理解を深めるために開発しました。

## 概要
2人プレイ形式のインタラクティブなゲームです。
1. **プレイヤー1**が「秘密の単語」と「難易度（許容されるミスの回数）」を設定します。
2. コンソール画面がクリアされ、単語が隠されます。
3. **プレイヤー2**が1文字ずつ推測して入力し、単語を当てます。

## 主な機能とこだわり
* **オブジェクト指向設計**: `HangmanGame` クラスを作成し、ゲームの状態管理とロジックをカプセル化しています。
* **入力バリデーション**: アルファベット以外の文字や数字、空文字などが入力された際にエラーメッセージを表示し、クラッシュを防ぐ処理を実装しています。
* **難易度設定**: 許容されるミスの回数を6回〜11回の間で自由に設定可能です。
* **動的な描画**: 外部テキストファイルを読み込むことで、残りライフに応じたハングマンのアスキーアートを表示します。

## 実行方法

### 前提条件
* Python 3.x

### 手順
1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/YOUR_USERNAME/hangman-game.git
   ```
2. ディレクトリに移動します。
   ```bash
   cd hangman-game
   ```
3. コマンドを実行してゲームを開始します。
   ```bash
   python project.py
   ```
   ※ `Hangman_xx.txt` ファイル群が同じディレクトリに存在することを確認してください。

## ファイル構成

```text
.
├── project.py          # ゲームのメインスクリプト
├── Hangman_00.txt      # アスキーアート用テキストファイル
├── ...
├── Hangman_11.txt
└── README.md           # ドキュメント
```

## 今後の展望
* 外部APIやローカル辞書を使用した、1人プレイモード（CPU対戦）の実装。
* `unittest` や `pytest` を用いた単体テストの導入による品質担保。