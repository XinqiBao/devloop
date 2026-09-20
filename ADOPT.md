# Assess and Adopt

Use this entry point when setting up a new environment, reviewing an existing one, considering newer devloop guidance, or helping someone else adopt selected practices. [PRACTICES.md](PRACTICES.md) is the candidate set, not a configuration to deploy. Start with the person's goal and scope; specific instructions take priority.

1. Inspect the relevant project, agent instructions, existing configuration, and native capabilities. Limit inspection to what the request warrants; avoid reading secrets or treating files you did not create as yours to manage.
2. Compare current behavior with the relevant practices. Identify a concrete gap that matters here and whether the current setup already addresses it. A newer practice is a candidate for evaluation, not an update to apply automatically.
3. Recommend the smallest useful change at the narrowest scope, if any. Prefer an existing instruction or native behavior; do not copy this repository wholesale, create a fixed file tree, track versions, or link the environment to this checkout. If the request leaves a material tradeoff or conflict unsettled, explain it and ask the owner before changing their configuration.
4. Make only authorized, in-scope changes. Preserve unrelated content, verify meaningful discovery or behavior where practical, and report what changed, what stayed as it was, and any unverified behavior. If the current setup is sufficient, explicitly report no change.

For example, an established project whose instructions and agent capabilities already produce risk-appropriate checks needs no devloop file. If an existing personal rule conflicts with a candidate practice, keep the rule in place, explain the conflict, and ask its owner whether to change it; do not replace or uninstall their setup as part of this review.
