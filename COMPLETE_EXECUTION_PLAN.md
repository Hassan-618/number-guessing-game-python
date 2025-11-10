# CSC-44102 Assessment 2 - Complete Execution Plan

## 📋 **Assignment Overview**

**Module Code:** CSC-44102  
**Assessment Title:** Assessment 2  
**Weighting:** 20% of module mark  
**Submission Length:** Equivalent of 1000 words  
**Submission Deadline:** 14 November 2025, 1 pm  
**Format of Submission:** A link to your public GitHub repository  
**Type of GenAI Use Permitted:** Full GenAI co-creation  

---

## 🎯 **Mandatory Requirements (Must Complete All 6)**

### **Requirement 1: Create a Game in Python**
- ✅ Write a game in Python (with or without AI help)
- ✅ Game must be functional and runnable
- ✅ Focus on Git usage over code complexity

### **Requirement 2: Use a Public GitHub Repository**
- ✅ Create public GitHub repository
- ✅ Use Keele email address for GitHub account
- ✅ Use Keele email for all commits
- ✅ Repository must remain public for assessment

### **Requirement 3: Commit Regularly**
- ✅ Make regular commits of code versions
- ✅ Minimum 5 commits required (plan for 8+)
- ✅ Each commit should represent meaningful progress

### **Requirement 4: Use Branching and Merging**
- ✅ Create feature branches for different features
- ✅ Perform at least one branch merge
- ✅ Show branching activity in repository history

### **Requirement 5: Acknowledge GenAI Use**
- ✅ Add AI acknowledgment at top of each code file
- ✅ Use specific format with AI tool, version, and URL
- ✅ Apply to ALL Python files created

### **Requirement 6: Submit the Link**
- ✅ Submit GitHub repository URL to KLE drop-box
- ✅ Ensure URL is accessible and public
- ✅ Submit before deadline: 14 November 2025, 1 pm

---

## 📊 **Assessment Criteria (100% Total)**

| Criteria | Weight | Requirements |
|----------|--------|-------------|
| **Python Game Code** | 25% | Public GitHub repository contains functional Python game |
| **Commit Frequency** | 25% | Five or more commits to repository |
| **Commit Quality** | 25% | Informative and descriptive commit messages |
| **Branch Management** | 25% | Activity history shows one or more branch merges |

**Critical Note:** 75% of marks are for Git/GitHub usage, only 25% for Python code.

---

## 🕒 **Complete 1-Day Execution Schedule**

### **Pre-Work Setup (30 minutes)**
**Time:** 8:30 AM - 9:00 AM

1. **GitHub Account Setup**
   - Ensure GitHub account uses Keele email: `y6y18@students.keele.ac.uk`
   - Verify account is active and accessible

2. **Repository Creation**
   - Create public repository: `number-guessing-game-python`
   - Initialize with README
   - Set visibility to PUBLIC (critical)

3. **Local Environment Setup**
   - Install Git if not present
   - Configure Git credentials:
     ```bash
     git config --global user.name "Hassan-618"
     git config --global user.email "y6y18@students.keele.ac.uk"
     ```

---

### **Session 1: Foundation (3 hours)**
**Time:** 9:00 AM - 12:00 PM  
**Goal:** Repository setup + Basic game implementation

#### **9:00 AM - 9:30 AM: Project Initialization**
**Tasks:**
- Clone repository locally
- Create project structure
- Add .gitignore for Python
- Create initial README.md

**Deliverables:**
- Local repository clone
- Basic file structure
- Python .gitignore file

#### **9:30 AM - 11:00 AM: Core Game Development**
**Tasks:**
- Create `game.py` with basic Number Guessing Game
- Implement core functionality:
  - Random number generation (1-100)
  - User input handling
  - Guess validation
  - Basic game loop
- Add AI acknowledgment header

**Deliverables:**
- Functional basic game
- AI acknowledgment in code
- Core game mechanics working

