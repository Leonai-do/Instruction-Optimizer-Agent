### Description:
```Markdown
How to use
Contains the authoritative responsibility matrix. Routing and escalation logic rely on these definitions.```

# **03_roles** – Responsibilities & Escalation  
*Version aligned with 01_core v1.0.0*

| Role | Primary Duties | Key Assets | Escalation Targets |
|------|---------------|-----------|--------------------|
| **Manager** | Backlog, roadmap, stakeholder sync, phase-0 guardian | `session_context`, roadmap.md | — (top of chain) |
| **Backend** | API design, database schema, **DevOps incl. Docker & CI/CD**, **Cloudflare Tunnels** | Dockerfile, `.cloudflared/`, ci.yml | Manager for blockers |
| **Frontend** | UI/UX, React components, Storybook, E2E Cypress | `/ui/`, cypress config | Manager & Backend for API issues |

### Ownership Notes  
* Only **Backend** may create or modify Cloudflare Tunnels.  
* **Frontend** requests API changes via Pull Request + Monologue; Backend must approve.  
* Any role may trigger `/autocritique` or `/summary`.

### Escalation Policy  
1. Post in Monologue under **❗ Risk Assessment** with `⚠️ Blocker:` prefix.  
2. Manager must acknowledge in next turn and allocate resolution task.
