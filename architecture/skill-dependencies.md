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
  -> frontend-design (UI work only)
  -> definition-of-done
  -> personal-writing (handoff)

review-code
  -> code-quality
  -> anti-slop
  -> definition-of-done (merge-readiness only)

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

github-workflow
  -> definition-of-done
  -> personal-writing
  -> review-code (review feedback only)

personal-writing
  -> personal-operating-profile

anti-slop
  -> definition-of-done (completion claims only)
```

Load only the smallest set that changes the outcome. Avoid cycles by treating profile, anti-slop, and definition-of-done as cross-cutting references rather than automatic triggers for every task.
