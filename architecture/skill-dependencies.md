# Skill Dependencies

This is the initial dependency contract. Concrete edges are added as skills are implemented.

```text
personal-operating-profile
  -> anti-slop
  -> decision-making
  -> definition-of-done

project-start
  -> personal-operating-profile
  -> decision-making

build-feature
  -> project-start
  -> code-quality
  -> definition-of-done

review-code
  -> code-quality
  -> anti-slop

review-ui
  -> frontend-design
  -> visual-ux-review
  -> definition-of-done

research-topic
  -> research-quality
  -> decision-making

github-workflow
  -> definition-of-done
  -> personal-writing
```

Dependencies are behavioral references, not mandatory nested invocations. A task should load only the smallest set that changes its outcome.