#### **11:00 AM - 12:00 PM: Initial Commits**
**Tasks:**
- Make first 3 commits with descriptive messages
- Test game functionality
- Push to GitHub

**Commits:**
1. `feat: initialize project with basic structure and gitignore`
2. `feat: implement core number guessing game logic`
3. `feat: add win/lose conditions and attempt tracking`

---

### **Session 2: Feature Development (3 hours)**
**Time:** 1:00 PM - 4:00 PM  
**Goal:** Feature development with branching and merging

#### **1:00 PM - 2:30 PM: Branch Creation & Feature Development**
**Tasks:**
- Create `feature/difficulty-levels` branch
- Implement difficulty settings:
  - Easy: 1-50, 10 attempts
  - Medium: 1-100, 7 attempts
  - Hard: 1-200, 5 attempts
- Create `feature/gui-version` branch
- Implement basic tkinter GUI interface

**Deliverables:**
- Two feature branches created
- Difficulty levels implemented
- Basic GUI interface created

#### **2:30 PM - 4:00 PM: Merging & Integration**
**Tasks:**
- Switch back to main branch
- Merge `feature/difficulty-levels` branch
- Merge `feature/gui-version` branch
- Resolve any merge conflicts
- Test integrated features
- Make integration commits

**Commits:**
4. `feat: add difficulty levels (easy/medium/hard)` (on feature branch)
5. `feat: implement basic tkinter GUI interface` (on feature branch)
6. `merge: integrate difficulty levels into main branch`
7. `merge: integrate GUI version into main branch`

---

### **Session 3: Finalization (2 hours)**
**Time:** 5:00 PM - 7:00 PM  
**Goal:** Documentation, testing, and submission preparation

#### **5:00 PM - 6:00 PM: Documentation & Polish**
**Tasks:**
- Update README.md with comprehensive documentation
- Add game instructions and setup guide
- Ensure all AI acknowledgments are present
- Create requirements.txt if needed
- Final testing of all features

**Deliverables:**
- Complete README.md
- All files have AI acknowledgments
- Game fully tested and functional

#### **6:00 PM - 7:00 PM: Final Commits & Submission Prep**
**Tasks:**
- Make final commits
- Push all changes to GitHub
- Verify repository is public and accessible
- Test repository URL
- Prepare submission

**Commits:**
8. `docs: update README with comprehensive game instructions`
9. `final: complete game with all features integrated and tested`

---

## 🎮 **Game Implementation Specifications**

### **Core Game: Number Guessing Game**
```python
# Basic Features (Session 1)
- Random number generation
- User input handling with validation
- Guess counting and attempt tracking
- Win/lose conditions
- Basic feedback (too high/too low)
- Game restart functionality
```

### **Enhanced Features (Session 2)**
```python
# Difficulty Levels
- Easy: Range 1-50, 10 attempts
- Medium: Range 1-100, 7 attempts  
- Hard: Range 1-200, 5 attempts

# GUI Interface (tkinter)
- Main game window
- Entry field for guesses
- Submit button
- Feedback labels
- Attempt counter display
- Difficulty selection
```

---

## 📁 **Required File Structure**

```
number-guessing-game-python/
│
├── README.md              # Project documentation (REQUIRED)
├── .gitignore            # Python gitignore (REQUIRED)
├── game.py               # Main console game (REQUIRED)
├── gui_game.py           # GUI version (REQUIRED)
├── requirements.txt      # Dependencies (if needed)
└── .git/                 # Git repository data
```

---

## 🔀 **Git Workflow Requirements**

### **Branch Strategy**
1. **main** - Primary development branch
2. **feature/difficulty-levels** - Difficulty implementation
3. **feature/gui-version** - GUI implementation

### **Commit Message Standards**
- Use conventional commit format
- Be descriptive and specific
- Include feature/fix/docs prefixes
- Examples:
  - `feat: implement core number guessing logic`
  - `merge: integrate difficulty levels into main`
  - `docs: update README with installation instructions`

