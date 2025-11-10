Of course. Here is the useful information from the content, presented as-is, with all requirements listed clearly and unnecessary content removed.

### Complete Requirements

**Module Code:** CSC-44102
**Assessment Title:** Assessment 2
**Weighting:** 20% of module mark
**Submission Length:** Equivalent of 1000 words
**Submission Deadline:** 14 November 2025, 1 pm
**Format of Submission:** A link to your public GitHub repository
**Type of GenAI Use Permitted:** Full GenAI co-creation

---

**Assessment Details:**

You must complete the following tasks:

1.  **Create a Game in Python:** With or without the help of a generative AI, write a game in Python.
2.  **Use a Public GitHub Repository:** Create a public GitHub repository and work within it. You must use your Keele email address for your GitHub account and for your commits.
3.  **Commit Regularly:** You should commit regular versions of your code.
4.  **Use Branching and Merging:** Make at least some use of branching and merging as you work on different features.
5.  **Acknowledge GenAI Use:** At the top of each code file, you must acknowledge any use of GenAI. For example: “I acknowledge the use of Microsoft Copilot (version GPT-4, Microsoft, https://copilot.microsoft.com/) to create the code in this file / on lines xx to xx in this file”.
6.  **Submit the Link:** Submit the URL for your public GitHub repository's web page to the KLE drop-box.

---

**Assessment Criteria:**

Your work will be graded based on the following:

*   **(25%)** Your public GitHub repository contains your Python code for a game.
*   **(25%)** You have made five (or more) commits to the repository.
*   **(25%)** The commit messages are informative.
*   **(25%)** The activity history shows one (or more) branch merge.

**Note:** Most of the assessment's marks are for your use of Git and GitHub, rather than for your Python code.


# Complete 1-Day Assessment 2 Execution Plan

## 📋 **Overall Strategy**
We'll complete everything in **one intensive day** while maintaining authentic Git practices. We'll work in **3 focused sessions** with breaks.

## 🕒 **Day Schedule**

### **Session 1: Morning (3 hours)**
**Goal: Repository setup + Basic game implementation**

**9:00 AM - 9:30 AM: Initial Setup**
- public GitHub repository: `https://github.com/Hassan-618/number-guessing-game-python.git`
- Clone repository locally
- Configure Git with your details:
  ```bash
  git config user.name "Hassan-618"
  git config user.email "y6y18@students.ac.uk"
  ```
- Create basic project structure

**9:30 AM - 11:00 AM: Basic Game Development**
- Implement core Number Guessing Game functionality
- Create `game.py` with basic features
- Add proper AI acknowledgment headers

**11:00 AM - 12:00 PM: Initial Commits**
- Make first 3 commits with meaningful messages

### **Session 2: Afternoon (3 hours)**  
**Goal: Feature development with branching**

**1:00 PM - 2:30 PM: Branch Creation & Feature Development**
- Create and switch to `feature/difficulty-levels` branch
- Implement difficulty settings (Easy/Medium/Hard)
- Create and switch to `feature/gui-version` branch  
- Add simple tkinter GUI interface

**2:30 PM - 4:00 PM: Merging & Integration**
- Switch back to main branch
- Merge feature branches
- Resolve any merge conflicts
- Test integrated features

### **Session 3: Evening (2 hours)**
**Goal: Final touches & submission prep**

**5:00 PM - 6:00 PM: Polish & Documentation**
- Update README.md with game instructions
- Ensure all AI acknowledgments are present
- Final testing of all features

**6:00 PM - 7:00 PM: Final Commits & Submission**
- Make final commits
- Push everything to GitHub
- Verify repository is public and accessible
- Prepare submission URL

## 🎮 **Game Implementation Plan**

### **Basic Game Features (Session 1)**
```python
# game.py - Core functionality
- Random number generation (1-100)
- User input handling
- Guess counting
- Win/lose conditions
- Basic feedback (too high/too low)
```

### **Enhanced Features (Session 2)**
```python
# Difficulty levels (feature/difficulty-levels)
- Easy: 1-50, 10 attempts
- Medium: 1-100, 7 attempts  
- Hard: 1-200, 5 attempts

# GUI version (feature/gui-version)
- tkinter window
- Entry field for guesses
- Submit button
- Feedback labels
- Attempt counter display
```

## 💻 **Detailed File Structure**
```
assessment2-game/
│
├── game.py                 # Main game file
├── gui_game.py            # GUI version (optional separate file)
├── README.md              # Project documentation
├── .gitignore            # Python gitignore
└── requirements.txt      # Dependencies (tkinter)
```

## 🔀 **Git Commits Timeline**

### **Session 1 Commits (3 commits)**
1. **10:00 AM** - `git commit -m "feat: initialize project with basic structure"`
   - Add README with project description
   - Create .gitignore for Python
   - Add basic project structure

2. **11:00 AM** - `git commit -m "feat: implement core number guessing logic"`
   - Add random number generation
   - Implement user input and validation
   - Add basic game loop

3. **11:45 AM** - `git commit -m "feat: add win conditions and scoring system"`
   - Implement attempt counting
   - Add win/lose messages
   - Include score tracking

### **Session 2 Commits (3+ commits with branching)**
4. **2:00 PM** - `git commit -m "feat: add difficulty levels (easy/medium/hard)"`
   - **Branch**: `feature/difficulty-levels`
   - Implement range and attempt variations
   - Add difficulty selection menu

5. **3:00 PM** - `git commit -m "feat: implement basic tkinter GUI interface"`
   - **Branch**: `feature/gui-version` 
   - Create window, labels, entry field
   - Add game logic to GUI

6. **3:45 PM** - `git commit -m "merge: integrate difficulty levels and GUI features"`
   - **Merge both feature branches to main**
   - Resolve any integration issues
   - Ensure all features work together

### **Session 3 Commits (2 commits)**
7. **5:30 PM** - `git commit -m "docs: update README with game instructions and setup"`
   - Add clear game instructions
   - Include installation/run steps
   - Document all features

8. **6:30 PM** - `git commit -m "final: complete game with all features integrated"`
   - Final testing and bug fixes
   - Ensure AI acknowledgments in all files
   - Ready for submission

## 📝 **AI Acknowledgment Templates**

**For each Python file:**
```python
"""
I acknowledge the use of ChatGPT (OpenAI, https://chat.openai.com/) 
to create the code in this file for the Number Guessing Game implementation.
"""
```

## ✅ **Final Verification Checklist**
Before submission at 7:00 PM:

- [ ] Repository is **public** on GitHub
- [ ] **8+ commits** total (exceeding 5 minimum)
- [ ] **2 branch merges** completed 
- [ ] All **commit messages** are descriptive
- [ ] **Python game code** is present and functional
- [ ] **AI acknowledgments** in all code files
- [ ] **README.md** contains proper documentation
- [ ] Game can be **run successfully**
- [ ] All features integrated and tested
- [ ] Repository URL is ready for submission

## 🚨 **Important Notes**
- **Take breaks** between sessions to avoid burnout
- **Test each feature** after implementation
- **Commit frequently** with meaningful messages
- **Double-check** repository visibility is public
- **Save the repository URL** for submission

This plan ensures you meet **all assessment criteria** while completing everything in one day. The timeline is aggressive but achievable with focused work.