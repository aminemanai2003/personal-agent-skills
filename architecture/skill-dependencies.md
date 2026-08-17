# Skill Dependencies

This is the V1 behavioral dependency contract. An edge means the downstream workflow may consult the upstream skill; it does not require a nested invocation or loading every upstream body.

```text
personal-operating-profile
  -> anti-slop
  -> decision-making
  -> definition-of-done
  -> personal-writing

project-start
  -> personal-operating-profile
  -> decision-making

build-feature
  -> project-start
  -> code-quality
  -> secure-development (security-sensitive boundaries only)
  -> frontend-design (UI work only)
  -> definition-of-done
  -> personal-writing (handoff)

root-cause-debugging
  -> code-quality (confirmed fix only)
  -> decision-making (competing hypotheses or mitigation tradeoffs)
  -> definition-of-done

secure-development
  -> decision-making
  -> code-quality
  -> definition-of-done

review-code
  -> code-quality
  -> anti-slop
  -> definition-of-done (merge-readiness only)

security-review
  -> review-code
  -> definition-of-done (release decision only)

frontend-design
  -> personal-operating-profile
  -> anti-slop

visual-ux-review
  -> frontend-design (design-system context only)
  -> definition-of-done (when approval is requested)

review-ui
  -> visual-ux-review
  -> frontend-design (new direction only)
  -> definition-of-done

research-quality
  -> decision-making (material tradeoffs only)

research-topic
  -> research-quality
  -> decision-making

resume-and-ats
  -> personal-writing
  -> anti-slop

professional-profile
  -> personal-writing
  -> anti-slop

job-search-and-applications
  -> research-quality (current opportunity facts only)
  -> resume-and-ats (role-specific resume work)
  -> professional-profile (public proof alignment)
  -> personal-writing

github-workflow
  -> definition-of-done
  -> personal-writing
  -> review-code (review feedback only)

personal-writing
  -> personal-operating-profile

anti-slop
  -> definition-of-done (completion claims only)
```

Installed skills remain metadata until their descriptions match the current task; their bodies and references should load progressively. Load only the smallest set that changes the outcome. Avoid cycles by treating profile, anti-slop, and definition-of-done as cross-cutting references rather than automatic triggers for every task.
