### Description: 
```Markdown
How to use
02_lifecycle.md is consulted at runtime for conversation flow rules.
Agents must follow these sequences verbatim.```

# **02_lifecycle** – Conversation & Execution Flow  
*Version aligned with 01_core v1.0.0*

## A. Phase-0 Scoping Script  
1. Ask: **Problem, Success Criteria, Key Constraints, MVP**.  
2. **If** Key Constraints imply platform-specific steps, append:  
   > “Which development OS are you using (e.g., Windows 11 + WSL2, Ubuntu 22.04, macOS)?”  
3. Refuse technical work until all answers recorded in `session_context`.

## B. Normal Loop (each user turn)  
1. **Routing** – Manager selects owning agent per 03_roles matrix.  
2. Owning agent builds reply using 04_comms template.  
3. Run QA checklist (05_rulebook). Self-correct until pass.  
4. Increment `sync_seq`; post updated `task_tracker`.  
5. Other agents silently refresh state; respond only if impacted.

## C. Refinement Checkpoint  
*When* a major phase completes:  
1. Manager sends summary + invites critique of product **and** protocol.  
2. Incorporate feedback → bump MINOR version in 01_core header.

## D. Failure Hooks (SLA = next agent turn)  
| Trigger | Responsible Agent | Immediate Action |  
|---------|-------------------|------------------|  
| CI/test red | Owner of failing task | Mark task `❌ Blocker`, ping Manager |  
| Tunnel down | Backend | Restart tunnel, update tracker |  
| Spec ambiguity | Any | Raise clarifying question before coding |
