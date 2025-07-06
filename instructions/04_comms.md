# **04_comms** – Templates & Schemas  
*Version aligned with 01_core v1.0.0*

## 1. Development Monologue Template (mandatory every reply)

> ### Development Monologue  
> **🎯 Goal:** {objective}  
> **🗺️ Plan:** {strategy}  
> **🧠 Reasoning:** {why}  
> **⚖️ Trade-offs:** {alt options / n/a}  
> **✅ Validation Plan:** {test / proof}  
> **❗ Risk Assessment:** {blockers / n/a}  
> **▶️ Action:** {next step}

*Agents MAY use one-liners for minor fixes but headers must stay.*

---

## 2. Task-Tracker Schema

```jsonc
{
  "sync_seq": 0,
  "tasks": [
    { "id": "T-000", "title": "Phase-0 Scoping", "status": "⌛", "owner": "Manager" }
  ]
}
```
## 3. Slash-Command Registry


| Command                      | Purpose                               |
| ---------------------------- | ------------------------------------- |
| `/help`                      | Show capabilities & commands          |
| `/summary`                   | Summarise project & decisions         |
| `/autocritique` or `/review` | Re-run QA checklist, self-correct     |
| `/q`                         | Suggest follow-up questions           |
| `/more`                      | Drill deeper into last topic          |
| `/redo`                      | Re-answer previous prompt differently |

### 4. Examples (Good vs Bad)
- Good (minor typo):
🎯 Goal: fix README typo  
🗺️ Plan: edit line 12 …  
🧠 Reasoning: docs quality …  
⚖️ Trade-offs: n/a  
✅ Validation Plan: grep …  
❗ Risk Assessment: none  
▶️ Action: apply patch

- Bad: missing headers, no task-tracker update, fence not closed.
