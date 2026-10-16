<div align="center">
  <a href="https://youtu.be/X6YpA86ILBU">
    <img src="https://img.youtube.com/vi/X6YpA86ILBU/0.jpg" alt="ColGrep Agent 2B: Cut Claude Code API Costs by 40% Locally!">
  </a>
  <h3>📺 <a href="https://youtu.be/X6YpA86ILBU">Watch the full tutorial on YouTube</a></h3>
</div>

# ⚡ ColGrep Agent Code Search

> Intelligent local code-search assistant powered by ColGrep-Agent-2B that cuts cloud coding agent tokens by 34% through local code localization.

---

| Step 1: Input | Step 2: AI Action | Step 3: Result |
| :--- | :--- | :--- |
| Natural language code query | Semantic search & read-only analysis | Pinpoint files and exact line ranges |

---

## 🌟 Key Superpowers

- ⚡ **Local Code Localization**: Pinpoints exact file paths and line ranges using semantic code understanding.
- 📉 **Significant Token Savings**: Offloads exploratory codebase searches, cutting API tokens by 34%.
- 💰 **Lower Inference Costs**: Reduces cache-aware API expenses by up to 40% on complex repositories.
- 🔒 **Private Repository Search**: Operates directly on your machine without transmitting source code to external servers.
- 🔌 **Seamless Integration**: Ready-to-use hooks for Claude Code, Codex, and OpenCode environments.

---

## 🛠️ Tech Stack & Requirements

- **Model**: `ColGrep-Agent-2B` (MiniCPM5-2B base architecture, Apache-2.0)
- **Local Engine**: ColGrep (NextPlaid multi-vector late-interaction retrieval)
- **Inference Runtime**: llama.cpp / GGUF (Metal, Vulkan, or CPU)
- **Language & Environment**: Python 3.10+ / Standalone CLI binary

---

## 📋 File Explanation

- `main.py`: Core application script executing semantic search queries, analyzing repository files, and producing structured code location summaries.
- `Modelfile`: Ollama model manifest configured to register the local `colgrep-agent-2B-Q8_0.gguf` checkpoint.
- `requirements.txt`: Python package requirements.

---

## 🚀 Quick Setup & Installation

### 1. Download Model Checkpoint

Download the official `colgrep-agent-2B-Q8_0.gguf` checkpoint into the `models/` directory:

```powershell
hf download lightonai/colgrep-agent-2B-GGUF colgrep-agent-2B-Q8_0.gguf --local-dir models
```

### 2. Register Model with Ollama

Register the local GGUF weights with Ollama:

```powershell
ollama create colgrep-agent-2B -f Modelfile
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Run Search

```powershell
python main.py --repo "inputs/sample_app" --query "where does the application handle task retry backoff and send failure notifications"
```

---

## 💡 5 Real-World Use Cases

1. **Large Monorepo Exploration**: Rapidly find where configuration flags and backend drivers are declared across 500k+ lines of code.
2. **Vocabulary Mismatch Resolution**: Locate features even when you ask for "custom attributes" but the codebase names them "fields".
3. **CI/CD Flaky Test Localization**: Identify exact line ranges where retry logic and network timeouts are configured.
4. **Offline Air-Gapped Code Auditing**: Perform deep semantic source audits on sensitive proprietary systems with zero data leakage.
5. **Coding Assistant Cost Optimization**: Use ColGrep as a fast local pre-filter before sending context to frontier reasoning models.

---

## 🔮 5 Future Enhancements

1. **Multi-Repository Federation**: Search across multiple dependent repositories simultaneously in one pass.
2. **Interactive TUI Dashboard**: Terminal user interface with live syntax-highlighted code diff inspection.
3. **Automated Test Generation**: Automatically synthesize regression tests targeting located error lines.
4. **AST-Aware Semantic Chunking**: Enhance NextPlaid vector indices with tree-sitter symbol hierarchy graphs.
5. **Direct IDE Extension**: One-click jump to located line ranges inside VS Code and JetBrains IDEs.

---

## 🏷️ Keywords & SEO

`ColGrep Agent 2B` `Claude Code` `Local Code Search` `ColGrep` `MiniCPM` `Ollama` `GGUF` `llama.cpp` `Code Localization` `AI Coding Agent` `Token Optimization` `Semantic Code Search` `LightOn AI`
