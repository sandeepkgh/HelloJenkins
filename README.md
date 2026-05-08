# HelloJenkins - Jenkins Pipeline Learning Project

A simple, educational repository to learn Jenkins CI/CD pipeline basics using Python.

## 📋 Contents

- **hello_world.py** - A simple Python script demonstrating basic functions
- **Jenkinsfile** - Declarative Jenkins pipeline configuration

## 🚀 Getting Started

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/sandeepkgh/HelloJenkins.git
   cd HelloJenkins
   ```

2. **Run the Python script locally**
   ```bash
   python3 hello_world.py
   ```

3. **Expected Output**
   ```
   ==================================================
   Hello from Jenkins Pipeline!
   Python Jenkins Integration - Hello World Example
   ==================================================
   Hello, Jenkins User! Welcome to Jenkins CI/CD Pipeline.

   Script execution completed successfully!
   ```

### Jenkins Pipeline Setup

1. **Create a new Pipeline job in Jenkins**
   - Job Type: Pipeline
   - Pipeline → Definition: Pipeline script from SCM
   - SCM: Git
   - Repository URL: `https://github.com/sandeepkgh/HelloJenkins.git`
   - Branch: `*/main`
   - Script Path: `Jenkinsfile`

2. **Configure GitHub Webhook (Optional)**
   - Navigate to repo Settings → Webhooks
   - Add Jenkins webhook URL for automatic triggers

3. **Build the Job**
   - Click "Build Now" to trigger the pipeline

## 📊 Pipeline Stages Explained

| Stage | Purpose | What It Does |
|-------|---------|-------------|
| **Checkout** | Source Control | Pulls the latest code from GitHub |
| **Setup** | Environment Check | Verifies Python 3 is installed |
| **Run Hello World** | Execution | Runs the hello_world.py script |
| **Test** | Quality Check | Validates Python syntax |
| **Summary** | Information | Reports build details |

## 📚 Learning Path

### Beginner Level
- [ ] Run pipeline locally with `python3 hello_world.py`
- [ ] Create Jenkins job and trigger manually
- [ ] View console output and understand each stage

### Intermediate Level
- [ ] Add Git triggers for automatic builds
- [ ] Modify Jenkinsfile to add environment variables
- [ ] Add error handling and post-build actions
- [ ] Create parameterized builds

### Advanced Level
- [ ] Use Docker agents in pipeline
- [ ] Implement parallel stages
- [ ] Add code quality checks (linting, formatting)
- [ ] Set up artifact archiving
- [ ] Create multi-branch pipelines

## 🔧 Next Steps for Enhancement

Consider adding:
- **Unit Tests** - Use pytest framework
- **Code Quality** - pylint or flake8
- **Coverage Reports** - Code coverage metrics
- **Artifact Archiving** - Save build outputs
- **Slack Notifications** - Pipeline status alerts
- **Docker Support** - Containerized builds

## 📖 Resources

- [Jenkins Official Documentation](https://www.jenkins.io/doc/)
- [Declarative Pipeline Syntax](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [Python with Jenkins](https://www.jenkins.io/doc/book/pipeline/syntax/)
- [GitHub Webhooks](https://docs.github.com/en/developers/webhooks-and-events/webhooks)

## 💡 Tips

- Always check the **Console Output** in Jenkins for debugging
- Use **Blue Ocean** plugin for better visualization
- Enable **Timestamps** to track stage execution time
- Set **Build Timeout** to prevent hanging builds

## 📝 License

This project is open source and available for learning purposes.

---

**Happy Learning! 🎓**

Feel free to fork, modify, and experiment with this repository to deepen your Jenkins knowledge.
