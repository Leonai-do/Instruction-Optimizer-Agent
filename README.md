# 📚 DevPartner Instruction Suite &nbsp;|&nbsp; **README**

Welcome to the **DevPartner Instruction Suite**—a lean, five-file playbook that turns any multi-agent AI crew into a disciplined, self-auditing software-development powerhouse.  
If you’re reading this, you’re about to **use**, **extend**, or **embed** these instructions. This single document is your streamlined guide.

---

## 🗂️ Folder Structure

```text
instructions/
├── 01_core.md          # Mission, principles, emoji glossary
├── 02_lifecycle.md     # Phase-0 flow & failure hooks
├── 03_roles.md         # Responsibilities & escalation
├── 04_comms.md         # Comm templates & schemas
├── 05_rulebook.yml     # ALWAYS/NEVER rules + QA
└── assemble.py         # (optional) glue → FULL_PROMPT.md
```


---

## ✨ What to Expect

| Aspect               | Outcome                                                                                           |
|----------------------|----------------------------------------------------------------------------------------------------|
| **Predictable Flow** | Phase-0 scoping → routed conversations → refinement checkpoints.                                   |
| **Self-Auditing**    | Every agent reply runs an internal QA checklist *before* the user sees it.                         |
| **Token Efficiency** | Only five short files are loaded each session—no bloated prompts.                                  |
| **Protocol Evolution** | Stakeholders can tweak rules at each major milestone; SemVer communicates impact automatically. |
| **Reversible History** | Every change is Git-tracked; you can revert to any prior version.                                |

---

## 🚀 Quick Start

1. **Clone / copy** the `instructions/` folder into your repository.  
2. *(Optional)* **Run** `python instructions/assemble.py` to generate `FULL_PROMPT.md`.  
3. Feed **either** the concatenated `FULL_PROMPT.md` **or** the five files (in lexical order) into your agent’s system-prompt slot.  
4. Boot the agent—Phase-0 kicks off automatically. 🎉

---

## ⚙️ Deployment Tips

| Runtime                 | Integration Hint                                                                                           |
|-------------------------|-------------------------------------------------------------------------------------------------------------|
| **OpenAI API / ChatGPT**| Load the concatenated prompt as the `system` message.                                                       |
| **LangChain**           | `SystemMessage(Path("FULL_PROMPT.md").read_text())`                                                         |
| **Local Fine-Tune**     | Bundle the five files as system messages in your training dataset.                                         |
| **CI (GitHub Actions)** | Add a lint job:<br>`markdownlint instructions/**/*.md && yamllint instructions/05_rulebook.yml`             |

---

## 🛠️ Customisation Workflow  *(“Change with Confidence”)*

1. **Create a branch** → `feature/rule-tweak`.  
2. **Edit exactly one file**—keep diffs atomic.  
3. **Bump the version header** in the changed file per `semver_rules` in `05_rulebook.yml`.  
4. **Update `CHANGELOG.md`** with a concise entry.  
5. **Run local QA** (Markdown, YAML, assemble test).  
6. **Open a PR**—the Optimizer Agent (or a human) will run `/autocritique`.  
7. **Merge after approval**. CI tags the repo: `vX.Y.Z`. 🚀

---

## 💡 Improvement Ideas

| Idea                                         | Effort | Benefit                                           |
|----------------------------------------------|--------|---------------------------------------------------|
| Add `/docs` runbooks (Docker, Cloudflare)    | 🟡     | Paste-ready setup scripts for newcomers           |
| Automate `assemble.py` in CI                 | 🟢     | Guarantees `FULL_PROMPT.md` is always up-to-date  |
| Add PII scanner to QA pipeline               | 🟡     | Safety net when examples include user data        |
| Hook metrics (latency, token count)          | 🟡     | Spot inefficiencies early                         |

---

## 🤝 Contributing

1. **Fork** 🍴  
2. Follow the **Customisation Workflow** above.  
3. **Sign commits** (`git commit -s`) if your organisation requires DCO.  
4. Keep PR descriptions *concise*—let the diff speak for itself.

---

## 🛡️ License

* **Docs** – CC BY-SA 4.0  
* **Code (assemble.py)** – MIT

---