### **Merge Requirements**
- Minimum 2 branch merges required
- Use merge commits (not rebase)
- Ensure merge history is visible in GitHub

---

## 📝 **AI Acknowledgment Template**

**Required in ALL Python files:**
```python
"""
I acknowledge the use of ChatGPT (OpenAI, https://chat.openai.com/) 
to create the code in this file for the Number Guessing Game implementation.
"""
```

**Alternative format if using different AI:**
```python
"""
I acknowledge the use of [AI_TOOL] (version [VERSION], [COMPANY], [URL]) 
to create the code in this file / on lines xx to xx in this file.
"""
```

---

## ✅ **Pre-Submission Checklist**

### **Repository Requirements**
- [ ] Repository is PUBLIC on GitHub
- [ ] Repository uses Keele email address
- [ ] Repository contains all required files
- [ ] Repository URL is accessible

### **Commit Requirements**
- [ ] Minimum 5 commits completed (target: 8+)
- [ ] All commit messages are informative
- [ ] Commits show regular development progress
- [ ] All commits use Keele email address

### **Branch Requirements**
- [ ] At least 2 feature branches created
- [ ] At least 1 branch merge completed
- [ ] Branch history visible in GitHub
- [ ] Merge commits are present

### **Code Requirements**
- [ ] Python game is functional
- [ ] Game can be run successfully
- [ ] All Python files have AI acknowledgments
- [ ] Code follows basic Python standards

### **Documentation Requirements**
- [ ] README.md is comprehensive
- [ ] Installation instructions included
- [ ] Game instructions included
- [ ] All features documented

### **Submission Requirements**
- [ ] Repository URL copied and ready
- [ ] Submission deadline confirmed: 14 November 2025, 1 pm
- [ ] KLE drop-box access confirmed

---

## 🚨 **Critical Success Factors**

### **Must-Do Items**
1. **Repository Visibility:** MUST be public
2. **Email Address:** MUST use Keele email for all Git operations
3. **Commit Count:** MUST have 5+ commits
4. **Branch Merges:** MUST show at least 1 merge in history
5. **AI Acknowledgments:** MUST be in every Python file
6. **Functional Code:** Game MUST run without errors

### **Common Pitfalls to Avoid**
- Private repository (automatic failure)
- Wrong email address in commits
- Insufficient commit messages
- No visible branch merges
- Missing AI acknowledgments
- Non-functional code
- Late submission

### **Quality Indicators**
- Clear, descriptive commit messages
- Logical development progression
- Clean branch merge history
- Comprehensive documentation
- Well-structured code files

---

## 📞 **Emergency Contingencies**

### **If Behind Schedule**
- Prioritize Git requirements over code complexity
- Simplify game features but maintain functionality
- Focus on meeting all 6 mandatory requirements
- Ensure minimum viable product is complete

### **If Technical Issues**
- Have backup plan for Git operations
- Test repository access regularly
- Keep local backups of all work
- Verify GitHub visibility settings

### **Final Hour Checklist**
- Repository is public and accessible
- All commits are pushed to GitHub
- Branch merges are visible
- AI acknowledgments are present
- Game runs successfully
- README is complete
- Submission URL is ready

---

## 🎯 **Success Metrics**

**Minimum Acceptable:**
- 5 commits with good messages
- 1 branch merge visible
- Functional Python game
- Public repository with Keele email
- AI acknowledgments in all files

**Target Excellence:**
- 8+ commits showing clear progression
- 2+ branch merges with clean history
- Well-documented, feature-rich game
- Comprehensive README documentation
- Professional Git workflow demonstration

---

**Final Note:** This assessment is primarily about demonstrating Git and GitHub proficiency. The Python game is secondary to proper version control practices. Focus on meeting all Git requirements first, then enhance the game features as time permits.